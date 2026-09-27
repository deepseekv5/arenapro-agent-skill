---
name: arenapro-docs
description: ArenaPro（神岛/dao3）与 Arena 编辑器的任务导向文档库。在 ArenaPro/Arena 项目里开发时使用：要写组件、调 HMR、发布构建、用 @dao3fun/react、配权限、接平台 API 等场景，按本文件的任务路由直接定位并通读 references/docs/ 下对应的 Markdown 文档（glob/grep/read 直读，不依赖任何脚本）。涉及 ArenaPro 插件、神岛、dao3、VSCode 游戏脚本、组件生命周期、EntityNode、HMR、npm 包、React UI、dao3Cfg、权限、MCP、Arena 编辑器、SEL、地图集成、Game*/Client* API 的问题与编码任务都应触发本 Skill；也用于查询本 Skill 的安装与使用方法。
---

# ArenaPro / Arena 任务文档路由

## 这个 Skill 怎么工作

内置 ArenaPro 中文文档 + Arena 官方产品文档（Apache-2.0 镜像）共 300 篇 Markdown。你的用法不是跑检索工具，而是：**判断开发任务 → 按下方路由表直接 Read 对应文件 → 依据原文作答/写码**。文档就放在本目录 `references/docs/` 下，用你自带的文件能力（glob、grep、read）即可，任何环境都工作。路由表没覆盖时，按「目录地图与命名规律」自行定位，再不通读兜底协议。

## 开发任务 → 该读哪几篇（主路由表）

路径均相对 `references/docs/`。写码任务先读路由列出的篇目再动手。

### ArenaPro 插件工具链（VSCode 开发）

| 你要做的事 | 直接读 |
| --- | --- |
| 第一次配置环境 / 连不上云端 | `guide/02-getting-started/01-install.md`、`guide/02-getting-started/02-create-project.md`、`guide/02-getting-started/03-connect-to-cloud.md` |
| 跑通第一个世界 / 理解 TS 约定 | `guide/03-basic-tutorial/01-hello-world-tutorial.md`、`guide/03-basic-tutorial/typescript-vs-javascript.md` |
| 改了代码没生效 / 热更新配置 | `guide/04-development-workflow/hmr.md`、`guide/04-development-workflow/compilationPrinciple.md` |
| 断点调试 / Debug 与 Release 差异 | `guide/04-development-workflow/debugger.md`、`guide/04-development-workflow/debug.md` |
| 写/改组件：创建、销毁、装饰器 | `package/component/componentGuide/create-destroy.md`、`decorator.md`、`component.md` |
| 组件生命周期顺序与回调 | `package/component/componentGuide/lifecycle.md` |
| 组件访问节点/基础 API | `package/component/componentGuide/access-node-component.md`、`basic-node-api.md` |
| 节点/世界事件通信 | `package/component/componentGuide/event-node.md`、`event-world.md`；共享数据结构约定 → `guide/05-best-practices/communicationAgreement.md`、`codeReuse.md` |
| 节点系统、时间管理、性能优化 | `package/component/componentGuide/system.md`、`time.md`、`performance.md` |
| 时间回溯（存档/回放） | `package/component/timeRewindSystem/timeRewindComponent.md`、`intermediateTopics.md`、`advancedTopics.md` |
| 查组件类 API 签名 | `package/component/api/Component.md`、`EntityNode.md`、`EventEmitter.md`、`NodeSystem.md`、`NodeTime.md` |
| 写游戏内 UI（React） | `package/react/reactGuide/setup.md`、`xml.md`、`api.md`；钩子/refs/事件 → `hooks.md`、`refs.md`、`eventHandlers.md`；进阶 → `domTree.md`、`multiComponent.md`、`tsType.md` |
| 引入 npm 包 / 团队私有包 / 发包 | `guide/06-advanced-topics/npmPackage.md`、`local-npm-package.md`、`guide/07-publishing/createNPMProject.md` |
| 特定库用法 | `remeda.md`、`npm-zod-runtime-validation.md`、`gl-matrix.md`、`simplex-noise.md`、`pathfinding-rbush.md`（均在 `guide/06-advanced-topics/`） |
| 数据与资源配置 | `guide/06-advanced-topics/json.md`、`resources.md`、`uploadResources.md`、`asset-synchronization.md`、`i18n.md`、`uiIndex-usage.md`、`nodeGraph.md` |
| 构建定制 / 环境变量 / 分包 / webpack | `guide/06-advanced-topics/env.md`、`bulidName.md`、`webpackPlugins.md`、`vscode-workspace.md`、`code-linting-and-formatting.md` |
| 导出发布到 Arena | `guide/06-advanced-topics/toArena.md` |
| 权限与配置 | `authority/storage.md`、`dao3Cfg/file.md`、`dao3Cfg/attribute.md` |
| Arena↔ArenaPro 写法差异（dialog/voxel/storage/resourcePath/customizeEntity/remoteChannel/findChildByName） | `difference/` 同名七篇 |
| MCP 工具接入 | `mcp/chat-only-knowledgebase.md` |
| 版本变更/社区 | `community/release-notes.md` 等五篇 |

### Arena 编辑器与其平台 API（arena-official/，Apache-2.0 镜像）

| 你要做的事 | 直接读 |
| --- | --- |
| Arena 编辑器入门/建模/发布 | `arena-official/getting-started/create.md`、`helloWorld-models.md`、`helloWorld-code.md`、`publish.md` |
| SEL 赛制 / 赛事地图集成 | `arena-official/SEL/sel-rules.md`、`map-Info.md`、`map-integration.md` |
| 编辑器功能与核心概念 | `arena-official/editor/`、`arena-official/core/`、`arena-official/features/` |
| 游戏脚本平台 API（世界/玩家/实体/UI/声音/HTTP 等） | `arena-official/api/<类名>/`，如 `api/ClientWorld/`、`api/GamePlayerEntity/`、`api/GameWorld/`、`api/ClientUI/`、`api/Sound/`、`api/RemoteChannel/`；总览 `arena-official/api/index.md` |
| js 入口与模块机制 | `arena-official/javascriptEntry/`、`arena-official/javascriptDaoAPI/`、`arena-official/plugIns/` |

双源分流：ArenaPro 插件/工具链问题走上表第一段；Arena 编辑器使用与其运行时平台 API 走 `arena-official/`。跨界问题两边都读并注明来源。

## 目录地图与命名规律（路由未覆盖时自助定位）

```
references/docs/
├── README.md            全站侧边栏导航树（拿不准先扫它）
├── guide/0X-<主题>/     编号前缀=学习顺序：01简介 02上手 03教程 04工作流 05实践 06进阶 07发布
├── package/component/   组件框架：componentGuide/ 教程、api/ 类参考、timeRewindSystem/ 时间回溯
├── package/react/       @dao3fun/react：reactGuide/ 教程 + selectCode.md
├── difference/ authority/ dao3Cfg/  差异·权限·配置，文件名=被讨论的 API 或配置项
├── mcp/ community/      MCP 与社区
└── arena-official/      Arena 官方产品文档镜像（README.md 载来源与许可声明）
    ├── SEL/ core/ editor/ features/ getting-started/ javascript*/ plugIns/   用户手册
    └── api/<Game*|Client*|Sound|RemoteChannel>/                               平台 API 手册
```

自助定位方法：① 用 glob 按上表规律缩小目录；② 用 grep 在 `references/docs/` 全树搜 API 名/中文关键词（如 `onLoad`、`热更新`、`GamePlayerEntity`）；③ 命中文档的 frontmatter 含 `title`、`source`（ArenaPro 站为 docs.dao3.fun 原文，arena-official 为 GitHub blob + site + license）。

## 使用准则

- 先读后答：API 名、参数、快捷键（`Alt+Q`）、包名（`@dao3fun/react`）以读到的原文为准，不得臆造；示例代码优先直接引用文档示例。
- 冲突时以 `package/*/api/` 与 `arena-official/api/` 参考章优先于教程章。
- 引用出处：答复附文档标题 + frontmatter source URL；`arena-official/` 内容注明 Apache-2.0（box3lab/box3-product-document）。
- 文档未覆盖 → 走 `references/own/answer-playbook.md`「未覆盖协议」：合理推断需显式声明，无从推断直说未记载。
- 快照可能滞后官网：涉及版本行为差异时提醒可跑 `refresh_docs.py` 同步（或提示用户更新本 Skill）。

## 可选加速器（非必需）

有 python3 时可借用脚本加快定位；没有也完全不影响上面主路径：

```bash
python3 scripts/search.py <关键词...>        # AND 字面检索，输出 文件:行 + 排名
python3 scripts/refresh_docs.py [--arena-only]  # 从两个官方源重拉快照（own/ 不被覆盖）
```
