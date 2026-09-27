---
title: S-🏠 游戏实体
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/index.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# S-🏠 游戏实体

**GameEntity** 是游戏世界中的基础对象，提供了以下核心功能：

- 外观控制：管理实体的形状、位置、旋转、颜色等视觉属性
- 物理系统：控制实体的碰撞、重力、质量等物理特性
- 粒子效果：创建和管理实体的粒子系统
- 交互系统：处理实体与玩家的互动、点击等操作
- 战斗系统：管理实体的生命值、伤害、死亡等状态

## 类定义

```typescript
declare class GameEntity {
  //...
}
```

## 属性列表

### 基础信息

- [`isPlayer`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/isPlayer#isPlayer) : 实体是否为玩家
- [`player`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/isPlayer#player) : 索引与玩家相关的全部状态和方法
- [`id`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/label#id) : 已在编辑器中添加的实体名称

### 外观系统

- [`mesh`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#mesh) : 实体形状数据(mesh)的 hash
- [`position`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#position) : 实体的位置
- [`meshOrientation`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#meshOrientation) : 实体的旋转角度
- [`meshScale`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#meshScale) : 实体的缩放比例
- [`meshColor`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#meshColor) : 实体的颜色
- [`meshInvisible`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#meshInvisible) : 控制实体隐形
- [`meshEmissive`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#meshEmissive) : 实体的发光度
- [`meshMetalness`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#meshMetalness) : 实体的金属感
- [`meshShininess`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#meshShininess) : 实体的反光度
- [`meshOffset`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#meshOffset) : 实体的位移

#### 名称显示

- [`showEntityName`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#showEntityName) : 是否展示实体的默认名称
- [`customName`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#customName) : 自定义需要展示的名称
- [`nameRadius`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#nameRadius) : 名称展示范围，数值越小，则需要靠近实体才会出现名称
- [`nameColor`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#nameColor) : 进入实体名称展示范围时，实体名称的颜色

### 物理系统

- [`bounds`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#bounds) : 实体边界框的半径
- [`collides`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#collides) : 实体是否碰撞
- [`fixed`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#fixed) : 实体是否移动
- [`friction`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#friction) : 控制实体的粘性(0 = 滑，1 = 粘)
- [`gravity`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#gravity) : 实体是否下落
- [`mass`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#mass) : 实体物理质量
- [`restitution`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#restitution) : 控制实体的弹性(0 = 软, 1 = 弹)
- [`velocity`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#velocity) : 实体的速度
- [`contactForce`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#contactForce) : 实体受到的碰撞力
- [`entityContacts`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#entityContacts) : 返回正在和玩家/实体发生碰撞的全部实体列表
- [`voxelContacts`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#voxelContacts) : 返回正在和玩家/实体发生碰撞的全部方块列表
- [`fluidContacts`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#fluidContacts) : 返回正在被玩家/实体触碰的全部液体方块列表

### 音效系统

- [`chatSound`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/music#chatSound) : 当实体说话时，播放聊天音效。通过`say()`触发
- [`hurtSound`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/music#hurtSound) : 当实体触发受伤事件时，播放受伤音效。通过`onTakeDamage()`触发
- [`dieSound`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/music#dieSound) : 当实体触发死亡事件时，播放死亡音效。通过`onDie()`触发
- [`interactSound`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/music#interactSound) : 当实体进行互动时，播放互动音效。此音效仅互动的玩家可听见。通过`onInteract()`触发

### 粒子系统

- [`particleRate`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleRate) : 实体平均每秒产生粒子的数量
- [`particleRateSpread`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleRateSpread) : 如果设定了该属性的值，实体每一秒产生粒子的数量将不再是个固定值
- [`particleLimit`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleLimit) : 实体可产生的粒子总数的上限
- [`particleLifetime`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleLifetime) : 粒子的存活时间，以秒为单位
- [`particleLifetimeSpread`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleLifetimeSpread) : 如果设定了该属性的值，粒子的存活时间将不再是固定值
- [`particleSize`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleSize) : 该属性的值可以是一个长度为 0 至 5 的数组。每个粒子的存活时间被平均分为五个阶段
- [`particleSizeSpread`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleSizeSpread) : 如果设定了该属性，但没设定 particleSize 的值，每产生一个粒子，会从区间[0， particleSizeSpread)里选取的一个随机数作为它的大小
- [`particleColor`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleColor) : 类似 particleSize，该属性的值可以是一个长度为 0 至 5 的数组，数组里的每个值分别指定了粒子在各个阶段的颜色
- [`particleVelocity`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleVelocity) : 该实体产生的所有粒子的初始速度
- [`particleVelocitySpread`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleVelocitySpread) : 增加该实体产生的所有粒子初始速度的不确定性
- [`particleDamping`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleDamping) : 如果该属性的值为正数，会短暂减少该实体所产生粒子的初始速度，数值越大，减少初始速度的效果持续得越久
- [`particleAcceleration`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleAcceleration) : 该实体所产生粒子的加速度
- [`particleNoise`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleNoise) : 指定粒子相对于之前运动方向的最大偏离值，数值越大，各个粒子的运动相对原有方向的偏离越明显
- [`particleNoiseFrequency`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/particle#particleNoiseFrequency) : 指定粒子改变运动方向的频率，数值越大，各个粒子的运动方向越没有规律

### 交互系统

- [`enableInteract`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#enableInteract) : 是否允许实体进行互动
- [`interactRadius`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#interactRadius) : 实体互动范围。数值越小，则需要靠近实体才会出现互动提示
- [`interactHint`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#interactHint) : 进入实体互动范围时，实体身上出现的提示文本
- [`interactColor`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#interactColor) : 进入实体互动范围时，提示文本的颜色

### 战斗系统

- [`destroyed`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#destroyed) : 实体是否销毁
- [`enableDamage`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#enableDamage) : 实体是否显示可以进行伤害
- [`showHealthBar`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#showHealthBar) : 实体是否显示生命值 HP
- [`hp`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#hp) : 实体的当前生命值 hp
- [`maxHp`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#maxHp) : 实体的最大生命值 hp

## 方法列表

### 外观控制

- [`lookAt`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/appearance#lookAt) : 将实体旋转至面向指定位置的方向
- [`animate`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/animate#animate) : 创建一个关键帧动画
- [`getAnimations`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/animate#getAnimations) : 获取实体的所有已创建的动画

### 音效控制

- [`sound`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/music#sound) : 在实体所在的位置播放声音

### 标签系统

- [`addTag`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/label#addTag) : 为实体添加一个新标签
- [`hasTag`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/label#hasTag) : 判断实体是否带有某个标签
- [`removeTag`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/label#removeTag) : 从实体移除标签
- [`tags`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/label#tags) : 获取编辑器中给实体添加的全部标签

### 交互控制

- [`say`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#say) : 让实体说话

### 战斗控制

- [`destroy`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#destroy) : 销毁实体
- [`hurt`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#hurt) : 对实体的伤害数值

## 事件监听

### 交互事件

- [`onClick`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#onClick) : 当玩家用鼠标点击实体时触发
- [`onInteract`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#onInteract) : 当实体进行互动时触发

### 碰撞事件

- [`onEntityContact`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#onEntityContact) : 当实体触碰另一个实体时触发
- [`onEntitySeparate`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#onEntitySeparate) : 当实体停止触碰另一个实体时触发
- [`onFluidEnter`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#onFluidEnter) : 当实体进入液体时触发
- [`onFluidLeave`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#onFluidLeave) : 当实体离开液体时触发
- [`onVoxelContact`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#onVoxelContact) : 当实体触碰方块时触发
- [`onVoxelSeparate`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#onVoxelSeparate) : 当实体停止触碰方块时触发

### 战斗事件

- [`onDestroy`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#onDestroy) : 当实体被销毁时触发
- [`onTakeDamage`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#onTakeDamage) : 实体受到伤害时触发的事件
- [`onDie`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#onDie) : 实体死亡时触发的事件

## 接口定义

### 动画接口

- [`GameEntityKeyframe`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/animate#GameEntityKeyframe) : Entity 实体动画关键帧参数

### 事件接口

- [`GameEntityContactEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#GameEntityContactEvent) : 当两个实体碰撞时触发的事件
- [`GameFluidContactEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#GameFluidContactEvent) : 当实体进入或离开液体时触发的事件
- [`GameVoxelContactEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#GameVoxelContactEvent) : 当实体触碰方块时触发的事件
- [`GameHurtOptions`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#GameHurtOptions) : 攻击/伤害的相关参数
- [`GameDamageEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#GameDamageEvent) : 当实体收到伤害时触发的事件
- [`GameDieEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#GameDieEvent) : 当实体死亡时触发的事件

### 碰撞接口

- [`GameEntityContact`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#GameEntityContact) : 活跃实体对接触
- [`GameVoxelContact`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#GameVoxelContact) : 活跃方块接触状态
- [`GameFluidContact`](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/physics#GameFluidContact) : 活跃流体接触
