import streamlit as st

# === Konfigurasi Halaman ===
st.set_page_config(page_title="UncertaintyCalc", layout="wide")

# === Tambahkan CSS untuk Background & Transparansi ===
st.markdown(
    """
    <style>
    /* Gambar Latar Belakang */
    .stApp {
        background-image: url("https://id.images.search.yahoo.com/images/view;_ylt=Awrx_PXw8nhoMAwfktDNQwx.;_ylu=c2VjA3NyBHNsawNpbWcEb2lkA2E2YzIyYjVhYThlZmQ0NTEyOTg5YzMzYjA0N2Q5Yjg3BGdwb3MDNjcEaXQDYmluZw--?back=https%3A%2F%2Fid.images.search.yahoo.com%2Fsearch%2Fimages%3Fp%3Dbackground%2Bkimia%2Bpanjang%26ei%3DUTF-8%26type%3DE211ID885G0%26fr%3Dmcafee%26fr2%3Dp%253As%252Cv%253Ai%252Cm%253Asb-top%26nost%3D1%26tab%3Dorganic%26ri%3D67&w=1200&h=1800&imgurl=png.pngtree.com%2Fpng-clipart%2F20190921%2Foriginal%2Fpngtree-chemical-appliance-long-funnel-illustration-png-image_4759668.jpg&rurl=https%3A%2F%2Fid.pngtree.com%2Ffreepng%2Fchemical-appliance-long-funnel-illustration_4759668.html&size=137KB&p=background+kimia+panjang&oid=a6c22b5aa8efd4512989c33b047d9b87&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&fr=mcafee&tt=Gambar+Alat+Kimia+Ilustrasi+Corong+Panjang%2C+Peralatan+Kimia%2C+Corong+...&b=61&ni=90&no=67&ts=&tab=organic&sigr=6P4BpqoZqmW3&sigb=790MFGhHnHJT&sigi=d2bbb5T1ugzc&sigt=f3KCowtwlfb4&.crumb=BIFLTqJlF5S&fr=mcafee&fr2=p%3As%2Cv%3Ai%2Cm%3Asb-top&type=E211ID885G0");
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
