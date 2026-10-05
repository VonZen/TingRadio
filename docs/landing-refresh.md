# Ting Radio landing 改版记录

## 范围与默认方向

- 保留 GitHub Pages / Jekyll；不迁移框架。
- 默认英文入口 `/`；保留简体中文 `/zh/`，新增繁体中文与西班牙语、德语、法语、俄语、意大利语、希腊语、荷兰语、波兰语、葡萄牙语；保留 App 内引用的法律页面路径。
- 使用 App 的暖白、品牌橙、品牌图形与当前英文 App 界面截图。
- 官网按当前 App 功能介绍，不展示版本号；发布时间与平台分发无需再确认。
- 本地改版；未发布网站、未修改 App 源码。最新阶段按用户授权在 iPhone 17 Pro 模拟器中拍摄素材。

## 内容依据

| 内容 | 来源 | 页面约束 |
| --- | --- | --- |
| 品牌橙 / 动作色 | `ting_radio/Shared/Core/AppColors.swift` | #E05E0C 用于装饰，#AD4300 用于可读文字与按钮 |
| 系统要求 | `ting_radio/project.yml` | iOS 18、macOS 15、watchOS 11；不展示 App 版本号 |
| Free / Pro | `ting_radio/Shared/Core/ProBenefit.swift` | 识曲 5 次/日、歌词 10 次/日；睡眠预设和基础可视化免费；其余权益以 App 内为准 |
| 识曲 | ShazamKit 相关实现 | 识别支持的电台音频；并非所有流可用；Watch 不支持 |
| 歌词 | Lyrics / NowPlaying 实现 | 取决于音源和歌词数据；逐字歌词不是全量保证 |
| 闹钟 | RadioAlarm / AlarmKit 实现 | 采用“电台自动叫醒”；小字注明 iOS 26+、Pro、闹钟权限及响铃后点按打开电台 |
| 设备协同 | CompanionStationSync | 已实现 iPhone 与配对 Watch 的收藏 / 最近 / 自定义电台同步；不宣称全设备云同步 |
| CarPlay | CarPlay scene 与 ProBenefit | 基础播放与 Pro 分类浏览分开；兼容环境限制保留，分发无需确认 |
| 广告 | ProBenefit / 新增 AdMob 方案文档 | 未实现广告系统，不销售“去广告”权益，不承诺电台音源无广告 |
| 内容回放 | 播放器 / 分享实现 | 分享电台地址；没有已验证的录制或离线回放，不宣传 |

## 实施与 review 阶段

1. 内容与发布边界：事实表、双语文案与待确认清单，独立 review。
2. 视觉与页面实现：响应式页面、真实品牌资产、可访问交互，独立 review。
3. 构建与浏览器验证：链接、语言、无 JS、移动尺寸、法律页面兼容，独立 review。

阶段一完成：独立 reviewer 核对源码，删除旧 Flutter 识曲登录限制，明确 HLS 对歌词/识曲/可视化的限制；双语补审通过。

阶段二静态 review 的语言记忆、中文法律链接语言标记和小字可读性问题已修正。实际桌面和 320px 英文全页截图补审通过。需要用户确认的内容集中在 `pending-confirmations.md`。


## 最终验证（2026-10-04）

- 阶段三独立 review：修复语言切换 click 冒泡覆写偏好的问题，只绑定 `a[data-language]`；8 项事件/导航/Storage 拒绝验证通过。无其他未修复 P1/P2。
- GitHub Pages 官方依赖 github-pages 232 / Jekyll 3.10，Ruby 3.3.12 本地生产构建通过。Ruby 4 与当前 GitHub Pages commonmarker 依赖不兼容，因此安装独立、未链接为系统默认的 Ruby 3.3 供验证；默认 Ruby 与 shell 配置没有更改。
- 最终 `JEKYLL_ENV=production` 构建到独立 `/tmp/ting-radio-refresh/production-site`，避免开发服务器 localhost canonical 混入生产校验。
- `scripts/validate_site.py` 对独立生产输出通过：英文、简体中文、两份法律页面与 404；标题、lang、h1、canonical/hreflang、下载链接、本地资源与锚点、分享与搜索资产、内部文档排除。
- 双语 YAML 键、数组数量与嵌套类型一致；JavaScript 语法与 `git diff --check` 通过。
- 初版改造仅更换法律页面样式；本轮按用户指示重写中英文正文，见下方追加记录。
- 实际 Chrome 网页响应式检查：英文 320 / 390 / 768 和桌面；中文 320 / 390 / 768 / 1280。测得各检查宽度 scrollWidth 等于 innerWidth，main 元素无横向溢出；首屏加载图片无损坏。
- 实际浏览器验证中英文双向切换、回访恢复中文偏好；关闭 JavaScript 后中文/英文页面、导航与静态下载入口仍可用。
- 键盘 Tab 首次到 Skip link，Enter 聚焦 main，下一次 Tab 到主下载入口。已为系统 reduced-motion 提供 CSS 降级；未声称完整辅助技术认证。
- 没有运行 App 或模拟器。没有推送、部署、创建 PR，也没有修改关联 App 仓库。

截图保存在 Codex 本地可视化目录 `ting-radio-landing-refresh/`；部分中文截图上的粉色悬浮按钮来自本机 Chrome 翻译扩展，不属于网站代码。

初版限制：当时尚未补充最新真实 App 截图；未对远端发布执行验证，也未做正式网络节流性能基准或全浏览器兼容测试。当前截图已在下方新阶段补齐。

## 用户决定落实（2026-10-04）

- 移除官网及分享卡版本号；Free / Pro 保留功能差异，移除价格措辞。
- 电台自动叫醒采用用户指定命名，条件移至小字；锁屏实时歌词与统计营销不展示。
- 中英文品牌与文案由本次改版确定；上述事项均不再等待确认。
- 隐私政策与服务条款依据原生 App 当前代码重写，新增对应中文页；保留原英文路径与双语切换。
- 本地处理、Radio Browser 搜索/点击/投票、IP 地区、ShazamKit、歌词与封面来源、RevenueCat 启动校验、Watch 协同、AlarmKit、GitHub 托管与网站语言存储分别披露。
- 不虚构法定主体、管辖地、第三方保留期限，也不将未来广告方案或历史 Flutter SDK 当作现状。

事实依据：`Shared/Core/{IPLocation,RadioBrowserClient,PremiumStore,ShazamRecognition,iTunesArtworkLookup,CompanionStationSync}.swift`、`Shared/Lyrics/LyricsRepository.swift`、`Shared/Alarm/RadioAlarmService.swift` 及 `project.yml`。外部处理说明核对了 Apple ShazamKit、App Store EULA/取消订阅/退款文档、RevenueCat Apple 隐私指引、GitHub Pages 与隐私声明。官方链接收录于政策和条款正文中。

追加验证通过：隐私源码 reviewer 与最终导航 reviewer 独立补审；修正后台播放和支付资料措辞。生产构建覆盖 7 页，六个翻译页面的 canonical/hreflang、法律页对应语言切换、首页专用偏好重定向均校验通过。浏览器实际验证四份法律页双向切换与 320px 布局，无横向溢出；自动叫醒备注在 320px 为 12px，内容完整。新版分享卡去除版本号，保留原字体方向。JS 语法、双语 YAML 结构与 diff 检查通过。

新增截图：`privacy-zh-320-updated.png`、`everyday-zh-updated.png`，位于同一 Codex 可视化目录。本轮同样未运行 App/模拟器，未推送或部署。

## 十二语言国际化（2026-10-04）

- 英文为默认入口和 SEO x-default；浏览器旧语言偏好不再触发重定向，不依据系统语言自动切换。每个语言 URL 固定显示对应语言。
- 十二种语言覆盖首页、隐私政策和服务条款，共 36 个内容页面及英文 404；保留原英文与简体中文路径。
- `_data/languages.json` 管理原文语言名称、BCP 47 标签、Open Graph locale 与路径。简体/繁体分别使用 zh-Hans / zh-Hant；葡萄牙语采用欧洲葡萄牙语文案与通用 pt 路径。
- 原生 details/summary 语言选择器无需 JS 即可导航；JS 仅补充 Escape 返回焦点与点击外部关闭。切换隐私或条款时保留文档类别。政策已同步说明不保存浏览器语言偏好。
- 三个子代理分组翻译后交叉审查其他组，修正法语歌词时间与提供方限定、希腊语崩溃上报措辞、俄语与波兰语表达；分享图片 alt 改为对应语言文案。
- 构建集成修复了七个语言首页缺少 landing include 的问题；生产 validator 校验 37 页的标题/语言/h1、十二选项路径与当前语言、精确 canonical/hreflang、法律链接、下载与资源锚点、36 个内容页面 sitemap、内容约束和内部文档排除。
- 浏览器实际检查 12 个首页各 320 / 768 / 1280px 共 36 个场景，及 24 个法律页面的 320px 布局；页面、文字、导航与分类卡片均无溢出或裁切。长分类名称增加自动断词及换行。
- 实际浏览器验证法语隐私切到希腊语及葡萄牙语后仍是隐私页；语言菜单 Escape 关闭并返回焦点、外部点击关闭、底部选项可选；返回默认入口保持英文。
- JS 轻量 VM 验证不读取语言存储、不触发自动跳转，并覆盖菜单内部/外部点击与 Escape；全部 YAML 结构和注册元数据一致。

新增截图 `i18n-default-en-menu.png`，完整布局检查结果为 `i18n-layout-checks.json`，保存在原 Codex 可视化目录。尚未推送或部署；未修改关联 App，未运行 App 或模拟器。

## 页面精简（2026-10-04）

按用户要求移除所有语言首页的 Free / Pro 对比区块及导航入口，并从所有页面页脚移除制作署名与电台内容说明。清理十二语言数据中的对应文案；保留版权行、联系与法律链接。首页其他功能说明及政策正文保持原有含义。

## 真实 App 展示与权益卡（2026-10-04）

用户在参考 RGB Radio 页面后明确需要权益功能卡，并授权自行运行 iPhone 17 Pro 模拟器拍摄一套英文素材，完成素材后实施。

- 构建关联 App 当前工作区，在 iPhone 17 Pro / iOS 27 模拟器拍摄 Genres、Player、Song History、Sleep Timer；不修改原生源码、不启用测试数据。使用真实电台播放及其元数据，未用旧测试电台、未伪造成功识曲或歌词。
- 四张 1206×2622 PNG 保留原比例转 WebP，总计约 619 KiB；所有语言共用一套英文素材，文字与 alt 完整本地化。素材 provenance 见 `assets.md`。停止 App、关闭临时模拟器浏览服务，并恢复临时状态栏和 Reduce Motion 设置。
- 首屏采用两张真实界面和品牌底色；紧接着三张产品展示说明发现、播放、歌曲历史。手机使用可手动横向滚动的截图画廊，无自动轮播、无新 JS 依赖。
- 六张权益卡分别介绍发现与收藏、识曲与歌词、歌曲历史、睡眠定时、驾驶与 CarPlay、电台自动叫醒；清楚标注已包含与 Pro 扩展范围，保留准确的流媒体和设备限制。
- 产品事实独立 review 修正了驾驶权益描述：基础 CarPlay 包含，专门驾驶视图与 CarPlay 曲风/心情浏览需要 Pro。叫醒继续明确系统先响铃，点按 Open Station 后开始播放；版本与权限条件在小字中保留。
- 使用现有官方英文 App Store 标识与本地 SVG 图标；继续保留暖白与橙色、十二语言菜单、简洁版权及法律页脚。
- 十二份 YAML 的键、嵌套类型、图片及图标顺序一致；每种语言均有三张展示和六张功能卡。生产 validator 新增对共享截图、原生图片尺寸与权益区完整性的检查。
- 独立 UI review 结合实际桌面和手机截图通过，无阻塞项。浏览器实际验证十二语言 × 320 / 768 / 1280px 共 36 个布局：页面、导航与正文无溢出；320px 的画廊水平滚动限于自身范围，ArrowRight 键盘滚动正常。
- 实际浏览器验证菜单 Escape 返回焦点、外部点击关闭、最后一个葡语选项可选，葡语隐私政策切换繁体后仍保持隐私页，320px 法律页面无溢出。
- 最终独立复核通过：52 个模板使用键在全部语言中齐全且非空，权益与原生 gate 实现一致；所有首页均无禁止营销文案、旧对比表或个人署名。最终生产构建与 37 页 / 12 语言 validator、`git diff --check` 通过。

新增浏览器证明保存在同一 Codex 可视化目录：`real-app-hero-en.png`、`real-app-showcase-en.png`、`benefit-cards-en.png`、`real-app-mobile-zh.png`、`real-app-gallery-mobile-zh.png`、`real-app-tablet-de.png`、`real-app-mobile-en-320.png`，最终完整区块截图为 `real-app-hero-zh-final.png`、`benefit-cards-zh-final.png`，完整布局数据为 `real-app-layout-checks.json`。当前没有阻塞实施的待确认项；未推送或部署。
