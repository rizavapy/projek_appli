import streamlit as st
import numpy as np
import pandas as pd

# ---------------------- SETUP ----------------------
st.set_page_config(page_title="Aplikasi Ketidakpastian", layout="wide")

# ---------------------- SIDEBAR MENU ----------------------
menu = st.sidebar.radio(
    "Navigasi / Navigation",
    (
        "1. Beranda / Home",
        "2. Dasar Teori / Theory",
        "3. Cara Perhitungan Manual / Manual Calculation",
        "4. Fitur Perhitungan / Calculation Tool",
        "5. Kemungkinan Kesalahan / Possible Errors",
        "6. Contoh Soal & Pembahasan / Example Questions",
        "7. Referensi / References",
        "8. Tentang Aplikasi / About",
        "9. Fitur Tambahan / Extra Features"
    )
)

# ---------------------- 1. BERANDA ----------------------
if menu == "1. Beranda / Home":
    st.title("🔬 Aplikasi Web Perhitungan Nilai Ketidakpastian")
    st.markdown("""
    ### Selamat datang!
    Aplikasi ini dirancang untuk membantu mahasiswa dan analis kimia dalam melakukan **perhitungan nilai ketidakpastian** pengukuran secara akurat, mudah, dan cepat.

    #### Tujuan:
    - Memahami konsep ketidakpastian dalam pengukuran.
    - Melakukan perhitungan secara otomatis dan manual.
    - Menyediakan pembelajaran interaktif.

    #### Kelebihan:
    - Ramah pengguna
    - Dilengkapi teori & contoh soal
    - Bisa download hasil perhitungan
    - Mendukung simulasi interaktif

    ---
    ### Welcome!
    This web app helps chemistry students and lab analysts to **calculate measurement uncertainty** easily and accurately.

    #### Purpose:
    - Understand uncertainty concepts
    - Perform automatic and manual calculations
    - Learn with interactive examples

    #### Advantages:
    - User-friendly interface
    - Complete with theory and practice
    - Downloadable results
    - Interactive simulations
    """)

# ---------------------- 2. DASAR TEORI ----------------------
elif menu == "2. Dasar Teori / Theory":
    st.title("📚 Dasar Teori / Theory")
    st.markdown("""
    ### Apa itu Ketidakpastian dalam Pengukuran?
    Ketidakpastian adalah parameter yang menyatakan tingkat ketidakyakinan terhadap hasil pengukuran.

    ### Jenis Ketidakpastian:
    **Tipe A (Statistik):**
    - Diperoleh dari hasil pengulangan (repeatability)
    - Contoh: simpangan baku dari beberapa kali pengukuran

    **Tipe B (Non-Statistik):**
    - Berdasarkan data eksternal: spesifikasi alat, kalibrasi, dll.
    - Contoh: dari datasheet, sertifikat

    ### Cara Menggabungkan:
    Gunakan rumus akar jumlah kuadrat dari ketidakpastian (Root Sum Square/RSS)

    ### Ketidakpastian Diperluas:
    Gunakan faktor cakupan *k* (umumnya k=2 untuk 95% interval)

    ### Rumus Umum:
    - Simpangan baku: √(∑(xi - x̄)² / (n - 1))
    - Ketidakpastian gabungan: √(ua² + ub²)
    - Ketidakpastian diperluas: U = k × uc

    ### Standar Referensi:
    - ISO GUM: Guide to the Expression of Uncertainty in Measurement
    """)

# ---------------------- 3. CARA PERHITUNGAN MANUAL ----------------------
elif menu == "3. Cara Perhitungan Manual / Manual Calculation":
    st.title("📝 Cara Perhitungan Manual")
    st.markdown("""
    #### 1. Hitung rata-rata hasil pengukuran
    #### 2. Hitung simpangan baku (standar deviasi)
    #### 3. Hitung ketidakpastian tipe A: SE = s / √n
    #### 4. Masukkan nilai ketidakpastian tipe B (jika ada)
    #### 5. Gabungkan tipe A dan B menggunakan:
    `uc = √(ua² + ub²)`
    #### 6. Kalikan dengan faktor cakupan (k) untuk mendapatkan ketidakpastian diperluas:
    `U = k × uc`
    """)

# ---------------------- 4. FITUR PERHITUNGAN ----------------------
elif menu == "4. Fitur Perhitungan / Calculation Tool":
    st.title("🧮 Fitur Perhitungan")
    st.markdown("Masukkan data untuk perhitungan ketidakpastian.")

    st.subheader("Tipe A - Statistik")
    data = st.text_area("Masukkan hasil pengukuran (pisahkan dengan koma)", "10.1, 10.2, 10.3")
    try:
        values = [float(x.strip()) for x in data.split(",")]
        mean = np.mean(values)
        std_dev = np.std(values, ddof=1)
        se = std_dev / np.sqrt(len(values))

        st.success(f"Rata-rata: {mean:.4f}")
        st.success(f"Simpangan Baku: {std_dev:.4f}")
        st.success(f"Standard Error (ua): {se:.4f}")
    except:
        st.warning("Masukkan data numerik yang valid.")

    st.subheader("Tipe B - Non Statistik")
    ub = st.number_input("Masukkan nilai ketidakpastian Tipe B (ub)", min_value=0.0, value=0.0)

    st.subheader("Gabungan dan Diperluas")
    k = st.selectbox("Pilih faktor cakupan (k)", [1, 2, 3])
    uc = np.sqrt(se**2 + ub**2)
    U = k * uc

    st.info(f"Ketidakpastian Gabungan (uc): {uc:.4f}")
    st.info(f"Ketidakpastian Diperluas (U): {U:.4f}")

# ---------------------- 5. KEMUNGKINAN KESALAHAN ----------------------
elif menu == "5. Kemungkinan Kesalahan / Possible Errors":
    st.title("⚠️ Kemungkinan Kesalahan")
    st.markdown("""
    ### Faktor penyebab ketidakpastian tinggi:
    - Alat ukur tidak dikalibrasi
    - Teknik pengukuran tidak konsisten
    - Operator berbeda
    - Kondisi lingkungan tidak stabil
    - Pembulatan angka signifikan
    - Kesalahan sistematis dan acak
    """)

# ---------------------- 6. CONTOH SOAL ----------------------
elif menu == "6. Contoh Soal & Pembahasan / Example Questions":
    st.title("📘 Contoh Soal dan Pembahasan")
    st.markdown("""
    #### 🔹 Gravimetri
    - Menghitung massa endapan dan ketidakpastiannya
    
    #### 🔹 Titrasi Asam-Basa
    - Menghitung konsentrasi HCl berdasarkan volume titran
    
    #### 🔹 Spektrofotometri
    - Pengukuran konsentrasi Cu²⁺ menggunakan kurva kalibrasi
    
    #### 🔹 Voltametri
    - Mengukur kadar Pb²⁺ dengan teknik stripping
    
    #### 🔹 Kromatografi
    - Penentuan kadar kafein dari luas puncak (area under the curve)
    """)

# ---------------------- 7. REFERENSI ----------------------
elif menu == "7. Referensi / References":
    st.title("📚 Referensi")
    st.markdown("""
    - Quantitative Chemical Analysis – Daniel C. Harris
    - Metrologi dan Ketidakpastian Pengukuran – BSN
    - ISO GUM (Guide to the Expression of Uncertainty in Measurement)
    - Jurnal dan artikel ilmiah terkait ketidakpastian pengukuran
    """)

# ---------------------- 8. TENTANG APLIKASI ----------------------
elif menu == "8. Tentang Aplikasi / About":
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
    ### Aplikasi ini dikembangkan oleh:
    **Mahasiswa POLITEKNIK AKA BOGOR 2025 - Kelompok 3**

    #### Anggota:
    - Aditya Dwika Iannanda  
    - Dhe Adila Zahra Tubarila  
    - Naura Amalia Shaliha  
    - Rizava Apriza  
    - Syalwa Fitriani

    ### Tujuan:
    Membantu pengguna dalam melakukan perhitungan ketidakpastian secara digital dan edukatif.

    ### Kontak:
    Email: ketidakpastian.app@aka.ac.id (fiktif)
    """)

# ---------------------- 9. FITUR TAMBAHAN ----------------------
elif menu == "9. Fitur Tambahan / Extra Features":
    st.title("🧰 Fitur Tambahan (Coming Soon)")
    st.markdown("""
    - ✅ **Download hasil perhitungan (PDF/Excel)**
    - ✅ **Simulasi interaktif (drag & drop alat lab)**
    - ✅ **Login pengguna untuk menyimpan histori**
    - ✅ **Mode Gelap (Dark Mode)**

    > Fitur ini dalam tahap pengembangan. Silakan tunggu update selanjutnya.
    """)
