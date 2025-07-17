def add_background_with_transparency():
    st.markdown(
        f"""
        <style>
        /* Gambar background */
        .stApp {{
            background-image: url("https://i.pinimg.com/originals/e3/4c/53/e34c53e857fe80c47c1fdf0d50dc0615.jpg");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}

        /* Sidebar dengan warna biru */
        section[data-testid="stSidebar"] > div:first-child {{
            background-color: rgba(0, 123, 255, 0.9);  /* Biru semi-transparan */
            color: white;
        }}

        /* Kontainer utama transparan */
        .main > div {{
            background-color: rgba(255, 255, 255, 0.75);  /* Putih semi-transparan */
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }}

        /* Warna teks sidebar agar tetap terbaca */
        div[data-testid="stSidebar"] label,
        div[data-testid="stSidebar"] span {{
            color: white !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_background_with_transparency()
