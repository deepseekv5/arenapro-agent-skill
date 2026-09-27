---
title: arenapro-docs Skill 安装与使用指南
source: 原创文档（本项目产出，非 docs.dao3.fun 原文）
---

# arenapro-docs Skill 安装与使用指南

## 安装

Skill 是自包含目录，安装即拷贝到 Skills 加载路径，两种方式任选：

**1) 项目级**（只对当前项目生效）

```bash
mkdir -p <项目根>/.qoder/skills
cp -R arenapro-project/skill/arenapro-docs <项目根>/.qoder/skills/
```

**2) 用户级**（对该用户所有会话生效）

```bash
cp -R arenapro-project/skill/arenapro-docs ~/.qoderwake/qodercli/skills/
```

安装后重启会话（或执行 `/skills reload`），用 `/skills list` 确认 `arenapro-docs` 已出现。QoderWake 数字员工也可通过平台 Skill 管理入口挂载同一目录。

## 触发方式

无需显式调用。frontmatter 的 description 覆盖以下场景关键词，Agent 在相关提问时自动加载本 Skill：

- ArenaPro / 神岛 / dao3 开发问题（安装、调试、发布、配置、权限）
- 组件体系：Component、EntityNode、EventEmitter、NodeSystem、NodeTime、生命周期、装饰器、时间回溯
- React UI：`@dao3fun/react`、hooks、XML 标签、refs、事件处理器
- 工作流：HMR 热更新、`Alt+Q` 完整构建、Debug/Release、webpack、npm 包管理
- MCP 工具与社区章节

也可用 `/arenapro-docs <问题>` 手动调用。

## 检索使用方法

脚本入口：`python3 <skill_dir>/scripts/search.py`（零依赖，`<skill_dir>` 为 Skill 安装目录）。

| 模式 | 命令 | 输出 |
| --- | --- | --- |
| 关键词 AND 检索 | `search.py 组件 生命周期` | `文件:行号: 命中行`，附命中摘要与最佳文件排名 |
| 只看文件排名 | `search.py --files HMR` | 每个命中文件的命中次数与标题 |
| 全站目录 | `search.py --toc` | 89 篇文档的相对路径与标题清单 |
| 分页读取 | `search.py --read guide/04-development-workflow/hmr.md --lines 1-80` | 指定行段正文，尾部提示剩余行数 |

文档目录解析优先级：`--docs-dir` 参数 > 环境变量 `ARENAPRO_DOCS_DIR` > Skill 内置 `references/docs/` > 相邻 `../../docs-md/`。若项目库 `docs-md/` 更新了原文档，可让 Skill 直接指向它而无需重装：

```bash
export ARENAPRO_DOCS_DIR=/path/to/arenapro-project/docs-md
```

## 使用示例

**示例 1 — API 答疑**

用户：「ArenaPro 组件的生命周期方法执行顺序是什么？」

Agent 执行 `search.py --files 生命周期`，命中 `package/component/componentGuide/lifecycle.md`（8 处，排名第一），再 `--read` 该文件相关行段，按文档原文给出 `onLoad → onEnable → start → update/lateUpdate` 顺序与注意事项，附官网链接。

**示例 2 — 写码前查约定**

用户：「用 @dao3fun/react 写一个点击按钮。」

Agent 执行 `search.py onClick` 或 `search.py 事件处理器`，定位 `package/react/reactGuide/eventHandlers.md`，引用文档示例代码骨架完成实现。

**示例 3 — 定位不清的章节**

用户：「发布 npm 包给团队用怎么搞？」

Agent 先 `search.py --toc` 浏览标题树，锁定 `guide/07-publishing/createNPMProject.md` 与 `guide/06-advanced-topics/local-npm-package.md`，读取后分步作答。

## 文档更新后如何刷新 docs-md

`docs-md/` 是转化快照，原站更新后不会自动同步。随 Skill 附带了自包含刷新工具 `scripts/refresh_docs.py`：

```bash
# 依赖一次即可：pip install beautifulsoup4 markdownify lxml
python3 skill/arenapro-docs/scripts/refresh_docs.py            # 默认写回 ../docs-md
python3 skill/arenapro-docs/scripts/refresh_docs.py /tmp/chk   # 输出到临时目录先做 diff
```

工具行为：页面清单从站点侧边栏自动发现（无需维护列表）；只新增/覆盖站点转化件，`own/` 自写文档与根 `index.md` 不会被触碰；空壳页自动跳过；`README.md` 索引自动再生并追加 own/ 条目。刷新后建议：重跑 `search.py --list | wc -l` 记录篇数，并抽查 2-3 篇的 frontmatter `source` 可达；若 Skill 已安装到别处，记得同步其 `references/docs/` 副本（`rm -rf <skill>/references/docs && cp -R docs-md <skill>/references/docs`），或直接用 `ARENAPRO_DOCS_DIR` 指回项目库免重装。

## 注意事项

- 回答中的 API 名、参数、包名必须以检索结果为准；无命中时如实说明文档未覆盖。
- 内置 `references/docs/` 是发布时快照；需要最新内容时用 `ARENAPRO_DOCS_DIR` 指回项目库 `docs-md/`。
- 文档语言为中文；跨语言提问时翻译结论，但保留代码与 API 原文。
