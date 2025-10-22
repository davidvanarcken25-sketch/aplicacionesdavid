import streamlit as st
from PIL import Image

# ---- CONFIGURACIÓN DE PÁGINA ----
st.set_page_config(page_title="Aplicaciones de IA", layout="wide")

# ---- ESTILOS PERSONALIZADOS ----
st.markdown(
    """
    <style>
        /* Fondo general */
        body, .stApp {
            background-color: #1a1a1a;
            color: #f2f2f2;
            font-family: 'Poppins', sans-serif;
        }

        /* Títulos */
        h1, h2, h3 {
            color: #ff4b4b;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.7);
        }

        /* Subtítulos del sidebar */
        .css-1d391kg, .css-qri22k {
            color: #f2f2f2 !important;
        }

        /* Botones personalizados */
        .stButton>button {
            background-color: #8b0000;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 0.5em 1em;
            font-weight: 600;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #ff4b4b;
            color: white;
            transform: scale(1.05);
        }

        /* Imágenes con borde redondeado */
        .stImage>img {
            border-radius: 15px;
            box-shadow: 0 0 10px rgba(255,255,255,0.1);
        }

        /* Párrafos */
        p {
            color: #e0e0e0;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# ---- CONTENIDO ----
st.title("🤖 Aplicaciones de Inteligencia Artificial")

with st.sidebar:
    st.subheader("🌐 Aplicaciones con Inteligencia Artificial")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, "
        "lo que resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

# Enlace principal
url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("💡 En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.markdown(f"[Ir a ejercicios prácticos]({url_ia})")

# ---- COLUMNAS ----
col1, col2, col3 = st.columns(3)

# ---- COLUMNA 1 ----
with col1:
    st.subheader("🗣️ Conversión de texto a voz")
    image = Image.open('txt_to_audio2.png')
    st.image(image, width=190)
    st.write("Convierte texto en audio con IA de manera interactiva.")
    if st.button("Abrir aplicación: Texto a voz", key="voz"):
        st.write("[Ir a la app](https://imultimod.streamlit.app/)", unsafe_allow_html=True)

    st.subheader("📷 Reconocimiento de Objetos")
    image = Image.open('txt_to_audio.png')
    st.image(image, width=200)
    st.write("Detecta objetos en imágenes usando modelos YOLO.")
    if st.button("Abrir aplicación: YOLO", key="yolo1"):
        st.write("[Ir a la app](https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/)", unsafe_allow_html=True)

    st.subheader("🤖 Entrenando Modelos")
    image = Image.open('OIG5.jpg')
    st.image(image, width=200)
    st.write("Usa tus propios modelos entrenados en esta plataforma.")
    if st.button("Abrir aplicación: Entrenar Modelo", key="modelo"):
        st.write("[Ir a la app](https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/)", unsafe_allow_html=True)

# ---- COLUMNA 2 ----
with col2:
    st.subheader("🎙️ Conversión de voz a texto")
    image = Image.open('OIG8.jpg')
    st.image(image, width=200)
    st.write("Transforma tu voz en texto de manera automática.")
    if st.button("Abrir aplicación: Voz a texto", key="voz_texto"):
        st.write("[Ir a la app](https://traductor-ab0sp9f6fi.streamlit.app/)", unsafe_allow_html=True)

    st.subheader("📊 Análisis de Datos")
    image = Image.open('data_analisis.png')
    st.image(image, width=190)
    st.write("Analiza datos fácilmente con ayuda de agentes inteligentes.")
    if st.button("Abrir aplicación: Análisis de datos", key="datos"):
        st.write("[Ir a la app](https://asistpy-csv.streamlit.app/)", unsafe_allow_html=True)

    st.subheader("🎧 Transcriptor Audio y Video")
    image = Image.open('OIG3.jpg')
    st.image(image, width=200)
    st.write("Transcribe audio y video automáticamente con Whisper.")
    if st.button("Abrir aplicación: Transcriptor", key="transcriptor"):
        st.write("[Ir a la app](https://transcript-whisper.streamlit.app/)", unsafe_allow_html=True)

# ---- COLUMNA 3 ----
with col3:
    st.subheader("📄 Generación en Contexto (RAG)")
    image = Image.open('Chat_pdf.png')
    st.image(image, width=190)
    st.write("Interpreta documentos PDF usando modelos de lenguaje.")
    if st.button("Abrir aplicación: RAG", key="rag"):
        st.write("[Ir a la app](https://chatpdf-cc.streamlit.app/)", unsafe_allow_html=True)

    st.subheader("🧠 Análisis de Imagen")
    image = Image.open('OIG4.jpg')
    st.image(image, width=200)
    st.write("Analiza y comprende imágenes con visión artificial.")
    if st.button("Abrir aplicación: Vision", key="vision"):
        st.write("[Ir a la app](https://vision2-gpt4o.streamlit.app/)", unsafe_allow_html=True)

    st.subheader("⚙️ Sistema Ciberfísico")
    image = Image.open('OIG6.jpg')
    st.image(image, width=200)
    st.write("Explora la interacción entre IA y el mundo físico.")
    if st.button("Abrir aplicación: Ciberfísico", key="ciber"):
        st.write("[Ir a la app](https://vision2-gpt4o.streamlit.app/)", unsafe_allow_html=True)
