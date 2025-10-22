import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portafolio Apps IA", page_icon="🐱", layout="wide")

# --- 🌼 Estilos personalizados ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #330621; /* Fondo naranjita claro */
    }
    .stButton>button {
        background-color: #a06cd5;
        color: white;
        border-radius: 12px;
        border: none;
        font-size: 16px;
        padding: 0.5em 1em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #7b2cbf;
        color: #fff;
        transform: scale(1.05);
    }
    .title {
        color: #7b2cbf;
        text-align: center;
        font-size: 42px;
        font-weight: 700;
    }
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #4b4b4b;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- 🐱 Título principal ---
st.markdown('<div class="title">🐱 Portafolio de Aplicaciones con Inteligencia Artificial</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Angie Estrella Espinosa Valdez 💜</div>', unsafe_allow_html=True)

# --- 📚 Sidebar ---
with st.sidebar:
    st.subheader("📖 Portafolio")
    st.write("""
    Portafolio de los ejercicios desarrollados en clase.
    """)

st.divider()

# --- 🧠 Lista de aplicaciones con imágenes del 1 al 10 ---
apps = [
    ("1️⃣ Introducción", "Presentación general del portafolio.", "21.jpg", None),
    ("2️⃣ Texto a Voz", "Convierte texto en audio narrado (cuento).", "10.jpg", "https://imultimod.streamlit.app/"),
    ("3️⃣ Voz a Texto", "Convierte voz en texto (traductor).", "11.jpg", "https://traductor-ab0sp9f6fi.streamlit.app/"),
    ("4️⃣ OCR", "Reconocimiento óptico de caracteres (leer texto en imágenes).", "12.jpg", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"),
    ("5️⃣ Análisis de Sentimiento", "Detecta emociones en texto.", "13.jpg", None),
    ("6️⃣ Análisis de Texto (Inglés)", "Identifica temas y estructura gramatical.", "14.jpg", None),
    ("7️⃣ Análisis de Texto (Español)", "Procesamiento de lenguaje natural.", "15.jpg", None),
    ("8️⃣ Reconocimiento de Objetos", "Detección de objetos en imágenes (YOLO).", "16.jpg", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"),
    ("9️⃣ Reconocimiento de Gestos", "Interpreta movimientos usando visión computacional.", "17.jpg", None),
    ("🔟 Chatbot (Sistema Experto)", "Sistema de conversación LLM.", "18.jpg", "https://chatpdf-cc.streamlit.app/"),
    ("11️⃣ Interpretación de Imagen", "Análisis avanzado de imágenes con IA.",  "19.jpg", "https://vision2-gpt4o.streamlit.app/"),
    ("12️⃣ Interfaz Táctil", "Tablero interactivo personalizado.", "22.jpg", None),
    ("13️⃣ Reconocimiento de Bocetos", "Identifica dibujos hechos a mano.", "20.jpg", None)
]

# --- 🎨 Diseño con columnas ---
for i in range(0, len(apps), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(apps):
            titulo, desc, img_url, link = apps[i + j]
            with col:
                st.image(img_url, use_column_width=True)
                st.markdown(f"### {titulo}")
                st.write(desc)
                if link:
                    st.markdown(f'<a href="{link}" target="_blank"><button class="css-1q8dd3e edgvbvh1">💜 Ir a la aplicación</button></a>', unsafe_allow_html=True)
                st.divider()

# --- 🎉 Final ---
st.balloons()
st.success("¡Fin del portafolio! 🌟")


