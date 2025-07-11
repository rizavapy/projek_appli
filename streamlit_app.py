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
        Masukkan hasil pengukuran berulang (Type A) **atau** komponen ketidakpastian (Type B).

        Rumus GUM:  
        \\[
            u_c = \\sqrt{\\sum_{i=1}^{n} u_i^2}, \\quad
            U = k\\,u_c \\quad (k=2\\:≈95\\%\\,CI)
        \\]
        """
    )

    # TYPE A: repetitive data
    st.subheader("Type A – Data Berulang")
    raw = st.text_area(
        "Tempel/ketik data (pisahkan dengan koma, spasi, atau baris baru)",
        placeholder="10.13 10.11 10.15 10.14",
    )

    col1, col2 = st.columns(2)
    with col1:
        n_dec = st.number_input("Resolusi alat / digit", value=0.01)
    with col2:
        k = st.selectbox("Coverage factor k", options=[2, 3], index=0)

    data = None
    if raw.strip():
        try:
            data = np.fromstring(raw, sep=" ")
        except ValueError:
            st.error("Format data salah 🤔")

    # TYPE B: list of components
    st.subheader("Type B – Komponen Individu")
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
            u_dig = n_dec / math.sqrt(12)  # half‑digit / √3
            u_components.extend([u_stats, u_dig])

            st.success(
                f"Type A → s={s:.5g},  uₛ={u_stats:.5g},  u_digit={u_dig:.5g}"
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
                * u<sub>c</sub> = `{uc:.5g}`  
                * U (k={k}) = `{U:.5g}`
                """,
                unsafe_allow_html=True,
            )
        else:
            st.warning("Tambahkan minimal satu komponen uncertainty!")

# ----------------------------------------------------------------------------
# 2) pH MEASUREMENT MODULE
# ----------------------------------------------------------------------------
elif page == "🧪 pH Measurement":
    st.header("Uncertainty Estimator – pH Meter")

    col1, col2 = st.columns(2)
    with col1:
        resol = st.number_input("Resolusi display (pH)", 0.01, 0.1, 0.01)
        buffer_unc = st.number_input("Uncertainty buffer (pH)", 0.005, 0.1, 0.02)
        drift = st.number_input("Drift per jam (pH)", 0.0, 0.1, 0.02)
    with col2:
        temp = st.number_input("Suhu ± (°C)", 0.1, 5.0, 1.0)
        coeff = 0.003  # pH per °C

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
        u<sub>r</sub>={u_r:.4f},  u<sub>b</sub>={u_b:.4f},  
        u<sub>T</sub>={u_T:.4f},  u<sub>d</sub>={u_d:.4f}  

        **u<sub>c</sub>(pH) = {u_c_ph:.4f}**  
        **U (k=2) = {U_ph:.4f}**
        """,
        unsafe_allow_html=True,
    )

# ----------------------------------------------------------------------------
# 3) ERROR CHECKLIST
# ----------------------------------------------------------------------------
else:
    st.header("Lab Error Checklist")

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
            "Salah satuan lar
