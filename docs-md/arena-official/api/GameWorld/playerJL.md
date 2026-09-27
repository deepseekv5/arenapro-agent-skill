---
title: 玩家进入/离开地图
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/playerJL.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 玩家进入/离开地图
## 方法

#### <font id="API" /><font id="Event">事件</font>onPlayerJoin(<font id="Type">handler:(event:[GamePlayerEntityEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/playerJL#GamePlayerEntityEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font> {#onPlayerJoin}
当玩家加入地图时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| handler | _是_ | | function | 监听到玩家加入时的处理函数 |



**[details]**
```javascript
// 玩家进入地图时，向TA发送一条私信。
world.onPlayerJoin(({ entity }) => {
  entity.player.directMessage(`你好，${entity.player.name}`);
});
```
---
```javascript
// 玩家进入地图时，开启飞行功能
world.onPlayerJoin(({ entity }) => {
  entity.player.canFly = true;
});
```
---
```javascript
const TEST_PLAYER = ['吉吉喵', '搬砖喵', '美术喵', '文档喵']

world.onPlayerJoin(({ entity }) => {
  if (!TEST_PLAYER.includes(entity.player.name)) return; // 如果玩家名称不在列表里，则跳过后续脚本。
  world.say(`${entity.player.name} 出现了！`);
})
```
---
---


#### <font id="API" /><font id="Event">事件</font>onPlayerLeave(<font id="Type">handler:(event:[GamePlayerEntityEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/playerJL#GamePlayerEntityEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onPlayerLeave}
当玩家离开地图时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| handler | _是_ | | function | 监听到玩家离开时的处理函数 |



**[details]**
```javascript
// 玩家离开地图时，在控制台输出玩家的名字。
world.onPlayerLeave(({ entity }) => {
  console.log(`玩家 ${entity.player.name} 退出了地图。`);
});
```
---
## 接口

#### <font id="API" />GamePlayerEntityEvent{#GamePlayerEntityEvent}
当创建或销毁实体时触发的事件

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| entity | [GameEntity](https://docs.dao3.fun/api/GameEntity/) | 创建的实体 |
| tick | number | 事件发生时间 |
