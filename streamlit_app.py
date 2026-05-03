import streamlit as st

st.set_page_config(
    page_title="Cecilia Snack x INDI 4.0",
    page_icon="🍟",
    layout="wide"
)

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Cecilia Snack x INDI 4.0</title>
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
}
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: 'DM Sans', sans-serif; background: #FFF8EE; color: #3E2000; }

.hero {
  background: linear-gradient(135deg, #3E2000 0%, #6B3500 60%, #E8650A 100%);
  color: white;
  padding: 60px 40px 50px;
  text-align: center;
}
.hero-badge {
  display: inline-block;
  background: #E8650A;
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
  font-size: 56px;
  font-weight: 900;
  line-height: 1.1;
  margin-bottom: 16px;
}
.hero h1 span { color: #FFD580; }
.hero-desc {
  font-size: 16px;
  opacity: 0.85;
  max-width: 580px;
  margin: 0 auto 32px;
  line-height: 1.7;
}
.hero-stats {
  display: flex;
  justify-content: center;
  gap: 50px;
  flex-wrap: wrap;
}
.stat-num {
  font-family: 'Playfair Display', serif;
  font-size: 38px;
  font-weight: 900;
  color: #FFD580;
  display: block;
}
.stat-label { font-size: 12px; opacity: 0.75; letter-spacing: 1px; }

.section { padding: 60px 40px; max-width: 1100px; margin: 0 auto; }
.section-tag {
  font-family: 'Space Mono', monospace;
  font-size: 11px;
  letter-spacing: 3px;
  color: #E8650A;
  text-transform: uppercase;
  margin-bottom: 8px;
}
.section-title {
  font-family: 'Playfair Display', serif;
  font-size: 36px;
  font-weight: 900;
  color: #3E2000;
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
  background: linear-gradient(90deg, #E8650A, transparent);
  width: 60px;
  margin-bottom: 16px;
}

.ba-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 24px;
  margin-bottom: 40px;
}
.ba-card { border-radius: 16px; padding: 32px; }
.ba-card-before { background: #FFF0F0; border: 2px solid #FFCDD2; }
.ba-card-after { background: #E8F5E9; border: 2px solid #A5D6A7; }
.ba-label-before {
  font-family: 'Space Mono', monospace;
  font-size: 10px;
  letter-spacing: 3px;
  font-weight: 700;
  margin-bottom: 18px;
  display: inline-block;
  padding: 4px 12px;
  border-radius: 2px;
  background: #B71C1C;
  color: white;
}
.ba-label-after {
  font-family: 'Space Mono', monospace;
  font-size: 10px;
  letter-spacing: 3px;
  font-weight: 700;
  margin-bottom: 18px;
  display: inline-block;
  padding: 4px 12px;
  border-radius: 2px;
  background: #1A5C2A;
  color: white;
}
.ba-card h3 { font-family: 'Playfair Display', serif; font-size: 22px; margin-bottom: 20px; }
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
.ico { font-size: 18px; flex-shrink: 0; margin-top: 1px; }

.score-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  margin-bottom: 20px;
}
.score-card {
  background: white;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 4px 20px rgba(62,32,0,0.12);
  border-left: 4px solid #E8650A;
}
.score-card h4 { font-size: 12px; color: #7A5C3A; margin-bottom: 12px; line-height: 1.4; font-weight: 500; }
.score-bar-wrap { background: #F0E6D6; border-radius: 99px; height: 8px; margin-bottom: 10px; overflow: hidden; }
.score-bar { height: 100%; border-radius: 99px; background: linear-gradient(90deg, #E8650A, #C89B2A); }
.score-nums { display: flex; justify-content: space-between; font-size: 12px; font-family: 'Space Mono', monospace; }
.s-before { color: #B71C1C; }
.s-after { color: #1A5C2A; font-weight: 700; }

.steps-row {
  display: flex;
  gap: 0;
  margin-bottom: 40px;
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(62,32,0,0.12);
}
.step {
  flex: 1;
  padding: 28px 20px;
  text-align: center;
  border-right: 1px solid #F0E6D6;
}
.step:last-child { border-right: none; }
.step-num {
  font-family: 'Playfair Display', serif;
  font-size: 36px;
  font-weight: 900;
  color: #F5E6C8;
  line-height: 1;
  margin-bottom: 8px;
}
.step-icon { font-size: 26px; margin-bottom: 8px; }
.step-title { font-weight: 700; font-size: 14px; color: #3E2000; margin-bottom: 6px; }
.step-desc { font-size: 12px; color: #7A5C3A; line-height: 1.5; }

.products-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
}
.product-card {
  background: white;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(62,32,0,0.12);
}
.product-top {
  height: 160px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 56px;
  position: relative;
}
.tag-halal {
  position: absolute;
  top: 10px; right: 10px;
  background: #1A5C2A;
  color: white;
  font-size: 9px;
  font-weight: 700;
  letter-spacing: 1px;
  padding: 3px 7px;
  border-radius: 3px;
}
.tag-pirt {
  position: absolute;
  top: 10px; left: 10px;
  background: #3E2000;
  color: white;
  font-size: 9px;
  font-weight: 700;
  padding: 3px 7px;
  border-radius: 3px;
}
.product-body { padding: 18px; }
.product-name { font-family: 'Playfair Display', serif; font-size: 17px; font-weight: 700; margin-bottom: 3px; }
.product-brand { font-size: 11px; color: #E8650A; font-weight: 500; margin-bottom: 10px; font-family: 'Space Mono', monospace; }
.product-price { font-size: 18px; font-weight: 700; color: #3E2000; margin-bottom: 12px; }
.product-price-coret { font-size: 12px; font-weight: 400; color: #999; text-decoration: line-through; margin-left: 5px; }
.qr-section {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
  background: #FFF8EE;
  border-radius: 8px;
  margin-bottom: 10px;
}
.qr-box {
  width: 48px;
  height: 48px;
  background: white;
  border: 2px solid #3E2000;
  border-radius: 4px;
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 1px;
  padding: 4px;
  flex-shrink: 0;
}
.qr-on { background: #3E2000; border-radius: 1px; }
.qr-off { background: transparent; border-radius: 1px; }
.qr-info p { font-size: 10px; color: #7A5C3A; line-height: 1.4; }
.qr-info strong { font-size: 11px; color: #3E2000; display: block; margin-bottom: 2px; }
.barcode-wrap {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 8px;
  background: white;
  border-radius: 6px;
  border: 1px solid #E8DDD0;
}
.barcode-lines { display: flex; gap: 2px; height: 24px; margin-bottom: 3px; }
.bl { width: 2px; background: #3E2000; border-radius: 1px; }
.bl-t { width: 1px; background: #3E2000; border-radius: 1px; opacity: 0.6; }
.bl-k { width: 3px; background: #3E2000; border-radius: 1px; }
.barcode-num { font-family: 'Space Mono', monospace; font-size: 8px; color: #3E2000; letter-spacing: 2px; }

.phone-wrap { display: flex; justify-content: center; padding: 20px 0; }
.phone-mockup {
  width: 270px;
  background: #3E2000;
  border-radius: 36px;
  padding: 14px;
  box-shadow: 0 24px 64px rgba(62,32,0,0.4);
}
.phone-screen { background: #FFF8EE; border-radius: 24px; overflow: hidden; }
.phone-notch {
  background: #3E2000;
  height: 26px;
  display: flex;
  align-items: center;
  justify-content: center;
}
.phone-dot { width: 7px; height: 7px; background: #555; border-radius: 50%; }
.phone-header {
  background: linear-gradient(135deg, #3E2000, #E8650A);
  color: white;
  padding: 18px 14px 14px;
  text-align: center;
}
.phone-logo { font-family: 'Playfair Display', serif; font-size: 18px; font-weight: 900; }
.phone-tagline { font-size: 10px; opacity: 0.8; margin-top: 2px; }
.phone-img { font-size: 52px; text-align: center; padding: 18px; background: #F5E6C8; }
.phone-content { padding: 14px; }
.phone-pname { font-family: 'Playfair Display', serif; font-size: 17px; font-weight: 900; margin-bottom: 4px; }
.phone-pprice { font-size: 20px; font-weight: 700; color: #E8650A; margin-bottom: 10px; }
.phone-chips { display: flex; gap: 6px; flex-wrap: wrap; margin-bottom: 10px; }
.chip { font-size: 10px; font-weight: 600; padding: 3px 9px; border-radius: 20px; }
.chip-g { background: #E8F5E9; color: #1A5C2A; }
.chip-o { background: #FFF3E0; color: #E8650A; }
.phone-pdesc { font-size: 11px; color: #7A5C3A; margin-bottom: 12px; line-height: 1.6; }
.phone-btn-main {
  display: block;
  background: #E8650A;
  color: white;
  text-align: center;
  padding: 11px;
  border-radius: 9px;
  font-weight: 700;
  font-size: 12px;
  margin-bottom: 7px;
  text-decoration: none;
}
.phone-btn-alt {
  display: block;
  background: transparent;
  border: 2px solid #3E2000;
  color: #3E2000;
  text-align: center;
  padding: 9px;
  border-radius: 9px;
  font-weight: 700;
  font-size: 12px;
  text-decoration: none;
}

.priority-grid {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 20px;
  margin-bottom: 40px;
}
.priority-card {
  background: white;
  border-radius: 14px;
  padding: 24px;
  box-shadow: 0 4px 20px rgba(62,32,0,0.12);
  border-top: 4px solid #E8650A;
}
.priority-num { font-family: 'Space Mono', monospace; font-size: 11px; color: #E8650A; letter-spacing: 2px; margin-bottom: 8px; }
.priority-card h3 { font-family: 'Playfair Display', serif; font-size: 17px; font-weight: 700; margin-bottom: 10px; }
.priority-card p { font-size: 13px; color: #7A5C3A; line-height: 1.6; }
.badge-now { margin-top: 14px; font-size: 11px; font-weight: 700; letter-spacing: 1px; padding: 4px 10px; border-radius: 3px; display: inline-block; background: #FFF3E0; color: #E8650A; }
.badge-next { margin-top: 14px; font-size: 11px; font-weight: 700; letter-spacing: 1px; padding: 4px 10px; border-radius: 3px; display: inline-block; background: #E8F5E9; color: #1A5C2A; }

.bg-warm { background: #F5E6C8; }
.bg-white { background: white; }
.full-pad { padding: 60px 40px; }
.inner { max-width: 1100px; margin: 0 auto; }

.footer {
  background: #3E2000;
  color: rgba(255,255,255,0.7);
  padding: 40px;
  text-align: center;
}
.footer-title { color: #FFD580; font-family: 'Playfair Display', serif; font-size: 20px; display: block; margin-bottom: 6px; }
.footer p { font-size: 13px; line-height: 1.8; }
</style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="hero-badge">Proyek TI — INDI 4.0</div>
  <h1>Cecilia Snack<br><span>Menuju Digital</span></h1>
  <p class="hero-desc">Digitalisasi Label QR Code pada Kemasan Produk UMKM sebagai Solusi Peningkatan Indeks INDI 4.0</p>
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
    <div class="ba-card ba-card-before">
      <span class="ba-label-before">Kondisi Sebelum</span>
      <h3>Masih Manual</h3>
      <ul class="ba-list">
        <li><span class="ico">&#127991;&#65039;</span><span>Harga ditempel manual dengan kertas tulisan tangan</span></li>
        <li><span class="ico">&#128230;</span><span>Kemasan plastik polos tanpa identitas produk</span></li>
        <li><span class="ico">&#9634;</span><span>Tidak ada barcode maupun QR code di kemasan</span></li>
        <li><span class="ico">&#128210;</span><span>Pencatatan keuangan masih di buku tulis manual</span></li>
        <li><span class="ico">&#128227;</span><span>Pemasaran hanya dari mulut ke mulut</span></li>
        <li><span class="ico">&#127760;</span><span>Tidak ada kehadiran digital sama sekali</span></li>
      </ul>
    </div>
    <div class="ba-card ba-card-after">
      <span class="ba-label-after">Sesudah Solusi</span>
      <h3>Serba Terdigitalisasi</h3>
      <ul class="ba-list">
        <li><span class="ico">&#128241;</span><span>QR code di kemasan terhubung ke halaman produk digital</span></li>
        <li><span class="ico">&#128179;</span><span>Harga tampil otomatis di halaman web saat scan</span></li>
        <li><span class="ico">&#128290;</span><span>Barcode produk tersedia untuk sistem inventori</span></li>
        <li><span class="ico">&#128202;</span><span>Data scan otomatis tersimpan untuk analitik</span></li>
        <li><span class="ico">&#128242;</span><span>Konsumen bisa pesan WhatsApp langsung dari QR</span></li>
        <li><span class="ico">&#127885;</span><span>Label HALAL dan nomor PIRT terpasang resmi</span></li>
      </ul>
    </div>
  </div>
</div>

<!-- SKOR INDI -->
<div class="bg-warm full-pad">
  <div class="inner">
    <div class="section-tag">Evaluasi INDI 4.0</div>
    <div class="divider"></div>
    <h2 class="section-title">Peningkatan Skor INDI 4.0</h2>
    <p class="section-sub">Perbandingan skor per indikator sebelum dan sesudah implementasi solusi digitalisasi.</p>
    <div class="score-grid">
      <div class="score-card">
        <h4>Identifikasi Produk Digital</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:80%"></div></div>
        <div class="score-nums"><span class="s-before">Sebelum: 1/5</span><span class="s-after">Sesudah: 4/5</span></div>
      </div>
      <div class="score-card">
        <h4>Kemasan dan Branding Digital</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:60%"></div></div>
        <div class="score-nums"><span class="s-before">Sebelum: 1/5</span><span class="s-after">Sesudah: 3/5</span></div>
      </div>
      <div class="score-card">
        <h4>Pemasaran Digital</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:60%"></div></div>
        <div class="score-nums"><span class="s-before">Sebelum: 1/5</span><span class="s-after">Sesudah: 3/5</span></div>
      </div>
      <div class="score-card">
        <h4>Transparansi Harga</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:80%"></div></div>
        <div class="score-nums"><span class="s-before">Sebelum: 1/5</span><span class="s-after">Sesudah: 4/5</span></div>
      </div>
      <div class="score-card">
        <h4>Ketelusuran Produk</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:60%"></div></div>
        <div class="score-nums"><span class="s-before">Sebelum: 0/5</span><span class="s-after">Sesudah: 3/5</span></div>
      </div>
      <div class="score-card">
        <h4>Pencatatan Digital</h4>
        <div class="score-bar-wrap"><div class="score-bar" style="width:40%"></div></div>
        <div class="score-nums"><span class="s-before">Sebelum: 1/5</span><span class="s-after">Sesudah: 2/5</span></div>
      </div>
    </div>
  </div>
</div>

<!-- ALUR SISTEM -->
<div class="bg-white full-pad">
  <div class="inner">
    <div class="section-tag">Sistem QR Code</div>
    <div class="divider"></div>
    <h2 class="section-title">Alur 4 Langkah Digitalisasi</h2>
    <p class="section-sub">Cara kerja sistem QR Code dari kemasan produk hingga konsumen mendapat informasi lengkap.</p>
    <div class="steps-row">
      <div class="step">
        <div class="step-num">01</div>
        <div class="step-icon">&#127912;</div>
        <div class="step-title">Desain Label</div>
        <p class="step-desc">QR code dan barcode didesain lalu dicetak di kemasan</p>
      </div>
      <div class="step">
        <div class="step-num">02</div>
        <div class="step-icon">&#128230;</div>
        <div class="step-title">Tempel Kemasan</div>
        <p class="step-desc">Label ditempelkan pada setiap produk yang dijual</p>
      </div>
      <div class="step">
        <div class="step-num">03</div>
        <div class="step-icon">&#128241;</div>
        <div class="step-title">Konsumen Scan</div>
        <p class="step-desc">Pembeli scan QR, langsung terbuka halaman produk</p>
      </div>
      <div class="step">
        <div class="step-num">04</div>
        <div class="step-icon">&#128722;</div>
        <div class="step-title">Aksi Digital</div>
        <p class="step-desc">Lihat harga, info produk, dan order via WhatsApp</p>
      </div>
    </div>
  </div>
</div>

<!-- MOCKUP PRODUK -->
<div class="section">
  <div class="section-tag">Mockup Produk</div>
  <div class="divider"></div>
  <h2 class="section-title">Desain Kemasan Digital</h2>
  <p class="section-sub">4 produk utama Cecilia Snack dengan label QR code, barcode, sertifikasi HALAL dan nomor PIRT.</p>
  <div class="products-grid">

    <!-- Keripik Singkong -->
    <div class="product-card">
      <div class="product-top" style="background:linear-gradient(135deg,#FFF3E0,#FFE0B2);">
        &#129364;
        <span class="tag-halal">HALAL</span>
        <span class="tag-pirt">PIRT</span>
      </div>
      <div class="product-body">
        <div class="product-name">Keripik Singkong</div>
        <div class="product-brand">CECILIA SNACK - 250g</div>
        <div class="product-price">Rp 12.000 <span class="product-price-coret">Rp 15.000</span></div>
        <div class="qr-section">
          <div class="qr-box">
            <div class="qr-on"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div>
            <div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div>
            <div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div>
            <div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div>
            <div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-on"></div>
          </div>
          <div class="qr-info">
            <strong>Scan Info Produk</strong>
            <p>Harga, Bahan, Expired, Order WA</p>
          </div>
        </div>
        <div class="barcode-wrap">
          <div class="barcode-lines">
            <div class="bl-k"></div><div class="bl-t"></div><div class="bl"></div><div class="bl-k"></div>
            <div class="bl-t"></div><div class="bl"></div><div class="bl-k"></div><div class="bl-t"></div>
            <div class="bl"></div><div class="bl-k"></div><div class="bl-t"></div><div class="bl-k"></div>
            <div class="bl"></div><div class="bl-t"></div><div class="bl-k"></div><div class="bl"></div>
          </div>
          <div class="barcode-num">8 99301 22001 4</div>
        </div>
      </div>
    </div>

    <!-- Keripik Pisang -->
    <div class="product-card">
      <div class="product-top" style="background:linear-gradient(135deg,#FFFDE7,#FFF9C4);">
        &#127820;
        <span class="tag-halal">HALAL</span>
        <span class="tag-pirt">PIRT</span>
      </div>
      <div class="product-body">
        <div class="product-name">Keripik Pisang</div>
        <div class="product-brand">CECILIA SNACK - 200g</div>
        <div class="product-price">Rp 10.000 <span class="product-price-coret">Rp 13.000</span></div>
        <div class="qr-section">
          <div class="qr-box">
            <div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div>
            <div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div>
            <div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div>
            <div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div>
            <div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div>
          </div>
          <div class="qr-info">
            <strong>Scan Info Produk</strong>
            <p>Harga, Bahan, Expired, Order WA</p>
          </div>
        </div>
        <div class="barcode-wrap">
          <div class="barcode-lines">
            <div class="bl-t"></div><div class="bl-k"></div><div class="bl-t"></div><div class="bl"></div>
            <div class="bl-k"></div><div class="bl-t"></div><div class="bl"></div><div class="bl-k"></div>
            <div class="bl-t"></div><div class="bl"></div><div class="bl-k"></div><div class="bl-t"></div>
            <div class="bl-k"></div><div class="bl"></div><div class="bl-t"></div><div class="bl-k"></div>
          </div>
          <div class="barcode-num">8 99301 22002 1</div>
        </div>
      </div>
    </div>

    <!-- CocoCrunch -->
    <div class="product-card">
      <div class="product-top" style="background:linear-gradient(135deg,#EFEBE9,#D7CCC8);">
        &#129381;
        <span class="tag-halal">HALAL</span>
        <span class="tag-pirt">PIRT</span>
      </div>
      <div class="product-body">
        <div class="product-name">CocoCrunch</div>
        <div class="product-brand">CECILIA SNACK - 150g</div>
        <div class="product-price">Rp 15.000 <span class="product-price-coret">Rp 18.000</span></div>
        <div class="qr-section">
          <div class="qr-box">
            <div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div>
            <div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-off"></div>
            <div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-on"></div>
            <div class="qr-off"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div>
            <div class="qr-on"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div>
          </div>
          <div class="qr-info">
            <strong>Scan Info Produk</strong>
            <p>Harga, Bahan, Expired, Order WA</p>
          </div>
        </div>
        <div class="barcode-wrap">
          <div class="barcode-lines">
            <div class="bl"></div><div class="bl-k"></div><div class="bl-t"></div><div class="bl-k"></div>
            <div class="bl-t"></div><div class="bl-k"></div><div class="bl"></div><div class="bl-t"></div>
            <div class="bl-k"></div><div class="bl"></div><div class="bl-t"></div><div class="bl-k"></div>
            <div class="bl-t"></div><div class="bl"></div><div class="bl-k"></div><div class="bl-t"></div>
          </div>
          <div class="barcode-num">8 99301 22003 8</div>
        </div>
      </div>
    </div>

    <!-- Roti Kering -->
    <div class="product-card">
      <div class="product-top" style="background:linear-gradient(135deg,#FBE9E7,#FFCCBC);">
        &#127838;
        <span class="tag-halal">HALAL</span>
        <span class="tag-pirt">PIRT</span>
      </div>
      <div class="product-body">
        <div class="product-name">Roti Kering</div>
        <div class="product-brand">CECILIA SNACK - 180g</div>
        <div class="product-price">Rp 13.000 <span class="product-price-coret">Rp 16.000</span></div>
        <div class="qr-section">
          <div class="qr-box">
            <div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-off"></div>
            <div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div>
            <div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div>
            <div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div>
            <div class="qr-off"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-on"></div><div class="qr-off"></div>
          </div>
          <div class="qr-info">
            <strong>Scan Info Produk</strong>
            <p>Harga, Bahan, Expired, Order WA</p>
          </div>
        </div>
        <div class="barcode-wrap">
          <div class="barcode-lines">
            <div class="bl-k"></div><div class="bl-t"></div><div class="bl-k"></div><div class="bl"></div>
            <div class="bl-t"></div><div class="bl"></div><div class="bl-k"></div><div class="bl-t"></div>
            <div class="bl"></div><div class="bl-k"></div><div class="bl-t"></div><div class="bl"></div>
            <div class="bl-k"></div><div class="bl-t"></div><div class="bl-k"></div><div class="bl"></div>
          </div>
          <div class="barcode-num">8 99301 22004 5</div>
        </div>
      </div>
    </div>

  </div>
</div>

<!-- SIMULASI HP -->
<div class="bg-warm full-pad">
  <div class="inner">
    <div class="section-tag">Simulasi Konsumen</div>
    <div class="divider"></div>
    <h2 class="section-title">Tampilan Saat Scan QR</h2>
    <p class="section-sub">Begini yang dilihat konsumen ketika scan QR code pada kemasan produk Cecilia Snack.</p>
    <div class="phone-wrap">
      <div class="phone-mockup">
        <div class="phone-screen">
          <div class="phone-notch"><div class="phone-dot"></div></div>
          <div class="phone-header">
            <div class="phone-logo">Cecilia Snack</div>
            <div class="phone-tagline">Camilan Rumahan Berkualitas</div>
          </div>
          <div class="phone-img">&#129364;</div>
          <div class="phone-content">
            <div class="phone-pname">Keripik Singkong</div>
            <div class="phone-pprice">Rp 12.000</div>
            <div class="phone-chips">
              <span class="chip chip-g">HALAL MUI</span>
              <span class="chip chip-o">PIRT Terdaftar</span>
              <span class="chip chip-g">250g</span>
            </div>
            <p class="phone-pdesc">Keripik singkong renyah khas Cecilia Snack. Bahan: singkong, minyak, garam. <strong>Exp: Jan 2026</strong></p>
            <a class="phone-btn-main">Pesan via WhatsApp</a>
            <a class="phone-btn-alt">Lokasi Toko</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- PRIORITAS -->
<div class="section">
  <div class="section-tag">Rencana Implementasi</div>
  <div class="divider"></div>
  <h2 class="section-title">Skala Prioritas</h2>
  <p class="section-sub">Urutan implementasi solusi yang realistis untuk UMKM kecil seperti Cecilia Snack.</p>
  <div class="priority-grid">
    <div class="priority-card">
      <div class="priority-num">PRIORITAS 01</div>
      <h3>QR Label</h3>
      <p>Pasang QR code dan barcode di semua kemasan produk. Paling impactful dengan biaya cetak label minimal.</p>
      <span class="badge-now">IMPLEMENTASI SEKARANG</span>
    </div>
    <div class="priority-card">
      <div class="priority-num">PRIORITAS 02</div>
      <h3>Kemasan Baru</h3>
      <p>Redesain kemasan dengan identitas merek yang kuat, info gizi, tanggal kedaluwarsa, dan komposisi bahan.</p>
      <span class="badge-next">BERIKUTNYA</span>
    </div>
    <div class="priority-card">
      <div class="priority-num">PRIORITAS 03</div>
      <h3>Harga Digital</h3>
      <p>Sistem harga otomatis terintegrasi QR sehingga perubahan harga cukup dilakukan di satu tempat.</p>
      <span class="badge-next">BERIKUTNYA</span>
    </div>
    <div class="priority-card">
      <div class="priority-num">PRIORITAS 04</div>
      <h3>Pencatatan</h3>
      <p>Migrasi dari buku tulis ke Google Sheets atau aplikasi kasir sederhana untuk pencatatan keuangan.</p>
      <span class="badge-next">JANGKA PANJANG</span>
    </div>
  </div>
</div>

<!-- FOOTER -->
<div class="footer">
  <span class="footer-title">Cecilia Snack x INDI 4.0</span>
  <p>Proyek Teknologi Informasi — Digitalisasi UMKM<br>
  <span style="font-size:12px;opacity:0.6;">Solusi QR Code Label untuk Peningkatan Indeks INDI 4.0</span></p>
</div>

</body>
</html>"""

st.components.v1.html(html_content, height=5200, scrolling=True)
