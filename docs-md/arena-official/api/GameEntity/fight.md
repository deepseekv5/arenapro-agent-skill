---
title: 销毁与生命值
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 销毁与生命值
## 属性

#### <font id="API" />destroyed<font id="Type">: boolean</font>  {#destroyed}
> 默认值：false

如果为真(true)，实体就被销毁。



---


#### <font id="API" />enableDamage<font id="Type">: boolean</font>  {#enableDamage}
> 默认值：false

如果为真true，则可对实体进行伤害。



---


#### <font id="API" />showHealthBar<font id="Type">: boolean  </font>{#showHealthBar}
> 默认值：true

如果为真true，则显示实体的生命值HP。



---


#### <font id="API" />hp<font id="Type">: number </font>{#hp}
> 默认值：100

实体的当前生命值hp。



---


#### <font id="API" />maxHp<font id="Type">: number </font>{#maxHp}
> 默认值：100

实体的最大生命值hp。




## 方法

#### <font id="API" />destroy()<font id="Type">:  void</font>{#destroy}
销毁实体



---


#### <font id="API" />hurt(<font id="Type">amount:number,options?:Partial<[GameHurtOptions](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#GameHurtOptions)></font>)<font id="Type">:  void</font>{#hurt}
对实体的伤害数值。

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| amount | 是 | | number | 伤害值 |
| options | | | Partial‹GameHurtOptions› | 伤害的相关配置 |




---


#### <font id="API" /><font id="Event">事件</font>onDestroy(<font id="Type">handler:(event:[GameEntityEvent](https://docs.dao3.fun/api/GameWorld/playerJL#GameEntityEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onDestroy}
当实体被销毁时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| handler | 是 | | function | 监听到实体被销毁时的处理函数 |




---


#### <font id="API" /><font id="Event">事件</font>onTakeDamage(<font id="Type">handler:(event:[GameDamageEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#GameDamageEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onTakeDamage}
实体受到伤害时触发的事件

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| handler | 是 | | function | 监听到实体受到伤害时的处理函数 |




---


#### <font id="API" /><font id="Event">事件</font>onDie(<font id="Type">handler:(event:[GameDieEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/fight#GameDieEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onDie}
实体死亡时触发的事件

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明** |
| --- | --- | --- | --- | --- |
| handler | 是 | | function | 监听到实体死亡时的处理函数 |






## 接口

#### <font id="API" />GameHurtOptions{#GameHurtOptions}
攻击/伤害的相关参数

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| attacker | [GameEntity](https://docs.dao3.fun/api/GameEntity/) | 发出攻击的实体 |
| damageType | string | 伤害类型，可自行定义 |




---


#### <font id="API" />GameDamageEvent{#GameDamageEvent}
当实体收到伤害时触发的事件

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| entity | [GameEntity](https://docs.dao3.fun/api/GameEntity/) | 受到伤害的实体 |
| damage | number | 伤害值的大小 |
| attacker | [GameEntity](https://docs.dao3.fun/api/GameEntity/) &#124; null | 攻击者 |
| damageType | string | 伤害的类型 |
| tick | number | 事件发生的时间 |




---


#### <font id="API" />GameDieEvent{#GameDieEvent}
当实体死亡时触发的事件

| **参数** | **类型** | **说明** |
| --- | --- | --- |
| entity | [GameEntity](https://docs.dao3.fun/api/GameEntity/) | 死亡的实体 |
| attacker | [GameEntity](https://docs.dao3.fun/api/GameEntity/) &#124; null | 击杀者 |
| damageType | string | 伤害的类型 |
| tick | number | 事件发生的时间 |
