
import streamlit as st
from PIL import Image

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="My Concentration. GC",
    page_icon="🧪",
    layout="centered"
)

# ===== SESSION STATE =====
if "menu" not in st.session_state:
    st.session_state.menu = "home"

# ===== CUSTOM CSS STYLE =====
st.markdown("""
    <style>
        body {
            background-color: #f3f1e7;
        }
        .main {
            background-color: #ffffffdd;
            padding: 2rem;
            border-radius: 1.25rem;
            box-shadow: 0px 0px 12px rgba(0,0,0,0.07);
        }
        h1, h2, h3, h4 {
            color: #333;
            text-align: center;
            font-family: 'Segoe UI', sans-serif;
        }
        .stButton>button {
            background-color: #524d82;
            color: white;
            border-radius: 10px;
            padding: 10px 24px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# ===== LANDING PAGE =====
if st.session_state.menu == "home":
    with st.container():
        st.markdown("<h1 style='font-size: 48px;'>🐼 My Concentration. GC</h1>", unsafe_allow_html=True)
        st.markdown("<h3 style='color:#888;'>Kelompok 5 - LPK</h3>", unsafe_allow_html=True)

        st.markdown("""
            <div style='text-align: center; font-size: 16px; color: #555; max-width: 600px; margin: auto;'>
            Aplikasi pintar untuk konversi dan perhitungan larutan kimia.
            <br><br>
            <strong>Dibuat oleh:</strong><br>
            Arsal · Danis · Nana · Yasifah · Raffi
            </div>
        """, unsafe_allow_html=True)

        try:
            logo = Image.open("panda.png")
            st.image(logo, width=150)
        except:
            st.warning("Logo panda tidak ditemukan. Pastikan 'panda.png' ada di direktori yang sama.")

        st.markdown("<hr style='margin-top:2rem; margin-bottom:1.5rem;'>", unsafe_allow_html=True)

        st.markdown("### 📂 Silakan pilih menu:", unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("🚀 Buka Aplikasi Konversi"):
                st.session_state.menu = "konversi"
                st.experimental_rerun()

        with col2:
            if st.button("📘 Lihat Tabel Periodik"):
                st.session_state.menu = "tabel"
                st.experimental_rerun()

# ===== MENU: KONVERSI =====
elif st.session_state.menu == "konversi":
    st.markdown("<h2>🧪 Aplikasi Konversi Kimia</h2>", unsafe_allow_html=True)
    kategori = st.selectbox("Pilih Kategori:", ["💧 Konsentrasi", "⚗️ Molaritas", "📘 Normalitas"])

    if kategori == "💧 Konsentrasi":
        jenis = st.selectbox("Jenis Konversi:", ["ppm ke mg/L", "mg/L ke ppm", "% b/b ke g/100 mL"])
        nilai = st.number_input("Masukkan Nilai:", step=0.0001)
        if st.button("Konversi"):
            if jenis == "ppm ke mg/L":
                st.success(f"{nilai} ppm = {nilai} mg/L")
            elif jenis == "mg/L ke ppm":
                st.success(f"{nilai} mg/L = {nilai} ppm")
            elif jenis == "% b/b ke g/100 mL":
                st.success(f"{nilai} % b/b = {nilai} g / 100 mL")

    elif kategori == "⚗️ Molaritas":
        jenis = st.selectbox("Jenis:", ["mol/L ke mg/L", "mg/L ke mol/L"])
        nilai = st.number_input("Nilai:", key="mol_val")
        bm = st.number_input("Berat Molekul (BM):")
        if st.button("Konversi Molaritas"):
            if bm > 0:
                if jenis == "mol/L ke mg/L":
                    st.success(f"{nilai} mol/L = {nilai * bm * 1000:.4f} mg/L")
                elif jenis == "mg/L ke mol/L":
                    st.success(f"{nilai} mg/L = {nilai / (bm * 1000):.6f} mol/L")
            else:
                st.warning("Masukkan BM yang valid.")

    elif kategori == "📘 Normalitas":
        metode = st.radio("Metode:", ["Molaritas ke Normalitas", "Massa → Normalitas"])
        if metode == "Molaritas ke Normalitas":
            mol = st.number_input("Molaritas (mol/L):")
            n = st.number_input("Valensi:", step=1)
            if st.button("Hitung Normalitas"):
                st.success(f"Normalitas = {mol * n:.4f} N")
        else:
            massa = st.number_input("Massa (g):")
            bm = st.number_input("BM:")
            valensi = st.number_input("Valensi:", step=1)
            volume = st.number_input("Volume (mL):")
            if st.button("Hitung dari Massa"):
                if bm > 0 and valensi > 0 and volume > 0:
                    be = bm / valensi
                    eq = massa / be
                    N = eq * 1000 / volume
                    st.success(f"Normalitas = {N:.4f} N")
                else:
                    st.warning("Masukkan semua input dengan benar.")

    st.button("⬅️ Kembali ke Menu Utama", on_click=lambda: st.session_state.update({"menu": "home"}))

# ===== MENU: TABEL PERIODIK =====
elif st.session_state.menu == "tabel":
    st.markdown("<h2>📘 Tabel Periodik Sederhana</h2>", unsafe_allow_html=True)
    try:
        st.image("tabel_periodik.png", caption="Tabel Periodik Unsur")
    except:
        st.warning("Gambar tabel_periodik.png tidak ditemukan. Silakan upload ke folder yang sama.")
    st.button("⬅️ Kembali ke Menu Utama", on_click=lambda: st.session_state.update({"menu": "home"}))
