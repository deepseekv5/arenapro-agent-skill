---
title: 点击与互动
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 点击与互动

## 属性

#### <font id="API" />enableInteract<font id="Type">: boolean</font>{#enableInteract}

> 默认值：false

是否允许实体进行互动。如果允许互动，走进互动范围之内，实体身上将会出现互动提示。

#### <font id="API" />interactRadius<font id="Type">: number</font>{#interactRadius}

> 默认值：16

实体互动范围。数值越小，则需要靠近实体才会出现互动提示。

范围有多个可互动实体，按下键盘'['或']'键，切换互动目标。

#### <font id="API" />interactHint<font id="Type">: string</font>{#interactHint}

> 默认值：无

进入实体互动范围时，实体身上出现的提示文本。

#### <font id="API" />interactColor<font id="Type">: [GameRGBColor](https://docs.dao3.fun/api/GameRGBColor/)</font>{#interactColor}

> 默认值：GameRGBColor(0, 1, 0)

进入实体互动范围时，提示文本的颜色。

**[details]**

```javascript
// 先在场景中放置一个名称为 NPC 的实体。
const npc = world.querySelector("#NPC");
npc.enableInteract = true; // 允许进行互动
npc.interactRadius = 16; // 实体的互动范围
npc.interactHint = npc.id; // 互动提示框显示实体的名称
npc.interactColor = new GameRGBColor(1, 0, 1); // 互动提示的文字颜色

// 玩家与实体进行交互时触发
npc.onInteract(async ({ entity }) => {
  const result = await entity.player.dialog({
    type: GameDialogType.TEXT, // 对话框的类型，TEXT是文本框。
    title: npc.id, // 对话框标题为NPC名字，表示正在说话的是NPC
    lookEye: entity, // 将相机放在玩家位置
    lookTarget: npc, // 相机镜interactHint头对准NPC
    content: `你好，${entity.player.name}，很高兴认识你。`,
  });
});
```

---
## 方法

#### <font id="API" />say(<font id="Type">message:string,options?: Partial<{duration: number,hideFloat: boolean}></font>)<font id="Type">: void</font>{#say}

让实体说话。

**输入参数**

| **参数**          | **必填** | **默认值** | **类型** | **说明**                         |
| ----------------- | -------- | ---------- | -------- | -------------------------------- |
| message           | 是       |            | string   | 说话的内容                       |
| options.duration  |          | 2000       | number   | 气泡及广播提示语的持续时间（ms） |
| options.hideFloat |          | false      | boolean  | 气泡内容是否在世界广播上隐藏？   |

**[details]**

```javascript
// 创建一个实体并让它每秒说一句话
const e = world.createEntity({
  position: [64, 9, 64],
});

setInterval(() => {
  e.say("hey, im a box.  my position is " + e.position.toString());
}, 1000);
```

---
#### <font id="API" /><font id="Event">事件</font>onClick(<font id="Type">handler:(event:[GameClickEvent](https://docs.dao3.fun/api/GameWorld/input#GameClickEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onClick}

当玩家用鼠标点击实体时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                   |
| -------- | -------- | ---------- | -------- | -------------------------- |
| handler  | 是       |            | function | 监听到鼠标点击时的处理函数 |

#### <font id="API" /><font id="Event">事件</font>onInteract(<font id="Type">handler:(event:[GameInteractEvent](https://docs.dao3.fun/api/GameWorld/input#GameInteractEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onInteract}

当实体进行互动时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**               |
| -------- | -------- | ---------- | -------- | ---------------------- |
| handler  | 是       |            | function | 监听到互动时的处理函数 |

#### <font id="API" /><font id="Event">事件</font>onEntityContact(<font id="Type">handler:(event:[GameEntityContactEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#GameEntityContactEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onEntityContact}

当实体触碰另一个实体时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                       |
| -------- | -------- | ---------- | -------- | ------------------------------ |
| handler  | 是       |            | function | 监听到碰到另外的实体的处理函数 |

#### <font id="API" /><font id="Event">事件</font>onEntitySeparate(<font id="Type">handler:(event:[GameEntityContactEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#GameEntityContactEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onEntitySeparate}

当实体停止触碰另一个实体时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                           |
| -------- | -------- | ---------- | -------- | ---------------------------------- |
| handler  | 是       |            | function | 监听到停止碰到另外的实体的处理函数 |

#### <font id="API" /><font id="Event">事件</font>onFluidEnter(<font id="Type">handler:(event:[GameFluidContactEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#GameFluidContactEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onFluidEnter}

当实体进入液体时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                       |
| -------- | -------- | ---------- | -------- | ------------------------------ |
| handler  | 是       |            | function | 监听到进入液体的实体的处理函数 |

#### <font id="API" /><font id="Event">事件</font>onFluidLeave(<font id="Type">handler:(event:[GameFluidContactEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#GameFluidContactEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onFluidLeave}

当实体离开液体时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                       |
| -------- | -------- | ---------- | -------- | ------------------------------ |
| handler  | 是       |            | function | 监听到离开液体的实体的处理函数 |

#### <font id="API" /><font id="Event">事件</font>onVoxelContact(<font id="Type">handler:(event:[GameVoxelContactEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#GameVoxelContactEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onVoxelContact}

当实体触碰方块时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                       |
| -------- | -------- | ---------- | -------- | ------------------------------ |
| handler  | 是       |            | function | 监听到触碰方块的实体的处理函数 |

#### <font id="API" /><font id="Event">事件</font>onVoxelSeparate(<font id="Type">handler:(event:[GameVoxelContactEvent](https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/input#GameVoxelContactEvent))=>void</font>)<font id="Type">: [GameEventHandlerToken](https://docs.dao3.fun/api/GameEventHandlerToken/)</font>{#onVoxelSeparate}

当实体停止触碰方块时触发

**输入参数**

| **参数** | **必填** | **默认值** | **类型** | **说明**                           |
| -------- | -------- | ---------- | -------- | ---------------------------------- |
| handler  | 是       |            | function | 监听到停止触碰方块的实体的处理函数 |

## 接口

#### <font id="API" />GameEntityContactEvent{#GameEntityContactEvent}

当两个实体碰撞时触发的事件

| **参数** | **类型**                     | **说明**                                 |
| -------- | ---------------------------- | ---------------------------------------- |
| entity   | [GameEntity](https://docs.dao3.fun/api/GameEntity/)   | 碰撞中的第一个实体                       |
| other    | [GameEntity](https://docs.dao3.fun/api/GameEntity/)   | 碰撞中的第二个实体                       |
| axis     | [GameVector3](https://docs.dao3.fun/api/GameVector3/) | 碰撞的分离轴，也就是碰撞后物体弹飞的方向 |
| tick     | number                       | 两个实体碰撞的时间                       |
| force    | [GameVector3](https://docs.dao3.fun/api/GameVector3/) | 碰撞所产生的力                           |

#### <font id="API" />GameFluidContactEvent{#GameFluidContactEvent}

当实体进入或离开液体时触发的事件

| **参数** | **类型**                   | **说明**                 |
| -------- | -------------------------- | ------------------------ |
| entity   | [GameEntity](https://docs.dao3.fun/api/GameEntity/) | 触碰液体的实体           |
| voxel    | number                     | 液体方块 id              |
| tick     | number                     | 实体进入或离开液体的时间 |

#### <font id="API" />GameVoxelContactEvent{#GameVoxelContactEvent}

当实体触碰方块时触发的事件

| **参数** | **类型**                     | **说明**                                 |
| -------- | ---------------------------- | ---------------------------------------- |
| entity   | [GameEntity](https://docs.dao3.fun/api/GameEntity/)   | 触碰到方块的实体                         |
| voxel    | number                       | 液体方块 id                              |
| tick     | number                       | 实体触碰方块的时间                       |
| axis     | [GameVector3](https://docs.dao3.fun/api/GameVector3/) | 触碰的分离轴，也就是触碰后物体弹飞的方向 |
| force    | [GameVector3](https://docs.dao3.fun/api/GameVector3/) | 碰撞力                                   |
| voxel    | number                       | 被触碰的方块 id                          |
| x        | number                       | 被触碰方块的 x 坐标                      |
| y        | number                       | 被触碰方块的 y 坐标                      |
| z        | number                       | 被触碰方块的 z 坐标                      |
