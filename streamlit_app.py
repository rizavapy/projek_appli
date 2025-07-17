import streamlit as st

background_url = "https://i.ytimg.com/vi/YDcGlzUgDBI/maxresdefault.jpg"

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{https://i.ytimg.com/vi/YDcGlzUgDBI/maxresdefault.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main > div {{
        background-color: rgba(255,255,255,0.8);
        padding: 2rem;
        border-radius: 1rem;
    }}
    </style>
""", unsafe_allow_html=True)

st.title("🎉 Selamat Datang di UncertaintyCalc")
st.write("Ini adalah tampilan dengan background gambar.")
# === Konten Aplikasi ===
st.title("🔬 Selamat Datang di UncertaintyCalc")
st.write("Ini adalah demo tampilan dengan gambar background dan efek transparansi.")
st.button("Tombol Coba")
