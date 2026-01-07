主要目标：做一个「AI翻译助手」，包含后端接口 + 简单界面。
项目结构
AITranslator下为readme等文档，src为源码
src下 backend为后端代码，frontend为前端代码

根据以下主要需求，写一份详细文档

## 后端接口
用 Python (FastAPI) 实现一个接口：
请求：POST /translate
参数：{"text": "要翻译的中文内容"}
返回：{"translation": "英文翻译结果", "keywords": ["关键词1", "关键词2", "关键词3"]}
要求：
- 调用gemini api
- 在.env存放apikey等配置文件
## 简单界面
Flutter
- 一个输入框：输入中文
- 一个按钮：点击翻译
- 结果显示区：展示英文翻译 + 关键词

