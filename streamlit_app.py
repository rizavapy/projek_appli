import streamlit as st
import numpy as np
import math

st.set_page_config(page_title="Nilai Ketidakpastian", layout="wide")

st.title("📏 Nilai Ketidakpastian dalam Pengukuran")

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Beranda", "📘 Dasar Teori", "🔢 Hitung Otomatis", 
    "✍️ Hitung Manual", "⚠️ Faktor Kesalahan", "🧪 Contoh Soal"
])

# ========================================
# 🏠 Tab 1: Beranda
with tab1:
    st.header("📏 Apa Itu Nilai Ketidakpastian?")
    st.write("""
    Dalam setiap pengukuran, selalu ada kemungkinan kesalahan atau deviasi dari nilai sebenarnya. 
    Nilai ketidakpastian menggambarkan seberapa besar keraguan kita terhadap hasil pengukuran tersebut.
    """)

    st.subheader("🛠️ Apa yang Bisa Kamu Lakukan di Sini?")
    st.markdown("""
    - 📘 **Belajar Dasar-Dasarnya**: Simpangan baku, ketidakpastian mutlak & relatif.
    - 🔢 **Hitung Nilai Ketidakpastian**: Kalkulator ketidakpastian tipe A, B, dan gabungan.
    - ✍️ **Perhitungan Manual**: Langkah-langkah menggunakan kalkulator.
    - ⚠️ **Faktor Kesalahan**: Suhu, kelembaban, dan faktor lingkungan lain.
    - 🧪 **Contoh Soal & Pembahasan**: Soal interaktif beserta pembahasan.

    > 💡 “Pengukuran tanpa ketidakpastian hanyalah angka – pahami artinya, bukan hanya nilainya.”
    """)

    st.subheader("🎯 Siapa yang Cocok Menggunakan Situs Ini?")
    st.write("""
    Mahasiswa, pelajar, guru, dosen, teknisi laboratorium, atau siapa pun yang ingin menguasai konsep ketidakpastian dalam pengukuran secara praktis dan mudah dipahami.
    """)

# ========================================
# 📘 Tab 2: Dasar Teori
with tab2:
    st.header("📘 Dasar Teori: Pahami Ketidakpastian Pengukuran")
    st.markdown("""
### 📌 1. Apa Itu Ketidakpastian Pengukuran?
Setiap pengukuran memiliki ketidakpastian – yaitu tingkat keraguan terhadap nilai hasil ukur.

### 🧪 2. Jenis-Jenis Ketidakpastian
- ✅ **Tipe A**: Dari data eksperimen berulang.
- ✅ **Tipe B**: Dari referensi/manual.

### 🔍 3. Simpangan Baku (Standard Deviation)
$$ s = \\sqrt{\\frac{\\sum{(x_i - \\bar{x})^2}}{n - 1}} $$

### 🔧 4. Ketidakpastian Gabungan
$$ u_c = \\sqrt{u_1^2 + u_2^2 + ... + u_n^2} $$

### 💬 5. Ketidakpastian Mutlak dan Relatif
- Mutlak: langsung dari simpangan.
- Relatif: $ \\frac{u}{x} \\times 100\\% $

### ✍️ 6. Cara Menyajikan Hasil
Contoh: $ T = 27.4 \\pm 0.3 ^\\circ C $

### 🎯 8. Kesalahan Umum
- Tidak menyertakan ketidakpastian
- Alat digital dianggap pasti
- Salah jumlahkan ketidakpastian

### 📎 9. Tabel Ringkasan Rumus

| Konsep | Rumus |
|-------|-------|
| Rata-rata | $\\bar{x} = \\frac{\\sum x_i}{n}$ |
| Simpangan Baku | $s = \\sqrt{\\frac{\\sum(x_i - \\bar{x})^2}{n - 1}}$ |
| Ketidakpastian Gabungan | $u_c = \\sqrt{\\sum u_i^2}$ |
| Ketidakpastian Relatif | $\\frac{u}{x} \\times 100\\%$ |
    """)

# ========================================
# 🔢 Tab 3: Hitung Otomatis
with tab3:
    st.header("🔢 Hitung Nilai Ketidakpastian Otomatis")

    data = st.text_area("Masukkan data pengukuran (pisahkan dengan koma):", "120.1, 120.3, 120.0, 120.2, 120.4")

    if st.button("Hitung Ketidakpastian"):
        try:
            values = [float(i.strip()) for i in data.split(',')]
            n = len(values)
            mean = np.mean(values)
            std_dev = np.std(values, ddof=1)
            uncertainty_A = std_dev / math.sqrt(n)

            st.success("📊 Hasil Perhitungan:")
            st.write(f"Rata-rata (x̄): **{mean:.2f}**")
            st.write(f"Simpangan Baku (s): **{std_dev:.4f}**")
            st.write(f"Ketidakpastian Tipe A: **± {uncertainty_A:.2f}**")
            st.write(f"Hasil Pengukuran: **{mean:.2f} ± {uncertainty_A:.2f}**")
        except:
            st.error("⚠️ Pastikan input berupa angka yang dipisahkan dengan koma.")

# ========================================
# ✍️ Tab 4: Hitung Manual
with tab4:
    st.header("✍️ Perhitungan Manual")

    st.write("Contoh data pengukuran panjang meja (dalam cm):")
    st.code("120.1, 120.3, 120.0, 120.2, 120.4")

    st.markdown("""
Langkah:
1. Hitung rata-rata
2. Hitung simpangan baku
3. Hitung ketidakpastian A = s / √n

Contoh:
- Rata-rata = 120.18
- Simpangan baku = 0.1596
- Ketidakpastian A = 0.1596 / √5 ≈ 0.0713

📏 **Hasil Akhir:**  
120.18 ± 0.07 cm
""")

# ========================================
# ⚠️ Tab 5: Faktor Kesalahan
with tab5:
    st.header("⚠️ Kemungkinan Kesalahan Pengukuran")
    st.markdown("""
Beberapa faktor umum:
- 🌡️ **Suhu**: Alat dan benda bisa memuai.
- 💧 **Kelembaban**: Mengubah sifat bahan.
- ✋ **Human Error**: Salah membaca alat.
- 🔧 **Kalibrasi Buruk**: Alat tidak akurat.
- 📊 **Lingkungan**: Getaran, cahaya, atau medan magnet.
- 🔁 **Sampel Tidak Seragam**: Ukuran/berat bervariasi.

🛡️ **Tips Mengurangi Kesalahan**:
- Gunakan alat presisi tinggi
- Kalibrasi alat
- Ulangi pengukuran 5–10 kali
""")

# ========================================
# 🧪 Tab 6: Contoh Soal & Pembahasan
with tab6:
    st.header("🧪 Contoh Soal & Pembahasan")

    st.subheader("Contoh Soal 1 – Ketidakpastian Tipe A")
    st.markdown("""
Seorang siswa mengukur waktu (dalam detik):  
`1.20, 1.18, 1.22, 1.19, 1.21`

✅ Rata-rata: 1.20 s  
✅ Simpangan baku: 0.0158 s  
✅ Ketidakpastian A = 0.0158 / √5 ≈ 0.0071 s  

📏 **Hasil Akhir**: 1.20 ± 0.01 s
""")

    st.subheader("Contoh Soal 2 – Ketidakpastian Gabungan")
    st.markdown("""
Panjang = 120.0 ± 0.5 cm  
Lebar = 60.0 ± 0.3 cm  

✅ Luas = 120 × 60 = 7200 cm²  
✅ Relatif:  
$$ u_L/L = \\sqrt{(0.5/120)^2 + (0.3/60)^2} ≈ 0.00651 $$  
✅ u_L = 0.00651 × 7200 ≈ 46.87

📏 **Hasil Akhir**: 7200 ± 47 cm²
""")
