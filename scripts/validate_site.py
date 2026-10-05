#!/usr/bin/env python3
"""Validate locale pages, product copy and links in the generated Pages site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
from xml.etree import ElementTree
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SITE = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"
BASE = "/TingRadio"
ORIGIN = "https://vonzen.github.io"
LOCALES = json.loads((ROOT / "_data/languages.json").read_text())
GROUPS = {"home": "", "privacy": "privacypolicy/", "terms": "termsofservice/"}
errors = []


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.source = source
        self.ids, self.urls, self.heading_count = set(), [], 0
        self.lang, self.body_lang, self.title, self.title_open = "", "", "", False
        self.canonical, self.alternates, self.language_links = [], {}, {}
        self.current_languages, self.og_locale, self.text = [], "", []
        self.class_counts, self.images = {}, []
        self.landing = False
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for name in attrs.get("class", "").split():
            self.class_counts[name] = self.class_counts.get(name, 0) + 1
        if tag == "html":
            self.lang = attrs.get("lang", "")
        if tag == "body":
            self.body_lang = attrs.get("data-language", "")
            self.landing = attrs.get("data-landing") == "true"
        if tag == "a" and "data-language" in attrs:
            lang = attrs["data-language"]
            if lang in self.language_links:
                errors.append(f"duplicate language option: {lang}")
            self.language_links[lang] = attrs.get("href", "")
            if attrs.get("lang") != lang or attrs.get("hreflang") != lang:
                errors.append(f"language option metadata mismatch: {lang}")
            if attrs.get("aria-current") == "page":
                self.current_languages.append(lang)
        if tag == "title":
            self.title_open = True
        if tag == "h1":
            self.heading_count += 1
        if "id" in attrs:
            if attrs["id"] in self.ids:
                errors.append(f"duplicate id: {attrs['id']}")
            self.ids.add(attrs["id"])
        if tag == "img" and "alt" not in attrs:
            errors.append(f"image missing alt: {attrs.get('src')}")
        if tag == "img":
            self.images.append(attrs)
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs.get("href"))
        if tag == "link" and attrs.get("rel") == "alternate":
            lang = attrs.get("hreflang")
            if lang in self.alternates:
                errors.append(f"duplicate alternate: {lang}")
            self.alternates[lang] = attrs.get("href")
        if tag == "meta" and attrs.get("property") == "og:locale":
            self.og_locale = attrs.get("content", "")
        for attr in ("href", "src"):
            if attr in attrs:
                self.urls.append(attrs[attr])

    def handle_endtag(self, tag):
        if tag == "title":
            self.title_open = False

    def handle_data(self, data):
        self.text.append(data)
        if self.title_open:
            self.title += data


expected = {}
for locale in LOCALES:
    for group, suffix in GROUPS.items():
        if group != "home" and locale["key"] != "en":
            continue
        path = locale["home"].lstrip("/") + suffix + "index.html"
        expected[path] = (locale, group)
expected["404.html"] = (LOCALES[0], None)
if LOCALES[0]["key"] != "en" or LOCALES[0]["home"] != "/":
    errors.append("default locale must be English at /")

pages = {}
for path, (locale, group) in expected.items():
    file = SITE / path
    if not file.is_file():
        errors.append(f"missing page: {path}")
        continue
    page = pages[path] = Page(file.read_text())
    if page.lang != locale["lang"] or page.body_lang != locale["lang"] or not page.title.strip() or page.heading_count != 1:
        errors.append(f"invalid language, title or h1 count: {path}")
    if page.og_locale != locale["locale"]:
        errors.append(f"invalid Open Graph locale: {path}")
    canonical = ORIGIN + BASE + ("/404.html" if group is None else locale["home"] + GROUPS[group])
    if page.canonical != [canonical]:
        errors.append(f"incorrect canonical: {path}")
    if "{{" in page.source or "{%" in page.source:
        errors.append(f"unrendered Liquid: {path}")
    if re.search(r"\b2\.0(?:\.\d+)?\b", page.source):
        errors.append(f"version number shown: {path}")
    is_legal = group in ("privacy", "terms")
    routes = {} if is_legal else {item["lang"]: BASE + item["home"] for item in LOCALES}
    current_languages = [] if is_legal else [locale["lang"]]
    if page.language_links != routes or page.current_languages != current_languages:
        errors.append(f"incorrect language menu paths/current locale: {path}")
    if is_legal:
        if page.alternates or 'property="og:locale:alternate"' in page.source:
            errors.append(f"English-only legal page advertises translations: {path}")
    elif group is not None:
        alternates = {lang: ORIGIN + route for lang, route in routes.items()}
        alternates["x-default"] = ORIGIN + routes["en"]
        if page.alternates != alternates:
            errors.append(f"incorrect translated-page alternates: {path}")
    if page.landing != (group == "home"):
        errors.append(f"incorrect landing flag: {path}")
    for suffix in ("privacypolicy/", "termsofservice/"):
        if BASE + "/" + suffix not in page.urls:
            errors.append(f"missing shared English legal link: {path}")
    if group == "home":
        for name, count in {"showcase-item": 3, "feature-card": 6, "feature-entitlement": 6, "store-badge": 2}.items():
            if page.class_counts.get(name) != count:
                errors.append(f"missing product showcase, feature cards or download badge: {path}: {name}")
        captures = [img for img in page.images if img.get("src", "").endswith("-en.webp")]
        expected_captures = ["genres-en.webp", "player-en.webp", "genres-en.webp", "player-en.webp", "song-history-en.webp", "sleep-timer-en.webp"]
        if [img["src"].split("/")[-1] for img in captures] != expected_captures:
            errors.append(f"incorrect shared English screenshot set: {path}")
        if any(not img.get("alt", "").strip() or img.get("width") != "1206" or img.get("height") != "2622" for img in captures):
            errors.append(f"missing screenshot description or native dimensions: {path}")
        text = " ".join(page.text)
        forbidden = r"1\.2\.0|\bpreview\b|预览|\bprices?\b|价格|價格|[￥¥$€]\s*\d|锁屏实时歌词|鎖定畫面即時歌詞|Lock Screen lyrics|数据统计|數據統計|\bstatistics\b|\banalytics\b"
        if re.search(forbidden, text, re.I):
            errors.append(f"excluded marketing content: {path}")
        if "https://apps.apple.com/app/id6451428572" not in page.urls:
            errors.append(f"missing static App Store link: {path}")

for path, page in pages.items():
    source_url = ORIGIN + BASE + "/" + path.replace("index.html", "")
    for raw in page.urls:
        if not raw:
            errors.append(f"empty URL: {path}")
            continue
        url = urlparse(urljoin(source_url, raw))
        if url.scheme not in ("http", "https") or url.netloc != "vonzen.github.io":
            continue
        if not url.path.startswith(BASE + "/"):
            errors.append(f"link escapes project base path: {path}: {raw}")
            continue
        target = unquote(url.path[len(BASE) + 1:])
        if not target or target.endswith("/"):
            target += "index.html"
        file = SITE / target
        if not file.is_file():
            errors.append(f"missing local target: {path}: {raw}")
        elif url.fragment and file.suffix == ".html":
            dest = pages.get(target) or Page(file.read_text())
            if unquote(url.fragment) not in dest.ids:
                errors.append(f"missing anchor: {path}: {raw}")

for private in ("docs", "scripts", "vendor", "Gemfile", "README.md", ".DS_Store"):
    if (SITE / private).exists():
        errors.append(f"private source included in output: {private}")
for required in ("sitemap.xml", "robots.txt", "assets/images/social.jpg"):
    if not (SITE / required).is_file():
        errors.append(f"missing search/share asset: {required}")
sitemap = SITE / "sitemap.xml"
removed_legal_urls = set()
for locale in LOCALES:
    if locale["key"] == "en":
        continue
    for group in ("privacy", "terms"):
        route = locale["home"].lstrip("/") + GROUPS[group]
        removed_legal_urls.add(ORIGIN + BASE + "/" + route)
        if (SITE / route).exists():
            errors.append(f"removed legal translation still generated: {route}")
        filename = "privacypolicy" if group == "privacy" else "termsofservice"
        if (ROOT / "_pages" / f"{locale['key']}-{filename}.md").exists():
            errors.append(f"removed legal translation still in source: {locale['key']}-{filename}.md")
if sitemap.is_file():
    urls = {node.text for node in ElementTree.parse(sitemap).iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")}
    if urls & removed_legal_urls:
        errors.append("removed legal translations still in sitemap")
    for path, page in pages.items():
        if path == "404.html":
            continue
        if page.canonical[0] not in urls:
            errors.append(f"page missing from sitemap: {page.canonical[0]}")
if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(pages)} pages / {len(LOCALES)} landing locales; English-only legal pages, headings, locale menus, SEO, links, product copy and output exclusions.")
