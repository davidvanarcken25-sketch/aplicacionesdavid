import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portafolio Apps IA", page_icon="🐱", layout="wide")

# --- 🌼 Estilos personalizados ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #330621; 
    }
    .stButton>button {
        background-color: #F72866;
        color: white;
        border-radius: 12px;
        border: none;
        font-size: 16px;
        padding: 0.5em 1em;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #F9518C;
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
        color: white; /* 🌼 Ahora blanco */
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
    ("Introducción", "Presentación general del portafolio.", "21.jpg", None),
    (" Texto a Voz", "Convierte texto en audio narrado (cuento).", "10.jpg", "https://imultimod.streamlit.app/"),
    (" Voz a Texto", "Convierte voz en texto (traductor).", "11.jpg", "https://traductor-ab0sp9f6fi.streamlit.app/"),
    (" OCR", "Reconocimiento óptico de caracteres (leer texto en imágenes).", "12.jpg", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"),
    (" Análisis de Sentimiento", "Detecta emociones en texto.", "13.jpg", None),
    (" Análisis de Texto (Inglés)", "Identifica temas y estructura gramatical.", "14.jpg", None),
    (" Análisis de Texto (Español)", "Procesamiento de lenguaje natural.", "15.jpg", None),
    (" Reconocimiento de Objetos", "Detección de objetos en imágenes (YOLO).", "16.jpg", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"),
    (" Reconocimiento de Gestos", "Interpreta movimientos usando visión computacional.", "17.jpg", None),
    (" Chatbot (Sistema Experto)", "Sistema de conversación LLM.", "18.jpg", "https://chatpdf-cc.streamlit.app/"),
    (" Interpretación de Imagen", "Análisis avanzado de imágenes con IA.",  "19.jpg", "https://vision2-gpt4o.streamlit.app/"),
    (" Interfaz Táctil", "Tablero interactivo personalizado.", "22.jpg", None),
    (" Reconocimiento de Bocetos", "Identifica dibujos hechos a mano.", "20.jpg", None)
]

# --- 🎨 Diseño con columnas ---
for i in range(0, len(apps), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(apps):
            titulo, desc, img_url, link = apps[i + j]
            with col:
                st.image(img_url, use_container_width=True)
                st.markdown(f"### {titulo}")
                st.write(desc)
                if link:
                    st.markdown(
                        f'<a href="{link}" target="_blank"><button class="css-1q8dd3e edgvbvh1">💜 Ir a la aplicación</button></a>',
                        unsafe_allow_html=True
                    )
                st.divider()

# --- 🎉 Final ---
st.balloons()
st.success("¡Fin del portafolio! 🌟")

