---
title: 模板字面量（Template Literals）
source: https://github.com/box3lab/box3-product-document/blob/master/arena/javascriptEntry/06-advanced-topics/05-23-template-literals.md
site: https://docs.dao3.fun/arena/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 模板字面量（Template Literals）

模板字面量使用反引号 `\`` 定义，支持插值、跨行字符串与更灵活的拼接方式，是现代 JS 构建字符串的首选。

## 1. 基本语法与插值

```javascript
const name = "Elara";
const score = 1500;
const msg = `玩家 ${name} 的分数是 ${score}`;
console.log(msg);
```

- 使用反引号 `\`` 包裹。
- 通过 `${...}` 插入任意 JS 表达式（变量、运算、函数调用等）。

## 2. 任意表达式与函数调用

```javascript
const x = 3,
  y = 4;
const len = Math.hypot(x, y);
console.log(`向量长度 = ${len.toFixed(2)}`); // 5.00

function upper(s) {
  return String(s).toUpperCase();
}
console.log(`Hi, ${upper("world")}`); // Hi, WORLD
```

## 3. 多行字符串与缩进

```javascript
const multi = `
  任务：
  - 收集 10 颗宝石
  - 打败史莱姆王
`;
console.log(multi);
```

- 反引号天然支持跨行字符串。
- 若需要移除首尾换行或统一缩进，可用小工具函数：

```javascript
function dedent(strings, ...values) {
  const raw = typeof strings === "string" ? [strings] : strings.raw;
  let result = "";
  for (let i = 0; i < raw.length; i++) {
    result += raw[i].replace(/\r/g, "");
    if (i < values.length) result += values[i];
  }
  const lines = result.split("\n");
  // 去掉首尾空行
  while (lines[0] !== undefined && lines[0].trim() === "") lines.shift();
  while (
    lines[lines.length - 1] !== undefined &&
    lines[lines.length - 1].trim() === ""
  )
    lines.pop();
  // 计算最小公共缩进
  const indents = lines
    .filter((l) => l.trim())
    .map((l) => l.match(/^\s*/)[0].length);
  const min = indents.length ? Math.min(...indents) : 0;
  return lines.map((l) => l.slice(min)).join("\n");
}

const text = dedent`
    标题
      子项 1
      子项 2
`;
console.log(text);
```

## 4. 模板中包含特殊字符与嵌套

- 反引号本身可通过反斜杠转义：`` \` ``。
- 插值占位可嵌套表达式：

```javascript
const a = 2,
  b = 3;
console.log(`结果 = ${a + b * (a + b)}`);
```

## 5. `String.raw` 与原始字符串

`String.raw` 可获取“未处理转义”的原始文本，常用于正则、路径等：

```javascript
console.log(String.raw`C:\\temp\\file.txt`); // C:\\temp\\file.txt
```

## 6. 结构化拼接与可读性

```javascript
const lines = [
  `名称: ${name}`,
  `分数: ${score}`,
  `时间: ${new Date().toLocaleString()}`,
].join("\n");
```

- 使用数组 + `join` 组织内容，避免长串难维护。

## 7. 安全性（XSS/注入）

模板字面量不会自动转义。拼接用户输入到 HTML/SQL 时要格外小心：

```javascript
const userInput = "<img src=x onerror=alert(1)>";
const html = `<div>${userInput}</div>`; // 直接赋给 innerHTML 存在 XSS 风险
```

- 解决：在插入前进行转义，或使用可信的渲染/模板方案（例如前端框架的安全插值、或“标签模板”过滤；详见下文）。

## 8. 与“标签模板（Tagged Templates）”的关系

- 标签模板是模板字面量的进阶能力，可自定义模板解析逻辑（如转义、国际化）。
- 请继续阅读《标签模板（Tagged Templates）》：`/javascriptEntry/06-advanced-topics/05-14-tagged-templates`

## 9. 常见坑

- 在循环内频繁用模板字面量拼接超长字符串可能带来性能压力（可积累到数组最后一次 `join`）。
- 将不可信内容直接插到 HTML 字符串里使用 `innerHTML`。
- 插值表达式里副作用过多，使得模板难以调试。

## 10. 最佳实践

- 优先用模板字面量替代 `+` 字符串拼接，提升可读性；
- 复杂文本用数组 + `join` 组织；
- 需要转义或定制渲染规则时，使用“标签模板”封装；
- 涉及用户输入时，始终做转义或使用安全渲染 API。

## 11. 练习

1. 将项目中使用 `+` 的字符串拼接重写为模板字面量，并比较可读性。
2. 编写一个 `escapeHTML` 标签模板，自动转义插值中的特殊字符（`<`, `>`, `&`, `"`, `'`）。
3. 使用 `dedent` 和模板字面量输出一段带缩进的多行文本，并去除公共缩进。
