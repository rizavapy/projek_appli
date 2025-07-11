import streamlit as st
import numpy as np
import math

st.set_page_config(page_title="Ketidakpastian Pengukuran", layout="wide")

st.title("📏 Aplikasi Ketidakpastian Pengukuran")

st.sidebar.title("Navigasi")
halaman = st.sidebar.radio("Pilih Halaman:", [
    "📘 Dasar Teori",
    "🔢 Hitung Otomatis",
    "✍️ Hitung Manual",
    "⚠️ Faktor Kesalahan",
    "🧪 Contoh Soal & Pembahasan"
])

# 📘 DASAR TEORI
if halaman == "📘 Dasar Teori":
    st.header("📘 Dasar-Dasar Ketidakpastian Pengukuran")
    st.subheader("1. Apa Itu Ketidakpastian?")
    st.markdown("""
Setiap pengukuran pasti memiliki **keraguan terhadap hasil**.  
Contoh: hasil pengukuran 120 cm bisa saja 119.8 cm atau 120.2 cm.

Ketidakpastian membantu menyampaikan seberapa **akurat dan terpercaya** hasil tersebut.
""")

    st.subheader("2. Jenis-Jenis Ketidakpastian")
    st.markdown("""
- **Tipe A**: dari data eksperimen berulang → dihitung secara statistik  
- **Tipe B**: dari pengalaman, spesifikasi alat, manual buku  
""")

    st.subheader("3. Rumus-Rumus Penting")
    st.latex(r"\bar{x} = \frac{\sum x_i}{n}")
    st.latex(r"s = \sqrt{\frac{\sum (x_i - \bar{x})^2}{n-1}}")
    st.latex(r"u_A = \frac{s}{\sqrt{n}}")
    st.latex(r"u_c = \sqrt{u_1^2 + u_2^2 + ... + u_n^2}")
    st.latex(r"u_{relatif} = \frac{u}{x} \times 100\%")

    st.subheader("4. Penyajian Hasil")
    st.markdown("Format: **Hasil = Nilai ± Ketidakpastian (satuan)**")
    st.markdown("Contoh: Suhu = 27.4 ± 0.3 °C")

# 🔢 KALKULATOR OTOMATIS
elif halaman == "🔢 Hitung Otomatis":
    st.header("🔢 Kalkulator Otomatis Ketidakpastian")

    st.markdown("Masukkan data pengukuran (misal: `120.1, 120.3, 120.0, 120.2, 120.4`)")

    data_input = st.text_area("Data Pengukuran:", "120.1, 120.3, 120.0, 120.2, 120.4")
    try:
        data = np.array([float(i.strip()) for i in data_input.split(",")])
        n = len(data)
        xbar = np.mean(data)
        s = np.std(data, ddof=1)
        uA = s / np.sqrt(n)

        st.success("✅ Hasil Tipe A")
        st.write(f"Rata-rata (x̄): {xbar:.5f}")
        st.write(f"Simpangan Baku (s): {s:.5f}")
        st.write(f"Ketidakpastian Tipe A (uA): ± {uA:.5f}")
        st.markdown(f"**Hasil Akhir:** {xbar:.2f} ± {uA:.2f} satuan")

        st.markdown("---")
        st.subheader("➕ Tambahkan Ketidakpastian Tipe B (opsional)")
        ub = st.number_input("Ketidakpastian Tipe B (misal spesifikasi alat)", 0.0)
        if ub > 0:
            uc = math.sqrt(uA**2 + ub**2)
            st.success(f"✅ Ketidakpastian Gabungan (uc): ± {uc:.5f}")
            st.markdown(f"**Hasil Gabungan:** {xbar:.2f} ± {uc:.2f} satuan")

    except:
        st.error("Pastikan format input benar. Pisahkan angka dengan koma.")

# ✍️ HITUNG MANUAL
elif halaman == "✍️ Hitung Manual":
    st.header("✍️ Perhitungan Manual: Contoh Kasus")

    st.markdown("**Data:** `120.1, 120.3, 120.0, 120.2, 120.4`")
    st.markdown("Langkah:")
    st.markdown("""
1. Hitung rata-rata:  
   𝑥̄ = (jumlah data) / n = 120.18  
2. Hitung (xi - x̄)² → jumlahkan  
3. Hitung simpangan baku (s)  
4. Hitung uA = s / √n  
5. Hasil: Nilai ± uA
""")

    st.code("""
Selisih kuadrat:
(120.1 − 120.18)² = 0.0064
(120.3 − 120.18)² = 0.0144
...
Jumlah = 0.102 → s = √(0.102/4) ≈ 0.1596
uA = 0.1596 / √5 ≈ 0.0713
Hasil = 120.18 ± 0.07 cm
""")

# ⚠️ KESALAHAN UMUM
elif halaman == "⚠️ Faktor Kesalahan":
    st.header("⚠️ Faktor Penyebab Ketidakpastian Tinggi")

    st.markdown("""
**1. Perubahan Suhu** 🌡️  
   → Alat memuai/menciut

**2. Kelembaban Udara** 💧  
   → Benda menyerap air

**3. Human Error** ✋  
   → Membaca alat tidak sejajar (paralaks)

**4. Alat Tidak Dikalibrasi** 🔧  
   → Timbangan miring, alat rusak

**5. Lingkungan** 📊  
   → Getaran, cahaya, listrik

**6. Sampel Tidak Seragam** 🔁  
   → Objek tidak homogen
""")

# 🧪 CONTOH SOAL
elif halaman == "🧪 Contoh Soal & Pembahasan":
    st.header("🧪 Contoh Soal & Pembahasan")

    with st.expander("📘 Soal 1: Ketidakpastian Tipe A"):
        st.markdown("""
Data waktu (s): `1.20, 1.18, 1.22, 1.19, 1.21`

Rata-rata = 1.20 s  
s = √(jumlah selisih kuadrat / 4) ≈ 0.0158  
uA = s / √5 ≈ 0.0071 s  
**Jawaban:** 1.20 ± 0.01 s
""")

    with st.expander("📘 Soal 2: Ketidakpastian Gabungan"):
        st.markdown("""
Panjang = 120.0 ± 0.5 cm  
Lebar = 60.0 ± 0.3 cm  
Luas = 120 × 60 = 7200 cm²

uL/L = √[(0.5/120)² + (0.3/60)²] = 0.00651  
uL = 0.00651 × 7200 ≈ 47 cm²  
**Jawaban:** Luas = 7200 ± 47 cm²
""")
