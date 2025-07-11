import streamlit as st

# ----------------------------- CONFIG
st.set_page_config(page_title="Beranda Kimia", page_icon="🧪", layout="centered")

# ----------------------------- MULTILANGUAGE CONTROL
lang = st.radio("🌐 Pilih Bahasa", ["Indonesia", "English"])

# ----------------------------- TITLE
st.title("🧪 Aplikasi Analisis Kimia")
st.markdown("---")

# ----------------------------- CONTENT
if lang == "Indonesia":
    st.header("Selamat Datang! 👋")
    st.markdown(
        """
        Ini adalah aplikasi web interaktif untuk mendukung pembelajaran dan pekerjaan di bidang **analisis kimia**.  
        Cocok untuk mahasiswa, dosen, analis laboratorium, dan siapa pun yang berkecimpung di dunia kimia.

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
