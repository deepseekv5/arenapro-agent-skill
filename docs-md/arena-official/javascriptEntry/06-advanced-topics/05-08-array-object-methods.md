---
title: 常用 Array / Object 新方法
source: https://github.com/box3lab/box3-product-document/blob/master/arena/javascriptEntry/06-advanced-topics/05-08-array-object-methods.md
site: https://docs.dao3.fun/arena/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 常用 Array / Object 新方法

## Array

```javascript
[1, 2, 3].includes(2);              // true
[1, 2, 3].find(x => x > 1);         // 2
Array.from('abc');                  // ['a','b','c']
[1, 2, 3].flatMap(x => [x, x * 2]); // [1,2,2,4,3,6]
```

## Object

```javascript
const obj = { a: 1, b: 2 };
Object.assign({ c: 3 }, obj);        // { c: 3, a: 1, b: 2 }
Object.entries(obj);                  // [['a',1], ['b',2]]
Object.fromEntries([['x', 10]]);     // { x: 10 }
```

适用场景：
- 包含检索、转换、合并、构建对象等常见数据处理。
