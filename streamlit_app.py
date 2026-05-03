import streamlit as st
import os

st.set_page_config(
    page_title="Cecilia Snack × INDI 4.0",
    page_icon="🍟",
    layout="wide"
)

html_path = os.path.join(os.path.dirname(__file__), "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

st.components.v1.html(html_content, height=4000, scrolling=True)

<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cecilia Snack and INDI 4.0</title>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {
    --cream: #FFF8EE;
    --warm: #F5E6C8;
    --brown: #3E2000;
    --orange: #E8650A;
    --gold: #C89B2A;
    --green: #1A5C2A;
    --red: #B71C1C;
    --light-green: #E8F5E9;
    --shadow: rgba(62,32,0,0.15);
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--cream);
    color: var(--brown);
  }

  /* ===== HERO ===== */
  .hero {
    background: linear-gradient(135deg, var(--brown) 0%, #6B3500 60%, var(--orange) 100%);
    color: white;
    padding: 60px 40px 50px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }
  .hero::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse at 70% 30%, rgba(232,101,10,0.35) 0%, transparent 65%);
  }
  .hero-badge {
    display: inline-block;
    background: var(--orange);
    color: white;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    padding: 6px 18px;
    border-radius: 2px;
    margin-bottom: 22px;
    text-transform: uppercase;
  }
  .hero h1 {
    font-family: 'Playfair Display', serif;
    font-size: clamp(32px, 6vw, 64px);
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 16px;
    position: relative;
  }
  .hero h1 span { color: #FFD580; }
  .hero p {
    font-size: 16px;
    opacity: 0.85;
    max-width: 580px;
    margin: 0 auto 32px;
    line-height: 1.7;
  }
  .hero-stats {
    display: flex;
    justify-content: center;
    gap: 40px;
    flex-wrap: wrap;
    position: relative;
  }
  .stat-item { text-align: center; }
  .stat-num {
    font-family: 'Playfair Display', serif;
    font-size: 36px;
    font-weight: 900;
    color: #FFD580;
    display: block;
  }
  .stat-label { font-size: 12px; opacity: 0.75; letter-spacing: 1px; }

  /* ===== SECTION TITLES ===== */
  .section {
    padding: 60px 40px;
    max-width: 1100px;
    margin: 0 auto;
  }
  .section-tag {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    letter-spacing: 3px;
    color: var(--orange);
    text-transform: uppercase;
    margin-bottom: 8px;
  }
  .section-title {
    font-family: 'Playfair Display', serif;
    font-size: clamp(24px, 4vw, 40px);
    font-weight: 900;
    color: var(--brown);
    margin-bottom: 10px;
  }
  .section-sub {
    font-size: 15px;
    color: #7A5C3A;
    margin-bottom: 40px;
    max-width: 600px;
    line-height: 1.7;
  }
  .divider {
    height: 3px;
    background: linear-gradient(90deg, var(--orange), transparent);
    width: 60px;
    margin-bottom: 16px;
  }

  /* ===== BEFORE AFTER ===== */
  .ba-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 24px;
    margin-bottom: 40px;
  }
  @media(max-width:640px){ .ba-grid{ grid-template-columns:1fr; } }
  .ba-card {
    border-radius: 16px;
    padding: 32px;
    position: relative;
    overflow: hidden;
  }
  .ba-card.before {
    background: #FFF0F0;
    border: 2px solid #FFCDD2;
  }
  .ba-card.after {
    background: var(--light-green);
    border: 2px solid #A5D6A7;
  }
  .ba-label {
    font-family: 'Space Mono', monospace;
    font-size: 10px;
    letter-spacing: 3px;
    font-weight: 700;
    margin-bottom: 18px;
    display: inline-block;
    padding: 4px 12px;
    border-radius: 2px;
  }
  .before .ba-label { background: var(--red); color: white; }
  .after .ba-label { background: var(--green); color: white; }
  .ba-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 22px;
    margin-bottom: 20px;
  }
  .ba-list { list-style: none; }
  .ba-list li {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 10px 0;
    border-bottom: 1px solid rgba(0,0,0,0.06);
    font-size: 14px;
    line-height: 1.5;
  }
  .ba-list li:last-child { border-bottom: none; }
  .icon { font-size: 18px; flex-shrink: 0; margin-top: 1px; }

  /* ===== INDI SCORE CHART ===== */
  .score-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 20px;
  }
  .score-card {
    background: white;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 4px 20px var(--shadow);
    border-left: 4px solid var(--orange);
  }
  .score-card h4 {
    font-size: 12px;
    color: #7A5C3A;
    margin-bottom: 12px;
    line-height: 1.4;
    font-weight: 500;
  }
  .score-bar-wrap {
    background: #F0E6D6;
    border-radius: 99px;
    height: 8px;
    margin-bottom: 10px;
    overflow: hidden;
  }
  .score-bar {
    height: 100%;
    border-radius: 99px;
    background: linear-gradient(90deg, var(--orange), var(--gold));
    transition: width 1s ease;
  }
  .score-nums {
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    font-family: 'Space Mono', monospace;
  }
  .score-before { color: var(--red); }
  .score-after { color: var(--green); font-weight: 700; }

  /* ===== PACKAGING MOCKUPS ===== */
  .products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 24px;
  }
  .product-card {
    background: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 8px 32px var(--shadow);
    transition: transform 0.3s ease;
  }
  .product-card:hover { transform: translateY(-6px); }
  .product-top {
    height: 180px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 64px;
    position: relative;
  }
  .product-tag-halal {
    position: absolute;
    top: 12px; right: 12px;
    background: var(--green);
    color: white;
    font-size: 9px;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 3px 8px;
    border-radius: 3px;
  }
  .product-tag-pirt {
    position: absolute;
    top: 12px; left: 12px;
    background: var(--brown);
    color: white;
    font-size: 9px;
    font-weight: 700;
    padding: 3px 8px;
    border-radius: 3px;
  }
  .product-body { padding: 20px; }
  .product-name {
    font-family: 'Playfair Display', serif;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 4px;
  }
  .product-brand {
    font-size: 12px;
    color: var(--orange);
    font-weight: 500;
    margin-bottom: 14px;
    font-family: 'Space Mono', monospace;
  }
  .product-price {
    font-size: 20px;
    font-weight: 700;
    color: var(--brown);
    margin-bottom: 14px;
  }
  .product-price span { font-size: 13px; font-weight: 400; color: #999; text-decoration: line-through; margin-left: 6px; }
  .qr-section {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px;
    background: var(--cream);
    border-radius: 10px;
    margin-bottom: 10px;
  }
  .qr-box {
    width: 52px;
    height: 52px;
    background: white;
    border: 2px solid var(--brown);
    border-radius: 6px;
    display: grid;
    grid-template-columns: repeat(5,1fr);
    gap: 1px;
    padding: 4px;
    flex-shrink: 0;
  }
  .qr-dot { border-radius: 1px; }
  .qr-dot.on { background: var(--brown); }
  .qr-dot.off { background: transparent; }
  .qr-info { flex: 1; }
  .qr-info p { font-size: 11px; color: #7A5C3A; line-height: 1.5; }
  .qr-info strong { font-size: 12px; color: var(--brown); }
  .barcode-wrap {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 10px;
    background: white;
    border-radius: 8px;
    border: 1px solid #E8DDD0;
  }
  .barcode-lines {
    display: flex;
    gap: 2px;
    height: 28px;
    margin-bottom: 4px;
  }
  .b-line {
    width: 2px;
    background: var(--brown);
    border-radius: 1px;
  }
  .b-line.thin { width: 1px; opacity: 0.6; }
  .b-line.thick { width: 3px; }
  .barcode-num {
    font-family: 'Space Mono', monospace;
    font-size: 9px;
    color: var(--brown);
    letter-spacing: 2px;
  }

  /* ===== FLOW STEPS ===== */
  .steps-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0;
    margin-bottom: 40px;
    background: white;
    border-radius: 16px;
    overflow: hidden;
    box-shadow: 0 8px 32px var(--shadow);
  }
  .step {
    flex: 1;
    min-width: 160px;
    padding: 28px 24px;
    text-align: center;
    position: relative;
    border-right: 1px solid #F0E6D6;
  }
  .step:last-child { border-right: none; }
  .step-num {
    font-family: 'Playfair Display', serif;
    font-size: 40px;
    font-weight: 900;
    color: var(--warm);
    line-height: 1;
    margin-bottom: 8px;
  }
  .step-icon { font-size: 28px; margin-bottom: 10px; }
  .step-title {
    font-weight: 700;
    font-size: 14px;
    color: var(--brown);
    margin-bottom: 6px;
  }
  .step-desc { font-size: 12px; color: #7A5C3A; line-height: 1.5; }

  /* ===== QR LANDING MOCKUP ===== */
  .phone-mockup {
    width: 280px;
    margin: 0 auto;
    background: var(--brown);
    border-radius: 36px;
    padding: 16px;
    box-shadow: 0 24px 64px rgba(62,32,0,0.4);
  }
  .phone-screen {
    background: var(--cream);
    border-radius: 24px;
    overflow: hidden;
    min-height: 520px;
  }
  .phone-notch {
    background: var(--brown);
    height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .phone-notch-dot { width: 8px; height: 8px; background: #555; border-radius: 50%; }
  .phone-header {
    background: linear-gradient(135deg, var(--brown), var(--orange));
    color: white;
    padding: 20px 16px 16px;
    text-align: center;
  }
  .phone-header .logo { font-family: 'Playfair Display', serif; font-size: 20px; font-weight: 900; }
  .phone-header .tagline { font-size: 10px; opacity: 0.8; margin-top: 2px; }
  .phone-product-img {
    font-size: 56px;
    text-align: center;
    padding: 20px;
    background: var(--warm);
  }
  .phone-content { padding: 16px; }
  .phone-name { font-family: 'Playfair Display', serif; font-size: 18px; font-weight: 900; margin-bottom: 4px; }
  .phone-price { font-size: 22px; font-weight: 700; color: var(--orange); margin-bottom: 12px; }
  .phone-info-row { display: flex; gap: 8px; flex-wrap: wrap; margin-bottom: 12px; }
  .phone-chip {
    font-size: 10px; font-weight: 600;
    padding: 4px 10px; border-radius: 20px;
  }
  .chip-green { background: var(--light-green); color: var(--green); }
  .chip-orange { background: #FFF3E0; color: var(--orange); }
  .phone-btn {
    display: block;
    background: var(--orange);
    color: white;
    text-align: center;
    padding: 12px;
    border-radius: 10px;
    font-weight: 700;
    font-size: 13px;
    margin-bottom: 8px;
    text-decoration: none;
  }
  .phone-btn.outline {
    background: transparent;
    border: 2px solid var(--brown);
    color: var(--brown);
  }

  /* ===== PRIORITY CARDS ===== */
  .priority-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
    gap: 20px;
    margin-bottom: 40px;
  }
  .priority-card {
    background: white;
    border-radius: 14px;
    padding: 24px;
    box-shadow: 0 4px 20px var(--shadow);
    border-top: 4px solid var(--orange);
    display: flex;
    flex-direction: column;
  }
  .priority-num {
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: var(--orange);
    letter-spacing: 2px;
    margin-bottom: 8px;
  }
  .priority-card h3 {
    font-family: 'Playfair Display', serif;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 10px;
  }
  .priority-card p { font-size: 13px; color: #7A5C3A; line-height: 1.6; flex: 1; }
  .priority-status {
    margin-top: 14px;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1px;
    padding: 4px 10px;
    border-radius: 3px;
    display: inline-block;
    width: fit-content;
  }
  .status-now { background: #FFF3E0; color: var(--orange); }
  .status-next { background: #E8F5E9; color: var(--green); }

  /* ===== FOOTER ===== */
  .footer {
    background: var(--brown);
    color: rgba(255,255,255,0.7);
    padding: 40px;
    text-align: center;
  }
  .footer strong { color: #FFD580; font-family: 'Playfair Display', serif; }
  .footer p { font-size: 13px; line-height: 1.8; }

  /* ===== BG SECTIONS ===== */
  .bg-warm { background: var(--warm); }
  .bg-white { background: white; }
  .full-section { padding: 60px 40px; }
  .full-section .inner { max-width: 1100px; margin: 0 auto; }
</style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="hero-badge">Proyek TI — INDI 4.0</div>
  <h1>Cecilia Snack<br><span>Menuju Digital</span></h1>
  <p>Digitalisasi Label QR Code pada Kemasan Produk UMKM sebagai Solusi Peningkatan Indeks INDI 4.0</p>
  <div class="hero-stats">
    <div class="stat-item">
      <span class="stat-num">4</span>
      <span class="stat-label">Produk Didigitalisasi</span>
    </div>
    <div class="stat-item">
      <span class="stat-num">+62%</span>
      <span class="stat-label">Peningkatan Skor INDI</span>
    </div>
    <div class="stat-item">
      <span class="stat-num">6</span>
      <span class="stat-label">Indikator Tersentuh</span>
    </div>
    <div class="stat-item">
      <span class="stat-num">QRIS</span>
      <span class="stat-label">Sudah Digital</span>
    </div>
  </div>
</div>

<!-- BEFORE AFTER -->
<div class="section">
  <div class="section-tag">Analisis Kondisi</div>
  <div class="divider"></div>
  <h2 class="section-title">Sebelum vs Sesudah Digitalisasi</h2>
  <p class="section-sub">Perbandingan kondisi operasional Cecilia Snack sebelum dan sesudah implementasi solusi digitalisasi QR Code.</p>

  <div class="ba-grid">
    <div class="ba-card before">
      <span class="ba-label">Kondisi Sebelum</span>
      <h3>❌ Masih Manual</h3>
      <ul class="ba-list">
        <li><span class="icon">🏷️</span><span>Harga ditempel manual dengan kertas tulisan tangan</span></li>
        <li><span class="icon">📦</span><span>Kemasan plastik polos tanpa identitas produk</span></li>
        <li><span class="icon">🔲</span><span>Tidak ada barcode maupun QR code di kemasan</span></li>
        <li><span class="icon">📒</span><span>Pencatatan keuangan masih di buku tulis manual</span></li>
        <li><span class="icon">📣</span><span>Pemasaran hanya dari mulut ke mulut</span></li>
        <li><span class="icon">🌐</span><span>Tidak ada kehadiran digital sama sekali</span></li>
      </ul>
    </div>
    <div class="ba-card after">
      <span class="ba-label">Sesudah Solusi</span>
      <h3>✅ Serba Terdigitalisasi</h3>
      <ul class="ba-list">
        <li><span class="icon">📱</span><span>QR code di kemasan terhubung ke halaman produk digital</span></li>
        <li><span class="icon">💳</span><span>Harga tampil otomatis di halaman web saat scan</span></li>
        <li><span class="icon">🔢</span><span>Barcode produk tersedia untuk sistem inventori</span></li>
        <li><span class="icon">📊</span><span>Data scan otomatis tersimpan untuk analitik</span></li>
        <li><span class="icon">📲</span><span>Konsumen bisa pesan WhatsApp langsung dari QR</span></li>
        <li><span class="icon">🏅</span><span>Label HALAL dan nomor PIRT terpasang resmi</span></li>
      </ul>
    </div>
  </div>
</div>

<!-- INDI SCORE -->
<div class="bg-warm full-section">
  <div class="inner">
    <div class="section-tag">Evaluasi INDI 4.0</div>
    <div class="divider"></div>
    <h2 class="section-title">Peningkatan Skor INDI 4.0</h2>
    <p class="section-sub">Perbandingan skor per indikator sebelum dan sesudah implementasi solusi digitalisasi.</p>
    <div class="score-grid">
      <div class="score-card">
        <h4>Identifikasi Produk Digital</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:80%"></div></div>
        <div class="score-nums">
          <span class="score-before">Sebelum: 1/5</span>
          <span class="score-after">Sesudah: 4/5</span>
        </div>
      </div>
      <div class="score-card">
        <h4>Kemasan &amp; Branding Digital</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:60%"></div></div>
        <div class="score-nums">
          <span class="score-before">Sebelum: 1/5</span>
          <span class="score-after">Sesudah: 3/5</span>
        </div>
      </div>
      <div class="score-card">
        <h4>Pemasaran Digital</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:60%"></div></div>
        <div class="score-nums">
          <span class="score-before">Sebelum: 1/5</span>
          <span class="score-after">Sesudah: 3/5</span>
        </div>
      </div>
      <div class="score-card">
        <h4>Transparansi Harga</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:80%"></div></div>
        <div class="score-nums">
          <span class="score-before">Sebelum: 1/5</span>
          <span class="score-after">Sesudah: 4/5</span>
        </div>
      </div>
      <div class="score-card">
        <h4>Ketelusuran Produk</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:60%"></div></div>
        <div class="score-nums">
          <span class="score-before">Sebelum: 0/5</span>
          <span class="score-after">Sesudah: 3/5</span>
        </div>
      </div>
      <div class="score-card">
        <h4>Pencatatan Digital</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:40%"></div></div>
        <div class="score-nums">
          <span class="score-before">Sebelum: 1/5</span>
          <span class="score-after">Sesudah: 2/5</span>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- ALUR SISTEM -->
<div class="bg-white full-section">
  <div class="inner">
    <div class="section-tag">Sistem QR Code</div>
    <div class="divider"></div>
    <h2 class="section-title">Alur 4 Langkah Digitalisasi</h2>
    <p class="section-sub">Cara kerja sistem QR Code dari kemasan produk hingga konsumen mendapat informasi lengkap.</p>
    <div class="steps-row">
      <div class="step">
        <div class="step-num">01</div>
        <div class="step-icon">🎨</div>
        <div class="step-title">Desain Label</div>
        <p class="step-desc">QR code + barcode + info produk didesain dan dicetak di kemasan</p>
      </div>
      <div class="step">
        <div class="step-num">02</div>
        <div class="step-icon">📦</div>
        <div class="step-title">Tempel Kemasan</div>
        <p class="step-desc">Label ditempelkan pada setiap produk Cecilia Snack yang dijual</p>
      </div>
      <div class="step">
        <div class="step-num">03</div>
        <div class="step-icon">📱</div>
        <div class="step-title">Konsumen Scan</div>
        <p class="step-desc">Pembeli scan QR dengan kamera HP, langsung terbuka halaman produk</p>
      </div>
      <div class="step">
        <div class="step-num">04</div>
        <div class="step-icon">🛒</div>
        <div class="step-title">Aksi Digital</div>
        <p class="step-desc">Konsumen bisa lihat harga, info produk, dan order via WhatsApp</p>
      </div>
    </div>
  </div>
</div>

<!-- MOCKUP KEMASAN -->
<div class="section">
  <div class="section-tag">Mockup Produk</div>
  <div class="divider"></div>
  <h2 class="section-title">Desain Kemasan Digital</h2>
  <p class="section-sub">4 produk utama Cecilia Snack dengan label QR code, barcode, sertifikasi HALAL dan nomor PIRT.</p>
  <div class="products-grid">

    <!-- Keripik Singkong -->
    <div class="product-card">
      <div class="product-top" style="background:linear-gradient(135deg,#FFF3E0,#FFE0B2);">
        🥔
        <span class="product-tag-halal">HALAL</span>
        <span class="product-tag-pirt">PIRT</span>
      </div>
      <div class="product-body">
        <div class="product-name">Keripik Singkong</div>
        <div class="product-brand">CECILIA SNACK · 250g</div>
        <div class="prod

        
