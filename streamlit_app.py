import streamlit as st

# --------------------- PAGE CONFIG ---------------------
st.set_page_config(page_title="Beranda Aplikasi Kimia", page_icon="🧪")

# --------------------- TOGGLE LANGUAGE ---------------------
lang = st.sidebar.radio("🌐 Pilih Bahasa / Language", ("🇮🇩 Bahasa Indonesia", "🇬🇧 English"))

# --------------------- BAHASA INDONESIA ---------------------
if lang == "🇮🇩 Bahasa Indonesia":
    st.title("👩‍🔬 Selamat Datang di Aplikasi Analisis Kimia")

    st.markdown(
        """
        Aplikasi ini dirancang untuk membantu mahasiswa, analis, dan teknisi laboratorium 
        dalam memahami dan menghitung **ketidakpastian pengukuran**, serta menyediakan 
        alat bantu lain seputar **analisis kimia kuantitatif**.
        
        ### 📚 Apa Itu Ketidakpastian Pengukuran?
        Dalam dunia laboratorium, hasil pengukuran tidak pernah 100% pasti. 
        Ketidakpastian menggambarkan batas kepercayaan dari hasil yang didapat.
        
        Misalnya, saat kamu menimbang zat sebanyak **5,03 g**, nilai tersebut punya 
        *ketidakpastian* — mungkin ±0,01 g tergantung alat & kondisi.
        
        ### 🧭 Tujuan Aplikasi Ini:
        - Menyediakan **alat hitung cepat** ketidakpastian (Type A & B)
        - Memberikan edukasi tentang dasar-dasar ketidakpastian
        - Mendukung pemahaman praktikum & validasi metode
        
        ### 📎 Sumber Utama Referensi:
        - GUM (*Guide to the Expression of Uncertainty in Measurement*)
        - MK Training Blog: [Ketidakpastian Pengukuran](https://mktraining.co.id/blog/ketidakpastian-pengukuran-dalam-analisis-kimia/)
        """
    )

    with st.expander("🔍 Ringkasan dari MK Training"):
        st.markdown(
            """
            Ketidakpastian pengukuran dalam laboratorium **bukanlah kesalahan**, 
            tetapi bagian tak terhindarkan dari setiap pengukuran.  
            
            Menurut artikel MK Training:
            - Ketidakpastian menunjukkan **seberapa besar keraguan** terhadap hasil pengukuran.
            - Bisa berasal dari **alat ukur**, **pengamat**, **lingkungan**, atau **metode analisis**.
            - Ada dua jenis:
              - **Type A**: Berdasarkan statistik (pengulangan data)
              - **Type B**: Berdasarkan estimasi (pengalaman, spesifikasi alat)
            
            Penyajian akhir hasil harus ditulis seperti:
            ```
            pH = 6,90 ± 0,02 (k=2)
            ```
            """
        )

# --------------------- ENGLISH VERSION ---------------------
else:
    st.title("👩‍🔬 Welcome to the Chemical Analysis App")

    st.markdown(
        """
        This app is designed to help students, lab analysts, and technicians 
        understand and calculate **measurement uncertainty**, and also provides 
        tools for **quantitative chemical analysis**.

        ### 📚 What is Measurement Uncertainty?
        In laboratories, no measurement result is 100% exact.  
        Uncertainty reflects how confident we are about the reported result.

        For example, if you weigh a substance and get **5.03 g**, 
        the real value might be ±0.01 g depending on tools & conditions.

        ### 🧭 This App Aims to:
        - Provide **quick calculators** for uncertainty (Type A & B)
        - Educate users on the fundamentals of uncertainty
        - Support lab work and method validation

        ### 📎 Main Reference:
        - GUM (*Guide to the Expression of Uncertainty in Measurement*)
        - MK Training Blog: [Measurement Uncertainty](https://mktraining.co.id/blog/ketidakpastian-pengukuran-dalam-analisis-kimia/)
        """
    )

    with st.expander("🔍 Summary from MK Training (translated)"):
        st.markdown(
            """
            Measurement uncertainty is **not an error**, but a natural part 
            of any laboratory result.  

            According to MK Training:
            - Uncertainty shows **how much doubt** surrounds a measurement result.
            - It can come from **instrumentation**, **analyst skills**, **environment**, or **methods**.
            - Two main types:
              - **Type A**: Statistical, from repeated data
              - **Type B**: Estimated, from tool specs or experience
            
            Final reporting should look like:
            ```
            pH = 6.90 ± 0.02 (k=2)
            ```
            """
        )
