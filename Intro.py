import streamlit as st
from PIL import Image

st.set_page_config(page_title="Portafolio Apps IA", page_icon="🤖", layout="wide")

st.title("🤖 Portafolio de Aplicaciones con Inteligencia Artificial")

st.markdown("""
En este portafolio encontrarás diferentes **aplicaciones desarrolladas con IA**, 
desde conversión de voz y texto hasta análisis de imágenes, sentimientos y modelos entrenados.
""")

with st.sidebar:
    st.image("OIG5.jpg", use_column_width=True)
    st.subheader("Sobre el proyecto")
    st.write("""
    Este portafolio recopila proyectos creados con **Python 3.10** y herramientas de 
    **Inteligencia Artificial** aplicadas en entornos reales.
    """)
    st.markdown("📘 [Más recursos y ejercicios](https://sites.google.com/view/aplicacionesdeia/inicio)")

# --- Secciones del Portafolio ---
st.divider()
st.header("🧩 Aplicaciones del Portafolio")

apps = [
    ("📘 1. Introducción", "Presentación general del proyecto."),
    ("🔊 2. Interfaz Texto a Voz", "Convierte texto en audio narrado (cuento).", "txt_to_audio2.png", "https://imultimod.streamlit.app/"),
    ("🎙️ 3. Interfaz Voz a Texto", "Convierte voz en texto (traductor).", "OIG8.jpg", "https://traductor-ab0sp9f6fi.streamlit.app/"),
    ("📄 4. Interfaz OCR", "Reconocimiento óptico de caracteres (lectura de texto en imágenes).", "txt_to_audio.png", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"),
    ("💬 5. Análisis de Sentimiento", "Detecta emociones en texto."),
    ("📝 6. Análisis de Texto (Inglés)", "Identifica temas y gramática."),
    ("📝 7. Análisis de Texto (Español)", "Procesamiento de lenguaje natural."),
    ("🧠 8. Reconocimiento de Objetos", "Detección de objetos en imágenes (YOLO).", "OIG4.jpg", "https://xn3pg24ztuv6fdiqon8qn3.streamlit.app/"),
    ("🤹 9. Reconocimiento de Gestos", "Usa visión computacional para interpretar movimientos."),
    ("💬 10. Chatbot (Sistema Experto)", "Sistema de conversación LLM.", "Chat_pdf.png", "https://chatpdf-cc.streamlit.app/"),
    ("🖼️ 11. Interpretación de Imagen", "Análisis avanzado con modelos visuales.", "OIG4.jpg", "https://vision2-gpt4o.streamlit.app/"),
    ("🖐️ 12. Interfaz Táctil", "Tablero interactivo personalizado."),
    ("✏️ 13. Reconocimiento de Bocetos", "Reconoce y clasifica dibujos hechos a mano.")
]

# --- Mostrar las apps en diseño de columnas ---
for i in range(0, len(apps), 3):
    cols = st.columns(3)
    for j, col in enumerate(cols):
        if i + j < len(apps):
            app = apps[i + j]
            title = app[0]
            desc = app[1]
            image = app[2] if len(app) > 2 else None
            link = app[3] if len(app) > 3 else None

            with col:
                st.markdown(f"### {title}")
                if image:
                    st.image(image, use_column_width=True)
                st.write(desc)
                if link:
                    st.markdown(f"[🌐 Ir a la aplicación]({link})")
                st.divider()

st.success("✨ Fin del portafolio ✨")


