# ==============================================================
#  Aplikasi Perhitungan Ketidakpastian  –  Kelompok 3  AKA Bogor
#  Revisi: support kalibrasi alat + download Excel & PDF
# ==============================================================

import streamlit as st
import numpy as np
import pandas as pd
from io import BytesIO
from datetime import datetime

# ---------- konfigurasi & tema gelap --------------------------
st.set_page_config(page_title="Ketidakpastian", layout="wide")
if "dark" not in st.session_state:  # toggle tema
    st.session_state.dark = False
if st.sidebar.checkbox("🌙 Mode Gelap", value=st.session_state.dark):
    st.session_state.dark = True
    st.markdown(
        "<style>body, .stApp{background:#0e1117;color:#eee;}hr{color:#555}</style>",
        unsafe_allow_html=True
    )
else:
    st.session_state.dark = False

# ---------- utilitas download ---------------------------------
def df_to_excel(df: pd.DataFrame) -> bytes:
    buf = BytesIO()
    with pd.ExcelWriter(buf, engine="xlsxwriter") as w:
        df.to_excel(w, index=False, sheet_name="Hasil")
    return buf.getvalue()

def text_to_pdf(s: str) -> bytes:            # ringkasan → PDF
    try:
        from fpdf import FPDF                # pip install fpdf
    except ImportError:
        return s.encode()
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=11)
    for line in s.splitlines():
        pdf.multi_cell(0, 8, txt=line)
    return pdf.output(dest="S").encode("latin-1")

# ---------- navigasi ------------------------------------------
menu = st.sidebar.radio(
    "Navigasi",
    ("Beranda", "Dasar Teori", "Perhitungan", "Kesalahan", "Contoh Soal Kimia Fisik",
     "Referensi", "Tentang", "Roadmap")
)

# ==============================================================
# 1. Beranda
# ==============================================================
if menu == "Beranda":
    st.title("🔬 Aplikasi Ketidakpastian Pengukuran")
    st.write("""
Aplikasi ini membantu menghitung **nilai ketidakpastian** (Tipe A & Tipe B) \
termasuk **ketidakpastian kalibrasi alat**, dan mengekspor hasil ke **Excel/PDF**.
""")
    st.success("Selamat datang – Happy calculating!")

# ==============================================================
# 2. Dasar Teori
# ==============================================================
elif menu == "Dasar Teori":
    st.title("📚 Dasar Teori")
    st.markdown("""
**Tipe A** → data statistik *(repeatability)*  
**Tipe B** → data non-statistik (spesifikasi alat, sertifikat kalibrasi)  

$$u_c = \\sqrt{u_A^2 + u_B^2}$$  
$$U = k \\times u_c$$
""")

# ==============================================================
# 3. Perhitungan
# ==============================================================
elif menu == "Perhitungan":
    st.title("🧮 Kalkulator Ketidakpastian dengan Kalibrasi")

    # ----------- DATA TIPE A --------------
    st.subheader("Data Statistik (Tipe A)")
    A_raw = st.text_area("Masukkan data (pisahkan dengan koma)", "10.12, 10.15, 10.09, 10.11")
    try:
        A_vals = np.array([float(x) for x in A_raw.split(",")])
        n = len(A_vals)
        mean = A_vals.mean()
        s = A_vals.std(ddof=1)
        uA = s / np.sqrt(n)
        st.write(f"n = {n},  x̄ = {mean:.5f},  s = {s:.5f},  uA = {s/np.sqrt(n):.5f}")
    except Exception:
        st.error("Data tidak valid")
        uA = np.nan

    # ----------- DATA TIPE B --------------
    st.subheader("Data Kalibrasi / Tipe B")
    ub_manual = st.number_input("Masukkan uB manual (jika tidak upload)", 0.0, step=0.0001, format="%.5f")

    uploaded = st.file_uploader("Atau upload file Excel kalibrasi (kolom 'uB')", type=["xlsx"])
    if uploaded:
        try:
            df_cal = pd.read_excel(uploaded)
            ub = float(df_cal["uB"].iloc[0])
            st.success(f"uB dari file: {ub:.5f}")
        except Exception:
            st.error("File tidak sesuai – pakai kolom bernama 'uB'")
            ub = ub_manual
    else:
        ub = ub_manual

    # ----------- GABUNG & EXPANDED -----------
    st.subheader("Gabungan & Diperluas")
    k = st.selectbox("Faktor k", [1, 2, 3], index=1)
    if not np.isnan(uA):
        uc = np.sqrt(uA**2 + ub**2)
        U = k * uc
        st.success(f"uc = {uc:.5f} |  U = {U:.5f}")
    else:
        uc = U = np.nan

    # ----------- DOWNLOAD HASIL -------------
    if st.button("📥 Unduh Excel + PDF"):
        hasil = pd.DataFrame({
            "Tanggal": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "Mean": [mean], "s": [s], "uA": [uA],
            "uB": [ub], "uc": [uc], "k": [k], "U": [U]
        })
        st.download_button("Excel", df_to_excel(hasil),
                           "hasil_ketidakpastian.xlsx",
                           "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        ringkas = hasil.to_string(index=False)
        st.download_button("PDF", text_to_pdf(ringkas),
                           "hasil_ketidakpastian.pdf", "application/pdf")

# ==============================================================
# 4. Kesalahan
# ==============================================================
elif menu == "Kesalahan":
    st.title("⚠️ Sumber Kesalahan Umum")
    st.write("- Alat belum dikalibrasi\n- Operator berbeda\n- Suhu/kelembapan berubah")

# ==============================================================
# 5. Contoh Soal Kimia Fisik
# ==============================================================
elif menu == "Contoh Soal Kimia Fisik":
    st.title("📘 Contoh Soal – Praktikum Kimia Fisik")

    topik = st.selectbox("Pilih topik", ("Kalorimetri", "Viskositas", "Laju Reaksi"))
    if topik == "Kalorimetri":
        st.markdown("""
**Soal**  
Dilakukan penentuan kapasitas kalor kalorimeter. Empat kali percobaan menghasilkan ΔT (°C):  
`1.925, 1.932, 1.918, 1.929`  
Hitung uA, asumsikan uB (kalibrasi termometer) = 0.005 °C, hitung U (k = 2).

**Jawaban singkat**  
1. x̄ = 1.926 °C, s = 0.006 °C → uA = 0.003 °C  
2. uB = 0.005 °C (sertifikat)  
3. uc = √(0.003² + 0.005²) = 0.006 °C  
4. U = 2 × 0.006 = 0.012 °C
""")
    elif topik == "Viskositas":
        st.markdown("Contoh soal viskositas … (isi sendiri)")
    else:
        st.markdown("Contoh soal laju reaksi … (isi sendiri)")

# ==============================================================
# 6. Referensi
# ==============================================================
elif menu == "Referensi":
    st.title("📚 Referensi")
    st.write("* ISO GUM, Harris QCA, dll.*")

# ==============================================================
# 7. Tentang
# ==============================================================
elif menu == "Tentang":
    st.title("ℹ️ Tentang")
    st.write("""
Kelompok 3 – POLITEKNIK AKA Bogor 2025  
Aditya • Dhe Adila • Naura • Rizava • Syalwa
""")

# ==============================================================
# 8. Roadmap
# ==============================================================
else:
    st.title("🛠️ Roadmap")
    st.write("- Drag-and-drop simulasi\n- Database histori pengguna\n- API kalibrasi otomatis")
