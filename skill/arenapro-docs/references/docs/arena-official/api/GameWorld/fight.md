---
title: 战斗与生命值
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/fight.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 战斗与生命值
**[info]**
若实体开启了允许伤害的属性 `enableDamage = true` ，可以通过 `hurt()` 方法对该实体造成生命值伤害。

**伤害**: 实体受到伤害，会触发 `onTakeDamage()` 事件。

**死亡**: 实体生命值 HP 降为0以下时，实体将触发死亡事件 `onDie()` , 倒地不起。

**复活**: 实体死亡后，可通过增加生命值 HP ，让实体进行复活，同时触发 `onRespawn()` 事件。

**强制重生**: 如果实体类型为玩家，还可以通过 `forceRespawn()` 方法，使玩家强制重生，返回 出生点 。
---
## 方法

#### <font id="API" /><font id="Event">事件</font>onTakeDamage(<font id="Type">handler:(event:[GameDamageEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/fight#GameDamageEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onTakeDamage}
当实体受到伤害时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| handler | _是_ | | function | 监听到有实体受到伤害时的处理函数 |



**[details]**
```javascript
/* 受到伤害时，向玩家发送私信，提示战斗信息 */
world.onTakeDamage(({ entity, attacker, damage}) => {
  if (!entity.isPlayer) return;
  const attackerName = attacker.isPlayer ? attacker.player.name : attacker.id;
  entity.player.directMessage(`[剩余HP: {entity.hp}]: 你受到了 ${damage} 点来自 {attackerName} 的伤害`);
});
```
---
---


#### <font id="API" /><font id="Event">事件</font>onDie(<font id="Type">handler:(event:[GameDieEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/fight#GameDieEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onDie}
当实体死亡时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| handler | _是_ | | function | 监听到有实体死亡时的处理函数 |



**[details]**
```javascript
// 一名玩家被其他玩家击杀时，广播一条消息
world.onDie(({ entity, attacker }) => {
  if (!attacker || !entity.isPlayer) return;
  world.say(`{attacker.player.name}击杀了{entity.player.name}`);
});
```
---
```javascript
// 玩家死亡时，等待5秒后复活。 
world.onDie(async({ entity }) => { // 等待事件需要用 async
  if (!entity.isPlayer) return;  // 不处理非玩家的死亡事件 for (let t = 1; t <= 5; t++) {
    entity.player.directMessage(`倒计时 ${String(5 - t)} 秒后复活`);
    await sleep(1000);
  } entity.player.forceRespawn();  // 让玩家重生
});
```
---
---


#### <font id="API" /><font id="Event">事件</font>onRespawn(<font id="Type">handler:(event:[GameRespawnEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameWorld/fight#GameRespawnEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onRespawn}
当实体复活时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| handler | _是_ | | function | 监听到有实体复活时的处理函数 |



**[info]**
GameWorld 和 GameEntity 拥有相同的触发事件。 他们的区别是

- **GameWorld** 会触发世界所有的实体事件。
- **GameEntity** 只触发实体本身的事件。
---
**[details]**
```javascript
// 玩家复活时，广播一条消息
world.onRespawn(({ entity }) => {
  if (!entity.isPlayer) return;
  world.say(`${entity.player.name} 复活了`);
});
```
---
## 接口

#### <font id="API" />GameDamageEvent{#GameDamageEvent}
当实体收到伤害时触发的事件

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| entity | [GameEntity](https://docs.dao3.fun/api/GameEntity/) | 受到伤害的实体 |
| attacker | [GameEntity](https://docs.dao3.fun/api/GameEntity/) &#124; null | 攻击者 |
| damage | number | 伤害值 |
| damageType | string | 伤害类型 |
| tick | number | 事件发生时间 |



---


#### <font id="API" />GameDieEvent{#GameDieEvent}
当实体死亡时触发的事件

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| entity | [GameEntity](https://docs.dao3.fun/api/GameEntity/) | 死亡的实体 |
| attacker | [GameEntity](https://docs.dao3.fun/api/GameEntity/) &#124; null | 击杀者 |
| damageType | string | 伤害类型 |
| tick | number | 事件发生时间 |


---


#### <font id="API" />GameRespawnEvent{#GameRespawnEvent}
当实体复活时触发的事件

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| entity | [GamePlayerEntity](https://docs.dao3.fun/api/GameEntity/isPlayer) | 死亡的实体 |
| tick | number | 事件发生时间 |
