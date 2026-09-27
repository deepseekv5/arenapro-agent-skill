---
name: arenapro-docs
description: 检索并接入 ArenaPro（神岛/dao3 VSCode 游戏开发插件）官方中文文档。当问题涉及 ArenaPro、神岛、dao3、VSCode 编写 Minecraft 游戏脚本、TypeScript 世界/组件开发、组件生命周期、EntityNode、HMR 热更新、Alt+Q 构建、npm 包 (@dao3fun/react、@dao3fun/component)、React UI 钩子、dao3Cfg 配置、权限、MCP 工具、Arena 发布构建，或需要引用 docs.dao3.fun 文档原文作答时使用；也用于查询本 Skill 自身的安装、接入与检索使用方法。
---

# ArenaPro 中文文档检索

## Overview

本 Skill 内置 ArenaPro 官方中文文档全量 Markdown 版 + 本 Skill 自身的原创文档（来源 https://docs.dao3.fun/arenapro/zh/ ，共 89 篇），用于回答 ArenaPro/神岛开发问题、编写符合官方 API 的代码。所有回答必须基于检索到的文档原文，不得凭空臆造 API。

## 文档目录结构

文档位于 `references/docs/`（相对本 SKILL.md；站点首页为纯 hero 落地页，导航请看 references/docs/README.md 与 index.md）。先用检索脚本定位，再按需读取，禁止一次性读入多篇全文。

| 路径 | 内容 |
| --- | --- |
| `index.md` / `README.md` | 站点首页与全站导航索引（章节树） |
| `guide/01-introduction/` | 插件简介、创作者工具箱 |
| `guide/02-getting-started/` | 安装、创建项目、连接云端调试 |
| `guide/03-basic-tutorial/` | Hello World、TS vs JS、Arena 差异 |
| `guide/04-development-workflow/` | HMR、断点调试、Debug/Release 编译原理 |
| `guide/05-best-practices/` | 代码复用、通信约定 |
| `guide/06-advanced-topics/` | JSON 数据、资源管理、i18n、npm 包、webpack、gl-matrix、remeda、zod、pathfinding、自动化测试、环境变量、UI 索引、节点图 |
| `guide/07-publishing/` | 创建与发布 NPM 项目 |
| `package/component/componentGuide/` | 组件体系：创建、生命周期、装饰器、节点/世界事件、NodeSystem、时间、性能 |
| `package/component/api/` | API 参考：Component、EntityNode、EventEmitter、NodeSystem、NodeTime |
| `package/component/timeRewindSystem/` | 时间回溯系统（入门/进阶/高级/示例） |
| `package/react/reactGuide/` | @dao3fun/react：XML 标签、hooks、refs、事件、DOM 树、TS 类型、多组件 |
| `difference/` | ArenaPro 与 Arena 差异（dialog、voxel、storage、resourcePath、customizeEntity、remoteChannel、findChildByName） |
| `authority/` | 权限（storage 授权） |
| `dao3Cfg/` | dao3.cfg 配置文件与属性 |
| `own/` | 自写文档：index 说明、overview.md（是什么/接入后能力）、installation-and-usage.md（安装/检索方法/示例/文档刷新） |
| `mcp/` | MCP 工具：chat-only-knowledgebase 等 |
| `community/` | 社区：release notes、活动、奖励、行为准则、鸣谢 |

## 检索工作流

1. **定位**：用检索脚本按关键词找文件与行号（中文或英文 API 名均可，多词为 AND）：
   ```bash
   python3 <skill_dir>/scripts/search.py 组件 生命周期
   python3 <skill_dir>/scripts/search.py --files HMR        # 只看命中文件排名
   python3 <skill_dir>/scripts/search.py --toc              # 查看全部文档与标题
   ```
2. **读取**：只读命中最多的文件的相关段落：
   ```bash
   python3 <skill_dir>/scripts/search.py --read package/component/componentGuide/lifecycle.md --lines 1-80
   ```
   或直接 Read 该文件（`references/docs/` 下相对路径）。
3. **无命中时降级**：换同义词（如「热更新/HMR」、「发布/publish」、「组件/component」）、用单关键词、或先读 `README.md` 导航索引人工判断章节，再在该章节目录内检索。
4. **回答引用**：给出结论时附文档路径；每篇 frontmatter 的 `source:` 字段是官网原文链接，可向用户提供。

## 使用准则

- API 名称、参数、快捷键（如 `Alt+Q`）、包名（如 `@dao3fun/react`）以检索结果为准；文档含完整代码块，示例代码优先直接引用文档示例。
- 文档为 zh-CN；用户用其他语言提问时，翻译要点但保留 API/代码原文。
- 若文档间存在差异（如 guide 与 api 参考），以 `package/*/api/` 为准。
- 若 Skill 被安装到文档目录之外的位置且需指向项目库最新 docs-md，可设环境变量 `ARENAPRO_DOCS_DIR` 或传 `--docs-dir`。

## Resources

- `scripts/search.py`：零依赖检索/读取工具（模式：关键词检索、--files、--toc、--list、--read --lines）。输出自动截断防上下文溢出。
- `scripts/refresh_docs.py`：文档刷新工具（需 bs4/markdownify/lxml），重抓站点转化件并再生索引，不触碰 own/ 自写文档。
- `references/docs/`：ArenaPro 中文文档全量 md（89 篇，含 frontmatter title/source；由 https://docs.dao3.fun/arenapro/zh/ VitePress 站点转化，保留层级、代码块与内链）。
