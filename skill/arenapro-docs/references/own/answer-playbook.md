---
title: ArenaPro 答题与写码手册（自写文档，非 ArenaPro 官方内容）
author: 后端（本 Skill 制作者）
---

# ArenaPro 答题与写码手册

官方文档按"人怎么学"组织，这份手册按"问题怎么来"组织：拿到一个问题，先路由，再检索，最后按规范作答。路径均为 `references/docs/` 下真实文件。

## 问题路由表

| 问题类型 | 首选检索词 | 直达文档 |
| --- | --- | --- |
| 「装好后连不上/看不到地图」 | 连接 云端 / 扩展地图 | `guide/02-getting-started/03-connect-to-cloud.md` |
| 「改了代码没生效」 | HMR / Alt+Q / 构建 | `guide/04-development-workflow/hmr.md`、`guide/04-development-workflow/compilationPrinciple.md` |
| 「怎么断点/Debug 和 Release 有何不同」 | 断点 调试 | `guide/04-development-workflow/debugger.md`、`guide/04-development-workflow/debug.md` |
| 「组件什么时候初始化/顺序是什么」 | 生命周期 onLoad | `package/component/componentGuide/lifecycle.md` |
| 「组件间怎么传数据/事件」 | 事件 通信 | `package/component/componentGuide/event-node.md`、`package/component/componentGuide/event-world.md`、`guide/05-best-practices/communicationAgreement.md` |
| 「存档/读档/回退时间」 | 时间回溯 | `package/component/timeRewindSystem/timeRewindComponent.md` |
| 「UI 怎么写/按钮点击」 | onClick / 事件处理器 | `package/react/reactGuide/eventHandlers.md`、`package/react/reactGuide/api.md` |
| 「界面尺寸/屏幕适配」 | useScreenSize | `package/react/reactGuide/hooks.md` |
| 「资源传不上去/图片音效」 | 资源 上传 | `guide/06-advanced-topics/resources.md`、`guide/06-advanced-topics/uploadResources.md`、`guide/06-advanced-topics/asset-synchronization.md` |
| 「能不能用某个 npm 库」 | 白名单 npm | `guide/06-advanced-topics/npmPackage.md`；三个专章：`guide/06-advanced-topics/remeda.md`、`guide/06-advanced-topics/gl-matrix.md`、`guide/06-advanced-topics/simplex-noise.md`、`guide/06-advanced-topics/pathfinding-rbush.md`、`guide/06-advanced-topics/npm-zod-runtime-validation.md` |
| 「发布到平台/构建产物」 | 导出 Arena / 发布 | `guide/06-advanced-topics/toArena.md`、`guide/06-advanced-topics/bulidName.md`（源站如此拼写）、`guide/07-publishing/createNPMProject.md` |
| 「读档/存档被拒/权限」 | storage 权限 | `authority/storage.md`；配置项 → `dao3Cfg/file.md`、`dao3Cfg/attribute.md` |
| 「这段 Arena 代码为何在 ArenaPro 报错」 | 按 API 名查差异 | `difference/` 七篇（dialog、voxel、storage、resourcePath、customizeEntity、remoteChannel、findChildByName） |
| 「多套入口/分包/环境变量」 | 入口 分包 / 环境变量 | `guide/06-advanced-topics/bulidName.md`、`guide/06-advanced-topics/env.md` |
| 「让 AI 查文档的 MCP 方式」 | 知识库 | `mcp/chat-only-knowledgebase.md` |

## 检索降级阶梯（AND 无命中时按序尝试）

1. 中英互换：热更新↔HMR、组件↔component、生命周期↔lifecycle、发布↔publish、存档↔storage。
2. 减词：`search.py 生命周期` 命中散，加词 `onLoad 生命周期`；命中为零，去掉限定词只留 API 名。
3. 换 `--files` 看排名而非正文行：命中措辞可能跨行分散。
4. `--toc` 通读 91 篇标题，人工判定章节后在该路径内定向检索。
5. 仍无 → 走下面的"未覆盖协议"，禁止编造。

## 写码时的硬性检查清单

生成 ArenaPro 代码前后各过一遍：

- API 名与签名逐个能在文档中命中（`search.py 确切API名` 零命中即可疑）；
- 组件生命周期顺序按 `package/component/componentGuide/lifecycle.md`：onLoad → onEnable → start → update（lateUpdate 在动画/物理后）；不要套用 Unity/UE 的钩子名；
- React 侧只用 `@dao3fun/react` 文档列出的标签（box、text、image）与属性；HTML 标签默认不成立；
- import 路径以文档示例原文为准（`from "@dao3fun/react"` 等），不自造包名；
- 引擎差异 API 先查 `difference/`，Arena 写法不能直接搬；
- 事件/存档涉及权限时核对 `authority/storage.md`；
- 交付时说明构建方式：调试用 HMR，发布用 Alt+Q 完整构建（两者行为差异见 `guide/04-development-workflow/compilationPrinciple.md`）。

## 出处引用规范

- 单个结论：`《文档标题》 + frontmatter source URL`；
- 多文档综合：逐小节标注，标题与 URL 一一对应，不许合并出处；
- 转述与原文区分：给出代码块时注明"摘自文档示例"或"基于文档改写"；
- 快照时效：引用超过 30 天前，答复末尾附"文档可能已更新，可跑 refresh_docs.py 同步"。

## 未覆盖协议

文档没有的内容分两类处理，不许含糊：

1. **合理推断**：给出答案但显式声明"文档未覆盖，以下基于 X 章节外推，请以实机验证"；
2. **无从推断**（版本兼容、平台限制、账号权限）：直说"官方文档未记载"，给出验证路径（`search.py --toc` 自查 + docs.dao3.fun 站内搜 + 社区 `community/` 渠道）。
