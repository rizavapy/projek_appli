import streamlit as st
import numpy as np

# ===== CONFIG =====
st.set_page_config(page_title="UncertaintyCalc", layout="wide")

# ===== BACKGROUND & SIDEBAR STYLE =====
def add_background_and_sidebar_style():
    st.markdown(
        f"""
        <style>
        /* Background utama aplikasi */
        .stApp {{
            background-image: url(https://id.pinterest.com/pin/222998619041064434/);
            background-attachment: fixed;
            background-size: cover;
            background-position: center;
        }}

        /* Sidebar warna biru */
        section[data-testid="stSidebar"] > div:first-child {{
            background-color: #007bff;
            color: white;
        }}

        /* Warna teks di sidebar */
        div[data-testid="stSidebar"] label,
        div[data-testid="stSidebar"] span {{
            color: white !important;
        }}

        /* Warna item navigasi */
        div[data-testid="stSidebar"] .css-1v3fvcr {{
            color: white !important;
        }}

        /* Optional: ubah warna hover jika ingin lebih interaktif */
        div[data-testid="stSidebar"] .css-1v3fvcr:hover {{
            color: #ffd700 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_background_and_sidebar_style()

# ===== SIDEBAR MENU =====
menu = st.sidebar.radio("📂 Navigasi", [
    "Beranda",
    "Dasar Teori",
    "Kalkulator Ketidakpastian",
    "Cara Perhitungan Manual",
    "Faktor Kesalahan",
    "Contoh Soal dan Pembahasan"
])
