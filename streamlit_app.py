import streamlit as st
import math

st.set_page_config(page_title="Kalkulator Ketidakpastian Praktikum", page_icon="🧪")

st.title("🧪 Kalkulator Nilai Ketidakpastian Praktikum")
st.markdown("Hitung ketidakpastian berdasarkan nilai pH, galat, dan kesalahan laboratorium.")

# -------------------- INPUT --------------------
st.header("📥 Input Data")

ph_value = st.number_input("Nilai pH hasil pengukuran:", min_value=0.0, max_value=14.0, value=7.00, step=0.01)
alat_resolusi = st.number_input("Resolusi alat (misalnya pH meter = 0.01):", min_value=0.001, value=0.01)
jumlah_pengulangan = st.number_input("Jumlah pengulangan (n):", min_value=1, value=3)

pengukuran = []
st.write("Masukkan hasil pengukuran berulang (n kali):")
for i in range(jumlah_pengulangan):
    val = st.number_input(f"Hasil ke-{i+1}", key=f"rep{i}", format="%.3f")
    pengukuran.append(val)

galat_eksternal = st.number_input("Estimasi kesalahan lain (human error, suhu, dll) - opsional:", min_value=0.0, value=0.0)

# -------------------- PERHITUNGAN --------------------
st.header("📊 Hasil Perhitungan Ketidakpastian")

if st.button("Hitung Ketidakpastian"):

    # 1. Type A Uncertainty (standard deviation of repeated measurements)
    rata2 = sum(pengukuran) / jumlah_pengulangan
    varians = sum((x - rata2) ** 2 for x in pengukuran) / (jumlah_pengulangan - 1 if jumlah_pengulangan > 1 else 1)
    simpangan_baku = math.sqrt(varians)
    u_type_a = simpangan_baku / math.sqrt(jumlah_pengulangan)

    # 2. Type B Uncertainty (alat + galat eksternal)
    u_resolusi = alat_resolusi / math.sqrt(3)
    u_lain = galat_eksternal / math.sqrt(3) if galat_eksternal > 0 else 0

    # 3. Combine all uncertainty
    u_c = math.sqrt(u_type_a ** 2 + u_resolusi ** 2 + u_lain ** 2)

    # 4. Expanded uncertainty (k = 2 untuk 95% confidence level)
    U = 2 * u_c

    # -------------------- OUTPUT --------------------
    st.success("✅ Ketidakpastian Berhasil Dihitung!")
    st.write(f"📌 Rata-rata pH: **{rata2:.3f}**")
    st.write(f"📉 Ketidakpastian Tipe A: **±{u_type_a:.3f}**")
    st.write(f"🛠️ Ketidakpastian Tipe B (resolusi): **±{u_resolusi:.3f}**")
    if galat_eksternal > 0:
        st.write(f"📦 Ketidakpastian Eksternal Tambahan: **±{u_lain:.3f}**")
    st.write(f"📈 Ketidakpastian Kombinasi: **±{u_c:.3f}**")
    st.write(f"🧾 Ketidakpastian Diperluas (k=2): **±{U:.3f}**")
    st.markdown(f"**📄 Hasil Akhir:** `pH = {rata2:.3f} ± {U:.3f} (k=2)`")

    st.markdown("---")
    st.caption("Perhitungan mengikuti panduan GUM & ISO/IEC 17025")
