# ArenaPro Docs Skill 官网（V2）

介绍「我们基于 ArenaPro（an）中文文档构建的 Agent Skill」的项目官网（静态站），负责人：老攸前端。

> V2 定位修正：主角是 Agent Skill，ArenaPro Creator 产品降级为"背景"板块（05 节）。V1 的 ArenaPro 产品站口径已废弃。

## 打开方式

无需构建、无依赖，浏览器直接打开即可：

```
双击 index.html
```

或本地预览：

```
python3 -m http.server 8080 --directory .
```

## 文件结构

| 文件 | 说明 |
| --- | --- |
| `index.html` | 单页站点全部内容与结构 |
| `styles.css` | 全部样式（纸墨工程编辑风、响应式、reduced-motion） |
| `app.js` | 滚动渐入 + 移动端菜单，无框架依赖 |

## 页面板块（V2）

1. Hero — 主角为 Skill，配 Agent 会话 mock（检索 + 带出处回答）
2. 01 这个 Skill 是什么 — 全量结构化 / 按需检索 / 答案可溯源
3. 02 给谁用 — 创作者 / AI 编程助手与数字员工 / 团队与工具作者
4. 03 装后能做什么 — 8 项能力，逐项映射 docs-md 真实章节
5. 04 安装与使用 — 三步装载 + 自检清单
6. 05 背景：ArenaPro 是什么 — 产品一句话介绍 + 四步工作流 + 官方文档直达
7. 06 反馈与社区 — GitHub（保留官方原链，404 风险已交 qa 记录）/ QQ 群 / 更新日志 / 项目库

## 内容来源与校对状态（QA 返工后 · 2026-09-26）

- 口径同步：站内文档规模表述为 85 篇官方文档转化件；docs-md 全库共 89 篇 = 85 转化件 + index.md（自写导航）+ README.md + own/ 两篇原创。文档入口链接指向 `docs-md/own/overview.md` 与 `docs-md/own/installation-and-usage.md`（已实测存在）。
- 安装板块对应 `docs-md/own/installation-and-usage.md`：项目级/用户级两种 cp 路径、`/skills reload` + `/skills list` 自检、`/arenapro-docs <问题>` 手动调用、search.py 四模式、docs-dir 四级解析优先级；「文档时效」卡引用 `scripts/refresh_docs.py`。
- GitHub 两处链接（社区卡 + 页脚）按 QA 决定改指 `https://github.com/box3lab` 组织页（原仓库确认 404，死链记录保留在 qa/）。
- 社区卡文案改为 Skill 站定位（反馈渠道围绕本 Skill）。
- QA P1 修复：新增 `.term code { color: inherit; ... }`（置于组合选择器之后），终端代码块恢复深底浅绿字，对比度实测约 10:1（AA+）。
- QA P2 修复（390px 整页横滚）：`.start-steps`/`.start-step > div`/`.term` 显式 `min-width: 0`，并把 ≤1020/860/560px 媒体查询中三处单列 `1fr` 轨道改为 `minmax(0, 1fr)` 阻断最小内容传导；用测试同款同源 iframe 探针（390px 视口）headless Chrome 实测 `cw=375 / sw=375`、溢出元素为空。

## 设计说明

- 方向：warm-paper 底色 + 墨色正文 + 深青绿主色 + 陶土橙点缀，编辑式编号章节，规避渐变滥用/玻璃拟态/emoji 堆砌的模板站风格。
- 字体：Space Grotesk（拉丁标题）、IBM Plex Mono（代码与标签）、Noto Sans SC（中文正文），Google Fonts 加载失败时优雅回退，离线可正常浏览。
- 动效仅滚动渐入与状态点呼吸，遵循 `prefers-reduced-motion`。
