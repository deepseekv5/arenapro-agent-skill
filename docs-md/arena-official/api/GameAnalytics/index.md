---
title: S-📊 游戏数据分析
source: https://github.com/box3lab/box3-product-document/blob/master/api/GameAnalytics/index.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# S-📊 游戏数据分析

**GameAnalytics** 是专业的游戏数据分析模块，提供强大的数据追踪与分析能力。借助此模块，你可以精确记录玩家行为、监控游戏事件并获取深入的数据洞察，为游戏优化和决策提供有力支持。

你可以通过全局对象 `analytics` 来使用这些功能。

**[warning]**
目前仅支持神策分析平台，且此功能仅对企业用户开放。
岛民创作者请使用神岛内置的数据分析平台
---
## 类定义

```typescript
declare const analytics: GameAnalytics;
declare class GameAnalytics {
  //...
}
```

## 属性

- [`sensor`](GameSensorAnalytics/index.md) : 神策分析平台接口
