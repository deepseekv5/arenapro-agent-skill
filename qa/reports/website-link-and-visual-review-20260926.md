# 官网 QA 报告 — 外链可达性 + 视觉渲染审查

- 执行人：测试 (cpart_01m3f0ae4nbtpww813cf9awtjn)
- 时间：2026-09-26 22:20–22:35 UTC（本机 14:20–14:35）
- 被测对象：`arenapro-project/website/index.html`
- 快照说明：审查期间前端仍在持续编辑（index.html mtime 22:26 / 22:28，styles.css 22:27）。
  链接核查与视觉结论以 **22:28 版**为准；22:21 版（V1 尾部）发现的问题单独标注是否在新版复现。
- 方法：`curl` HTTP 状态探测 + GitHub API 仓库枚举；Chrome headless 全页截图（桌面 1440 / 窄屏）+ PIL 像素级对比度量化 + 注入脚本测量页面溢出。
- 证据目录：`qa/evidence/`（desktop-full.png、v2-desktop-full-seg0..4.png、v2-mobile-full-seg0..5.png、zoom-term-block.png、probe*.html）

---

## 任务 1：外链可达性

| # | 链接 | 状态 | 结论 |
|---|------|------|------|
| 1 | https://github.com/Box3Lab/box3-editor-support-for-vscode | **404** | **缺陷 P1（V1 报告属实，V2 仍存在）**。组织 `Box3Lab` 存在（200），其公开仓库共 16 个（ArenaPro-Creator、ArenaPro-CLI 等），**不含** `box3-editor-support-for-vscode`；GitHub 全局搜索该仓库名 0 结果。index.html 中 2 处引用：社区卡（"GitHub — ArenaPro 官方仓库"）与页脚。 |
| 2 | https://docs.dao3.fun/arenapro/zh/ | 200 | 正常 |
| 3 | https://docs.dao3.fun/arenapro/en/ | 200 | 正常 |
| 4 | https://docs.dao3.fun/arenapro/zh/community/release-notes.html | 200 | 正常 |
| 5 | https://docs.dao3.fun/arenapro/zh/mcp/chat-only-knowledgebase.html | 200 | 正常 |
| 6 | https://docs.box3lab.com/apapi/ | 200 | 正常 |
| 7 | fonts.googleapis.com/css2?...（字体样式表） | 200 | 正常 |
| 8 | https://fonts.googleapis.com / https://fonts.gstatic.com（preconnect 根域） | 根路径 404 | **非缺陷**。根域返回 404 是 Google Fonts 正常行为，preconnect 只需域名可达；实际资源走第 7 行 URL。 |
| 9 | qm.qq.com QQ 群链接 | 200 | 正常（HTML 中 `&amp;` 转义正确，浏览器解析无问题） |
| 10 | 相对链接 `../README.md`、`../docs-md/skill/overview.md`、`../docs-md/skill/installation-and-usage.md` | 文件均存在 | 本地/项目库语境可用。**提示（低优先级）**：若站点将来部署为公网静态站，点击 `.md` 链接浏览器会显示原始文本，建议届时改为渲染后页面或加说明。 |

**GitHub 404 修复建议（供前端/总管决策，QA 不改码）**：改指 `https://github.com/box3lab`（组织页）或确认正确仓库名（候选：`ArenaPro-Creator`），或直接移除该卡并在 V2 内容改版时替换为项目库/GitHub 正确入口。

## 任务 2：视觉渲染审查

### P1 — 04 节终端代码块文字近乎不可读（V1、V2 均存在，已量化）

- 现象：「安装与使用」三个步骤中 `.term` 深色代码块内文字为深绿色，近黑底上几乎看不清。
- 实测：截图像素采样，文字最亮像素 RGB(9,67,58) ≈ `#0A443B`（`--accent-ink`），代码块底色 `#14161B`，**对比度 1.62:1**，远低于 WCAG AA 正文 4.5:1。
- 根因（代码走读）：`styles.css:675` 组合选择器 `.pos-item code, .who-card code, ..., .start-step code, ...` 将 `.start-step` 内所有 `code` 设为 `color: var(--accent-ink)`；而 `<pre class="term"><code>…</code></pre>` 恰好位于 `.start-step` 内，被误伤。旁证：侧栏 `.start-aside` 中同款 term 块（`$ export ARENAPRO_DOCS_DIR=…`）颜色正常（`#9CD2BE`），因为不在 `.start-step` 下。
- 复现：浏览器打开 `website/index.html` → 定位 `#install` → 观察步骤 1/2/3 代码块 vs 右侧栏代码块。
- 修复建议（移交前端）：给 `.term code` 显式设定 `color: inherit`（或从 675 行选择器排除 `pre code`）。

### P2 — 窄屏横向溢出（仅 22:21 V1 快照出现，22:28 V2 快照未复现）

- V1 快照实测：485px 视口下 `documentElement.scrollWidth=587`，hero 标题、正文、卡片右缘被裁切（见 mobile-full-seg0/1/3.png）。
- V2 快照（22:28，注入脚本 probe3.html 排除滚动容器后枚举）：485/585/845px 三个宽度均无页面级溢出，移动端布局正常。
- 状态：疑似已被前端并行修改顺带修复；建议保留 `.term { overflow-x: auto }` 并在 V2 定稿后真机复测。
- 置信度说明：headless Chrome 窗口最小宽度钳制，**390px 真机档位未验证**，列入 V2 复测清单。

### P3 — 低优先级视觉/内容观察（V2）

1. 社区卡文案「ArenaPro 官方仓库（插件源码与 Issue）」与站点新定位（Agent Skill 介绍站）不符，且链接 404——内容层，待 V2 定稿复测。
2. 06 社区卡与尾章之间空白约 300px，节奏略松；桌面端 03 能力网格到 04 之间同样偏空。属设计品味项，非缺陷。
3. hero 右侧 agent mock 阴影 `14px 14px 0` 在窄容器贴边时右侧留白偏紧，485px 下正常。

### 通过项（桌面 1440，V2）

- 字体（Space Grotesk / Noto SC / IBM Plex Mono）加载渲染正常，无样式丢失、无图片破图、无元素重叠。
- 纸墨配色体系一致，章节编号、分隔线、卡片网格对齐良好。
- 可访问性基线良好：skip-link、nav `aria-expanded/controls`、`prefers-reduced-motion` 降级、`:focus-visible` 样式均在代码中确认存在。

---

## 结论与 V2 复测清单

- 阻塞级问题 1 个（P1 term 代码块对比度），内容错误 1 个（P1 GitHub 404，两处），均证据齐全，移交前端处理；QA 未改动任何产品文件。
- V2 定稿后需复测：① 上述两项修复验证；② 390px 真机/DevTools 视口；③ 内容层（Skill 定位文案、docs-md 数字口径 89 页一致性）。
