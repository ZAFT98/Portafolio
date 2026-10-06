import html
import streamlit as st

st.set_page_config(page_title="Portafolio | Juan Pablo Betancur Ocampo", page_icon="🚀", layout="wide")

# Pega aquí las URL reales de tus apps de Streamlit. No se pueden extraer
# automáticamente de la página de inicio de sesión de Community Cloud.
PROYECTOS = [
    {"titulo": "¿Qué fruta es más parecida?", "categoria": "Vectores y matrices", "descripcion": "Comparación de frutas a partir de sus características y similitudes.", "url": "", "icono": "🍎"},
    {"titulo": "Descenso de gradiente interactivo", "categoria": "Cálculo aplicado", "descripcion": "Exploración visual de cómo se optimiza una función paso a paso.", "url": "", "icono": "🎯"},
    {"titulo": "Detector de anomalías", "categoria": "Lógica y datos", "descripcion": "Identificación de valores que se salen del comportamiento habitual.", "url": "", "icono": "🚨"},
    {"titulo": "Preparación de datos", "categoria": "Datos", "descripcion": "Limpieza y organización de datos para analizarlos después.", "url": "", "icono": "🧹"},
    {"titulo": "Nivel de ríos y quebradas", "categoria": "Datos ambientales", "descripcion": "Consulta y visualización de mediciones de nivel de fuentes hídricas.", "url": "", "icono": "🌊"},
    {"titulo": "Regresión: conceptos clave", "categoria": "Modelos predictivos", "descripcion": "Explicación interactiva de los conceptos básicos de regresión.", "url": "", "icono": "📈"},
    {"titulo": "Serie de tiempo: sensor IoT", "categoria": "Series de tiempo", "descripcion": "Exploración de tendencias y cambios en datos de sensores.", "url": "", "icono": "📡"},
    {"titulo": "Motor predictivo de calidad del aire", "categoria": "Proyecto aplicado", "descripcion": "Proyecto de análisis y predicción de la calidad del aire.", "url": "", "icono": "🌤️"},
]

st.markdown("""<style>
.stApp {background: #090f20; color: #eaf0ff;}
.block-container {max-width: 1250px; padding-top: 2.5rem;}
h1,h2,h3,p {color: #eef3ff;}
.hero {padding: 3rem; border: 1px solid #283958; border-radius: 22px; background: linear-gradient(120deg,#172c55,#10172c 68%); margin-bottom: 2rem;}
.eyebrow {color:#76d7ff; font-size:.85rem; letter-spacing:.16em; font-weight:800; text-transform:uppercase;}
.hero h1 {font-size:clamp(2.2rem,5vw,4rem);line-height:1.08;margin:.7rem 0 1rem;}
.hero p {color:#d0dbec;font-size:1.12rem;line-height:1.7;max-width:850px;}
.card {height: 245px; padding: 1.4rem; border:1px solid #293953; border-radius:18px; background:#111a2e; display:flex; flex-direction:column; margin-bottom:1rem;}
.card .icon {font-size:2rem;}.card .category {font-size:.75rem;color:#76d7ff;text-transform:uppercase;letter-spacing:.12em;font-weight:800;margin-top:.5rem;}
.card h3 {font-size:1.2rem;margin:.45rem 0;}.card p {font-size:.93rem;color:#bdc9dd;line-height:1.5;margin:0;}
.card .action {margin-top:auto;color:#83cfff;font-weight:700;}.card a {color:#83cfff;text-decoration:none;}.card a:hover{text-decoration:underline;}
.small-note {color:#aab9d2;font-size:.88rem;}
</style>""", unsafe_allow_html=True)

st.markdown("""<section class="hero"><div class="eyebrow">Programación avanzada · Portafolio académico</div>
<h1>Hola, soy Juan Pablo Betancur Ocampo 👋</h1>
<p>Soy estudiante de Ingeniería en Desarrollo de Software. En este portafolio compartiré lo trabajado durante el semestre en la materia de Programación Avanzada, especialmente proyectos relacionados con modelos, inteligencia artificial y análisis de datos. Aquí encontrarás aplicaciones interactivas para explorar datos, hacer predicciones y entender cómo funcionan distintos métodos de programación.</p></section>""", unsafe_allow_html=True)

st.header("Proyectos realizados en clase")
st.caption("Aplicaciones y ejercicios desarrollados durante el semestre")

filtro = st.selectbox("Filtrar por tema", ["Todos"] + sorted({p["categoria"] for p in PROYECTOS}))
visibles = [p for p in PROYECTOS if filtro == "Todos" or p["categoria"] == filtro]

for inicio in range(0, len(visibles), 3):
    columnas = st.columns(3, gap="medium")
    for col, proyecto in zip(columnas, visibles[inicio:inicio + 3]):
        with col:
            titulo = html.escape(proyecto["titulo"])
            categoria = html.escape(proyecto["categoria"])
            descripcion = html.escape(proyecto["descripcion"])
            icono = html.escape(proyecto["icono"])
            url = proyecto["url"].strip()
            if url.startswith("https://") or url.startswith("http://"):
                accion = f'<a href="{html.escape(url, quote=True)}" target="_blank" rel="noopener noreferrer">Abrir proyecto ↗</a>'
            else:
                accion = "Enlace pendiente de añadir"
            st.markdown(f'<div class="card"><div class="icon">{icono}</div><div class="category">{categoria}</div><h3>{titulo}</h3><p>{descripcion}</p><div class="action">{accion}</div></div>', unsafe_allow_html=True)

st.divider()
st.markdown('<p class="small-note">Portafolio en construcción · Para activar una tarjeta, pega la URL pública de la app en el campo «url» del proyecto correspondiente dentro de PROYECTOS.</p>', unsafe_allow_html=True)
