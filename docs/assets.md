# 素材来源与处理

原项目：`/Users/vonzen/CodeX/ting_radio/Shared/Resources/`。

| 网站素材 | App 原始素材 | 处理 |
| --- | --- | --- |
| vinyl.webp | TingRadioCategoryIcons.xcassets/OnboardingWelcomeVinyl.imageset/OnboardingWelcomeVinyl.png | 原图转 WebP |
| jazz.webp / classical.webp | discovery_genre_jazz / discovery_genre_classical 的 jpg | 原图转 WebP |
| focus.webp / chill.webp / sleep.webp | discovery_mood_focus / discovery_mood_chill / discovery_mood_sleep 的 jpg | 原图转 WebP |
| brand-mark.png | Ting.icon/Assets/icon.png | 缩小至 256px |
| app-icon.png / apple-touch-icon.png | Ting.icon/Assets/icon.png 与 icon.json 原有橙色背景 | 原有图层按 0.65 比例合成静态网站图标，不是新设计的 App 截图 |
| social.jpg | vinyl.webp 与品牌文案 | 1200×630 分享卡，本地生成 |

页面摄影是 App 已有分类/欢迎素材，用于传递聆听场景；不伪装成当前原生 UI 截图。没有新增外部摄影、字体、图标或人物素材。页面使用系统字体，分享图使用本机 Avenir Next 渲染，不分发字体文件。

## 当前 App 截图（2026-10-04）

按用户授权，构建关联 App 当前工作区，在 iPhone 17 Pro / iOS 27 模拟器中使用英文界面拍摄。没有改动 App 源码，也没有启用 UI 测试数据、伪造歌词或识曲成功状态。

| 网站素材 | 真实界面 | 原图与处理 |
| --- | --- | --- |
| genres-en.webp | Genres 曲风列表与迷你播放器 | 1206×2622 PNG 转 WebP，保留完整比例 |
| player-en.webp | Classic Vinyl HD 播放页 | 1206×2622 PNG 转 WebP，保留完整比例 |
| song-history-en.webp | Song History；真实电台播放产生的歌曲元数据 | 1206×2622 PNG 转 WebP，保留完整比例 |
| sleep-timer-en.webp | Sleep Timer 预设与自定义入口 | 1206×2622 PNG 转 WebP，保留完整比例 |

四张截图共约 619 KiB。所有语言使用同一组英文截图，标题、说明和 alt 按页面语言翻译。截图仅格式压缩，无界面重绘、内容替换或裁切；网页的圆角与边框是 CSS 展示效果。拍摄时临时统一状态栏，并关闭文字滚动；拍摄后清除状态栏覆盖、恢复 Reduce Motion 原设置并停止 App。临时模拟器浏览服务已关闭。

完整 PNG 原图保存于 `/Users/vonzen/.codex/visualizations/2026/10/03/01a1024b-b0e0-74a3-87b8-fcc6ff46ff0c/ting-radio-landing-refresh/native-captures/`。下载按钮复用项目现有 `assets/appstore.png` 官方英文 App Store 标识；功能图标为本地 SVG，不新增外部依赖。
