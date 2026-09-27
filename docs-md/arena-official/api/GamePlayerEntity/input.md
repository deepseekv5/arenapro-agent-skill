---
title: 按键与行动
source: https://github.com/box3lab/box3-product-document/blob/master/api/GamePlayerEntity/input.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 按键与行动

## 属性

### 虚拟按键

#### <font id="API" />gamepad<font id="Type">: [Gamepad](https://github.com/box3lab/box3-product-document/blob/master/api/GamePlayerEntity/input#Gamepad)</font>{#gamepad}

设置虚拟按键图片

### 实体按键

#### <font id="API" />disableInputDirection<font id="Type">: [GameInputDirection](https://github.com/box3lab/box3-product-document/blob/master/api/GamePlayerEntity/input#GameInputDirection)</font>{#disableInputDirection}

> 默认值：GameInputDirection.NONE

禁用指定方向的摇杆输入偏移量，当横纵两个方向均被禁用时，将不显示此玩家的触屏虚拟摇杆。

#### <font id="API" />enableAction0<font id="Type">: boolean</font>{#enableAction0}

> 默认值：true

启动鼠标左键/移动端虚拟按钮 A 键

#### <font id="API" />enableAction1<font id="Type">: boolean</font>{#enableAction1}

> 默认值：true

启动鼠标右键/移动端虚拟按钮 B 键

#### <font id="API" />action0Button<font id="Type">: boolean</font>{#action0Button}

> 默认值：false

鼠标左键/移动端虚拟按钮 A 键

#### <font id="API" />action1Button<font id="Type">: boolean</font>{#action1Button}

> 默认值：false

鼠标右键/移动端虚拟按钮 B 键

#### <font id="API" />jumpButton<font id="Type">: boolean</font>{#jumpButton}

> 默认值：false

跳跃按钮

#### <font id="API" />walkButton<font id="Type">: boolean</font>{#walkButton}

> 默认值：false

步行按钮

### 行动

#### <font id="API" />swapInputDirection<font id="Type">: boolean</font>{#swapInputDirection}

> 默认值：false

是否交换方向按键

**[warning]**
相对摄像机视角而言：

不开启：w：前进，s：后退，a：左走，d：右走

开启：w：右走，s：左走，a：后退，d：前进
---
#### <font id="API" />reverseInputDirection<font id="Type">: [GameInputDirection](https://github.com/box3lab/box3-product-document/blob/master/api/GamePlayerEntity/input#GameInputDirection)</font>{#reverseInputDirection}

> 默认值：GameInputDirection.NONE

反转指定方向的摇杆

#### <font id="API" />facingDirection<font id="Type">: [GameVector3](https://docs.dao3.fun/api/GameVector3/)</font>{#facingDirection}

> 默认值：GameVector3(1, 0, 0)

玩家朝向

#### <font id="API" />canFly<font id="Type">: boolean</font>{#canFly}

> 默认值：false

如果为真(true)，则允许玩家飞行

#### <font id="API" />spectator<font id="Type">: boolean</font>{#spectator}

> 默认值：false

如果为真(true)，则玩家是一个幽灵，可以穿墙

#### <font id="API" />enableJump<font id="Type">: boolean</font>{#enableJump}

> 默认值：true

如果为假(false)，则不允许玩家跳跃

#### <font id="API" />enableDoubleJump<font id="Type">: boolean</font>{#enableDoubleJump}

> 默认值：true

如果为假(false)，则不允许玩家二段跳跃

#### <font id="API" />walkSpeed<font id="Type">: number</font>{#walkSpeed}

> 默认值：0.22

最大步行速度

#### <font id="API" />runSpeed<font id="Type">: number</font>{#runSpeed}

> 默认值：0.4

最大奔跑速度

#### <font id="API" />runAcceleration<font id="Type">: number</font>{#runAcceleration}

> 默认值：0.35

奔跑加速度

#### <font id="API" />jumpPower<font id="Type">: number</font>{#jumpPower}

> 默认值：0.96

跳跃力度

#### <font id="API" />jumpSpeedFactor<font id="Type">: number</font>{#jumpSpeedFactor}

> 默认值：0.85

跳跃速度

#### <font id="API" />jumpAccelerationFactor<font id="Type">: number</font>{#jumpAccelerationFactor}

> 默认值：0.55

跳跃加速率

#### <font id="API" />doubleJumpPower<font id="Type">: number</font>{#doubleJumpPower}

> 默认值：0.9

二段跳力度

#### <font id="API" />crouchSpeed<font id="Type">: number</font>{#crouchSpeed}

> 默认值：0.1

蹲着走路的速度

#### <font id="API" />crouchAcceleration<font id="Type">: number</font>{#crouchAcceleration}

> 默认值：0.09

蹲着走路的加速度

#### <font id="API" />flySpeed<font id="Type">: number</font>{#flySpeed}

> 默认值：2

最大飞行速度

#### <font id="API" />flyAcceleration<font id="Type">: number</font>{#flyAcceleration}

> 默认值：2

飞行加速度

#### <font id="API" />swimAcceleration<font id="Type">: number</font>{#swimAcceleration}

> 默认值：0.1

游泳加速度

#### <font id="API" />swimSpeed<font id="Type">: number</font>{#swimSpeed}

> 默认值：0.4

最大游泳速度

#### <font id="API" />walkAcceleration<font id="Type">: number</font>{#walkAcceleration}

> 默认值：0.19

步行加速度

#### <font id="API" /><font id="ReadOnly">只读</font>moveState<font id="Type">: [GamePlayerMoveState](https://github.com/box3lab/box3-product-document/blob/master/api/GamePlayerEntity/input#GamePlayerMoveState)</font>{#moveState}

> 默认值：GamePlayerMoveState.FALL

玩家的运动状态

#### <font id="API" /><font id="ReadOnly">只读</font>walkState<font id="Type">: [GamePlayerWalkState](https://github.com/box3lab/box3-product-document/blob/master/api/GamePlayerEntity/input#GamePlayerWalkState)</font>{#walkState}

> 默认值： GamePlayerWalkState.NONE

玩家的步行状态

#### <font id="API" /><font id="ReadOnly">只读</font>cameraPitch<font id="Type">: number</font>{#cameraPitch}

> 默认值：0

玩家视角准心绕水平方向的旋转弧度

#### <font id="API" /><font id="ReadOnly">只读</font>cameraYaw<font id="Type">: number</font>{#cameraYaw}

> 默认值：0

玩家视角准心绕垂直方向的旋转弧度

## 方法

#### <font id="API" /><font id="Event">事件</font>onPress(<font id="Type">handler:(event:[GameInputEvent](https://docs.dao3.fun/api/GameWorld/input#GameInputEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onPress}

当玩家按下按钮时调用

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                       |
| -------- | -------- | ---------- | -------- | ------------------------------ |
| handler  | 是       |            | function | 监听到玩家按下按钮时的处理函数 |

#### <font id="API" /><font id="Event">事件</font>onRelease(<font id="Type">handler:(event:[GameInputEvent](https://docs.dao3.fun/api/GameWorld/input#GameInputEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onRelease}

当玩家松开按钮时调用

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                       |
| -------- | -------- | ---------- | -------- | ------------------------------ |
| handler  | 是       |            | function | 监听到玩家松开按钮时的处理函数 |

#### <font id="API" /><font id="Event">事件</font>onKeyDown(<font id="Type">handler:(event:[GameKeyBoardEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GamePlayerEntity/input#GameKeyBoardEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onKeyDown}

当玩家按下键盘时调用

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                       |
| -------- | -------- | ---------- | -------- | ------------------------------ |
| handler  | 是       |            | function | 监听到玩家按下键盘时的处理函数 |

#### <font id="API" /><font id="Event">事件</font>onKeyUp(<font id="Type">handler:(event:[GameKeyBoardEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GamePlayerEntity/input#GameKeyBoardEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onKeyUp}

当玩家松开键盘时调用

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                       |
| -------- | -------- | ---------- | -------- | ------------------------------ |
| handler  | 是       |            | function | 监听到玩家松开键盘时的处理函数 |

#### <font id="API" />kick()<font id="Type">: void</font>{#kick}

把玩家"踢出"当前地图

## 接口

#### <font id="API" />GameKeyBoardEvent{#GameKeyBoardEvent}

输入事件，在玩家按下或松开按键时触发。

| **参数** | **类型** | **说明**                                  |
| -------- | -------- | ----------------------------------------- |
| keyCode  | number   | 按下/松开按键的[keyCode](https://github.com/box3lab/box3-product-document/blob/master/api/GamePlayerEntity/input#keyCode) |
| tick     | number   | 按下/松开按钮的时间                       |

#### <font id="API" />Gamepad{#Gamepad}

虚拟按键背景图片配置

| **参数**           | **类型** | **说明**       |
| ------------------ | -------- | -------------- |
| joystickBackground | string   | 操纵杆背景     |
| joystickController | string   | 操纵杆控制器   |
| flyButton          | string   | 飞行按钮       |
| flyingBackground   | string   | 飞行按钮背景   |
| flyingController   | string   | 飞行按钮控制器 |
| jump               | string   | 跳跃按钮       |
| crouch             | string   | 蹲下按钮       |
| actionA            | string   | A 键按钮       |
| actionB            | string   | B 键按钮       |

## 枚举

#### <font id="API" />GamePlayerMoveState{#GamePlayerMoveState}

玩家的运动状态

| **属性**    | **说明** |
| ----------- | -------- |
| FLYING      | 飞行中   |
| GROUND      | 在地上   |
| SWIM        | 游泳中   |
| FALL        | 下落中   |
| JUMP        | 跳跃中   |
| DOUBLE_JUMP | 二段跳中 |

#### <font id="API" />GamePlayerWalkState {#GamePlayerWalkState}

玩家的行走状态

| **属性** | **说明** |
| -------- | -------- |
| NONE     | 非行走中 |
| CROUCH   | 下蹲行走 |
| WALK     | 正常步行 |
| RUN      | 奔跑     |

#### <font id="API" />GameInputDirection{#GameInputDirection}

玩家通过输入设备控制移动时的方向

| **属性**   | **说明**       |
| ---------- | -------------- |
| NONE       | 无，代表不禁用 |
| VERTICAL   | 垂直方向       |
| HORIZONTAL | 水平方向       |
| BOTH       | 所有方向       |

## keyCode 映射表{#keyCode}

**字母和数字键的键码值**

| 按键  | 键码 |     | 按键  | 键码 |     | 按键  | 键码 |     | 按键  | 键码 |
| ----- | ---- | --- | ----- | ---- | --- | ----- | ---- | --- | ----- | ---- |
| **A** | 65   |     | **J** | 74   |     | **S** | 83   |     | **1** | 49   |
| **B** | 66   |     | **K** | 75   |     | **T** | 84   |     | **2** | 50   |
| **C** | 67   |     | **L** | 76   |     | **U** | 85   |     | **3** | 51   |
| **D** | 68   |     | **M** | 77   |     | **V** | 86   |     | **4** | 52   |
| **E** | 69   |     | **N** | 78   |     | **W** | 87   |     | **5** | 53   |
| **F** | 70   |     | **O** | 79   |     | **X** | 88   |     | **6** | 54   |
| **G** | 71   |     | **P** | 80   |     | **Y** | 89   |     | **7** | 55   |
| **H** | 72   |     | **Q** | 81   |     | **Z** | 90   |     | **8** | 56   |
| **I** | 73   |     | **R** | 82   |     | **0** | 48   |     | **9** | 57   |

**数字键盘上的键的键码值** | **功能键键码值**

| 按键  | 键码 |     | 按键      | 键码 |     | 按键   | 键码 |     | 按键    | 键码 |
| ----- | ---- | --- | --------- | ---- | --- | ------ | ---- | --- | ------- | ---- |
| **0** | 96   |     | **8**     | 104  |     | **F1** | 112  |     | **F7**  | 118  |
| **1** | 97   |     | **9**     | 105  |     | **F2** | 113  |     | **F8**  | 119  |
| **2** | 98   |     | \*        | 106  |     | **F3** | 114  |     | **F9**  | 120  |
| **3** | 99   |     | **+**     | 107  |     | **F4** | 115  |     | **F10** | 121  |
| **4** | 100  |     | **Enter** | 108  |     | **F5** | 116  |     | **F11** | 122  |
| **5** | 101  |     | **-**     | 109  |     | **F6** | 117  |     | **F12** | 123  |
| **6** | 102  |     | **.**     | 110  |     |        |      |     |         |      |
| **7** | 103  |     | **/**     | 111  |     |        |      |     |         |      |

**控制键键码值**

| 按键          | 键码 |     | 按键           | 键码 |     | 按键            | 键码 |     | 按键         | 键码 |
| ------------- | ---- | --- | -------------- | ---- | --- | --------------- | ---- | --- | ------------ | ---- |
| **BackSpace** | 8    |     | **Esc**        | 27   |     | **Right Arrow** | 39   |     | **-\_**      | 189  |
| **Tab**       | 9    |     | **Spacebar**   | 32   |     | **Dw Arrow**    | 40   |     | **.>**       | 190  |
| **Clear**     | 12   |     | **Page Up**    | 33   |     | **Insert**      | 45   |     | **/?**       | 191  |
| **Enter**     | 13   |     | **Page Down**  | 34   |     | **Delete**      | 46   |     | **`~**       | 192  |
| **Shift**     | 16   |     | **End**        | 35   |     | **Num Lock**    | 144  |     | **[{**       | 219  |
| **Control**   | 17   |     | **Home**       | 36   |     | **;:**          | 186  |     | **\\&#124;** | 220  |
| **Alt**       | 18   |     | **Left Arrow** | 37   |     | **=+**          | 187  |     | **]}**       | 221  |
| **Caps Lock** | 20   |     | **Up Arrow**   | 38   |     | **,<**          | 188  |     | **'"**       | 222  |

**多媒体键码值**
| 按键 | 键码 |
| --- | --- |
| **音量加** | 175 |  
| **音量减** | 174 |  
| **停止** | 179 |  
| **静音** | 173 |
| **浏览器** | 172 |  
| **邮件** | 180 |  
| **搜索** | 170 |  
| **收藏** | 171 |
