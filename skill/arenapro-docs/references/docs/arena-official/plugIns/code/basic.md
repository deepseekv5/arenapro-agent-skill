---
title: 插件开发基础
source: https://github.com/box3lab/box3-product-document/blob/master/arena/plugIns/code/basic.md
site: https://docs.dao3.fun/arena/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 插件开发基础

要开始插件开发，首先需要安装并打开 Tampermonkey 插件管理器，然后创建一个新的用户脚本。

## 开发资源参考

在开发过程中，以下资源可能对你有所帮助：

- [Tampermonkey 官方文档](https://www.tampermonkey.net/documentation.php)
- [JavaScript DOM 操作指南](https://developer.mozilla.org/zh-CN/docs/Web/API/Document_Object_Model)

## 获取创作端引擎 Core

要开发强大的神岛编辑器插件，首先需要获取创作端引擎的 Core 对象。获取 Core 对象后，你才能调用编辑器的各种接口，实现丰富的扩展功能。

以下是获取 Core 对象的基本脚本：

```js
// ==UserScript==
// @name         Arena创作端Core
// @match        https://dao3.fun/edit/*
// @match        https://view.dao3.fun/e/*
// @grant        unsafeWindow
// ==/UserScript==

(function () {
  "use strict";
  Object.defineProperty(Object.prototype, "permissionController", {
    set() {
      unsafeWindow.core = this;
      delete Object.prototype.permissionController;
    },
    configurable: true,
  });
})();
```

### 使用步骤

完成以上代码的编写后，按照以下步骤操作：

1. 保存脚本并确保 Tampermonkey 已启用
2. 进入神岛创作端页面
3. 打开浏览器开发者工具（F12 或右键选择"检查"）
4. 切换至 GameIframe 框架（如下图所示）
5. 在控制台输入 `core` 并按回车，验证是否成功获取核心对象

### 操作演示

下面是获取 Core 对象的操作流程图示：

1. 切换到 GameIframe：  
   ![切换到GameIframe](https://docs.dao3.fun/arena/QQ20250516-164307.png)

2. 在控制台查看 Core 对象：  
   ![查看Core对象](https://docs.dao3.fun/arena/QQ20250516-164351.png)

成功后，你就可以通过 `core` 对象来访问和调用神岛创作端的各种功能和 API 了。

## 后续学习

在下一章中，我们将详细介绍 Core 对象的各个关键属性和方法，帮助你深入了解如何利用这些接口开发功能丰富的插件。
