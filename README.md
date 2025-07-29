# 🤖 AI Todo App

A simple and intelligent todo application built with Streamlit and OpenAI API that allows you to manage tasks and translate them into different languages.

## ✨ Features

- ➕ **Add Tasks** - Create new todo items
- ✅ **Mark Complete** - Toggle task completion status
- 🌐 **Hybrid Translation** - Fast predefined translations + AI fallback
  - 📚 **Instant Translation** - Common tasks translated immediately
  - 🤖 **AI Translation** - OpenAI GPT for custom/complex tasks
- 🎨 **Clean UI** - Modern, responsive interface
- 💾 **Session Storage** - Tasks persist during your session

## 🚀 Live Demo

**Streamlit Cloud:** [Your-App-URL-Here](https://your-app-url.streamlit.app)

## 🛠️ Technologies Used

- **Frontend:** Streamlit
- **AI:** OpenAI GPT-3.5-turbo
- **Language:** Python 3.12
- **Deployment:** Streamlit Cloud

## 📋 Requirements

- Python 3.8+
- OpenAI API Key
- Dependencies listed in `requirements.txt`

## 🔧 Local Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-todo-app.git
   cd ai-todo-app
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the project root:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the application:**
   ```bash
   streamlit run app.py
   ```

6. **Open in browser:**
   Navigate to `http://localhost:8501`

## 🌐 Deployment

### Streamlit Cloud Deployment

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Add your `OPENAI_API_KEY` in the secrets management
5. Deploy!

### Environment Variables for Deployment

In Streamlit Cloud secrets management, add:
```toml
OPENAI_API_KEY = "your_openai_api_key_here"
```

## 🎯 How to Use

1. **Add a Task:** Type your task in the input field and click "Add Task"
2. **Translate:** Click the 🌐 button next to any task to translate it
3. **Complete:** Click ✅ to mark tasks as completed
4. **Undo:** Click ↩️ to mark completed tasks as pending again

## 🧠 Translation System

The app uses a **hybrid translation approach**:

### 📚 Predefined Translations (Instant)
- Common tasks like "buy groceries", "do laundry", "clean house"
- 15+ predefined phrases in 5 languages (Spanish, French, German, Italian, Portuguese)
- Instant results with no API calls
- Marked with 📚 icon

### 🤖 AI Translation (GPT-Powered)
- Custom or complex tasks not in predefined list
- Uses OpenAI GPT-3.5-turbo for accurate translations
- Supports all selected languages
- Marked with 🤖 icon

### 🔍 How it Works:
1. **First Check**: Searches predefined translations
2. **Partial Match**: Checks if task contains common phrases
3. **AI Fallback**: Uses GPT if no predefined match found

## 📁 Project Structure

```
ai-todo-app/
├── app.py              # Main application
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (local only)
├── .gitignore         # Git ignore rules
└── README.md          # Project documentation
```

## 🔐 Security Notes

- Never commit your `.env` file to version control
- Your OpenAI API key should be kept secure
- Use Streamlit Cloud's secrets management for deployment

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Created with ❤️ using AI assistance

## 🐛 Issues & Support

If you encounter any issues, please [create an issue](https://github.com/yourusername/ai-todo-app/issues) on GitHub.

---

**Built with Streamlit and OpenAI API**