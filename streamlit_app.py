import streamlit as st

# === Konfigurasi Halaman ===
st.set_page_config(page_title="UncertaintyCalc", layout="wide")

# === Tambahkan CSS untuk Background & Transparansi ===
st.markdown(
    """
    <style>
    /* Gambar Latar Belakang */
    .stApp {
        background-image: url("https://i.imgur.com/8zQ3q5D.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }

    /* Konten utama transparan */
    .main > div {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
    }

    /* Sidebar transparan */
    section[data-testid="stSidebar"] > div:first-child {
        background-color: rgba(0, 123, 255, 0.85);
        color: white;
    }

    div[data-testid="stSidebar"] label,
    div[data-testid="stSidebar"] span {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# === Konten Aplikasi ===
st.title("🔬 Selamat Datang di UncertaintyCalc")
st.write("Ini adalah demo tampilan dengan gambar background dan efek transparansi.")
st.button("Tombol Coba")
