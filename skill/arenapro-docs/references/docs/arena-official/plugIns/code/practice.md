---
title: 开发实战
source: https://github.com/box3lab/box3-product-document/blob/master/arena/plugIns/code/practice.md
site: https://docs.dao3.fun/arena/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 开发实战

下面，我们将通过几个示例，带你了解插件是如何运作的。

## 控制台执行脚本

目标：在编辑器界面上，创建一个按钮，点击按钮后，控制台会执行一段代码。

```javascript
// ==UserScript==
// @name         神岛编辑器自定义界面示例
// @namespace    https://dao3.fun/
// @version      1.0
// @description  在神岛编辑器中添加自定义界面和按钮
// @author       你的名字
// @match        https://dao3.fun/edit/*
// @match        https://view.dao3.fun/e/*
// @grant        unsafeWindow
// @require      https://cdn.jsdelivr.net/npm/lil-gui@0.18.2/dist/lil-gui.umd.min.js
// ==/UserScript==

(function () {
  "use strict";

  Object.defineProperty(Object.prototype, "permissionController", {
    set() {
      unsafeWindow.core = this;
      delete Object.prototype.permissionController;
      // 当Core对象获取成功后，初始化GUI
      initGUI();
    },
    configurable: true,
  });

  // 初始化GUI界面
  function initGUI() {
    // 确保页面已完全加载
    if (document.readyState !== "complete") {
      window.addEventListener("load", initGUI);
      return;
    }

    // 创建GUI配置对象
    const config = {
      message: "Hello Arena!",
      color: "#ff0000",
      showMessage: function () {
        console.log("按钮已点击!");
        console.log("消息内容:", config.message);
        console.log("选择的颜色:", config.color);

        try {
          //  在控制台执行代码
          core.debugger.scriptEval(
            `world.querySelectorAll('player').forEach((entity) => {entity.player.dialog({type: GameDialogType.TEXT, title: \`信息\`,content: \`信息：${config.message}，颜色：${config.color}\`,});console.log(\`${config.message},${config.color}\`);});`
          );
        } catch (err) {
          console.error("执行代码时出错:", err);
        }
      },
    };

    // 初始化lil-gui界面
    const gui = new lil.GUI();
    gui.domElement.style.position = "absolute";
    gui.domElement.style.top = "50px";
    gui.domElement.style.right = "10px";

    // 添加控件
    gui.add(config, "message").name("消息文本");
    gui.addColor(config, "color").name("选择颜色");
    gui.add(config, "showMessage").name("执行代码");

    // 添加GUI到页面
    document.body.appendChild(gui.domElement);

    console.log("自定义GUI界面已加载");
  }
})();
```

### 代码说明

这个示例展示了如何:

1. **引入 lil-gui 库**：使用 `@require` 标记从 CDN 加载 lil-gui
2. **获取 Core 对象**：使用与之前相同的方法获取神岛编辑器的 Core 对象
3. **创建自定义界面**：
   - 创建一个悬浮的控制面板
   - 添加文本输入框、颜色选择器和按钮
   - 创建分组文件夹组织更多控件
4. **执行代码功能**：点击按钮时在控制台执行自定义代码

### 关于 lil-gui

[lil-gui](https://github.com/georgealways/lil-gui) 是一个轻量级的 GUI 控件库，特点包括：

- 体积小（约 21KB）
- 简单易用的 API
- 支持多种控件类型：按钮、滑块、复选框、下拉菜单、颜色选择器等
- 支持分组和折叠

### 自定义拓展

你可以根据需要进一步拓展这个示例：

1. **更多控件类型**：添加更复杂的控制元素
2. **样式定制**：修改 GUI 的颜色、大小和位置
3. **多面板管理**：创建多个控制面板用于不同功能
4. **保存配置**：使用 localStorage 保存用户设置
5. **快捷键支持**：添加键盘快捷键来显示/隐藏界面

### 注意事项

- 确保 `@match` 规则正确匹配神岛编辑器的 URL
- 注意脚本执行时机，确保在页面完全加载后初始化 GUI
- 避免界面元素遮挡编辑器的重要功能区域

## 自定义 Monaco 编辑器菜单

目标：在神岛编辑器中自定义 Monaco 编辑器的功能

```javascript
// ==UserScript==
// @name         神岛编辑器Monaco菜单定制
// @namespace    https://dao3.fun/
// @version      1.0
// @description  自定义神岛编辑器Monaco编辑器右键菜单
// @author       你的名字
// @match        https://dao3.fun/edit/*
// @match        https://view.dao3.fun/e/*
// @grant        unsafeWindow
// ==/UserScript==

(function () {
  "use strict";
  let monaco = null;

  Object.defineProperty(Object.prototype, "permissionController", {
    set() {
      unsafeWindow.core = this;
      delete Object.prototype.permissionController;
      setTimeout(initMonacoCustomization, 6000); // 等待Monaco完全加载
    },
    configurable: true,
  });

  function initMonacoCustomization() {
    monaco = core.codeEditorController.monacoController.monaco;

    // 添加自定义编辑器操作
    addCustomEditorActions();
  }

  // 添加自定义菜单项和编辑器操作
  function addCustomEditorActions() {
    monaco.editor.addEditorAction({
      id: "code-output-action",
      label: "输出选中代码",
      contextMenuGroupId: "demo",
      contextMenuOrder: 1,
      run: (e) => {
        let select = e.getSelection();
        let value = e.getModel().getValueInRange(select);
        alert(value);
      },
    });
  }
})();
```

### 代码说明

这个示例代码展示了如何为 Monaco 编辑器添加自定义右键菜单项和操作：

#### 1. 获取 Monaco 对象

通过 Core 对象访问 Monaco 控制器，获取 Monaco 编辑器实例：

```javascript
monaco = core.codeEditorController.monacoController.monaco;
```

#### 2. 添加自定义编辑器操作

使用 `monaco.editor.addEditorAction` 方法添加自定义菜单项：

- **id**: 操作的唯一标识符
- **label**: 菜单中显示的文本
- **contextMenuGroupId**: 菜单项所属的分组
- **contextMenuOrder**: 分组内的排序位置
- **run**: 点击菜单项时执行的函数

#### 3. 实现操作逻辑

在 `run` 函数中定义菜单项的具体行为：

```javascript
run: (e) => {
  // 获取当前选中的文本范围
  let select = e.getSelection();
  // 根据选择范围获取文本内容
  let value = e.getModel().getValueInRange(select);
  // 执行操作（这里简单地显示弹窗）
  alert(value);
};
```

### 菜单操作示例

除了简单的"输出选中代码"操作外，你还可以添加以下类型的菜单项：

1. **代码转换**：将选定代码转换为注释、大写/小写、编码/解码等

```javascript
monaco.editor.addEditorAction({
  id: "convert-to-comment",
  label: "转换为注释",
  contextMenuGroupId: "transform",
  contextMenuOrder: 1,
  run: (e) => {
    // 代码实现转换为注释的逻辑
  },
});
```

2. **代码插入**：快速插入常用代码片段

```javascript
monaco.editor.addEditorAction({
  id: "insert-console-log",
  label: "插入console.log",
  contextMenuGroupId: "insert",
  contextMenuOrder: 1,
  run: (e) => {
    e.executeEdits("", [
      {
        range: e.getSelection(),
        text: "console.log()",
        forceMoveMarkers: true,
      },
    ]);
    // 可以调整光标位置到括号内
  },
});
```

3. **代码分析**：分析选中代码并提供建议

```javascript
monaco.editor.addEditorAction({
  id: "analyze-code",
  label: "分析代码",
  contextMenuGroupId: "analyze",
  contextMenuOrder: 1,
  run: (e) => {
    // 实现代码分析逻辑
  },
});
```

### 菜单分组

通过 `contextMenuGroupId` 可以将相关菜单项组织在一起：

1. **编辑组** (`edit`): 剪切、复制、粘贴等基本编辑操作
2. **变换组** (`transform`): 代码格式化、转换等操作
3. **导航组** (`navigation`): 跳转到定义、查找引用等操作
4. **分析组** (`analyze`): 代码分析、错误检查等操作

例如，添加多个菜单项到同一分组：

```javascript
// 添加到"变换"组的第1个位置
monaco.editor.addEditorAction({
  id: "format-code",
  label: "格式化代码",
  contextMenuGroupId: "transform",
  contextMenuOrder: 1,
  // ...
});

// 添加到"变换"组的第2个位置
monaco.editor.addEditorAction({
  id: "minify-code",
  label: "压缩代码",
  contextMenuGroupId: "transform",
  contextMenuOrder: 2,
  // ...
});
```

### 扩展方向

基于此示例，你可以进一步开发更多功能：

1. **代码生成工具**：快速生成常用神岛代码结构
2. **API 文档查询**：选中 API 名称后右键查看文档
3. **代码片段库**：添加常用代码片段的快速插入功能
4. **集成调试工具**：添加右键运行/调试选中代码的功能
5. **外部工具集成**：与外部工具如代码格式化器、Linter 等集成

### 注意事项

- 避免添加过多菜单项，导致右键菜单过长
- 为每个操作提供清晰、简洁的标签
- 考虑为常用操作提供键盘快捷键
- 处理可能的错误情况，如未选择文本时的操作
- 注意性能影响，特别是处理大量文本时

## ArenaNext 开源仓库参考

跟多能力，你可以参考 [ArenaNext 仓库](https://gitee.com/box3lab/arena-next-plugin)
