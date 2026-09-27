---
title: ArenaPro 答题与写码手册（自写文档，非官方内容）
author: 后端（本 Skill 制作者）
---

# ArenaPro 答题与写码手册

任务→文档的路由表已并入 SKILL.md 主流程；本篇只保留写码护栏与作答规范。定位文档请直接用 SKILL.md 的路由表与目录地图（glob/grep/read），本篇不再重复。

## 写码时的硬性检查清单

生成 ArenaPro/Arena 代码前后各过一遍：

- API 名与签名逐个能在已读文档中命中（对不上即可疑，宁可不写）；
- 组件生命周期顺序按 `package/component/componentGuide/lifecycle.md`：onLoad → onEnable → start → update（lateUpdate 在动画/物理后）；不要套用 Unity/UE 的钩子名；
- React 侧只用 `@dao3fun/react` 文档列出的标签（box、text、image、input 等）与属性；HTML 标签默认不成立；
- import 路径以文档示例原文为准，不自造包名；
- 引擎差异 API 先查 `difference/`，Arena 写法不能直接搬；Arena 平台 API 以 `arena-official/api/<类名>/` 为准；
- 事件/存档涉及权限时核对 `authority/storage.md`；
- 交付时说明构建方式：调试用 HMR，发布用 Alt+Q 完整构建（差异见 `guide/04-development-workflow/compilationPrinciple.md`）。

## 直读检索降级阶梯（grep 无命中时按序尝试）

1. 中英互换：热更新↔HMR、组件↔component、生命周期↔lifecycle、发布↔publish、存档↔storage；
2. 减词/换词：先只搜 API 名本身，再搜中文别名；
3. 扫 `references/docs/README.md` 导航树人工判定章节，目录内通读；
4. 仍无 → 走未覆盖协议，禁止编造。

## 出处引用规范

- 单个结论：`《文档标题》 + frontmatter source URL`；
- 多文档综合：逐小节标注，标题与 URL 一一对应，不许合并出处；
- `arena-official/` 内容额外注明 Apache-2.0（box3lab/box3-product-document）；
- 转述与原文区分：代码块注明「摘自文档示例」或「基于文档改写」；
- 快照超过 30 天：答复末尾附「文档可能已更新，可跑 refresh_docs.py 同步」。

## 未覆盖协议

文档没有的内容分两类处理，不许含糊：

1. **合理推断**：给出答案但显式声明「文档未覆盖，以下基于 X 章节外推，请以实机验证」；
2. **无从推断**（版本兼容、平台限制、账号权限）：直说「官方文档未记载」，给出验证路径（导航树自查 + docs.dao3.fun 站内搜 + `community/` 社区渠道）。
