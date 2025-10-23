import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portafolio Apps IA", page_icon="🚗", layout="wide")

# --- 🚗 Estilos personalizados ---
st.markdown(
    """
    <style>
    .stApp {
        background-color: #000000; 
    }
    .stButton>button {
        background-color: #FFFFFF;
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
        color: #0084FF;
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

# --- 🚗 Título principal ---
st.markdown('<div class="title">🚗 Portafolio de Aplicaciones con Inteligencia Artificial</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">David Mendoza Van-Arcken 🚗</div>', unsafe_allow_html=True)

# --- 📚 Sidebar ---
with st.sidebar:
    st.subheader("🚗 Portafolio")
    st.write("""
    Portafolio de los ejercicios desarrollados en clase.
    """)

st.divider()

# --- 🧠 Lista de aplicaciones ---
apps = [
    (" Introducción", "Presentación general del portafolio.", "1.jpg", "https://introduccion.streamlit.app/"),
    (" Introducción 2", "Segunda práctica introductoria.", "2.jpg", "https://ctrlvoicedavid-mqjex5dakxuyoiyzffvjou.streamlit.app/"),
    (" Voz a Texto", "Convierte voz en texto (traductor).", "3.jpg", "http://voztextodavid-3yvgszvpt9my53pts4c6z8.streamlit.app/"),
    (" OCR", "Reconocimiento óptico de caracteres (leer texto en imágenes).", "4.jpg", "https://ocr-audio-kj.streamlit.app/"),
    (" Análisis de Sentimiento", "Detecta emociones en texto.", "5.jpg", "https://fcehsbmnqppudl2tjz7vbn.streamlit.app/"),
    (" Análisis de Texto (Inglés)", "Identifica temas y estructura gramatical.", "6.jpg", "https://i6ph9xpzglhnr7eqhsjgib.streamlit.app/"),
    (" Análisis de Texto (Español)", "Procesamiento de lenguaje natural.", "7.jpg", "https://e7excrm8hqcovkyffhzgta.streamlit.app/"),
    (" Reconocimiento de Objetos", "Detección de objetos en imágenes (YOLO).", "8.jpg", "https://k4zkftbsu2yfj8vpqzvbkh.streamlit.app/"),
    (" Reconocimiento de Gestos", "Interpreta movimientos usando visión computacional.", "9.jpg", "https://reconocimientogestosdavid-hzccwagzvtwkuzbtiug9kk.streamlit.app/"),
    (" Chatbot (Sistema Experto)", "Sistema de conversación LLM.", "10.jpg", "https://chatpdfejercicio.streamlit.app/"),
    (" Interpretación de Imagen", "Análisis avanzado de imágenes con IA.", "11.jpg", "https://chatpdfdavid-ia6pxqx8cpt68mlroiflkt.streamlit.app/"),
    (" Interfaz Táctil", "Tablero interactivo personalizado.", "12.jpg", "https://drawrecog1.streamlit.app/"),
    (" Generador de Historias", "Crea historias con inteligencia artificial.", "13.jpg", "https://generador-de-historias.streamlit.app/"),
    (" Control MQTT (Botones)", "Control de dispositivos mediante MQTT y botones.", "14.jpg", "https://sendcmqtt2.streamlit.app/"),
    (" Control MQTT (Voz)", "Control de dispositivos mediante comandos de voz.", "15.jpg", "https://ctrlvoice3.streamlit.app/")
]

# --- 🎨 Diseño con columnas ---
for i in range(0, len(apps), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(apps):
            titulo, desc, img_url, link = apps[i + j]
            with col:
                st.image(img_url, use_container_width=True)
                st.markdown(f"### 🚗 {titulo}")
                st.write(desc)
                if link:
                    st.markdown(
                        f'<a href="{link}" target="_blank"><button class="css-1q8dd3e edgvbvh1">🚗 Ir a la aplicación</button></a>',
                        unsafe_allow_html=True
                    )
                st.divider()

# --- ❄️ Animación final ---
st.snow()
st.success("❄️ ¡Fin del portafolio! 🚗")



