---
title: 按开发场景找文档速查（自写文档）
source: 原创文档（本项目产出，非 docs.dao3.fun 原文）
---

# 按开发场景找文档速查

给在 ArenaPro/Arena 项目里干活的 agent 和人：不跑任何工具，按场景直接打开下列路径（相对 `docs-md/`，Skill 内对应 `references/docs/` 同结构）。已按真实文件逐一核对。

## ArenaPro 插件（VSCode 写游戏代码）

| 场景 | 读这些 |
| --- | --- |
| 环境装好但连不上/看不到扩展地图 | `guide/02-getting-started/03-connect-to-cloud.md` |
| 第一个项目跑通 | `guide/02-getting-started/02-create-project.md` → `guide/03-basic-tutorial/01-hello-world-tutorial.md` |
| 保存后代码不生效 | `guide/04-development-workflow/hmr.md`（热更新）与 `guide/04-development-workflow/compilationPrinciple.md`（Alt+Q 全量构建的区别） |
| 打断点、看调用栈 | `guide/04-development-workflow/debugger.md`、`guide/04-development-workflow/debug.md` |
| 写组件：生命周期该用哪个钩子 | `package/component/componentGuide/lifecycle.md`（onLoad→onEnable→start→update） |
| 组件创建/销毁/装饰器 | `package/component/componentGuide/create-destroy.md`、`decorator.md` |
| 组件拿节点、基础接口 | `package/component/componentGuide/access-node-component.md`、`basic-node-api.md` |
| 跨组件通信、事件 | `package/component/componentGuide/event-node.md`、`event-world.md`、`guide/05-best-practices/communicationAgreement.md` |
| 时间/性能/系统类组件 | `package/component/componentGuide/system.md`、`time.md`、`performance.md` |
| 查类与方法的权威签名 | `package/component/api/` 五篇：Component、EntityNode、EventEmitter、NodeSystem、NodeTime |
| 存档/回放（时间回溯） | `package/component/timeRewindSystem/`：timeRewindComponent → intermediateTopics → advancedTopics |
| 游戏内 UI（React） | `package/react/reactGuide/setup.md`、`xml.md`（box/text/image 标签）；事件 `eventHandlers.md`；状态 `hooks.md`（含 useScreenSize） |
| 引第三方 npm 包 | `guide/06-advanced-topics/npmPackage.md`；专用库：remeda、zod、gl-matrix、simplex-noise、pathfinding-rbush 各有专章 |
| 发自己的包 | `guide/07-publishing/createNPMProject.md`、`guide/06-advanced-topics/local-npm-package.md` |
| JSON 存档/配置数据 | `guide/06-advanced-topics/json.md` |
| 图片音效资源 | `guide/06-advanced-topics/resources.md`、`uploadResources.md`、`asset-synchronization.md` |
| 多语言 | `guide/06-advanced-topics/i18n.md` |
| 分包/多入口/环境变量/webpack | `guide/06-advanced-topics/bulidName.md`、`env.md`、`webpackPlugins.md` |
| 发布导出到 Arena | `guide/06-advanced-topics/toArena.md` |
| 存储权限被拒 | `authority/storage.md`；配置文件 → `dao3Cfg/file.md`、`dao3Cfg/attribute.md` |
| Arena 代码搬到 ArenaPro 报错 | `difference/` 按 API 名找同名篇（dialog、voxel、storage、resourcePath、customizeEntity、remoteChannel、findChildByName） |
| 让 IDE 里的 AI 直接查文档 | `mcp/chat-only-knowledgebase.md` |

## Arena 编辑器与其平台 API（`arena-official/`，Apache-2.0 镜像）

| 场景 | 读这些 |
| --- | --- |
| Arena 编辑器入门、建模、写代码、发布 | `arena-official/getting-started/` 四篇：create → helloWorld-models → helloWorld-code → publish |
| SEL 联赛规则/赛事地图接入 | `arena-official/SEL/sel-rules.md`、`map-Info.md`、`map-integration.md` |
| 编辑器功能、核心概念 | `arena-official/editor/`、`core/`、`features/` |
| 写游戏脚本查平台 API | `arena-official/api/<类名>/`：GameWorld、GamePlayerEntity、GameEntity、ClientWorld、ClientUI、ClientAudio、Sound、RemoteChannel、GameDataStorage、GameHttpAPI 等；总览 `arena-official/api/index.md` |
| js 模块与入口机制 | `arena-official/javascriptEntry/`、`arena-official/javascriptDaoAPI/`、`plugIns/` |

不确定属于哪个场景时：先扫 `README.md` 导航树，再按目录命名规律（`guide/0X-主题/`、`api/<类名>/`）进目录通读。
