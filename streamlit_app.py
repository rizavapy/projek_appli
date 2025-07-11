import streamlit as st
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="UncertaintyCalc", page_icon="📏", layout="wide")

# Sidebar Navigasi
menu = st.sidebar.radio("📚 Menu", [
    "🏠 Beranda",
    "📘 Dasar Teori",
    "🔢 Kalkulator Ketidakpastian (Tipe A & B)",
    "✍️ Perhitungan Manual",
    "⚠️ Faktor Kesalahan",
    "🧪 Contoh Soal"
])

# ======================================================
# 1. BERANDA
# ======================================================
if menu == "🏠 Beranda":
    st.title("🎉 Selamat Datang di ChemCalc!")
    st.markdown("""
    Situs web interaktif untuk memahami dan menghitung nilai **ketidakpastian** dalam pengukuran ilmiah dan teknis.

    ### 📏 Apa Itu Nilai Ketidakpastian?
    Setiap pengukuran mengandung potensi kesalahan. Ketidakpastian menggambarkan seberapa besar keraguan kita terhadap hasil tersebut.

    ### 🛠️ Apa yang Bisa Kamu Lakukan di Sini?
    - 🔢 Hitung Ketidakpastian Tipe A, B, dan Gabungan
    - 📘 Pelajari teori dasar ketidakpastian
    - 🧪 Latihan soal dengan pembahasan

    ### 🎯 Siapa yang Cocok Menggunakan Situs Ini?
    Mahasiswa, pelajar, guru, dosen, teknisi, dan semua yang ingin memahami ketidakpastian pengukuran.

    > 💡 *“Pengukuran tanpa ketidakpastian hanyalah angka – pahami artinya, bukan hanya nilainya.”*

    👉 Klik menu di sebelah kiri untuk mulai menjelajahi fitur!
    """)

# ======================================================
# 2. DASAR TEORI
# ======================================================
elif menu == "📘 Dasar Teori":
    st.title("📘 Dasar-Dasar Ketidakpastian Pengukuran")
    st.markdown("""
    Pelajari konsep penting seperti simpangan baku, ketidakpastian mutlak dan relatif, dan cara menyajikan hasil.

    #### ✅ Tipe A
    Berdasarkan data eksperimen → statistik
    \n\n\\( u_A = \\frac{s}{\\sqrt{n}} \\)

    #### ✅ Tipe B
    Berdasarkan ketelitian alat, referensi
    \n\n\\( u_B = \\frac{\\text{ketelitian}}{\\sqrt{3}} \\)

    #### 🔧 Gabungan
    \n\n\\( u_c = \\sqrt{u_A^2 + u_B^2} \\)

    #### 💬 Relatif
    \n\n\\( \\text{Relatif} = \\frac{u_c}{\\bar{x}} \\times 100\\% \\)

    """)

# ======================================================
# 3. KALKULATOR OTOMATIS TIPE A & B
# ======================================================
elif menu == "🔢 Kalkulator Ketidakpastian (Tipe A & B)":
    st.title("🔢 Kalkulator Ketidakpastian Tipe A & B")

    with st.expander("📥 Masukkan Data Hasil Pengukuran"):
        raw_data = st.text_area("Data pengukuran (pisahkan dengan koma):", "120.1, 120.3, 120.0, 120.2, 120.4")
        try:
            data = np.array([float(i.strip()) for i in raw_data.split(",") if i.strip() != ""])
            n = len(data)
        except:
            data = None
            n = 0
            st.warning("❗ Pastikan hanya angka dan dipisah dengan koma.")

    with st.expander("🛠️ Ketelitian Alat (untuk Tipe B)"):
        ketelitian = st.number_input("Masukkan nilai ketelitian alat ukur:", min_value=0.0, value=0.1, step=0.01)

    if st.button("🔍 Hitung Ketidakpastian"):
        if data is None or n < 2:
            st.error("❗ Minimal masukkan 2 data pengukuran yang valid.")
        else:
            rata2 = np.mean(data)
            simp_baku = np.std(data, ddof=1)
            uA = simp_baku / np.sqrt(n)
            uB = ketelitian / np.sqrt(3)
            uC = np.sqrt(uA**2 + uB**2)
            relatif = (uC / rata2) * 100

            st.success("✅ Hasil Perhitungan:")
            st.write(f"**Rata-rata (x̄):** {rata2:.5f}")
            st.write(f"**Simpangan Baku (s):** {simp_baku:.5f}")
            st.write(f"**Ketidakpastian Tipe A (uA):** ± {uA:.5f}")
            st.write(f"**Ketidakpastian Tipe B (uB):** ± {uB:.5f}")
            st.write(f"**Ketidakpastian Gabungan (uC):** ± {uC:.5f}")
            st.write(f"**Ketidakpastian Relatif:** {relatif:.2f}%")
            st.write(f"### 📏 Hasil Akhir: {rata2:.2f} ± {uC:.2f}")

# ======================================================
# 4. PERHITUNGAN MANUAL
# ======================================================
elif menu == "✍️ Perhitungan Manual":
    st.title("✍️ Perhitungan Manual Ketidakpastian")
    st.markdown("""
    Contoh data: 120.1, 120.3, 120.0, 120.2, 120.4

    1. Rata-rata:  
    \\( \\bar{x} = \\frac{\\sum x_i}{n} \\)

    2. Simpangan baku (s):  
    \\( s = \\sqrt{\\frac{\\sum(x_i - \\bar{x})^2}{n - 1}} \\)

    3. Ketidakpastian Tipe A:  
    \\( u_A = \\frac{s}{\\sqrt{n}} \\)

    4. Ketidakpastian Tipe B:  
    \\( u_B = \\frac{\\text{ketelitian}}{\\sqrt{3}} \\)

    5. Gabungan:  
    \\( u_c = \\sqrt{u_A^2 + u_B^2} \\)

    6. Hasil akhir:  
    \\( \\bar{x} \\pm u_c \\)
    """)

# ======================================================
# 5. FAKTOR KESALAHAN
# ======================================================
elif menu == "⚠️ Faktor Kesalahan":
    st.title("⚠️ Faktor Kesalahan Pengukuran")
    st.markdown("""
    ### Penyebab Umum:
    - 🌡️ **Suhu Lingkungan**
    - 💧 **Kelembaban Tinggi**
    - ✋ **Kesalahan Manusia**
    - 🔧 **Alat Tidak Dikalibrasi**
    - 📊 **Lingkungan Tidak Stabil**
    - 🔁 **Sampel Tidak Seragam**

    ### Cara Mengurangi:
    - Gunakan alat presisi tinggi
    - Kalibrasi berkala
    - Ulangi pengukuran
    - Hindari lingkungan ekstrem
    """)

# ======================================================
# 6. CONTOH SOAL
# ======================================================
elif menu == "🧪 Contoh Soal":
    st.title("🧪 Contoh Soal & Pembahasan")

    st.subheader("🔹 Soal 1 – Tipe A")
    st.markdown("""
    Data waktu (detik): 1.20, 1.18, 1.22, 1.19, 1.21  
    - \\( \\bar{x} = 1.20 \\)  
    - \\( s = 0.0158 \\)  
    - \\( u_A = 0.0071 \\)  
    **Hasil:** 1.20 ± 0.01 detik
    """)

    st.subheader("🔹 Soal 2 – Gabungan")
    st.markdown("""
    Panjang = 120.0 ± 0.5 cm  
    Lebar = 60.0 ± 0.3 cm  
    - Luas = 7200 cm²  
    - \\( u_c = \\sqrt{(0.5/120)^2 + (0.3/60)^2} × 7200 ≈ 47 \\)  
    **Luas Akhir:** 7200 ± 47 cm²
    """)

