---
title: 物理
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 物理

## 属性

#### <font id="API" /><font id="ReadOnly">只读</font>bounds<font id="Type">: [GameVector3](https://docs.dao3.fun/api/GameVector3/)</font>{#bounds}

> 默认值：GameVector3(1, 1, 1)

实体边界框的半径，沿着 x/y/z 方向，每帧都会重新计算

#### <font id="API" /><font id="ReadOnly">只读</font>entityContacts<font id="Type">: [GameEntityContact](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/#GameEntityContact)[]</font>{#entityContacts}

> 默认值：[]

返回正在和玩家/实体发生碰撞的全部实体列表。

#### <font id="API" /><font id="ReadOnly">只读</font>voxelContacts<font id="Type">: [GameVoxelContact](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/#GameVoxelContact)[]</font>{#voxelContacts}

> 默认值：[]

返回正在和玩家/实体发生碰撞的全部方块列表。

#### <font id="API" /><font id="ReadOnly">只读</font>fluidContacts<font id="Type">: [GameFluidContact](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/#GameFluidContact)[]</font>{#fluidContacts}

> 默认值：[]

返回正在被玩家/实体触碰的全部液体方块列表。

#### <font id="API" />collides<font id="Type">: boolean</font>{#collides}

> 默认值：true

如果为假(false)，则实体不会碰撞

#### <font id="API" />fixed<font id="Type">: boolean</font>{#fixed}

> 默认值：false

如果为真(true)，则实体不会移动

#### <font id="API" />meshScale<font id="Type">: [GameVector3](https://docs.dao3.fun/api/GameVector3/)</font>{#meshScale}

实体的缩放比例。

#### <font id="API" />friction<font id="Type">: number </font>{#friction}

> 默认值：0

范围：0-1

控制实体的粘性(0 = 滑，1 = 粘)

#### <font id="API" />gravity<font id="Type">: boolean</font>{#gravity}

> 默认值：true

如果为假(false)，则实体不会下落

#### <font id="API" />mass<font id="Type">: number </font>{#mass}

> 默认值：1

实体物理质量。

#### <font id="API" />restitution<font id="Type">: number</font>{#restitution}

> 默认值：0

范围：0-1

控制实体的弹性(0 = 软, 1 = 弹)

#### <font id="API" />velocity<font id="Type">: [GameVector3](https://docs.dao3.fun/api/GameVector3/)</font>{#velocity}

> 默认值：GameVector3(0, 0, 0)

实体的速度。

**[details]**

```javascript
// 让所有玩家每五秒跳一下
setInterval(() => {
  console.log("jump around!");
  world.querySelectorAll("player").forEach((e) => {
    e.velocity.y += 1;
  });
}, 5000);
```

---
#### <font id="API" />contactForce<font id="Type">: [GameVector3](https://docs.dao3.fun/api/GameVector3/)</font>{#contactForce}

> 默认值：GameVector3(0, 0, 0)

实体受到的碰撞力。

## 接口

#### <font id="API" />GameEntityContact{#GameEntityContact}

活跃实体对接触

| **参数** | **类型**                     | **说明**         |
| -------- | ---------------------------- | ---------------- |
| other    | [GameEntity](https://docs.dao3.fun/api/GameEntity/)   | 接触的另一个实体 |
| force    | [GameVector3](https://docs.dao3.fun/api/GameVector3/) | 接触力           |
| axis     | [GameVector3](https://docs.dao3.fun/api/GameVector3/) | 接触轴           |

#### <font id="API" />GameVoxelContact{#GameVoxelContact}

活跃方块接触状态

| **参数** | **类型**                     | **说明**      |
| -------- | ---------------------------- | ------------- |
| x        | number                       | 方块的 X 坐标 |
| y        | number                       | 方块的 Y 坐标 |
| z        | number                       | 方块的 Z 坐标 |
| voxel    | number                       | 方块 ID       |
| force    | [GameVector3](https://docs.dao3.fun/api/GameVector3/) | 接触力        |
| axis     | [GameVector3](https://docs.dao3.fun/api/GameVector3/) | 接触轴        |

#### <font id="API" />GameFluidContact{#GameFluidContact}

活跃流体接触

| **参数** | **类型** | **说明** |
| -------- | -------- | -------- |
| voxel    | number   | 方块 ID  |
| volume   | number   | 流体体积 |
