import streamlit as st
from openai import OpenAI
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Predefined translations dictionary
PREDEFINED_TRANSLATIONS = {
    # Common task phrases in different languages
    'Spanish': {
        'buy groceries': 'comprar comestibles',
        'do laundry': 'hacer la colada',
        'clean house': 'limpiar la casa',
        'walk the dog': 'pasear al perro',
        'pay bills': 'pagar facturas',
        'call doctor': 'llamar al doctor',
        'study for exam': 'estudiar para el examen',
        'finish project': 'terminar proyecto',
        'exercise': 'hacer ejercicio',
        'cook dinner': 'cocinar la cena',
        'water plants': 'regar plantas',
        'take medication': 'tomar medicación',
        'attend meeting': 'asistir a reunión',
        'read book': 'leer libro',
        'write report': 'escribir informe'
    },
    'French': {
        'buy groceries': 'acheter des courses',
        'do laundry': 'faire la lessive',
        'clean house': 'nettoyer la maison',
        'walk the dog': 'promener le chien',
        'pay bills': 'payer les factures',
        'call doctor': 'appeler le docteur',
        'study for exam': 'étudier pour l\'examen',
        'finish project': 'terminer le projet',
        'exercise': 'faire de l\'exercice',
        'cook dinner': 'cuisiner le dîner',
        'water plants': 'arroser les plantes',
        'take medication': 'prendre des médicaments',
        'attend meeting': 'assister à la réunion',
        'read book': 'lire un livre',
        'write report': 'écrire un rapport'
    },
    'German': {
        'buy groceries': 'Lebensmittel einkaufen',
        'do laundry': 'Wäsche waschen',
        'clean house': 'Haus putzen',
        'walk the dog': 'mit dem Hund spazieren gehen',
        'pay bills': 'Rechnungen bezahlen',
        'call doctor': 'Arzt anrufen',
        'study for exam': 'für Prüfung lernen',
        'finish project': 'Projekt beenden',
        'exercise': 'Sport machen',
        'cook dinner': 'Abendessen kochen',
        'water plants': 'Pflanzen gießen',
        'take medication': 'Medikamente nehmen',
        'attend meeting': 'an Besprechung teilnehmen',
        'read book': 'Buch lesen',
        'write report': 'Bericht schreiben'
    },
    'Italian': {
        'buy groceries': 'comprare la spesa',
        'do laundry': 'fare il bucato',
        'clean house': 'pulire casa',
        'walk the dog': 'portare a spasso il cane',
        'pay bills': 'pagare le bollette',
        'call doctor': 'chiamare il dottore',
        'study for exam': 'studiare per l\'esame',
        'finish project': 'finire il progetto',
        'exercise': 'fare esercizio',
        'cook dinner': 'cucinare la cena',
        'water plants': 'annaffiare le piante',
        'take medication': 'prendere farmaci',
        'attend meeting': 'partecipare alla riunione',
        'read book': 'leggere libro',
        'write report': 'scrivere rapporto'
    },
    'Portuguese': {
        'buy groceries': 'comprar mantimentos',
        'do laundry': 'lavar roupa',
        'clean house': 'limpar casa',
        'walk the dog': 'passear com o cachorro',
        'pay bills': 'pagar contas',
        'call doctor': 'ligar para o médico',
        'study for exam': 'estudar para o exame',
        'finish project': 'terminar projeto',
        'exercise': 'fazer exercício',
        'cook dinner': 'cozinhar jantar',
        'water plants': 'regar plantas',
        'take medication': 'tomar medicação',
        'attend meeting': 'participar da reunião',
        'read book': 'ler livro',
        'write report': 'escrever relatório'
    }
}

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

# Function to translate text
def translate_task(text, language):
    """
    Translate text using predefined translations first, then GPT if not found
    """
    # Check predefined translations first
    text_lower = text.lower().strip()
    
    if language in PREDEFINED_TRANSLATIONS:
        predefined_dict = PREDEFINED_TRANSLATIONS[language]
        
        # Check for exact match
        if text_lower in predefined_dict:
            return f"📚 {predefined_dict[text_lower]}"
        
        # Check for partial matches (if task contains predefined phrase)
        for predefined_phrase, translation in predefined_dict.items():
            if predefined_phrase in text_lower:
                return f"📚 {translation} (partial match)"
    
    # If not found in predefined, use GPT
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
        return f"🤖 {response.choices[0].message.content.strip()}"
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
            'selected_language': 'Spanish',  # Default language for each task
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
        
        # Task content and complete button
        col1, col2 = st.columns([4, 1])
        
        with col1:
            # Show task with strikethrough if completed
            text_class = "completed-text" if todo['completed'] else ""
            st.markdown(f'<p class="{text_class}"><strong>{todo["text"]}</strong></p>', unsafe_allow_html=True)
            st.caption(f"{'✅ Completed' if todo['completed'] else '⏳ Pending'} | Created: {todo['created_at']}")
        
        with col2:
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
        
        # Translation section for THIS specific task
        st.markdown("---")
        trans_col1, trans_col2 = st.columns([2, 1])
        
        with trans_col1:
            # Language dropdown for THIS task only
            languages = ['Spanish', 'French', 'German', 'Italian', 'Portuguese', 'Chinese', 'Japanese', 'Korean', 'Arabic', 'Hindi']
            current_language = todo.get('selected_language', 'Spanish')
            
            selected_language = st.selectbox(
                "🌐 Select language to translate:",
                languages,
                index=languages.index(current_language) if current_language in languages else 0,
                key=f"lang_select_{todo['id']}"
            )
            
            # Update the task's selected language if it changed
            if selected_language != current_language:
                st.session_state.todos[i]['selected_language'] = selected_language
                st.session_state.todos[i]['translation'] = None  # Clear old translation
                st.rerun()
        
        with trans_col2:
            # Translate button for THIS task
            if st.button(f"🌐 Translate", key=f"translate_{todo['id']}", type="secondary"):
                with st.spinner(f"Translating to {selected_language}..."):
                    translation = translate_task(todo['text'], selected_language)
                    st.session_state.todos[i]['translation'] = translation
                    st.rerun()
        
        # Show translation if available for THIS task
        if todo.get('translation'):
            st.markdown(f'<div class="translation">🌐 <strong>{selected_language}:</strong> {todo["translation"]}</div>', unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown("---")

# Footer
st.markdown("---")
st.caption("Built with Streamlit and OpenAI API")