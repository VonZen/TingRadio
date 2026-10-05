# Ting Radio website

Official multilingual landing page for Ting Radio. Built with GitHub Pages / Jekyll, native HTML, CSS, and a small progressive-enhancement script.

## Local preview

Use Ruby 3.3, matching the [GitHub Pages supported dependency line](https://pages.github.com/versions/). Ruby 4 cannot resolve the current GitHub Pages dependency set.

```sh
rtk proxy bundle install --jobs 1
rtk proxy bundle exec jekyll serve --host 127.0.0.1
```

Open `http://127.0.0.1:4000/TingRadio/` for English. Other languages use their own paths, including `/zh/`, `/zh-hant/`, `/es/`, `/de/`, `/fr/`, `/ru/`, `/it/`, `/el/`, `/nl/`, `/pl/` and `/pt/`. If your default Ruby is 4, select a Ruby 3.3 executable for Bundler without changing the system default.

## Validate

```sh
rtk proxy bundle exec jekyll build
rtk proxy python3 scripts/validate_site.py
```

The validator checks all 15 generated pages, the 12-language landing-page selector, locale metadata, shared English legal routes, sitemap entries, base-path links and private-source exclusions. It also checks that removed legal translations are absent. Browser checks cover responsive layout, English as the default, keyboard navigation and native language selection.

## Edit content

- `_data/languages.json`: language names, locale tags and paths; English is first and is the default.
- `_data/landing/*.yml`: matching translation keys, screenshot captions and six feature/entitlement cards for each language.
- `_includes/landing.html`: shared landing structure.
- `assets/css/site.css`: app-aligned palette and responsive styles.
- `assets/js/site.js`: closes the native language selector on Escape or an outside click. Locale URLs determine language; no browser preference or automatic redirect overrides English at `/`.
- `_pages/`: English-only privacy policy and terms, based on the current native app. All website languages link to `/privacypolicy/` and `/termsofservice/`, matching the app's current links.
- `_config.yml`: production URL/base path, static App Store destination and sitemap.

The site describes the current app without a version badge or pricing comparison section. Six feature cards explain included and Pro benefits. Radio wake-up uses a small-print note for system requirements and its Open Station action. Lock Screen lyrics and statistics are omitted from marketing. The footer keeps the copyright line and useful links. Internal docs and validation scripts are excluded from the public build.

Translated landing-page frontmatter uses `translation_key: home`. The shared selector and hreflang entries link the corresponding landing pages. Legal pages use `translated: false` and `english_only: true`, with no language selector or translation metadata. All pages remain static and accessible without JavaScript.

## Assets

The hero and product showcase use current App screenshots captured on an iPhone 17 Pro simulator. All locales share one English set, with localised captions and alt text. Brand images come from the associated native App repository. Screenshots are compressed to WebP at their original dimensions; phone frames and icons use local CSS/SVG. No third-party fonts, icon CDN, jQuery, remote App Store lookup or analytics are required. See [asset provenance](docs/assets.md).
