import streamlit as st

st.set_page_config(
    page_title="Beranda • Analis Kimia",
    page_icon="🧪",
    layout="wide"
)

# ------------------- HEADER -------------------
st.title("🧪 Beranda: Dasar-Dasar Analis Kimia")
st.markdown("---")

# ------------------- PROFIL ANALIS KIMIA -------------------
st.header("🔬 Siapa Itu Analis Kimia?")
st.write("""
Analis kimia adalah tenaga profesional yang berperan dalam menganalisis komposisi zat kimia, 
baik dalam bentuk padatan, cairan, maupun gas. Tugas utama mereka meliputi:

- Melakukan pengambilan sampel
- Melakukan analisis kuantitatif & kualitatif
- Menyiapkan larutan standar
- Melakukan validasi metode dan kalibrasi alat
- Menghitung dan melaporkan hasil analisa beserta **ketidakpastiannya**

Pekerjaan ini sangat penting dalam industri farmasi, makanan, kosmetik, lingkungan, dan lainnya.
""")

# ------------------- PERBANDINGAN KONSEP -------------------
st.header("📏 Perbedaan Antara Akurasi, Toleransi, Kesalahan, dan Ketidakpastian")

# ---- AKURASI ----
with st.expander("🎯 Akurasi"):
    st.write("""
**Akurasi** adalah kedekatan hasil pengukuran terhadap nilai sebenarnya dari besaran ukur.
Akurasi biasanya ditentukan oleh **pabrikan alat**.

📌 **Contoh**:
- Akurasi pengukur tekanan = **±2% F.S**
- Jika skala penuh = 40 bar → maka akurasi ±0.8 bar
- Artinya pembacaan 20 bar dianggap akurat jika berada antara **19.2 – 20.8 bar**
""")

# ---- KESALAHAN ----
with st.expander("⚠️ Kesalahan (Error)"):
    st.write("""
**Kesalahan** adalah selisih antara nilai terukur dan nilai referensi/standar.

📌 **Contoh**:
- Master Gauge membaca: 20 bar  
- Alat Uji (UUC) membaca: 19.8 bar  
- Kesalahan = **19.8 − 20 = −0.2 bar**

🔁 **Perbedaan istilah**:
- Kesalahan = Pembacaan − Nilai referensi  
- Koreksi = Nilai referensi − Pembacaan  
- Penyimpangan = Selisih absolut atau relatif  
""")

# ---- TOLERANSI ----
with st.expander("📐 Toleransi"):
    st.write("""
**Toleransi** adalah deviasi maksimum yang masih dapat diterima menurut desain atau kebutuhan pengguna.

📌 **Contoh**:
- Potongan logam 10 mm, toleransi ±0,01 mm  
- Artinya hasil pengukuran di luar **9.99 – 10.01 mm** dianggap tidak memenuhi spesifikasi.

🔁 **Perbedaan**:
- **Akurasi** → ditentukan pabrikan  
- **Toleransi** → ditentukan pengguna/desainer  
""")

# ---- KETIDAKPASTIAN ----
with st.expander("🔎 Ketidakpastian"):
    st.write("""
**Ketidakpastian** adalah ukuran keraguan terhadap hasil pengukuran. Semua pembacaan memiliki tingkat ketidakpastian.

💡 Termasuk faktor:
- Keahlian analis
- Resolusi alat
- Fluktuasi suhu
- Kalibrasi dan akurasi alat

📌 **Contoh nyata**:
Ketika pengukuran pH dilakukan dengan pH meter, meskipun hasil terlihat **5.60**, ketidakpastian bisa ±0.05. Artinya nilai sebenarnya bisa antara **5.55 – 5.65**.

❗ **Kesalahan umum**:
Banyak yang hanya membandingkan **Error vs Akurasi** atau **Error vs Toleransi**, **tanpa mempertimbangkan Ketidakpastian**.
""")

# ------------------- PENTINGNYA GABUNGKAN -------------------
st.info("""
🔄 Untuk evaluasi instrumen, **Error dan Ketidakpastian** harus digabung sebelum menyatakan “Lulus” atau “Gagal”.

Contoh:  
Jika Akurasi = ±1 bar, dan Error = 0.8 bar tapi Ketidakpastian = 0.4 bar → Maka total deviasi = 0.8 + 0.4 = 1.2 → melebihi batas → **Gagal**.
""")

# ------------------- MANUAL CALCULATION -------------------
st.header("📚 Cara Menghitung Ketidakpastian Secara Manual")

with st.expander("📝 Langkah-Langkah Manual Menentukan Ketidakpastian (GUM Based)"):
    st.markdown("""
### ✏️ Langkah-Langkah:

1. **Identifikasi Besaran Ukur**  
   Misalnya: massa, volume, pH, panjang, suhu, dll.

2. **Tentukan Semua Sumber Ketidakpastian**  
   - Type A: Hasil pengukuran berulang  
   - Type B: Sertifikat kalibrasi, spesifikasi alat, literatur

3. **Konversi Semua ke Simpangan Baku (Standard Deviation)**  
   - Type A → `u = s / √n`  
   - Type B → `u = resolusi / √3` (jika batas toleransi)

4. **Gabungkan Semua (Propagasi)**  
   \n\\( u_c = \\sqrt{\\sum u_i^2} \\)

5. **Hitung Ketidakpastian Diperluas**  
   \\( U = k \\cdot u_c \\)  
   (k = 2 untuk 95% CI)

6. **Laporan Hasil**  
   Misalnya: `pH = 5.60 ± 0.05 (k=2)` atau `massa = 10.24 ± 0.15 g (k=2)`
    """)

# ------------------- FOOTER -------------------
st.markdown("---")
st.caption("Dibuat dengan ❤️ oleh Mahasiswa Analis Kimia • 2025")
