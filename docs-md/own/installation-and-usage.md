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
cp -R <仓库或发布包>/skill/arenapro-docs <项目根>/.qoder/skills/
```

**2) 用户级**（对该用户所有会话生效）

```bash
cp -R <仓库或发布包>/skill/arenapro-docs ~/.qoder/skills/
```

Qoder CLI / QoderWake 也可放 `~/.qoderwake/qodercli/skills/`；其他客户端把 `arenapro-docs` 目录放进各自的技能等价目录即可。安装后重启会话（或 `/skills reload`），用 `/skills list` 确认 `arenapro-docs` 已出现。

**最省事的方式**：直接复制仓库根 `INSTALL.md` 首段整句话贴给任意有文件能力的 AI agent，它会自己完成下载、放置与自检。

## 自检（不需要任何脚本）

装好后向 agent 提问：「ArenaPro 组件的生命周期执行顺序是什么？」

安装正确的表现：agent 打开 `references/docs/package/component/componentGuide/lifecycle.md`（或引用路由表指向它），按原文回答 onLoad → onEnable → start → update（lateUpdate 在动画/物理之后），并附文档出处。若 agent 凭记忆作答或说找不到文档，说明未装载成功。

## 触发方式

无需显式调用。frontmatter 的 description 覆盖以下场景关键词，Agent 在相关任务时自动加载本 Skill：

- ArenaPro / 神岛 / dao3 开发（安装、调试、HMR、构建、发布、配置、权限）
- 组件体系：Component、EntityNode、EventEmitter、NodeSystem、NodeTime、生命周期、装饰器、时间回溯
- React UI：`@dao3fun/react`、hooks、XML 标签、refs、事件处理器
- Arena 编辑器与平台 API：SEL、地图集成、GameWorld、GamePlayerEntity、ClientWorld、ClientUI 等
- MCP 工具与社区章节

也可用 `/arenapro-docs <问题>` 手动调用。

## 使用后 Agent 怎么干活

主路径全在 SKILL.md 内，概括三步：

1. **判任务**：从「开发任务 → 该读哪几篇」路由表定位文档（含 arena-official 双源分流）；
2. **直读**：用 glob/grep/read 打开对应 md 通读；路由表没覆盖时按目录地图自助定位（`guide/0X-主题/`、`api/<类名>/` 命名规律），或扫 `references/docs/README.md` 导航树；
3. **带出处作答/写码**：遵循 answer-playbook 的检查清单与引用规范；无覆盖走「未覆盖协议」。

场景化速查表另见 [own/scene-quickref.md](scene-quickref.md)（与 SKILL.md 路由等价的文档视角版）。

## 可选加速器：检索脚本

有 python3 的环境可以更快，但脚本只是加速器，主路径不依赖：

```bash
python3 <skill_dir>/scripts/search.py 组件 生命周期   # AND 字面检索，输出 文件:行: 命中
python3 <skill_dir>/scripts/search.py --files HMR     # 文件命中排名
python3 <skill_dir>/scripts/search.py --toc           # 300 篇路径+标题清单
```

## 文档更新后如何刷新 docs-md

`docs-md/` 是转化快照，原站更新后不会自动同步。维护工具 `scripts/refresh_docs.py`（需 `pip install beautifulsoup4 markdownify lxml`）：

```bash
python3 skill/arenapro-docs/scripts/refresh_docs.py               # 双源全量刷新
python3 skill/arenapro-docs/scripts/refresh_docs.py --arena-only  # 只刷新 Arena 产品文档镜像
```

行为：两个官方源自动发现页面清单；只覆盖站点/镜像来源件，`own/` 自写文档与根 `index.md` 不触碰；空壳页过滤；README 索引再生。刷新后同步已安装 Skill 的 `references/docs/` 副本（`rm -rf <skill>/references/docs && cp -R docs-md <skill>/references/docs`）。

## 注意事项

- 回答中的 API 名、参数、包名必须以读到的文档为准；未覆盖时如实说明。
- 内置 `references/docs/` 是发布时快照，需要最新内容时按上节刷新。
- 文档语言为中文；跨语言提问时翻译结论，但保留代码与 API 原文。
