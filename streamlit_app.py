import streamlit as st
import numpy as np

# ===== DEFINISI FUNGSI HARUS DI ATAS =====
def add_background_with_transparency():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://i.pinimg.com/originals/e3/4c/53/e34c53e857fe80c47c1fdf0d50dc0615.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        section[data-testid="stSidebar"] > div:first-child {{
            background-color: rgba(0, 123, 255, 0.9);
            color: white;
        }}
        .main > div {{
            background-color: rgba(255, 255, 255, 0.75);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }}
        div[data-testid="stSidebar"] label,
        div[data-testid="stSidebar"] span {{
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ===== SET PAGE CONFIG & PANGGIL FUNGSI =====
st.set_page_config(page_title="UncertaintyCalc", layout="wide")
add_background_with_transparency()
