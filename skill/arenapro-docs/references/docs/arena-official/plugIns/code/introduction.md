---
title: Arena 创作端插件开发介绍
source: https://github.com/box3lab/box3-product-document/blob/master/arena/plugIns/code/introduction.md
site: https://docs.dao3.fun/arena/
license: Apache-2.0 (box3lab/box3-product-document)
---

# Arena 创作端插件开发介绍

你是否使用过[建筑师工具箱](https://docs.dao3.fun/arena/plugIns/building)、[Chat 吉 PT](https://docs.dao3.fun/arena/plugIns/arenanext) 或 [ArenaNext](https://docs.dao3.fun/arena/plugIns/arenanext) 插件？这些便捷的工具是否给你的创作带来了极大帮助？这些优秀的工具都是由用户自己开发的插件。

搬砖喵说了：合法合规的插件开发是完全被支持的。你可以自由创作插件，甚至分享给社区中的其他岛民使用。

坚决反对开发外挂、盗号等非法工具。我们鼓励大家开发创意性、辅助创作的插件，为整个社区带来价值。

如果你开发的插件足够出色，搬砖喵甚至会考虑将其直接内置到编辑器中哦～

## 插件能做什么？

浏览器插件可以增强你的创作体验，常见用途包括：

1. **工具增强**：添加实用功能，如建筑辅助工具、地形编辑器等
2. **界面优化**：自定义编辑器界面，添加新的面板或快捷按钮
3. **开发辅助**：提供代码智能提示、错误检查等功能（如 ArenaNext）
4. **资源管理**：更便捷地管理和导入素材、模型和音效
5. **社区互动**：添加社区分享、协作开发功能
6. **自动化工具**：构建自动化脚本，简化重复操作

## 插件管理器

为了便于开发和管理，我们推荐使用篡改猴(Tampermonkey)作为插件管理器。
详细的安装方法请查看：[tampermonkey](https://docs.dao3.fun/arena/plugIns/tampermonkey)

## 开发语言

插件开发使用 JavaScript/TypeScript 语言，与神奇代码岛的开发语言保持一致。不同的是，插件开发环境中可以使用更多的功能和 API，不会像神岛中那样受到严格限制。
