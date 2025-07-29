import streamlit as st
from openai import OpenAI
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Configure page
st.set_page_config(
    page_title="Simple AI Todo App",
    page_icon="✅",
    layout="centered"
)

# Custom CSS
st.markdown("""
<style>
.todo-item {
    background-color: #f8f9fa;
    padding: 1rem;
    border-radius: 8px;
    margin: 0.5rem 0;
    border-left: 4px solid #007bff;
}

.completed {
    background-color: #d4edda;
    border-left-color: #28a745;
    opacity: 0.8;
}

.completed-text {
    text-decoration: line-through;
    color: #6c757d;
}

.translation {
    background-color: #e3f2fd;
    padding: 0.5rem;
    border-radius: 5px;
    margin-top: 0.5rem;
    font-style: italic;
}
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'todos' not in st.session_state:
    st.session_state.todos = []

# App header
st.title("🤖 Simple AI Todo App")
st.markdown("Add tasks, translate them, and delete when done!")

# Get API key from environment
api_key = os.getenv('OPENAI_API_KEY')

# Check if API key is available
if not api_key:
    st.error("❌ OPENAI_API_KEY not found in environment variables. Please add it to your .env file.")
    st.stop()

# Language selection
languages = ['Spanish', 'French', 'German', 'Italian', 'Portuguese', 'Chinese', 'Japanese', 'Korean', 'Arabic', 'Hindi']
target_language = st.sidebar.selectbox("Translation Language", languages)

# Function to translate text
def translate_task(text, language):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini-2024-07-18",
            messages=[
                {"role": "system", "content": f"Translate the following text to {language}. Only return the translation:"},
                {"role": "user", "content": text}
            ],
            max_tokens=100,
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Translation failed: {str(e)}"

# Add new task section
st.header("➕ Add New Task")
with st.form("add_task"):
    new_task = st.text_input("What do you need to do?", placeholder="Enter your task here...")
    submit = st.form_submit_button("Add Task", type="primary")
    
    if submit and new_task.strip():
        task_data = {
            'id': len(st.session_state.todos),
            'text': new_task.strip(),
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M"),
            'completed': False,
            'translation': None
        }
        st.session_state.todos.append(task_data)
        st.success(f"✅ Added: {new_task}")
        st.rerun()

# Display tasks
st.header("📝 Your Tasks")

if not st.session_state.todos:
    st.info("No tasks yet! Add your first task above.")
else:
    for i, todo in enumerate(st.session_state.todos):
        # Apply completed styling
        todo_class = "completed" if todo['completed'] else ""
        st.markdown(f'<div class="todo-item {todo_class}">', unsafe_allow_html=True)
        
        # Task content
        col1, col2, col3 = st.columns([3, 1, 1])
        
        with col1:
            # Show task with strikethrough if completed
            text_class = "completed-text" if todo['completed'] else ""
            st.markdown(f'<p class="{text_class}"><strong>{todo["text"]}</strong></p>', unsafe_allow_html=True)
            st.caption(f"{'✅ Completed' if todo['completed'] else '⏳ Pending'} | Created: {todo['created_at']}")
        
        with col2:
            # Translate button
            if st.button("🌐 Translate", key=f"translate_{todo['id']}"):
                with st.spinner("Translating..."):
                    translation = translate_task(todo['text'], target_language)
                    st.session_state.todos[i]['translation'] = translation
                    st.rerun()
        
        with col3:
            # Complete/Uncomplete button
            if todo['completed']:
                if st.button("↩️ Undo", key=f"undo_{todo['id']}", type="secondary"):
                    st.session_state.todos[i]['completed'] = False
                    st.success("Task marked as pending!")
                    st.rerun()
            else:
                if st.button("✅ Complete", key=f"complete_{todo['id']}", type="primary"):
                    st.session_state.todos[i]['completed'] = True
                    st.success("Task completed!")
                    st.rerun()
        
        # Show translation if available
        if todo['translation']:
            st.markdown(f'<div class="translation">🌐 {target_language}: {todo["translation"]}</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("---")

# Footer
st.markdown("---")
st.caption("Built with Streamlit and OpenAI API")