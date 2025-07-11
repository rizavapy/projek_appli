import streamlit as st

# ---------------- CONFIG ------------------
st.set_page_config(
    page_title="Beranda - Analisis Kimia",
    page_icon="🧪",
    layout="centered"
)

# ---------- SESSION LANGUAGE -------------
if "lang" not in st.session_state:
    st.session_state.lang = "id"

def switch_lang():
    st.session_state.lang = "en" if st.session_state.lang == "id" else "id"

# ------------- UI ------------------------
col1, col2 = st.columns([1, 4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3163/3163845.png", width=64)
with col2:
    st.title("Selamat Datang!! 🧪")

st.markdown("---")

# --------- TOGGLE TRANSLATE BUTTON -------
if st.session_state.lang == "id":
    st.button("Translate to English 🌐", on_click=switch_lang)
else:
    st.button("Terjemahkan ke Bahasa Indonesia 🇮🇩", on_click=switch_lang)

# --------- CONTENT ------------
if st.session_state.lang == "id":
    st.subheader("🔬 Apa itu Ketidakpastian dalam Analisis Kimia?")
    st.write("""
        Dalam dunia analisis kimia, **ketidakpastian pengukuran** adalah komponen penting yang
        mencerminkan seberapa besar keraguan terhadap hasil pengukuran. Tidak peduli seakurat
        apapun instrumen yang kita gunakan, setiap hasil pasti memiliki potensi deviasi dari nilai sebenarnya.

        Ketidakpastian berasal dari berbagai faktor:
        - Ketidaktepatan alat ukur
        - Variasi suhu dan lingkungan
        - Teknik pengambilan sampel
        - Faktor manusia seperti kesalahan pembacaan
    """)

    st.subheader("📖 Informasi Tambahan!!")
    st.write("""
        Berdasarkan [sumber MK Training](https://mktraining.co.id/blog/ketidakpastian-pengukuran-dalam-analisis-kimia/), 
        ketidakpastian diukur agar hasil analisis memiliki makna ilmiah dan dapat dipercaya.
        Dalam praktik laboratorium, ada dua jenis ketidakpastian:

        - **Type A**: Dihitung secara statistik dari data berulang
        - **Type B**: Diperoleh dari referensi, sertifikat kalibrasi, atau estimasi

        Tujuan utama dari perhitungan ini adalah untuk mengetahui tingkat kepercayaan pada hasil pengukuran,
        biasanya menggunakan **expanded uncertainty (U)** dengan faktor cakupan tertentu (k=2 untuk 95%).

        📌 *"Tanpa menyatakan ketidakpastian, data analitik tidak lengkap."*
    """)

else:
    st.subheader("🔬 Additional Information!!")
    st.write("""
        In the world of chemical analysis, **measurement uncertainty** reflects how much doubt
        we have about the result. No matter how accurate our instruments are, every result has a
        possible deviation from the true value.

        Sources of uncertainty:
        - Instrument inaccuracy
        - Temperature/environmental variations
        - Sampling technique
        - Human error (reading, recording)

    """)

    st.subheader("📖 Article Summary")
    st.write("""
        Based on [MK Training's article](https://mktraining.co.id/blog/ketidakpastian-pengukuran-dalam-analisis-kimia/),
        uncertainty is measured to make analytical results scientifically valid and trustworthy.

        There are two types of uncertainty:
        - **Type A**: Statistical, from repeated measurements
        - **Type B**: From references, certificates, or estimation

        The main goal is to define **expanded uncertainty (U)** with a confidence level (typically k=2 → 95%).

        📌 *"Without stating uncertainty, analytical data is incomplete."*
    """)

# ----------------- FOOTER ----------------
st.markdown("---")
st.caption("Dibuat dengan ❤️ oleh Mahasiswa Analis Kimia | Streamlit App 2025")
