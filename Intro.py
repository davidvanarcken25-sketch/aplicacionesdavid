import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portafolio Apps IA", page_icon="🐱", layout="wide")

# --- Encabezado principal ---
st.markdown(
    """
    <style>
    .main {
        background-color: #fdf9ff;
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
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="title">🐱 Portafolio de Aplicaciones con Inteligencia Artificial</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Angie Estrella Espinosa Valdez💜</div>', unsafe_allow_html=True)

# --- Sidebar ---
with st.sidebar:
    st.image("https://placekitten.com/300/200", use_column_width=True)
    st.subheader("Sobre el proyecto 🧠")
    st.write("""
    Este portafolio fue desarrollado en **Python 3.10** 
    e incluye ejemplos de aplicaciones con **Inteligencia Artificial**, 
    desde análisis de texto hasta reconocimiento de imágenes.
    """)
    st.markdown("📘 [Más recursos y ejercicios](https://sites.google.com/view/aplicacionesdeia/inicio)")
    st.image("https://placekitten.com/250/180", use_column_width=True)

st.divider()

# --- Lista de aplicaciones ---
apps = [
    (" 1. Introducción", "Presentación general del portafolio.", "https://placekitten.com/320/220", None),
    (" 2. Texto a Voz", "Convierte texto en audio narrado (cuento).", "https://placekitten.com/321/221", "https://imultimod.streamlit.app/"),
    (" 3. Voz a Texto", "Convierte voz en texto (traductor).", "https://placekitten.com/322/222", "https://traductor-ab0sp9f6fi.streamlit.app/"),
    (" 4. OCR", "Reconocimiento óptico de caracteres (leer texto en imágenes).", "https://placekitten.com/323/223", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"),
    (" 5. Análisis de Sentimiento", "Detecta emociones en texto.", "https://placekitten.com/324/224", None),
    (" 6. Análisis de Texto (Inglés)", "Identifica temas y estructura gramatical.", "https://placekitten.com/325/225", None),
    (" 7. Análisis de Texto (Español)", "Procesamiento de lenguaje natural.", "https://placekitten.com/326/226", None),
    (" 8. Reconocimiento de Objetos", "Detección de objetos en imágenes (YOLO).", "https://placekitten.com/327/227", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"),
    (" 9. Reconocimiento de Gestos", "Interpreta movimientos usando visión computacional.", "https://placekitten.com/328/228", None),
    (" 10. Chatbot (Sistema Experto)", "Sistema de conversación LLM.", "https://placekitten.com/329/229", "https://chatpdf-cc.streamlit.app/"),
    (" 11. Interpretación de Imagen", "Análisis avanzado de imágenes con IA.", "https://placekitten.com/330/230", "https://vision2-gpt4o.streamlit.app/"),
    (" 12. Interfaz Táctil", "Tablero interactivo personalizado.", "https://placekitten.com/331/231", None),
    (" 13. Reconocimiento de Bocetos", "Identifica dibujos hechos a mano.", "https://placekitten.com/332/232", None)
]

# --- Diseño con columnas ---
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
                    st.button("💜 Ir a la aplicación", key=f"{i}-{j}", on_click=lambda url=link: st.markdown(f"[Haz clic aquí]({url})", unsafe_allow_html=True))
                st.divider()

st.balloons()
st.success("¡Fin del portafolio🐾")


