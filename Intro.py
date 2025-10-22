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
        color: white;
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

# --- 🧠 Lista de aplicaciones con imágenes del 1 al 15 ---
apps = [
    (" Introducción", "Presentación general del portafolio.", "21.jpg", "https://introduccion.streamlit.app/"),
    (" Introducción 2", "Segunda práctica introductoria.", "10.jpg", "https://claseintroduccion2j.streamlit.app/"),
    (" Voz a Texto", "Convierte voz en texto (traductor).", "11.jpg", "https://traductorinterfaces-l.streamlit.app/"),
    (" OCR", "Reconocimiento óptico de caracteres (leer texto en imágenes).", "12.jpg", "https://ocr-audio-kj.streamlit.app/"),
    (" Análisis de Sentimiento", "Detecta emociones en texto.", "13.jpg", "https://bxevt8gne5jp7whkvp9cw8.streamlit.app/"),
    (" Análisis de Texto (Inglés)", "Identifica temas y estructura gramatical.", "14.jpg", "https://tdfesp1-aulmkzfpydhreyfy5vgtua.streamlit.app/"),
    (" Análisis de Texto (Español)", "Procesamiento de lenguaje natural.", "15.jpg", "https://x7uhxksclxqrup8a4fgnhe.streamlit.app/"),
    (" Reconocimiento de Objetos", "Detección de objetos en imágenes (YOLO).", "16.jpg", "https://k4zkftbsu2yfj8vpqzvbkh.streamlit.app/"),
    (" Reconocimiento de Gestos", "Interpreta movimientos usando visión computacional.", "17.jpg", "https://reconocimientogestos-1.streamlit.app/"),
    (" Chatbot (Sistema Experto)", "Sistema de conversación LLM.", "18.jpg", "https://chatpdfejercicio.streamlit.app/"),
    (" Interpretación de Imagen", "Análisis avanzado de imágenes con IA.", "19.jpg", "https://visionappejercicio.streamlit.app/"),
    (" Interfaz Táctil", "Tablero interactivo personalizado.", "22.jpg","https://drawrecog1.streamlit.app/"),
    (" Generador de Historias", "Crea historias con inteligencia artificial.", "20.jpg", "https://generador-de-historias.streamlit.app/"),
    (" Control MQTT (Botones)", "Control de dispositivos mediante MQTT y botones.", "23.jpg", "https://sendcmqtt2.streamlit.app/"),
    (" Control MQTT (Voz)", "Control de dispositivos mediante comandos de voz.", "16.jpg", "https://ctrlvoice3.streamlit.app/")
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

