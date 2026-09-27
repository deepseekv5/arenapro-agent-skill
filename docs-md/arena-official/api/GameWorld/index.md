---
title: S-🌏 游戏世界
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/index.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# S-🌏 游戏世界

**GameWorld** 是整个游戏世界的主要接口，它提供了以下核心功能：

- 控制环境：管理天气、物理重力、画面滤镜等全局场景属性
- 实体管理：创建和搜索游戏中的实体对象
- 事件系统：监听实体和玩家的碰撞、伤害、互动等事件

你可以通过全局对象 `world` 来使用这些功能。

## 类定义

```typescript
declare const world: GameWorld;
declare class GameWorld {
  //...
}
```

## 属性列表

### 基础信息

- [`projectName`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapInfo#projectName) : 本张地图名称，对应项目设置中的名称
- [`serverId`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapInfo#serverId) : 当前服务器 ID
- [`currentTick`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapInfo#currentTick) : 世界当前的 Tick 计数
- [`useOBB`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapInfo#useOBB) : 是否切换为 OBB 包围盒计算方式

### 物理系统

- [`gravity`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/physics#gravity) : 世界重力
- [`airFriction`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/physics#airFriction) : 空气阻力

### 天气效果

#### 雾效果

- [`maxFog`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/fog#maxFog) : 最大雾量
- [`fogColor`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/fog#fogColor) : 雾的颜色
- [`fogStartDistance`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/fog#fogStartDistance) : 雾起始距离
- [`fogHeightOffset`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/fog#fogHeightOffset) : 雾高度
- [`fogUniformDensity`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/fog#fogUniformDensity) : 均匀雾量
- [`fogHeightFalloff`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/fog#fogHeightFalloff) : 高度衰减系数

#### 雨天效果

- [`rainSpeed`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/rain#rainSpeed) : 雨的速度
- [`rainColor`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/rain#rainColor) : 雨的颜色
- [`rainDirection`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/rain#rainDirection) : 雨的方向
- [`rainDensity`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/rain#rainDensity) : 雨的密度
- [`rainInterference`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/rain#rainInterference) : 雨的不规则性
- [`rainSizeLo`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/rain#rainSizeLo) : 雨滴的最小直径
- [`rainSizeHi`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/rain#rainSizeHi) : 雨滴的最大直径

#### 下雪效果

- [`snowColor`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/snow#snowColor) : 雪花颜色
- [`snowTexture`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/snow#snowTexture) : 雪花纹理
- [`snowDensity`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/snow#snowDensity) : 雪的密度
- [`snowFallSpeed`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/snow#snowFallSpeed) : 雪花下落速度
- [`snowSpinSpeed`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/snow#snowSpinSpeed) : 雪花自旋速度
- [`snowSizeLo`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/snow#snowSizeLo) : 雪花的最小直径
- [`snowSizeHi`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/snow#snowSizeHi) : 雪花的最大直径

### 光照系统

- [`lightMode`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/illumination#lightMode) : 作用于天空和环境光的照明类型
- [`sunFrequency`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/illumination#sunFrequency) : 太阳运动的频率
- [`sunPhase`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/illumination#sunPhase) : 太阳的初始位置
- [`sunDirection`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/illumination#sunDirection) : 太阳光照明方向
- [`sunLight`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/illumination#sunLight) : 太阳光颜色亮度
- [`skyLeftLight`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/illumination#skyLeftLight) : 环境光在-X 轴方向的亮度
- [`skyRightLight`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/illumination#skyRightLight) : 环境光在+X 轴方向的亮度
- [`skyBottomLight`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/illumination#skyBottomLight) : 环境光在-Y 轴方向的亮度
- [`skyTopLight`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/illumination#skyTopLight) : 环境光在+X 轴方向的亮度
- [`skyFrontLight`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/illumination#skyFrontLight) : 环境光在-Z 轴方向的亮度
- [`skyBackLight`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/weather/illumination#skyBackLight) : 环境光在+Z 轴方向的亮度

### 音效系统

- [`ambientSound`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/music#ambientSound) : 设置背景音乐，从地图运行开始循环播放
- [`playerJoinSound`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/music#playerJoinSound) : 当玩家进入地图时，播放的音效
- [`playerLeaveSound`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/music#playerLeaveSound) : 当玩家离开地图时，播放的音效
- [`placeVoxelSound`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/music#placeVoxelSound) : 方块被放置时，播放的音效
- [`breakVoxelSound`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/music#breakVoxelSound) : 方块被销毁时，播放的音效

## 方法

### 聊天系统

- [`say`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/chat/resident#say) : 向所有玩家广播一条消息
- [`createTempChat`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/chat/temporary#createTempChat) : 创建临时聊天频道
- [`destroyTempChat`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/chat/temporary#destroyTempChat) : 批量销毁临时聊天频道
- [`addTempChatPlayer`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/chat/temporary#addTempChatPlayer) : 向临时聊天频道添加玩家
- [`removeTempChatPlayer`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/chat/temporary#removeTempChatPlayer) : 向临时聊天频道移除玩家
- [`getTempChats`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/chat/temporary#getTempChats) : 获取当前地图存在的临时聊天频道
- [`getTempChatUsers`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/chat/temporary#getTempChatUsers) : 获取临时聊天频道中的玩家

### 实体管理

- [`createEntity`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/entityCD#createEntity) : 创建一个新实体 GameEntity 或复制一个现有的实体
- [`entityQuota`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/entityCD#entityQuota) : 返回脚本当前仍可创建的实体数量
- [`querySelector`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/querySelectorEntity#querySelector) : 搜索满足条件的第一个实体
- [`querySelectorAll`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/querySelectorEntity#querySelectorAll) : 搜索满足条件的所有实体，返回一个列表
- [`searchBox`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/querySelectorEntity#searchBox) : 搜索指定范围中的全部实体
- [`raycast`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/querySelectorEntity#raycast) : 射线检测，返回碰到的实体或方块

### 区域管理

- [`addZone`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapZone#addZone) : 创建一个区域
- [`removeZone`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapZone#removeZone) : 删除指定区域
- [`zones`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapZone#zones) : 返回所有的区域列表

### 物理系统

- [`addCollisionFilter`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/physics#addCollisionFilter) : 添加碰撞过滤器，关闭两个实体组之间的碰撞
- [`removeCollisionFilter`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/physics#removeCollisionFilter) : 移除碰撞过滤器
- [`clearCollisionFilters`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/physics#clearCollisionFilters) : 清除全部碰撞过滤器
- [`collisionFilters`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/physics#collisionFilters) : 返回当前有效的全部碰撞过滤器
- [`testSelector`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/physics#testSelector) : 测试实体是否符合某个选择器的条件

### 音效与动画

- [`sound`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/music#sound) : 播放一段声音，所有玩家都能听到
- [`animate`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/animate#animate) : 创建一个关键帧动画
- [`getAnimations`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/animate#getAnimations) : 获取当前世界所有已创建的动画
- [`getEntityAnimations`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/animate#getEntityAnimations) : 获取实体所有已创建的动画
- [`getPlayerAnimations`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/animate#getPlayerAnimations) : 获取玩家所有已创建的动画

### 地图传送

- [`teleport`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/teleport#teleport) : 地图组内传送能力，能够让玩家被传送到指定地图中

## 事件监听

### 基础事件

- [`onTick`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapInfo#onTick) : 这是世界的计时事件，每 64 毫秒触发一次，Tick 计数加 1
- [`onPlayerJoin`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/playerJL#onPlayerJoin) : 当玩家加入地图时触发
- [`onPlayerLeave`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/playerJL#onPlayerLeave) : 当玩家离开地图时触发
- [`onChat`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/chat/resident#onChat) : 当玩家在聊天窗口说话时触发

### 实体事件

- [`onEntityCreate`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/entityCD#onEntityCreate) : 当实体被创建时触发
- [`onEntityDestroy`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/entityCD#onEntityDestroy) : 当实体被销毁时触发
- [`onInteract`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#onInteract) : 玩家与实体进行互动时触发
- [`onClick`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#onClick) : 当玩家用鼠标点击实体时触发

### 输入事件

- [`onPress`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#onPress) : 当玩家按下按钮时触发
- [`onRelease`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#onRelease) : 当玩家松开按钮时触发

### 战斗事件

- [`onTakeDamage`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/fight#onTakeDamage) : 当实体受到伤害时触发
- [`onDie`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/fight#onDie) : 当实体死亡时触发
- [`onRespawn`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/fight#onRespawn) : 当实体复活时触发

### 碰撞事件

- [`onEntityContact`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#onEntityContact) : 当实体与实体发生碰撞时触发
- [`onEntitySeparate`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#onEntitySeparate) : 当实体与实体结束碰撞时触发
- [`onVoxelContact`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#onVoxelContact) : 当实体与方块发生碰撞时触发
- [`onFluidEnter`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#airFriction) : 当实体进入水里/液体时触发
- [`onFluidLeave`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#airFriction) : 当实体离开水里/液体时触发

### 区域事件

- [`onEnter`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapZone#GameZone) : 当玩家进入该区域时触发
- [`onLeave`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapZone#GameZone) : 当玩离开该区域时触发

### 商城事件

- [`onPlayerPurchaseSuccess`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/shopping#onPlayerPurchaseSuccess) : 当玩家成功购买物品时触发

## 接口定义

### 事件接口

- [`GameTickEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapInfo#GameTickEvent) : 每一刻(tick)触发一次的事件
- [`GamePlayerEntityEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/playerJL#GamePlayerEntityEvent) : 当创建或销毁实体时触发的事件
- [`GameChatEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/chat/resident#GameChatEvent) : 由聊天触发的事件
- [`GameEntityEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/entityCD#GameEntityEvent) : 实体创建与销毁事件
- [`GameInteractEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#GameInteractEvent) : 当实体互动时触发的事件
- [`GameInputEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#GameInputEvent) : 输入事件，在玩家按下或松开按钮时触发
- [`GameClickEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#GameClickEvent) : 游戏检查事件
- [`GameDamageEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/fight#GameDamageEvent) : 当实体收到伤害时触发的事件
- [`GameDieEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/fight#GameDieEvent) : 当实体死亡时触发的事件
- [`GameRespawnEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/fight#GameRespawnEvent) : 当实体复活时触发的事件
- [`GameTriggerEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapZone#GameTriggerEvent) : 当实体/玩家触发区域的事件
- [`GameEntityContactEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#GameEntityContactEvent) : 当两个实体碰撞时触发的事件
- [`GameVoxelContactEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#GameVoxelContactEvent) : 当实体触碰方块时触发的事件
- [`GameFluidContactEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#GameFluidContactEvent) : 当实体进入或离开液体时触发的事件
- [`GamePurchaseSuccessEvent`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/shopping#GamePurchaseSuccessEvent) : 当玩家成功购买物品时触发的事件

### 配置接口

- [`GameEntityConfig`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/entityCD#GameEntityConfig) : 用于控制实体的参数组
- [`GameSelectorString`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/querySelectorEntity#GameSelectorString) : 选择器可以方便搜索游戏内的全部对象
- [`GameRaycastOptions`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/querySelectorEntity#GameRaycastOptions) : 进行射线检测的参数配置
- [`GameRaycastResult`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/querySelectorEntity#GameRaycastResult) : 射线检测的结果，包含射线和所击中目标的信息
- [`GameZoneConfig`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapZone#GameZoneConfig) : 用于区域的参数
- [`GameZone`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/mapZone#GameZone) : 用于区域的配置
- [`GameSoundEffect`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/music#GameSoundEffect) : 使用 Sound()方法播放声音时，传入的参数
- [`GameWorldKeyframe`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/animate#GameWorldKeyframe) : World 世界动画关键帧参数
- [`GameAnimationPlaybackConfig`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/animate#GameAnimationPlaybackConfig) : 用于动画播放配置的参数组
- [`TeleportResult`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/teleport#TeleportResult) : 传送结果

## 枚举值

- [`GameButtonType`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/input#GameButtonType) : 玩家按下的按钮类型
- [`GameEasing`](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/animate#GameEasing) : 动画的缓动效果
