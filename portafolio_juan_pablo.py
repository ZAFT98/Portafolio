"""Portafolio de Programación Avanzada. Ejecutar: streamlit run portafolio_juan_pablo.py"""
import html
import streamlit as st

st.set_page_config(page_title="Portafolio | Juan Pablo Betancur Ocampo", page_icon="🌿", layout="wide")

APPS = [
    {"titulo": "Programación Avanzada 1", "url": "https://programaci-n-avanzada-1-9wbnsraddqgphdub58v8fp.streamlit.app/"},
    {"titulo": "Descenso de gradiente interactivo", "url": "https://progavanza2-zxmnjx2nt4m3m2eexscxtb.streamlit.app/"},
    {"titulo": "Detector de anomalías", "url": "https://progavanza3-okwu5nh6wvd7egzg3dkrdn.streamlit.app/"},
    {"titulo": "Series de tiempo: sensor IoT", "url": "https://progavanza5-pcxddqzxmkqseaksx46qwb.streamlit.app/"},
    {"titulo": "Pronóstico CORNARE", "url": "https://progavanza6-2pykuiwwpkpvafu6iax3wz.streamlit.app/"},
    {"titulo": "Programación Avanzada 7", "url": "https://progavanza7-2ipvgd7bbxfw6t5qebtmdz.streamlit.app/"},
    {"titulo": "Programación Avanzada 9", "url": "https://progavanza9-bxgmprhrxb7hpzmpqxm4ex.streamlit.app/"},
]

# Proyectos que aparecen en la captura. No se asignan URL sin verificar correspondencia.
PROYECTOS = [
    ("🍎", "¿Qué fruta es más parecida?", "Vectores y matrices", "Comparación de frutas según sus características."),
    ("🎯", "Descenso de gradiente interactivo", "Cálculo aplicado", "Exploración visual de la optimización de funciones."),
    ("🔎", "Detector de anomalías", "Lógica y datos", "Identificación de valores fuera de lo habitual."),
    ("🧹", "Preparación de datos", "Datos", "Limpieza y organización de datos para analizarlos."),
    ("🌊", "Nivel de ríos y quebradas", "Datos ambientales", "Visualización de mediciones de fuentes hídricas."),
    ("📈", "Regresión: conceptos clave", "Modelos", "Explicación interactiva de conceptos de regresión."),
    ("📡", "Serie de tiempo: sensor IoT", "Series de tiempo", "Exploración de tendencias en datos de sensores."),
    ("🌤️", "Motor predictivo de calidad del aire", "Proyecto aplicado", "Análisis y predicción de la calidad del aire."),
]

st.markdown("""<style>
:root {color-scheme:dark;}
.stApp {background:#071b15;color:#edf8f0;}
.block-container {max-width:1200px;padding-top:2.5rem;padding-bottom:4rem;}
h1,h2,h3,p {color:#edf8f0;}
[data-testid="stHeader"] {background:transparent;}
.hero {background:linear-gradient(120deg,#164b36,#0a2b23 68%,#092119);border:1px solid #39755a;border-radius:22px;padding:clamp(1.5rem,4vw,3rem);margin-bottom:2rem;}
.eyebrow {color:#a7efbd;font-size:.8rem;letter-spacing:.15em;text-transform:uppercase;font-weight:800;}
.hero h1 {font-size:clamp(2rem,4vw,3.5rem);line-height:1.1;margin:.7rem 0 1rem;}
.hero p {color:#d7ecdc;font-size:1.05rem;line-height:1.7;max-width:900px;}
.card {height:205px;padding:1.35rem;background:#102d24;border:1px solid #315d48;border-radius:18px;margin-bottom:1rem;display:flex;flex-direction:column;}
.card:hover {border-color:#86d69e;background:#15392c;}
.card .icon {font-size:1.8rem;}
.card .tag {color:#9de5ae;font-size:.75rem;text-transform:uppercase;letter-spacing:.1em;font-weight:800;margin:.5rem 0;}
.card h3 {font-size:1.15rem;margin:.25rem 0 .5rem;}
.card p {font-size:.9rem;line-height:1.45;color:#c6dacb;margin:0;}
.card .action {margin-top:auto;font-weight:750;color:#9de5ae;}
.card a {color:#9de5ae;text-decoration:none;}
.card a:hover {text-decoration:underline;}
.note {color:#c6dacb;font-size:.9rem;}
</style>""", unsafe_allow_html=True)

st.markdown("""<section class="hero"><div class="eyebrow">Programación Avanzada · Portafolio académico</div>
<h1>Hola, soy Juan Pablo Betancur Ocampo 🌿</h1>
<p>Soy estudiante de Ingeniería en Desarrollo de Software. En este portafolio compartiré lo trabajado durante el semestre en la materia de Programación Avanzada, especialmente proyectos relacionados con modelos, inteligencia artificial y análisis de datos. Aquí encontrarás aplicaciones interactivas para explorar datos, hacer predicciones y comprender distintas técnicas de programación.</p></section>""", unsafe_allow_html=True)

st.header("Aplicaciones publicadas")
for start in range(0, len(APPS), 3):
    for col, app in zip(st.columns(3, gap="medium"), APPS[start:start + 3]):
        with col:
            title = html.escape(app["titulo"])
            url = html.escape(app["url"], quote=True)
            st.markdown(f'<div class="card"><div class="icon">🌱</div><div class="tag">Aplicación interactiva</div><h3>{title}</h3><p>Explora esta aplicación del portafolio.</p><div class="action"><a href="{url}" target="_blank" rel="noopener noreferrer">Abrir aplicación ↗</a></div></div>', unsafe_allow_html=True)

st.divider()
st.header("Proyectos realizados en clase")
for start in range(0, len(PROYECTOS), 3):
    for col, (icon, title, category, description) in zip(st.columns(3, gap="medium"), PROYECTOS[start:start + 3]):
        with col:
            st.markdown(f'<div class="card"><div class="icon">{html.escape(icon)}</div><div class="tag">{html.escape(category)}</div><h3>{html.escape(title)}</h3><p>{html.escape(description)}</p></div>', unsafe_allow_html=True)
