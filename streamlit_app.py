import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ----------------------------- CONFIG
st.set_page_config(page_title="Beranda Kimia", page_icon="🧪", layout="centered")

# ----------------------------- LOTTIE ANIMATION
def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_chem = load_lottie_url("https://lottie.host/c09fe831-e982-40a1-a725-183c2d3d7b16/9kDZnkgv9f.json")

# ----------------------------- MULTILANGUAGE CONTROL
lang = st.radio("🌐 Pilih Bahasa", ["Indonesia", "English"])

# ----------------------------- TITLE + ANIM
st_lottie(lottie_chem, speed=1, width=250, height=250, key="chem_anim")
st.title("🧪 Aplikasi Analisis Kimia")
st.markdown("---")

# ----------------------------- CONTENT
if lang == "Indonesia":
    st.header("Selamat Datang!!")
    st.markdown(
        """
        ### 📚 Dasar Kimia
        Analisis kimia melibatkan proses identifikasi dan kuantifikasi senyawa dalam sampel.  
        Hal ini mencakup metode klasik seperti titrasi, hingga metode instrumen seperti spektrofotometri dan kromatografi.

        ### 📏 Ketidakpastian Pengukuran
        Dalam dunia laboratorium, tidak ada pengukuran yang benar-benar *pasti*.  
        Oleh karena itu, penting untuk selalu menyertakan nilai **ketidakpastian** setiap kali melaporkan hasil.

        Menurut [MKTraining](https://mktraining.co.id/blog/ketidakpastian-pengukuran-dalam-analisis-kimia/):

        > Ketidakpastian pengukuran merupakan parameter penting dalam menyatakan keandalan nilai dari hasil pengukuran.  
        > Tanpa menyertakan ketidakpastian, hasil uji bisa menyesatkan, bahkan dianggap tidak sah oleh lembaga akreditasi.

        Kamu bisa mempelajari lebih lanjut di modul aplikasi kami atau kunjungi blog di atas.
        """
    )
else:
    st.header("Welcome! 👋")
    st.markdown(
        """
        This interactive web app supports learning and lab work in **chemical analysis**.  
        Designed for students, lecturers, lab analysts, and anyone involved in the world of chemistry.

        ### 📚 Chemistry Basics
        Chemical analysis involves identifying and quantifying compounds in a sample.  
        It includes classical methods (like titration) and instrumental methods (e.g., spectrophotometry, chromatography).

        ### 📏 Measurement Uncertainty
        In any lab, no measurement is completely *certain*.  
        That's why it's crucial to report **measurement uncertainty** together with your results.

        According to [MKTraining](https://mktraining.co.id/blog/ketidakpastian-pengukuran-dalam-analisis-kimia/):

        > Measurement uncertainty is a key parameter to express the reliability of results.  
        > Without including uncertainty, test results can be misleading or even invalidated by accreditation bodies.

        Learn more in the modules of this app or visit the blog above.
        """
    )

# ----------------------------- FOOTER
st.markdown("---")
st.caption("© 2025 | Aplikasi Analisis Kimia | Dibuat dengan ❤️ dan Streamlit")
