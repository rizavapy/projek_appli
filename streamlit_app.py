import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Mengukur Ketidakpastian dan Galat Praktikum",
    page_icon="🧪",
    layout="wide"
)

# ----------- Toggle Bahasa -------------
if "lang" not in st.session_state:
    st.session_state.lang = "id"

def toggle_language():
    st.session_state.lang = "en" if st.session_state.lang == "id" else "id"

# Tombol translate
if st.session_state.lang == "id":
    st.title("🧪 Mengukur Nilai Ketidakpastian dan Galat Suatu Praktikum")
    st.button("🌐 Translate to English", on_click=toggle_language)
else:
    st.title("🧪 Measuring Uncertainty and Error in a Lab Practical")
    st.button("🇮🇩 Terjemahkan ke Bahasa Indonesia", on_click=toggle_language)

st.markdown("---")

# --------- Konten Bahasa Indonesia ---------
if st.session_state.lang == "id":
    st.subheader("👋 Selamat Datang!")
    st.write("""
Selamat datang di aplikasi edukasi **kimia analitik praktikum**.

Kamu akan belajar tentang:
- Nilai **ketidakpastian** dalam pengukuran
- **Galat, akurasi, toleransi**, dan perbedaannya
- Pentingnya menyatakan ketidakpastian di laporan laboratorium
- Dasar-dasar ilmu kimia yang penting untuk analis

Aplikasi ini membantumu berpikir ilmiah dan kritis saat menganalisis data praktikum.
""")

    st.subheader("📘 Teori: Ketidakpastian dan Galat")
    st.write("""
**1. Apa itu Ketidakpastian?**  
Ketidakpastian adalah ukuran seberapa yakin (atau tidak yakin) kita terhadap hasil pengukuran.  
Tidak ada alat yang benar-benar 100% akurat.

**2. Perbedaan Penting:**
- **Akurasi**: Kedekatan hasil terhadap nilai benar. Ditentukan oleh pabrikan.
- **Galat (Error)**: Selisih antara nilai terukur dan nilai referensi.
- **Toleransi**: Batas maksimum deviasi yang bisa diterima. Ditentukan oleh pengguna.
- **Ketidakpastian**: Seberapa besar keraguan terhadap hasil.

**Contoh Akurasi:**  
Akurasi alat ukur tekanan 2% dari skala penuh (0–40 bar) = ±0,8 bar.  
Pembacaan 20 bar bisa berarti nilai sebenarnya ada di 19,2 – 20,8 bar.

**Contoh Kesalahan:**  
Nilai standar = 20 bar, alat uji = 19,8 bar → Galat = -0,2 bar  
Penting juga memahami:  
- **Koreksi** = Nilai referensi − pembacaan  
- **Penyimpangan** = deviasi dari hasil ke hasil

**Contoh Toleransi:**  
Plat logam 10 mm, toleransi ±0,01 mm. Maka hasil di luar 9,99 – 10,01 mm tidak valid.

**Contoh Ketidakpastian:**  
Alat pH membaca 6,80 ± 0,05 → artinya nilai sebenarnya bisa 6,75 – 6,85  
""")

    st.info("""
📌 **Catatan Penting:**  
Dalam evaluasi hasil praktikum, kita **harus mempertimbangkan galat + ketidakpastian**, bukan hanya salah satunya.
""")

    st.subheader("📚 Dasar Ilmu Kimia untuk Analis")
    st.markdown("""
- **Mol & Massa Molar:** `n = m / Mr`
- **Konsentrasi:** `M = n / V`, satuan ppm, %w/v, molalitas
- **Stoikiometri:** Reaksi setara untuk konversi mol antar zat
- **pH & Buffer:** `pH = −log[H⁺]`, gunakan Henderson-Hasselbalch
- **Satuan & Dimensi:** Penting untuk menghindari kesalahan konversi
- **Evaluasi Ketidakpastian:**
    - Type A: berdasarkan data statistik pengulangan
    - Type B: dari sertifikat kalibrasi, literatur, resolusi alat
""")

    st.subheader("📝 Cara Menghitung Ketidakpastian Secara Manual")
    st.markdown("""
1. **Identifikasi**: tentukan apa yang diukur (massa, volume, pH, dll)  
2. **Cari sumber ketidakpastian**: 
   - Type A: dari hasil pengukuran berulang  
   - Type B: dari informasi alat (spesifikasi, resolusi)
3. **Konversi ke simpangan baku**:
   - Type A: `s / √n`
   - Type B: `resolusi / √3` atau `range / 2√3`
4. **Gabungkan**:  
   `u_c = √(u₁² + u₂² + ... + uₙ²)`
5. **Diperluas**:  
   `U = k × u_c` (k = 2 → tingkat keyakinan 95%)
6. **Lapor hasil**:  
   Contoh: `pH = 6.80 ± 0.05 (k=2)`
""")

# --------- Konten Bahasa Inggris ---------
else:
    st.subheader("👋 Welcome!")
    st.write("""
Welcome to this **analytical chemistry practical** learning app!

In this app, you'll learn about:
- **Measurement uncertainty**
- Differences between **error, accuracy, tolerance**
- Why it's important to state uncertainty in lab reports
- Basic chemistry theory for chemical analysts

This app helps you think critically and scientifically about your lab data.
""")

    st.subheader("📘 Theory: Uncertainty and Error")
    st.write("""
**1. What is Uncertainty?**  
Uncertainty is how confident (or not) we are about a measurement.  
No device is ever 100% accurate.

**2. Key Differences:**
- **Accuracy**: Closeness to the true value (from manufacturer)
- **Error**: Difference between measured and reference
- **Tolerance**: Max allowable deviation (user-defined)
- **Uncertainty**: Quantification of doubt

**Accuracy Example:**  
Accuracy = ±2% of full scale (0–40 bar) → ±0.8 bar  
Reading 20 bar means the true value may be 19.2 – 20.8 bar

**Error Example:**  
Reference = 20 bar, device reads 19.8 bar → Error = -0.2 bar  
Also understand:  
- **Correction** = Reference − Reading  
- **Deviation** = Absolute or relative variation

**Tolerance Example:**  
Metal part 10 mm ± 0.01 mm → any reading outside 9.99 – 10.01 mm is invalid

**Uncertainty Example:**  
pH meter shows 6.80 ± 0.05 → true value may be between 6.75 – 6.85
""")

    st.info("""
📌 **Important Note:**  
To evaluate an instrument or result, you must **combine error and uncertainty**, not ignore one.
""")

    st.subheader("📚 Chemistry Basics for Analysts")
    st.markdown("""
- **Mol & Molar Mass:** `n = m / Mr`
- **Concentration:** `M = n / V`, units: ppm, %w/v, molality
- **Stoichiometry:** Use balanced equations for mol conversions
- **pH & Buffers:** `pH = −log[H⁺]`, use Henderson-Hasselbalch equation
- **Units & Dimensions:** Always double-check conversions
- **Uncertainty Evaluation:**
    - Type A: statistical (repetition)
    - Type B: from specs, certificates, resolution
""")

    st.subheader("📝 Manual Steps to Calculate Uncertainty")
    st.markdown("""
1. **Identify** what is being measured  
2. **List sources** of uncertainty  
   - Type A: from repeated data  
   - Type B: from instrument specs, resolution  
3. **Convert to standard deviation**:
   - Type A: `s / √n`
   - Type B: `resolution / √3`
4. **Combine**:  
   `u_c = √(u₁² + u₂² + ... + uₙ²)`
5. **Expand**:  
   `U = k × u_c` (k = 2 → 95% confidence level)
6. **Report**:  
   Example: `pH = 6.80 ± 0.05 (k=2)`
""")

# ----------- Footer -----------
st.markdown("---")
st.caption("Dibuat dengan ❤️ oleh Mahasiswa Analis Kimia • 2025")
