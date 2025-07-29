
# 🤖 AI Todo App – Smart, Fast & Multilingual Task Manager

A clean and intelligent task management app built with **Streamlit** and **OpenAI API**. Easily manage your todos and translate them across multiple languages using a hybrid approach: **predefined instant translations** and **AI-powered GPT fallback**.

---

## ✨ Features

- ➕ **Add Tasks** – Input and list new todos  
- ✅ **Complete Tasks** – Toggle completion with a single click  
- 🌐 **Hybrid Translation**  
  - 📚 **Instant Translations** – Predefined phrases translated instantly  
  - 🤖 **AI Translations** – Fallback to OpenAI GPT for custom text  
- 🎨 **Clean UI** – Minimalist and responsive design  
- 💾 **Session Storage** – Persist tasks during the browser session  

---

## 🚀 Live Demo

🔗 [Streamlit Cloud App](https://ganeshk17-ai-todo-app-app-ttmaev.streamlit.app/)

📦 [GitHub Repository](https://github.com/ganeshk17/Ai-Todo-App)

---

## 🛠️ Built With

- **UI & Backend:** [Streamlit](https://streamlit.io)  
- **AI Translation:** [OpenAI GPT-3.5 / GPT-4o]  
- **Language:** Python 3.12  
- **Deployment:** Streamlit Cloud  

---

## 📋 Requirements

- Python 3.8+
- OpenAI API Key
- `requirements.txt` dependencies

---

## 🔧 Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/ganeshk17/Ai-Todo-App
cd ai-todo-app

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add API Key to .env
echo "OPENAI_API_KEY=your_openai_key" > .env

# 5. Run the app
streamlit run app.py
```

App will open at: http://localhost:8501

---

🌐 **Deploy to Streamlit Cloud**

1. Push code to a GitHub repo  
2. Go to Streamlit Cloud  
3. Connect your GitHub repo  
4. Add the following to Secrets in deployment settings:

```toml
OPENAI_API_KEY = "your_openai_api_key"
```

Deploy 🎉

---

## 🎯 How to Use

- **Add:** Type a task and hit "Add Task"  
- **Translate:** Click 🌐 to translate to the selected language  
- **Complete:** Mark tasks done with ✅  
- **Undo:** Revert completion with ↩️  

---

## 🧠 Translation System

### 📚 Instant Predefined Phrases

Common actions like buy groceries, do laundry, etc.  
15+ hardcoded phrases across: Spanish, French, German, Italian, Portuguese  
No API usage  
Marked with 📚 icon

### 🤖 GPT Fallback

Handles custom or unfamiliar tasks  
Uses OpenAI's GPT-3.5 or GPT-4o  
Marked with 🤖 icon

---

## 🔍 Translation Flow

```sql
If exact match → use predefined 📚
Else if phrase match → use segment translation
Else → fallback to GPT 🤖
```

---

## 📁 Folder Structure

```bash
ai-todo-app/
├── app.py              # Main app logic
├── requirements.txt    # Pip dependencies
├── .env                # Local secrets (excluded from Git)
├── .gitignore          # Files to ignore
└── README.md           # You're reading it!
```

---

## 🔐 Security Best Practices

- Do NOT commit .env files  
- Use environment variables or Streamlit secrets  
- Rotate OpenAI keys regularly  

---

## 🤝 Contributing

- Fork the project  
- Create a feature branch  
- Commit your changes  
- Open a PR 🚀

---

## 📝 License

Licensed under the MIT License.

---

## 👨‍💻 Author

Made with ❤️ using Streamlit and OpenAI.

---

## 🐛 Issues & Feedback

Found a bug or want to suggest a feature? Open an issue.

Built with 🧠 AI and 🧰 Python for productive humans.
