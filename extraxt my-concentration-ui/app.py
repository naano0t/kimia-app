
import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Concentration. GC", page_icon="🧪", layout="centered")

if "menu" not in st.session_state:
    st.session_state.menu = "home"

# === STYLING ===
st.markdown("""
<style>
body {
    background-color: #f4f1ea;
}
h1, h2, h3 {
    text-align: center;
    color: #333;
}
.stButton>button {
    background-color: #5c5470;
    color: white;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

if st.session_state.menu == "home":
    st.markdown("<h1>🧪 My Concentration. GC</h1>", unsafe_allow_html=True)
    st.markdown("<h3>by Kelompok 5 – LPK</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#666;'>Arsal · Danis · Nana · Yasifah · Raffi</p>", unsafe_allow_html=True)

    try:
        st.image("panda.png", width=140)
    except:
        st.info("Logo panda tidak tersedia.")

    st.markdown("<hr>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚀 Buka Aplikasi Konversi"):
            st.session_state.menu = "konversi"
            st.experimental_rerun()
    with col2:
        if st.button("📘 Lihat Tabel Periodik"):
            st.session_state.menu = "tabel"
            st.experimental_rerun()

elif st.session_state.menu == "konversi":
    st.header("🔬 Konversi Konsentrasi")
    jenis = st.selectbox("Jenis:", ["ppm ke mg/L", "mg/L ke ppm", "% b/b ke g/100 mL"])
    nilai = st.number_input("Masukkan nilai:", step=0.0001)
    if st.button("Konversi"):
        if jenis == "ppm ke mg/L":
            st.success(f"{nilai} ppm = {nilai} mg/L")
        elif jenis == "mg/L ke ppm":
            st.success(f"{nilai} mg/L = {nilai} ppm")
        elif jenis == "% b/b ke g/100 mL":
            st.success(f"{nilai} % b/b = {nilai} g/100 mL")
    st.button("⬅️ Kembali", on_click=lambda: st.session_state.update({"menu": "home"}))

elif st.session_state.menu == "tabel":
    st.header("📘 Tabel Periodik Unsur")
    try:
        st.image("tabel_periodik.png", use_column_width=True)
    except:
        st.warning("Gambar tidak tersedia.")
    st.button("⬅️ Kembali", on_click=lambda: st.session_state.update({"menu": "home"}))
