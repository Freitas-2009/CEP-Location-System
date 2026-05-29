import streamlit as st
from ferramentas import buscar_cep
import pandas as pd

st.set_page_config(page_title="CEP Locator", layout="centered")

st.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at top, #0b0f1a, #05070d);
    color: #00ffd5;
}

h1, h2, h3 {
    color: #00ffd5;
    text-shadow: 0 0 12px #00ffd5;
}

[data-testid="metric-container"] {
    background: rgba(0, 255, 213, 0.06);
    border: 1px solid rgba(0, 255, 213, 0.25);
    padding: 12px;
    border-radius: 14px;
    box-shadow: 0 0 10px rgba(0, 255, 213, 0.15);
}

.stSidebar {
    background: #0a0f18;
    border-right: 1px solid rgba(0,255,213,0.2);
}
</style>
""", unsafe_allow_html=True)

st.sidebar.image("logo.png")
st.sidebar.title("📡 CEP Locator System")
st.sidebar.caption("GPS • Geolocation • Address Intelligence")

cep = st.sidebar.text_input("Digite o CEP:", placeholder="12345678")

if st.sidebar.button("Buscar"):
    dados = buscar_cep(cep)

    cidade = dados.get('city')
    estado = dados.get('state')
    rua = dados.get('address')
    lat = float(dados.get('lat'))
    lng = float(dados.get('lng'))

    st.title(f"🌍 {cidade}, {estado}")
    st.caption("📍 Localização detectada via API de geolocalização")

    st.subheader(f"🏠 {rua}")

    st.markdown("### 📡 Dados do sinal GPS")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📍 Estado", estado)
        st.metric("🏙️ Cidade", cidade)
        st.metric("🏠 Rua / Logradouro", rua)

    with col2:
        st.metric("🌐 Latitude", round(lat, 6))
        st.metric("🌐 Longitude", round(lng, 6))
        st.metric("📡 Precisão", "Alta" if abs(lat) > 0 else "N/A")

    st.markdown("### 🧭 Coordenadas em tempo real")

    coordenadas = pd.DataFrame({
        "latitude": [lat],
        "longitude": [lng]
    })

    st.map(coordenadas, zoom=14, use_container_width=True)

    st.markdown("---")
    st.caption("⚡ CEP Locator System • Developed by Freitas")