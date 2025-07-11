# app.py
# Aplikasi Web Perhitungan Nilai Ketidakpastian – Kelompok 3 POLITEKNIK AKA BOGOR 2025
# ------------------------------------------------------------

import streamlit as st
import numpy as np
import pandas as pd
from io import BytesIO
from datetime import datetime

# -------------- Konfigurasi awal + Tema gelap --------------
st.set_page_config(
    page_title="Aplikasi Ketidakpastian",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Terapkan mode gelap (kalau dipilih)
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

dark_css = """
<style>
body, .stApp {background-color:#0e1117;color:#f0f0f0;}
hr{color:#666;} .css-18ni7ap{background:#161b22;}
</style>"""

# --------- Fungsi utilitas ---------------------------------
def to_excel(df: pd.DataFrame) -> bytes:
    """Mengubah DataFrame ke bytes Excel (xlsx)."""
    output = BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Results")
    return output.getvalue()

def to_pdf(text: str) -> bytes:
    """Placeholder PDF (simbolis, memakai txt → PDF minimal)."""
    try:
        from fpdf import FPDF                          # pip install fpdf
    except ImportError:
        return text.encode()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Helvetica", size=11)
    for line in text.split("\n"):
        pdf.multi_cell(0, 8, txt=line)
    return pdf.output(dest="S").encode("latin-1")

# --------- Login sederhana ---------------------------------
def login_block():
    st.sidebar.markdown("### 🔐 Login Pengguna (opsional)")
    if "login" not in st.session_state:
        st.session_state.login = False
    if not st.session_state.login:
        with st.sidebar.form("login_form", clear_on_submit=False):
            user = st.text_input("Username")
            pwd  = st.text_input("Password", type="password")
            submit = st.form_submit_button("Login")
            if submit and user and pwd:
                st.session_state.login = True
                st.sidebar.success(f"Selamat datang, **{user}**!")
    else:
        if st.sidebar.button("Logout"):
            st.session_state.login = False

login_block()

# ---------- Sidebar ----------------------------------------
st.sidebar.markdown("## 🌐 Navigasi / Navigation")
page = st.sidebar.radio(
    label="Menu",
    options=(
        "Beranda / Home",
        "Dasar Teori / Theory",
        "Cara Perhitungan Manual",
        "Fitur Perhitungan",
        "Kemungkinan Kesalahan",
        "Contoh Soal & Pembahasan",
        "Referensi / References",
        "Tentang Aplikasi",
        "Fitur Tambahan"
    )
)

# Saklar mode gelap
if st.sidebar.checkbox("💡 Mode Gelap / Dark Mode", value=st.session_state.dark_mode):
    st.session_state.dark_mode = True
    st.markdown(dark_css, unsafe_allow_html=True)
else:
    st.session_state.dark_mode = False

# ============================================================
# 1. BERANDA
# ============================================================
if page == "Beranda / Home":
    st.title("🔬 Aplikasi Perhitungan Nilai Ketidakpastian")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
**Selamat datang!**  
Aplikasi ini membantu mahasiswa & analis kimia menghitung **nilai ketidakpastian pengukuran** secara cepat dan akurat.

**Tujuan / Purpose**  
- Memahami konsep ketidakpastian  
- Melakukan perhitungan manual & otomatis  
- Menyediakan pembelajaran interaktif  

**Kelebihan / Advantages**  
- Antarmuka ramah pengguna  
- Dilengkapi teori, contoh soal, & download hasil  
- Simulasi interaktif (coming soon)  
        """)
    with col2:
        st.image(
            "https://raw.githubusercontent.com/streamlit/brand/master/streamlit-logo-secondary.png",
            caption="Powered by Streamlit",
            width=280,
        )
    st.success("Happy calculating! / Selamat belajar!")

# ============================================================
# 2. DASAR TEORI
# ============================================================
elif page == "Dasar Teori / Theory":
    st.title("📚 Dasar Teori – Theory of Uncertainty")
    st.markdown("""
### Apa itu Ketidakpastian? / What is Uncertainty?
Ketidakpastian adalah parameter yang mengukur seberapa yakin kita terhadap nilai hasil pengukuran.

### Jenis Ketidakpastian
| Jenis | Sumber | Contoh |
|-------|--------|--------|
| **Tipe A** | Statistik (repeatability) | Simpangan baku dari 10 kali penimbangan |
| **Tipe B** | Non-statistik | Spesifikasi timbangan, sertifikat kalibrasi |

### Penggabungan (Combined)  
`uc = √(ua² + ub²)`

### Ketidakpastian Diperluas (Expanded)  
`U = k × uc` (dengan *k* = 2 → ≈95 % CI)

### Satuan dan Referensi  
- ISO GUM 1995 (dan JCGM 100:2008)  
- *Quantitative Chemical Analysis* – D.C. Harris  
""")

# ============================================================
# 3. Cara Perhitungan Manual
# ============================================================
elif page == "Cara Perhitungan Manual":
    st.title("📝 Panduan Perhitungan Manual")
    st.markdown("""
1. **Hitung rata-rata (x̄)**  
2. **Hitung simpangan baku (s)**  
3. **Ketidakpastian Tipe A**  `ua = s / √n`  
4. **Masukkan Ketidakpastian Tipe B (ub)**  
5. **Gabungkan** `uc = √(ua² + ub²)`  
6. **Perluas** `U = k × uc`  
""")
    st.info("Gunakan halaman *Fitur Perhitungan* untuk otomatisasi 👍")

# ============================================================
# 4. FITUR PERHITUNGAN
# ============================================================
elif page == "Fitur Perhitungan":
    st.title("🧮 Kalkulator Ketidakpastian")
    st.write("Masukkan data di bawah. Hasil bisa diunduh sebagai Excel/PDF.")

    # ---------- Input Tipe A ----------
    st.subheader("Tipe A – Data Statistik")
    raw = st.text_area(
        "Masukkan hasil pengukuran (pisahkan dengan koma / comma-separated)",
        "10.12, 10.15, 10.09, 10.11"
    )
    try:
        data = np.array([float(x.strip()) for x in raw.split(",")])
        n = len(data)
        mean = data.mean()
        std  = data.std(ddof=1)
        ua   = std / np.sqrt(n)
    except Exception:
        st.error("⚠️ Data tidak valid.")
        data, mean, std, ua = np.array([]), np.nan, np.nan, np.nan

    if data.size:
        st.write(f"n = {n} x̄ = {mean:.5f} s = {std:.5f} ua = {ua:.5f}")

    # ---------- Input Tipe B ----------
    st.subheader("Tipe B – Data Non-Statistik")
    ub = st.number_input("Masukkan nilai ketidakpastian Tipe B (ub)", value=0.0, min_value=0.0, step=0.0001, format="%.5f")

    # ---------- Gabungan & Diperluas ----------
    st.subheader("Gabungan & Diperluas")
    k = st.selectbox("Faktor cakupan (k)", [1, 2, 3], index=1)
    if np.isnan(ua):
        uc = np.nan
    else:
        uc = np.sqrt(ua**2 + ub**2)
    U = k * uc if not np.isnan(uc) else np.nan

    st.success(f"Ketidakpastian Gabungan (uc): **{uc:.5f}**")
    st.success(f"Ketidakpastian Diperluas  (U): **{U:.5f}** (k = {k})")

    # ---------- Download ----------
    if st.button("🔽 Download Hasil"):
        df = pd.DataFrame({
            "Tanggal": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "n": [n], "Mean": [mean], "s": [std], "ua": [ua],
            "ub": [ub], "uc": [uc], "k": [k], "U": [U]
        })
        excel_bytes = to_excel(df)
        pdf_bytes   = to_pdf(df.to_string(index=False))

        colE, colP = st.columns(2)
        with colE:
            st.download_button(
                label="📊 Excel (.xlsx)",
                data=excel_bytes,
                file_name="hasil_ketidakpastian.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
        with colP:
            st.download_button(
                label="📄 PDF (.pdf)",
                data=pdf_bytes,
                file_name="hasil_ketidakpastian.pdf",
                mime="application/pdf"
            )

# ============================================================
# 5. Kemungkinan Kesalahan
# ============================================================
elif page == "Kemungkinan Kesalahan":
    st.title("⚠️ Kemungkinan Kesalahan")
    st.markdown("""
**Penyebab nilai ketidakpastian besar:**

- Alat ukur belum / tidak dikalibrasi
- Teknik pengukuran tidak konsisten (repeatability rendah)
- Operator berbeda / kurang terlatih
- Lingkungan tidak terkontrol (suhu, kelembapan)
- Pembulatan angka signifikan
- Kesalahan sistematis (bias) & acak (noise)
""")

# ============================================================
# 6. Contoh Soal & Pembahasan
# ============================================================
elif page == "Contoh Soal & Pembahasan":
    st.title("📘 Contoh Soal – Example Problems")

    ex = st.selectbox(
        "Pilih topik contoh soal",
        ("Gravimetri", "Titrasi Asam-Basa", "Spektrofotometri", "Voltametri", "Kromatografi")
    )

    if ex == "Gravimetri":
        st.markdown("""
**Soal**  
Sebuah sampel dianalisis dengan metode gravimetri menghasilkan massa endapan (g):  
`0.3210, 0.3208, 0.3213, 0.3209`.  
Hitung ketidakpastian tipe A, gabungan, dan diperluas (**k=2**).

**Pembahasan Singkat**  
1. Hitung rata-rata → 0.3210 g  
2. Hitung s → 0.0002 g  
3. ua = s / √4 → 1.0 × 10⁻⁴ g  
4. Misal ub = 0.0001 g → uc = √(ua²+ub²)  
5. U = 2 × uc  
""")
    # Topik lain dapat ditambahkan serupa

# ============================================================
# 7. Referensi
# ============================================================
elif page == "Referensi / References":
    st.title("📚 Referensi")
    st.markdown("""
- Daniel C. Harris, *Quantitative Chemical Analysis*  
- BSN, *Metrologi & Ketidakpastian Pengukuran*  
- ISO GUM (JCGM 100:2008)  
- Artikel jurnal terbaru mengenai ketidakpastian kimia analisis  
""")

# ============================================================
# 8. Tentang Aplikasi
# ============================================================
elif page == "Tentang Aplikasi":
    st.title("ℹ️ Tentang Aplikasi")
    st.markdown("""
### Pengembang  
**Mahasiswa POLITEKNIK AKA BOGOR 2025 – Kelompok 3**

| No | Nama                             |
|----|----------------------------------|
| 1  | Aditya Dwika Iannanda            |
| 2  | Dhe Adila Zahra Tubarila         |
| 3  | Naura Amalia Shaliha             |
| 4  | Rizava Apriza                    |
| 5  | Syalwa Fitriani                  |

### Tujuan  
Menyediakan alat edukatif & praktis untuk perhitungan ketidakpastian di laboratorium kimia.

### Kontak  
✉️ ketidakpastian.app@aka.ac.id (fiktif)  
""")

# ============================================================
# 9. Fitur Tambahan
# ============================================================
elif page == "Fitur Tambahan":
    st.title("🧰 Fitur Tambahan (Roadmap)")
    st.markdown("""
- **Download hasil** → ✅ (Excel & PDF)  
- **Simulasi drag-and-drop alat** → 🛠️ dalam pengembangan  
- **Login & histori perhitungan** → 💡 versi sederhana aktif  
- **Mode gelap** → ✅  
""")
