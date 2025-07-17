# Tambahan CSS untuk latar belakang transparan dengan gambar
st.markdown("""
    <style>
    /* Background image */
    body {
        background-image: url("https://tse2.mm.bing.net/th/id/OIP.kj3LxnXHDV3J9ehvrr_gIAHaE8?pid=Api&P=0&h=180");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        background-repeat: no-repeat;
        color: #ffffff; /* text jadi putih agar kontras */
    }

    /* Transparansi konten utama */
    .stApp {
        background-color: rgba(0, 0, 0, 0.6); /* hitam transparan */
        padding: 20px;
        border-radius: 12px;
    }

    /* Sidebar transparan */
    section[data-testid="stSidebar"] {
        background-color: rgba(0, 0, 0, 0.5);
    }

    /* Judul dan markdown style */
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
    }

    .css-1v0mbdj p, .css-1v0mbdj {
        color: #ffffff;
    }

    /* Input dan area lainnya */
    .stTextInput, .stNumberInput, .stTextArea {
        background-color: rgba(255,255,255,0.2);
        border-radius: 8px;
        color: #ffffff;
    }

    </style>
""", unsafe_allow_html=True)

