---
title: C-🖼️ 游戏用户界面
source: https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/index.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# C-🖼️ 游戏用户界面

**ClientUI** 是管理游戏界面的主要接口，它提供了以下核心功能：

- 界面布局：管理 UI 节点的层级、位置、尺寸等布局属性
- 节点管理：创建和操作各类 UI 节点（屏幕、盒子、图片、文本、输入框等）
- 事件系统：处理用户交互、节点状态变化等事件
- 样式控制：自定义节点的颜色、透明度、旋转等视觉效果

**[tip]**
在推出此功能前，已有 GUI 功能（基于 xml 编写）。但已不推荐使用，因有更优方案且支持可视化编辑。推荐使用最新的 ClientUI。
对旧版 GUI 感兴趣可查阅[d.ts 文件](https://github.com/box3lab/arena_dts/blob/main/GameAPI.d.ts#L13224)。
---
## 类定义

```typescript
declare const ui: UiNode;
declare const input: InputSystem;
declare const screenWidth: number; // 全局对象，获取当前玩家屏幕宽度
declare const screenHeight: number; // 全局对象，获取当前玩家屏幕高度

declare class InputSystem {
  //...
}
declare class UiNode {
  //...
}
```

## 属性列表

### 基础属性

- [`name`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiNode#name) : 节点的标识符，可重复
- [`visible`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiRenderable#visible) : 节点的可见性
- [`zIndex`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiRenderable#zIndex) : 节点的层级，用于确定渲染顺序

### 节点结构

- [`parent`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiNode#parent) : 父节点，非根节点的父节点为空时不会被渲染
- [`children`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiNode#children) : 子节点列表，通过修改子节点的`parent`属性调整结构
- [`events`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiNode#events) : 节点事件管理器

### 布局与变换

- [`anchor`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiRenderable#anchor) : 节点锚点，用于确定位置
- [`position`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiRenderable#position) : 相对于父节点的位置
- [`size`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiRenderable#size) : 节点尺寸
- [`rotation`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiRenderable#rotation) : 旋转角度
- [`uiScale`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiNode#uiScale) : 等比例缩放数据
- [`autoResize`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiRenderable#autoResize) : 自动调整尺寸的方式

### 外观样式

- [`backgroundColor`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiRenderable#backgroundColor) : 背景颜色
- [`backgroundOpacity`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiRenderable#backgroundOpacity) : 背景透明度
- [`pointerEventBehavior`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiRenderable#pointerEventBehavior) : 鼠标指针事件响应方式

### 图片节点

- [`image`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiImage#image) : 图片内容（路径或 URL）
- [`imageOpacity`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiImage#imageOpacity) : 图片透明度
- [`imageDisplayMode`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiImage#imageDisplayMode) : 图像显示模式
- [`complete`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiImage#complete) : 图片加载状态

### 滚动框节点

- [`scrollPosition`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiScrollBox#scrollPosition) : 滚动的位置

### 文本节点

- [`textContent`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#textContent) : 文本内容
- [`richText`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#richText) : 是否支持富文本
- [`textFontSize`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#textFontSize) : 字体大小
- [`textColor`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#textColor) : 文本颜色
- [`textFontFamily`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiInput#textFontFamily) : 字体样式
- [`textXAlignment`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#textXAlignment) : 水平对齐方式
- [`textYAlignment`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#textYAlignment) : 垂直对齐方式
- [`autoWordWrap`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#autoWordWrap) : 自动换行
- [`textLineHeight`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#textLineHeight) : 行高
- [`textStrokeColor`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#textStrokeColor) : 描边颜色
- [`textStrokeOpacity`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#textStrokeOpacity) : 描边透明度
- [`textStrokeThickness`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#textStrokeThickness) : 描边厚度

### 输入节点

- [`placeholderColor`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiInput#placeholderColor) : 占位文本颜色
- [`placeholderOpacity`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiInput#placeholderOpacity) : 占位文本透明度
- [`isFocus`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiInput#isFocus) : 是否处于焦点状态

## 方法

### 节点操作

- [`findChildByName`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiNode#findChildByName) : 按名称查找子节点
- [`clone`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiNode#clone) : 复制节点

### 节点创建

- [`create`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiScreen#create) : 创建 UI 屏幕实例
- [`create`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiBox#create) : 创建 UI 盒子实例
- [`create`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiScrollBox#create) : 创建 UI 滚动框实例
- [`create`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiImage#create) : 创建 UI 图片实例
- [`create`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#create) : 创建 UI 文本实例
- [`create`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiInput#create) : 创建 UI 输入实例

### 屏幕管理

- [`getAllScreen`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiScreen#getAllScreen) : 获取所有屏幕实例

### 输入控制

- [`focus`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiInput#isFocus) : 使输入框获得焦点
- [`blur`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiInput#blur) : 使输入框失去焦点
- [`unlockPointer`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/input#unlockPointer) : 显示鼠标指针
- [`lockPointer`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/input#lockPointer) : 隐藏鼠标指针

### 事件处理

- [`on`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiEvent#on) : 监听事件
- [`once`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiEvent#once) : 监听一次性事件
- [`add`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiEvent#add) : 添加事件监听器（同 on）
- [`emit`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiEvent#emit) : 触发事件
- [`remove`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiEvent#remove) : 移除第一个匹配的监听器
- [`off`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiEvent#off) : 移除事件监听器（同 remove）
- [`removeAll`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiEvent#removeAll) : 移除所有监听器

## 枚举值

- [`PointerEventBehavior`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/UiRenderable#PointerEventBehavior) : 鼠标指针事件行为
- [`ImageDisplayMode`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiImage#ImageDisplayMode) : 图像显示模式
- [`UITextFontFamily`](https://github.com/box3lab/box3-product-document/blob/master/api/ClientUI/node/UiText#UITextFontFamily) : 字体样式
