---
title: 是否为玩家
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameEntity/isPlayer.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 是否为玩家

- **GamePlayerEntity** 是包含玩家属性的实体，可以同时访问[**GameEntity**](https://docs.dao3.fun/api/GameEntity/)和[**GamePlayerEntity**](https://docs.dao3.fun/api/GamePlayerEntity/)。

## 类型

```typescript
declare type GamePlayerEntity = GameEntity & {
  player: GamePlayerEntity;
  isPlayer: true;
};
```

## 属性

#### <font id="API" /><font id="ReadOnly">只读</font>isPlayer<font id="Type">: boolean</font>{#isPlayer}

如果为真，则实体为玩家。

#### <font id="API" />player<font id="Type">: [GamePlayerEntity](https://docs.dao3.fun/api/GamePlayerEntity/) | undefined</font>{#player}

如果是玩家，可以访问此属性。索引与玩家相关的全部状态和方法
