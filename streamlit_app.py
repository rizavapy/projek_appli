import streamlit as st
import numpy as np
import pandas as pd
import math
import datetime as dt

st.set_page_config(page_title="Lab Uncertainty Calculator", page_icon="⚗️")

# --------------------------- SIDEBAR NAVIGATION -----------------------------
st.sidebar.title("⚗️ Uncertainty Toolkit")
page = st.sidebar.radio(
    "Pilih modul",
    ("📊 Combined Uncertainty", "🧪 pH Measurement", "✅ Error Checklist"),
)

# ----------------------------------------------------------------------------
# 1) COMBINED UNCERTAINTY (generic)
# ----------------------------------------------------------------------------
if page == "📊 Combined Uncertainty":
    st.header("Combined & Expanded Uncertainty")

    st.markdown(
        """
        Masukkan hasil pengukuran berulang (Type A) **atau** cukup jumlahkan
        komponen ketidakpastian (Type B).  
        Rumus mengacu ke *Guide to the Expression of Uncertainty in Measurement (GUM)*:
        \\[
            u_c = \\sqrt{\\sum_{i=1}^{n} u_i^2}
        \\]
        dan
        \\[
            U = k\\,u_c \\quad (k = 2\\text{ untuk }95\\%~\\mathrm{CI})
        \\]
        """
    )

    # TYPE A: repetitive data
    st.subheader("Type A – Data Berulang")
    raw = st.text_area(
        "Tempel/ketik data (pisahkan dengan koma, spasi, atau baris baru)", 
        placeholder="10.13 10.11 10.15 10.14"
    )

    col1, col2 = st.columns(2)
    with col1:
        n_dec = st.number_input("Presisi alat (resolusi) / digit", value=0.01)
    with col2:
        k = st.selectbox("Coverage factor *k*", options=[2,3], index=0)

    data = None
    if raw.strip():
        try:
            data = np.fromstring(raw, sep=" ")
        except ValueError:
            st.error("Format data salah 🤔")

    # TYPE B: list of components
    st.subheader("Type B – Komponen Individu")
    st.markdown(
        "Contoh: **Timbangan (±0.005 g), Pipet (±0.03 mL)**, dll. "
        "Input (±)U disini:"
    )
    df = st.experimental_data_editor(
        pd.DataFrame({"Komponen": [], "u (σ atau U/√3)": []}),
        num_rows="dynamic",
        use_container_width=True,
    )

    # ------------------- CALCULATION -------------------
    if st.button("🔍 Hitung Uncertainty"):
        u_components = []

        # Type A
        if data is not None and len(data) > 1:
            s = np.std(data, ddof=1)
            u_stats = s / np.sqrt(len(data))
            # digitisation (half resolution / sqrt(3))
            u_dig = n_dec / math.sqrt(12)
            u_components.extend([u_stats, u_dig])

            st.success(
                f"Type A: s = {s:.5g},  uₛ = {u_stats:.5g}; "
                f"u_digit = {u_dig:.5g}"
            )

        # Type B table
        if not df.empty:
            for val in df["u (σ atau U/√3)"].dropna():
                try:
                    u_components.append(float(val))
                except ValueError:
                    pass

        if u_components:
            uc = math.sqrt(sum(u**2 for u in u_components))
            U = k * uc
            st.markdown(
                f"""
                ### 📈 Hasil  
                * **u<sub>c</sub> (combined)** = `{uc:.5g}`  
                * **U (expanded, k={k})** = `{U:.5g}`
                """
            )
        else:
            st.warning("Tambahkan minimal satu komponen uncertainty!")

# ----------------------------------------------------------------------------
# 2) pH MEASUREMENT MODULE
# ----------------------------------------------------------------------------
elif page == "🧪 pH Measurement":
    st.header("Uncertainty Estimator – pH Meter")

    st.markdown(
        """
        Sumber ketidakpastian umum untuk pH (electrode‐type):  

        | Komponen | Simbol | Default σ |
        |----------|--------|-----------|
        | Resolusi pembacaan | \(u_r\) | 0.01 pH |
        | Kalibrasi buffer | \(u_b\) | 0.01–0.05 pH |
        | Drift ± per jam | \(u_d\) | 0.02 pH |
        | Temperatur (0.003 pH/°C) | \(u_T\) | dihitung |
        """
    )

    col1, col2 = st.columns(2)
    with col1:
        resol = st.number_input("Resolusi display (pH)", 0.01, 0.1, 0.01)
        buffer_unc = st.number_input("Uncertainty buffer (pH)", 0.005, 0.1, 0.02)
        drift = st.number_input("Drift per jam (pH)", 0.0, 0.1, 0.02)
    with col2:
        temp = st.number_input("Suhu ± (°C) seberapa stabil?", 0.1, 5.0, 1.0)
        coeff = 0.003  # pH/°C

    # calculation
    u_r = resol / math.sqrt(12)
    u_b = buffer_unc / math.sqrt(3)
    u_T = coeff * temp / math.sqrt(3)
    u_d = drift / math.sqrt(3)

    u_c_ph = math.sqrt(u_r**2 + u_b**2 + u_T**2 + u_d**2)
    U_ph = 2 * u_c_ph

    st.markdown(
        f"""
        ### 📊 Output  
        * u<sub>r</sub> = {u_r:.4f}  
        * u<sub>b</sub> = {u_b:.4f}  
        * u<sub>T</sub> = {u_T:.4f}  
        * u<sub>d</sub> = {u_d:.4f}  

        **u<sub>c</sub>(pH) = {u_c_ph:.4f}**  
        **U (k=2, 95 %) = {U_ph:.4f}**
        """
    )

# ----------------------------------------------------------------------------
# 3) ERROR CHECKLIST
# ----------------------------------------------------------------------------
else:
    st.header("Lab Error Checklist")

    st.markdown(
        """
        Tandai faktor‐faktor yang *mungkin* terjadi selama percobaan.  
        (Tidak dikalkulasi otomatis—hanya sebagai catatan QA/QC.)
        """
    )

    categories = {
        "Instrumental": [
            "Kalibrasi kedaluwarsa",
            "Drift pembacaan",
            "Suhu tidak stabil",
        ],
        "Prosedural": [
            "Pembilasan buret kurang",
            "Menunda pembacaan titrasi",
            "Kontaminasi gelas ukur",
        ],
        "Human": [
            "Salah catat angka",
            "Salah satuan larutan",
            "Pengenceran ganda tak tercatat",
        ],
    }

    notes = {}
    for cat, items in categories.items():
        st.subheader(cat)
        cols = st.columns(3)
        for i, item in enumerate(items):
            key = f"{cat}-{i}"
            if cols[i % 3].checkbox(item, key=key):
                notes[key] = item

    st.markdown("---")
    if notes:
        st.markdown("### 📝 Catatan kesalahan tercentang:")
        for item in notes.values():
            st.write(f"- {item}")
    else:
        st.info("Belum ada kesalahan yang dicentang.")


# ----------------------- FOOTER -----------------------
st.markdown(
    """
    <hr>
    <center><small>
    Built with ❤️ and Streamlit  
    {:%d %b %Y}
    </small></center>
    """.format(dt.datetime.now()),
    unsafe_allow_html=True,
)
Cara Menjalankan
bash
Salin
Edit
# 1. Instal dependensi
pip install streamlit pandas numpy

# 2. Simpan kode di atas sebagai app_uncertainty.py
# 3. Jalankan
streamlit run app_uncertainty.py
