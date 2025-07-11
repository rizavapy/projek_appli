import streamlit as st

# ────────── PAGE CONFIG ──────────
st.set_page_config(
    page_title="Beranda • Analis Kimia",
    page_icon="🧪",
    layout="wide"
)

# ────────── LANGUAGE STATE ──────────
if "lang" not in st.session_state:
    st.session_state.lang = "id"

def switch_lang():
    st.session_state.lang = "en" if st.session_state.lang == "id" else "id"

# ────────── HEADER ──────────
col_logo, col_title = st.columns([1, 5])
with col_logo:
    st.image("https://cdn-icons-png.flaticon.com/512/3163/3163845.png", width=72)
with col_title:
    st.title("🧪 Lab Virtual Analisis Kimia")

# toggle language
if st.session_state.lang == "id":
    st.button("🌐 Translate to English", on_click=switch_lang)
else:
    st.button("🇮🇩 Terjemahkan ke Bahasa Indonesia", on_click=switch_lang)

st.markdown("---")

# ────────── CONTENT ──────────
txt_id = {
    "welcome": "Selamat datang di portal pembelajaran dan kalkulasi **Analisis Kimia**. "
               "Di sini kamu bisa mempelajari konsep dasar kimia, memahami cara menghitung "
               "ketidakpastian (uncertainty) menurut *Guide to the Expression of Uncertainty "
               "in Measurement* (GUM), dan menggunakan alat hitung interaktif.",
    "chem_basics": "📚 **Dasar‑dasar Kimia Penting**",
    "mol": "**Mol & MR**   *1 mol = 6,022 × 10²³ partikel.* Hitung mol dengan `n = m/Mr`.",
    "conc": "**Konsentrasi**   `M = n/V`; variasinya **ppm, %w/v, molality, formality**.",
    "ph": "**pH & pKa**   `pH = −log[H⁺]`. Buffer mengikuti persamaan Henderson‑Hasselbalch.",
    "stkm": "**Stoikiometri**   Gunakan persamaan tersetar untuk konversi reaktan‑produk.",
    "unc_head": "🎯 **Ketidakpastian Pengukuran**",
    "unc_body": (
        "Setiap nilai analitik **harus** disertai ketidakpastian agar dapat dibandingkan.\n\n"
        "**Langkah GUM (ringkas):**\n"
        "1. *Definisi* → Besaran measurand & model matematik\n"
        "2. *Identifikasi sumber* Type A (statistik) & Type B (non‑statistik)\n"
        "3. *Kuantifikasi* Konversi semua ke simpangan baku `uᵢ`\n"
        "4. *Propagasi* `u_c = √Σ(uᵢ·∂f/∂xᵢ)²` atau metode Monte‑Carlo\n"
        "5. *Ekspansi* `U = k·u_c` (k=2 ≈ 95 % CI)\n"
        "6. *Pelaporan* `x ± U (k=2)` dengan satuan & pembulatan sig‑fig sesuai GUM‑S1"
    ),
    "article_head": "🔗 **Ringkasan Artikel MK Training**",
    "article": (
        "Artikel menekankan pentingnya menghitung ketidakpastian **sebelum** hasil dilaporkan. "
        "Beberapa poin kunci:\n"
        "- Laboratorium terakreditasi *wajib* mendeklarasikan uncertainty.\n"
        "- Ketidakpastian *bukan* error—ia adalah rentang keyakinan.\n"
        "- Dokumen ISO/IEC 17025 juga mensyaratkan pernyataan `U`.\n\n"
        "➡️ [Lihat artikel lengkap](https://mktraining.co.id/blog/ketidakpastian-pengukuran-dalam-analisis-kimia/)"
    ),
    "footer": "Dibuat dengan ❤️ oleh Mahasiswa Analis Kimia • 2025"
}

txt_en = {
    "welcome": "Welcome to the **Chemical Analysis** learning & calculator portal. "
               "Here you can review core chemistry concepts, learn how to compute "
               "measurement uncertainty according to the *Guide to the Expression "
               "of Uncertainty in Measurement* (GUM), and try interactive tools.",
    "chem_basics": "📚 **Essential Chemistry Basics**",
    "mol": "**Mole & MR**   *1 mol = 6.022 × 10²³ particles.* Compute mole via `n = m/Mr`.",
    "conc": "**Concentration**   `M = n/V`; variants include **ppm, %w/v, molality, formality**.",
    "ph": "**pH & pKa**   `pH = −log[H⁺]`. Buffers follow the Henderson‑Hasselbalch equation.",
    "stkm": "**Stoichiometry**   Use the balanced equation to convert reactants/products.",
    "unc_head": "🎯 **Measurement Uncertainty**",
    "unc_body": (
        "Every analytical value **must** be accompanied by uncertainty to be comparable.\n\n"
        "**GUM workflow (concise):**\n"
        "1. *Definition* → Measurand & mathematical model\n"
        "2. *Source ID* Type A (stat.) & Type B (non‑stat.)\n"
        "3. *Quantification* Convert all to standard deviations `uᵢ`\n"
        "4. *Propagation* `u_c = √Σ(uᵢ·∂f/∂xᵢ)²` or Monte‑Carlo\n"
        "5. *Expansion* `U = k·u_c` (k=2 ≈ 95 % CI)\n"
        "6. *Report* `x ± U (k=2)` with units & sig‑fig rounding (GUM‑S1)"
    ),
    "article_head": "🔗 **MK Training Article Summary**",
    "article": (
        "The article stresses that uncertainty must be declared **before** releasing results. "
        "Key points:\n"
        "- Accredited labs *must* state uncertainty.\n"
        "- Uncertainty is *not* error—it is a confidence band.\n"
        "- ISO/IEC 17025 requires declaration of `U`.\n\n"
        "➡️ [Read full article](https://mktraining.co.id/blog/ketidakpastian-pengukuran-dalam-analisis-kimia/)"
    ),
    "footer": "Made with ❤️ by Chemical Analysis Student • 2025"
}

T = txt_id if st.session_state.lang == "id" else txt_en

st.info(T["welcome"])

# ────────── CHEM BASICS ──────────
with st.expander(T["chem_basics"], expanded=True):
    st.markdown(f"- {T['mol']}")
    st.markdown(f"- {T['conc']}")
    st.markdown(f"- {T['ph']}")
    st.markdown(f"- {T['stkm']}")

# ────────── UNCERTAINTY SECTION ──────────
st.markdown("---")
st.subheader(T["unc_head"])
st.markdown(T["unc_body"])

# ────────── ARTICLE SUMMARY ──────────
st.markdown("---")
st.subheader(T["article_head"])
st.markdown(T["article"])

# ────────── FOOTER ──────────
st.markdown("---")
st.caption(T["footer"])
