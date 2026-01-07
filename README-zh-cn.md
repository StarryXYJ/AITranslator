# AI 翻译助手

一个简单的全栈应用程序，用于将中文文本翻译成英文并提取关键词汇。

## 技术栈

- **后端**: Python (FastAPI)
- **前端**: Flutter (跨平台)
- **AI 模型**: Google Gemini API

## 项目设置

### 后端设置

1. 进入后端目录：
   ```bash
   cd src/backend
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 配置环境变量：
   - 复制 `.env.example` 文件为 `.env`
   - 在 `.env` 文件中添加你的 `GEMINI_API_KEY`

4. 启动服务器：
   ```bash
   uvicorn main:app --reload
   ```

   服务器将在 `http://localhost:8000` 运行

### 前端设置

1. 进入前端目录：
   ```bash
   cd src/frontend
   ```

2. 安装依赖：
   ```bash
   flutter pub get
   ```

3. 运行应用：
   - **Windows 桌面**: `flutter run -d windows`
   - **macOS 桌面**: `flutter run -d macos`
   - **Linux 桌面**: `flutter run -d linux`
   - **Web 浏览器**: `flutter run -d chrome`
   - **移动设备**: 连接设备后运行 `flutter run`

## 使用方法

1. 启动后端服务器（默认地址：`http://localhost:8000`）
2. 启动 Flutter 应用
3. 在输入框中输入中文文本
4. 点击"翻译"按钮
5. 查看英文翻译结果和提取的关键词

## 功能特性

- ✨ 中译英翻译
- 🔑 自动提取关键词汇
- 🎨 美观的渐变 UI 设计
- 📱 跨平台支持（Windows、macOS、Linux、Web、iOS、Android）
- ⚡ 基于 Google Gemini API 的智能翻译

## API 文档

### POST /translate

**请求体**:
```json
{
  "text": "要翻译的中文内容"
}
```

**响应体**:
```json
{
  "translation": "英文翻译结果",
  "keywords": ["关键词1", "关键词2", "关键词3"]
}
```

## 项目结构

```
AITranslator/
├── .env.example        # 环境变量模板
├── README.md           # 项目说明文档
├── Requirement.md      # 需求文档
├── ProjectDocumentation.md  # 详细技术文档
└── src/
    ├── backend/        # 后端代码
    │   ├── main.py     # FastAPI 入口文件
    │   └── requirements.txt  # Python 依赖
    └── frontend/       # 前端代码
        ├── lib/
        │   └── main.dart  # Flutter 主应用
        └── pubspec.yaml   # Flutter 依赖
```

## 注意事项

> ⚠️ **重要提示**
> 
> - 运行前必须在 `.env` 文件中配置有效的 `GEMINI_API_KEY`
> - 确保后端服务器已启动再运行前端应用
> - 首次运行前端需要先执行 `flutter pub get` 安装依赖

## 开发者信息

本项目使用 Google Gemini 2.5 Flash Lite 模型进行翻译。

## 许可证

本项目为开源项目，供学习和参考使用。
