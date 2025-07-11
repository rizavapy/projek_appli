import streamlit as st
import numpy as np

# Konfigurasi halaman
st.set_page_config(page_title="UncertaintyCalc", page_icon="📏", layout="wide")

# Navigasi
menu = st.sidebar.radio("📚 Menu", [
    "🏠 Beranda",
    "📘 Dasar Teori",
    "🔢 Hitung Nilai Ketidakpastian",
    "✍️ Perhitungan Manual",
    "⚠️ Faktor Kesalahan",
    "🧪 Contoh Soal"
])

# ============================================
# 1. BERANDA
# ============================================
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

    > 💡 “Pengukuran tanpa ketidakpastian hanyalah angka – pahami artinya, bukan hanya nilainya.”
    
    👉 Klik menu di sebelah kiri untuk mulai menjelajahi fitur!
    """)

# ============================================
# 2. DASAR TEORI
# ============================================
elif menu == "📘 Dasar Teori":
    st.title("📘 Belajar Dasar-Dasarnya")
    st.markdown("""
    Pahami konsep nilai ketidakpastian dari dasar hingga siap praktik!  
    Bagian ini menjelaskan teori, rumus, dan contoh praktis.

    ### 📌 1. Apa Itu Ketidakpastian?
    Ketidakpastian menunjukkan keraguan terhadap hasil pengukuran. Contoh:
    - Panjang meja: 120 cm → bisa jadi 119.8 cm atau 120.3 cm.

    ### 🧪 2. Jenis-Jenis Ketidakpastian
    - ✅ **Tipe A**: Berdasarkan eksperimen berulang → gunakan statistik.
    - ✅ **Tipe B**: Berdasarkan pengalaman, spesifikasi alat, referensi.

    ### 🔍 3. Simpangan Baku (s)
    \n\n\\( s = \\sqrt{\\frac{\\sum(x_i - \\bar{x})^2}{n-1}} \\)

    ### 🔧 4. Ketidakpastian Gabungan
    \n\n\\( u_c = \\sqrt{u_1^2 + u_2^2 + ... + u_n^2} \\)

    ### 💬 5. Ketidakpastian Relatif dan Mutlak
    - **Mutlak**: langsung dari simpangan.
    - **Relatif**: \\( \\frac{u}{x} \\times 100\\% \\)

    ### ✍️ 6. Menyajikan Hasil
    Format: nilai ± ketidakpastian (dua angka signifikan)

    ### 🧠 7. Kenapa Ini Penting?
    - Untuk kejujuran ilmiah dan kepercayaan data eksperimen.

    ### 🎯 8. Kesalahan Umum
    - Mengabaikan ketidakpastian, salah rumus, menulis angka berlebihan.

    ### 📎 9. Ringkasan Rumus
    | Konsep | Rumus |
    |--------|--------|
    | Rata-rata | \\( \\bar{x} = \\frac{\\sum x_i}{n} \\) |
    | Simpangan Baku | \\( s = \\sqrt{\\frac{\\sum(x_i - \\bar{x})^2}{n-1}} \\) |
    | Ketidakpastian Gabungan | \\( u_c = \\sqrt{\\sum u_i^2} \\) |
    | Ketidakpastian Relatif | \\( \\frac{u}{x} \\times 100\\% \\) |
    """)

# ============================================
# 3. PENGHITUNG OTOMATIS
# ============================================
elif menu == "🔢 Hitung Nilai Ketidakpastian":
    st.title("🔢 Hitung Nilai Ketidakpastian Otomatis")
    st.markdown("Masukkan data hasil pengukuran:")

    data_input = st.text_area("📝 Masukkan data dipisahkan dengan koma (misal: 120.1, 120.3, 120.0)", height=100)
    
    if st.button("🔍 Hitung"):
        try:
            data = np.array([float(x.strip()) for x in data_input.split(",") if x.strip() != ""])
            n = len(data)
            if n < 2:
                st.warning("Masukkan minimal 2 data.")
            else:
                rata2 = np.mean(data)
                simp_baku = np.std(data, ddof=1)
                uA = simp_baku / np.sqrt(n)

                st.success("✅ Hasil Perhitungan:")
                st.markdown(f"**Rata-rata (x̄):** {rata2:.5f}")
                st.markdown(f"**Simpangan Baku (s):** {simp_baku:.5f}")
                st.markdown(f"**Ketidakpastian Tipe A (uA):** ± {uA:.5f}")
                st.markdown(f"**Hasil Pengukuran Akhir:** {rata2:.2f} ± {uA:.2f}")
        except:
            st.error("❌ Format data salah. Pastikan hanya angka dan koma.")

# ============================================
# 4. PERHITUNGAN MANUAL
# ============================================
elif menu == "✍️ Perhitungan Manual":
    st.title("🧠 Perhitungan Manual")
    st.markdown("""
    ### Contoh Kasus:
    Kamu mengukur panjang meja sebanyak 5 kali:  
    **120.1, 120.3, 120.0, 120.2, 120.4 (cm)**

    ### Langkah-Langkah:
    1. Hitung rata-rata:  
       \\( \\bar{x} = \\frac{600.9}{5} = 120.18 \\)
    
    2. Hitung simpangan baku (s):  
       \\( s = \\sqrt{\\frac{0.102}{4}} = 0.1596 \\)

    3. Hitung ketidakpastian standar (uA):  
       \\( u_A = \\frac{0.1596}{\\sqrt{5}} \\approx 0.0713 \\)

    4. **Hasil Akhir**:  
       **Panjang meja = 120.18 ± 0.07 cm**
    
    ---  
    ### 🎓 Tutorial Kalkulator:
    - Gunakan MODE → STAT → 1-VAR
    - Masukkan semua data
    - SHIFT → 1 → 4 → lihat `x̄` dan `σn-1`
    - Hitung `σ ÷ √n` untuk uA
    """)

# ============================================
# 5. FAKTOR KESALAHAN
# ============================================
elif menu == "⚠️ Faktor Kesalahan":
    st.title("⚠️ Kemungkinan Kesalahan Pengukuran")
    st.markdown("""
    Mengapa nilai ketidakpastian bisa besar?

    ### 🌡️ 1. Suhu Lingkungan
    - Pemuaian alat ukur → hasil berubah

    ### 💧 2. Kelembaban
    - Bahan menyerap air → ukuran berubah

    ### ✋ 3. Kesalahan Manusia
    - Salah baca skala, tergesa-gesa

    ### 🔧 4. Alat Tidak Dikalibrasi
    - Kesalahan sistematis

    ### 📊 5. Lingkungan Tidak Stabil
    - Getaran, gangguan magnet, cahaya

    ### 🔁 6. Variasi Benda
    - Objek tidak seragam → variasi besar

    ### 🛡️ Solusi:
    - Kalibrasi alat, pengukuran ulang, gunakan lingkungan stabil
    """)

# ============================================
# 6. CONTOH SOAL
# ============================================
elif menu == "🧪 Contoh Soal":
    st.title("🧪 Contoh Soal dan Pembahasan")

    with st.expander("🔹 Contoh Soal 1 – Tipe A"):
        st.markdown("""
        Hasil waktu (detik): 1.20, 1.18, 1.22, 1.19, 1.21

        - **Rata-rata:** 1.20
        - **Simpangan Baku (s):** 0.0158
        - **uA = s / √n = 0.0158 / √5 ≈ 0.0071**

        **Hasil akhir: 1.20 ± 0.01 detik**
        """)

    with st.expander("🔹 Contoh Soal 2 – Ketidakpastian Gabungan"):
        st.markdown("""
        Panjang = 120.0 ± 0.5 cm  
        Lebar = 60.0 ± 0.3 cm  

        - **Luas = 120 × 60 = 7200 cm²**
        - Ketidakpastian relatif:
          \\( \\sqrt{(0.5/120)^2 + (0.3/60)^2} ≈ 0.00651 \\)

        - uL = 0.00651 × 7200 ≈ 47

        **Luas akhir: 7200 ± 47 cm²**
        """)

