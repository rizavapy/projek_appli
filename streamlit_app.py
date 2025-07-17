import streamlit as st

# === Gaya CSS Background ===
def add_background_with_transparency():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://id.pinterest.com/pin/22518066880644171/");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        .main > div {{
            background-color: rgba(255, 255, 255, 0.75);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }}
        section[data-testid="stSidebar"] > div:first-child {{
            background-color: rgba(0, 123, 255, 0.9);
            color: white;
        }}
        div[data-testid="stSidebar"] label,
        div[data-testid="stSidebar"] span {{
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# === Config & Styling ===
st.set_page_config(page_title="Tes Background", layout="wide")
add_background_with_transparency()

# === Tampilan Awal Sederhana ===
st.title("🔬 Aplikasi Percobaan Background")
st.write("Ini adalah halaman percobaan untuk memastikan background gambar dan transparansi bekerja dengan benar.")
