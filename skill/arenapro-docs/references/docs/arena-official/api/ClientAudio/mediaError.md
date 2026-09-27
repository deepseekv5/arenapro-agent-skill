---
title: 媒体播放错误码
source: https://github.com/box3lab/box3-product-document/blob/master/api/ClientAudio/mediaError.md
site: https://docs.dao3.fun/api/
license: Apache-2.0 (box3lab/box3-product-document)
---

# 媒体播放错误码

客户端脚本音频用于构建 error 对象（不是浏览器自己的 MediaError）
具体：[https://developer.mozilla.org/en-US/docs/Web/API/MediaError](https://developer.mozilla.org/en-US/docs/Web/API/MediaError)

## 构造函数

#### <font id="API" />MediaError(<font id="Type">code:[MediaErrorCode](https://github.com/box3lab/box3-product-document/blob/master/api/ClientAudio/mediaError#MediaErrorCode),message:string</font>)<font id="Type">: MediaError</font>

实例化一个音频播放错误码对象

**输入参数**

| **_参数_** | **_必填_** | **_默认值_** | **_类型_**     | **_说明_** |
| ---------- | ---------- | ------------ | -------------- | ---------- |
| code       | 是         |              | MediaErrorCode | 错误码     |
| message    | 是         |              | string         | 错误信息   |

## 属性

#### <font id="API" />code<font id="Type">: [MediaErrorCode](https://github.com/box3lab/box3-product-document/blob/master/api/ClientAudio/mediaError#MediaErrorCode)</font>{#code}

错误码

#### <font id="API" />message<font id="Type">: string</font>{#message}

错误信息

## 枚举

#### <font id="API" />MediaErrorCode{#MediaErrorCode}

错误码

| **属性**                    | **说明**       |
| --------------------------- | -------------- |
| MEDIA_ERR_ABORTED           | 播放被用户终止 |
| MEDIA_ERR_DECODE            | 播放时解码错误 |
| MEDIA_ERR_NETWORK           | 播放时网络错误 |
| MEDIA_ERR_SRC_NOT_SUPPORTED | 播放时源不支持 |
