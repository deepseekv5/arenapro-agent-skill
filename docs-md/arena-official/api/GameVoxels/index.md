---
title: S-🧱 游戏方块
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameVoxels/index.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# S-🧱 游戏方块

**GameVoxels** 是神奇代码岛提供的方块控制接口，它让你能够：

- 🏗️ **地形操作**：动态修改游戏世界的地形，批量生成或销毁方块
- 🎨 **方块属性**：获取和设置方块的类型、名称、旋转角度等属性
- 🔄 **批量处理**：使用循环语法高效处理大量方块

你可以通过全局对象 `voxels` 来使用这些功能。

## 类定义

```typescript
declare const voxels: GameVoxels;
declare class GameVoxels {
  //...
}
```

## 属性列表

### 基础属性

- [`shape`](https://github.com/box3lab/box3-product-document/blob/master/api/GameVoxels/operate#shape) : 当前世界地形的最大尺寸，返回一个包含 x、y、z 三个维度的向量
- [`VoxelTypes`](https://github.com/box3lab/box3-product-document/blob/master/api/GameVoxels/operate#VoxelTypes) : 返回包含所有可用方块名称的数组

## 方法列表

### 方块标识转换

- [`id`](https://github.com/box3lab/box3-product-document/blob/master/api/GameVoxels/operate#id) : 将方块 ID 转换为对应的方块名称
- [`name`](https://github.com/box3lab/box3-product-document/blob/master/api/GameVoxels/operate#name) : 将方块名称转换为对应的方块 ID

### 方块操作

- [`setVoxel`](https://github.com/box3lab/box3-product-document/blob/master/api/GameVoxels/operate#setVoxel) : 在指定的坐标位置放置一个方块，支持设置方块类型和旋转角度
- [`setVoxelId`](https://github.com/box3lab/box3-product-document/blob/master/api/GameVoxels/operate#setVoxelId) : 使用方块 ID 直接在指定坐标位置放置方块，适用于高性能场景
- [`getVoxelId`](https://github.com/box3lab/box3-product-document/blob/master/api/GameVoxels/operate#getVoxelId) : 获取指定位置方块的 ID
- [`getVoxelRotation`](https://github.com/box3lab/box3-product-document/blob/master/api/GameVoxels/operate#getVoxelRotation) : 获取指定位置方块的旋转码
