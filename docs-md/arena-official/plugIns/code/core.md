---
title: 创作端 Core 对象详解
source: https://github.com/box3lab/box3-product-document/blob/master/arena/plugIns/code/core.md
site: https://docs.dao3.fun/arena/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 创作端 Core 对象详解

本文档介绍神岛创作端引擎的 Core 对象主要组件及其功能，帮助插件创作者深入了解如何利用这些接口开发高级功能。

## 核心系统组件

### 游戏管理模块

- `onGameChange`：事件总线，用于监听和响应游戏状态变化
- `onGameReady`：事件总线，用于处理游戏初始化完成事件
- `setGameSettings`：函数，用于配置游戏参数和设置

### 资源管理系统

- `assetController`：资源控制器，负责管理游戏资产、素材并处理资源冲突检测
- `editContentStorage`：内容存储管理器，包含多种资源控制功能
- `seedController`：种子控制器，用于生成程序化内容和随机元素

### 环境控制系统

- `envController`：环境控制器，可调整以下参数：
  - 太阳相位和频率
  - 月亮相位和可见性
  - 天空和环境光效果
  - 雾效和大气参数

### 输入管理系统

- `gamepadController`：游戏控制器管理，提供以下功能：
  - 摇杆输入配置
  - 飞行控制按钮设置
  - 自定义按键映射
  - 多设备输入管理

## 开发工具集

### 代码编辑环境

- `codeEditorController`：代码编辑器控制器，核心功能包括：
  - 文件模型管理
  - 光标位置和选择区域控制
  - 代码折叠和导航
- `monacoController`：Monaco 编辑器接口（与 VS Code 使用相同的编辑器引擎）

### 调试工具链

- `debugger`：调试器模块，包含：
  - 调试协议实现
  - 状态管理
  - 控制台接口
- `scriptEval`：脚本评估函数，用于动态执行和测试代码
- `debugging`：布尔值，表示当前是否处于调试模式

### 发布功能

- `publish`：发布模块，提供完整的游戏保存和发布流程

## 网络与通信系统

- `brpc`：二进制远程过程调用客户端，用于高效数据传输
- `rpc`：远程过程调用模块，功能包括：
  - 回调管理
  - 服务调用接口
  - 通信事件处理
- `replica`：复制系统，管理：
  - 项目变更同步
  - 多人协作变更事件
  - 邀请和权限管理
- `bufferSink`：数据缓冲池，优化网络传输效率

## 用户界面控制

- `gameUIEditor`：游戏 UI 编辑器，提供以下功能：
  - 拖拽控制
  - 滚动管理
  - 轴向约束控制
  - 布局辅助功能
- `listeners`：事件监听器集合，包括：
  - 超链接事件
  - 音频事件
  - 复制和粘贴事件
  - 其他 UI 交互事件

## 实用工具

- `logger`：通用日志记录工具
- `pinLogger`：分级日志记录系统，支持不同日志级别
- `screenshot`：屏幕截图功能接口
- `measureMemory`：内存使用监测和分析工具
- `fetchUserListById`：通过 ID 查询和获取用户列表的功能

## 状态管理系统

- `state`：主状态结构，包含：
  - 管理员状态
  - 代码编辑器状态
  - 应用全局状态
- `frameState`：帧状态结构，管理各子系统的实时状态
- `reactEvent`：响应式事件系统，包含：
  - 事件监听器
  - 模式切换
  - UI 状态同步

随着对 Core 对象的深入理解，你将能够开发出更加强大和定制化的神岛编辑器插件。
