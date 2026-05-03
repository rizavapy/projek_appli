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

import streamlit as st
import qrcode
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
import io
import base64
import urllib.parse

st.set_page_config(
    page_title="Cecilia Snack — QR & Barcode Generator",
    page_icon="🍟",
    layout="wide"
)

# ─── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=DM+Sans:wght@300;400;500;700&family=Space+Mono:wght@400;700&display=swap');

:root {
  --cream: #FFF8EE; --brown: #3E2000; --orange: #E8650A;
  --gold: #C89B2A; --green: #1A5C2A;
}
html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }

/* Hide Streamlit default elements */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 0 !important; }

/* ── Hero ── */
.hero {
  background: linear-gradient(135deg, #3E2000 0%, #6B3500 55%, #E8650A 100%);
  color: white;
  padding: 52px 40px 44px;
  text-align: center;
  border-radius: 0 0 24px 24px;
  margin-bottom: 32px;
}
.hero-badge {
  display: inline-block;
  background: rgba(255,255,255,0.15);
  border: 1px solid rgba(255,255,255,0.3);
  font-family: 'Space Mono', monospace;
  font-size: 10px; letter-spacing: 3px;
  padding: 5px 16px; border-radius: 2px;
  margin-bottom: 18px; text-transform: uppercase;
}
.hero h1 {
  font-family: 'Playfair Display', serif;
  font-size: 44px; font-weight: 900; line-height: 1.1;
  margin-bottom: 12px;
}
.hero h1 span { color: #FFD580; }
.hero p { font-size: 15px; opacity: 0.85; max-width: 520px; margin: 0 auto; line-height: 1.7; }

/* ── Section Label ── */
.section-tag {
  font-family: 'Space Mono', monospace;
  font-size: 10px; letter-spacing: 3px; color: #E8650A;
  text-transform: uppercase; margin-bottom: 4px;
}
.divider {
  height: 3px;
  background: linear-gradient(90deg, #E8650A, transparent);
  width: 50px; margin-bottom: 12px; border-radius: 2px;
}
.section-title {
  font-family: 'Playfair Display', serif;
  font-size: 26px; font-weight: 900; color: #3E2000; margin-bottom: 6px;
}
.section-sub { font-size: 13px; color: #7A5C3A; line-height: 1.7; margin-bottom: 24px; }

/* ── Product Cards ── */
.product-card {
  background: white; border-radius: 14px; padding: 16px;
  border: 2px solid #F0E6D6; cursor: pointer;
  transition: all 0.2s; margin-bottom: 10px;
}
.product-card:hover { border-color: #E8650A; background: #FFF3E0; }
.product-card.selected { border-color: #E8650A; background: #FFF3E0; }

/* ── Info Box ── */
.info-box {
  background: #E8F5E9; border: 1.5px solid #A5D6A7;
  border-radius: 12px; padding: 14px 18px; margin-bottom: 16px;
}
.info-box p { font-size: 13px; color: #1A5C2A; line-height: 1.8; margin: 0; }

/* ── Result Card ── */
.result-card {
  background: white; border-radius: 16px; padding: 24px;
  box-shadow: 0 8px 32px rgba(62,32,0,0.12);
}

/* ── Badges ── */
.badge-halal {
  display: inline-block; background: #1A5C2A; color: white;
  font-size: 10px; font-weight: 700; padding: 3px 10px; border-radius: 3px; margin-right: 4px;
}
.badge-pirt {
  display: inline-block; background: #3E2000; color: white;
  font-size: 10px; font-weight: 700; padding: 3px 10px; border-radius: 3px;
}
.badge-orange {
  display: inline-block; background: #E8650A; color: white;
  font-size: 10px; font-weight: 700; padding: 3px 10px; border-radius: 3px; margin-right: 4px;
}

/* ── Product Page Preview ── */
.preview-header {
  background: linear-gradient(135deg,#3E2000,#E8650A);
  color: white; padding: 18px 20px; border-radius: 12px 12px 0 0;
}
.preview-body { background: #FFF8EE; padding: 18px; border-radius: 0 0 12px 12px; }

/* ── Footer ── */
.footer {
  background: #3E2000; color: rgba(255,255,255,0.7);
  padding: 28px; text-align: center; border-radius: 16px; margin-top: 40px;
}
.footer span { color: #FFD580; font-family: 'Playfair Display', serif; font-size: 18px; display: block; margin-bottom: 4px; }
.footer p { font-size: 12px; line-height: 1.8; }

/* stButton */
div.stButton > button {
  border-radius: 10px !important;
  font-family: 'DM Sans', sans-serif !important;
  font-weight: 700 !important;
}
</style>
""", unsafe_allow_html=True)


  

# ─── DATA PRODUK ──────────────────────────────────────────────────────────────

PRODUCTS = [
    {
        "id": "CS001", "name": "Keripik Singkong", "weight": "250g",
        "price": 12000, "price_ori": 15000, "emoji": "🥔",
        "halal": True, "pirt": "P-IRT No. 2153578010488-22",
        "expired": "12 bulan",
        "ingredients": "Singkong, Minyak Nabati, Garam, Bumbu",
        "desc": "Keripik singkong renyah dengan bumbu gurih khas Jawa.",
        "barcode": "8993012200140", "wa": "6281234567890",
        "bg_color": (255, 243, 224),
    },
    {
        "id": "CS002", "name": "Keripik Pisang", "weight": "200g",
        "price": 10000, "price_ori": 13000, "emoji": "🍌",
        "halal": True, "pirt": "P-IRT No. 2153578010488-23",
        "expired": "10 bulan",
        "ingredients": "Pisang, Minyak Nabati, Gula, Garam",
        "desc": "Keripik pisang manis legit, dibuat dari pisang pilihan.",
        "barcode": "8993012200157", "wa": "6281234567890",
        "bg_color": (255, 253, 231),
    },
    {
        "id": "CS003", "name": "Kue Bawang", "weight": "150g",
        "price": 8000, "price_ori": 10000, "emoji": "🧅",
        "halal": True, "pirt": "P-IRT No. 2153578010488-24",
        "expired": "8 bulan",
        "ingredients": "Tepung Terigu, Bawang Putih, Telur, Minyak, Garam",
        "desc": "Kue bawang gurih dan renyah, cocok untuk cemilan keluarga.",
        "barcode": "8993012200164", "wa": "6281234567890",
        "bg_color": (243, 229, 245),
    },
    {
        "id": "CS004", "name": "Rempeyek Kacang", "weight": "180g",
        "price": 11000, "price_ori": 14000, "emoji": "🥜",
        "halal": True, "pirt": "P-IRT No. 2153578010488-25",
        "expired": "9 bulan",
        "ingredients": "Tepung Beras, Kacang Tanah, Santan, Bumbu Rempah",
        "desc": "Rempeyek kacang tanah renyah dengan aroma rempah yang khas.",
        "barcode": "8993012200171", "wa": "6281234567890",
        "bg_color": (232, 245, 233),
    },
]
# ─── HELPER FUNCTIONS ─────────────────────────────────────────────────────────
def generate_qr(url: str, box_size: int = 8) -> Image.Image:
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=3,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#3E2000", back_color="#FFFDF8")
    return img.convert("RGB")


def generate_barcode(code: str) -> Image.Image:
    try:
        EAN = barcode.get_barcode_class("ean13")
        code13 = code[:12].ljust(12, "0")
        bc = EAN(code13, writer=ImageWriter())
        buf = io.BytesIO()
        bc.write(buf, options={
            "module_width": 0.5,
            "module_height": 12.0,
            "font_size": 7,
            "text_distance": 3.0,
            "background": "white",
            "foreground": "#3E2000",
            "write_text": True,
            "quiet_zone": 4,
        })
        buf.seek(0)
        return Image.open(buf).convert("RGB")
    except Exception:
        # Fallback: blank white image with text
        img = Image.new("RGB", (300, 80), "white")
        draw = ImageDraw.Draw(img)
        draw.text((10, 30), f"BARCODE: {code}", fill="#3E2000")
        return img


def img_to_b64(img: Image.Image, fmt: str = "PNG") -> str:
    buf = io.BytesIO()
    img.save(buf, format=fmt)
    return base64.b64encode(buf.getvalue()).decode()


def img_to_bytes(img: Image.Image, fmt: str = "PNG") -> bytes:
    buf = io.BytesIO()
    img.save(buf, format=fmt)
    return buf.getvalue()


def make_label_image(prod: dict, qr_img: Image.Image) -> Image.Image:
    """Buat label kemasan dengan QR code embedded."""
    W, H = 600, 200
    label = Image.new("RGB", (W, H), prod["bg_color"])
    draw = ImageDraw.Draw(label)

    # Orange accent bar kiri
    draw.rectangle([0, 0, 6, H], fill="#E8650A")

    # QR di kanan
    qr_small = qr_img.resize((140, 140))
    label.paste(qr_small, (W - 155, 30))

    # Text area
    try:
        font_big = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf", 22)
        font_med = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)
        font_sm  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 11)
        font_xs  = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 10)
    except Exception:
        font_big = font_med = font_sm = font_xs = ImageFont.load_default()

    draw.text((20, 18), prod["name"], fill="#3E2000", font=font_big)
    draw.text((20, 50), "CECILIA SNACK", fill="#E8650A", font=font_xs)
    draw.text((20, 66), prod["weight"], fill="#7A5C3A", font=font_sm)

    price_str = f"Rp {prod['price']:,}".replace(",", ".")
    draw.text((20, 86), price_str, fill="#3E2000", font=font_big)

    draw.text((20, 122), f"Bahan: {prod['ingredients'][:45]}...", fill="#7A5C3A", font=font_sm)
    draw.text((20, 140), f"Masa simpan: {prod['expired']}", fill="#7A5C3A", font=font_sm)
    draw.text((20, 158), prod["pirt"][:40], fill="#7A5C3A", font=font_xs)

    # Badge HALAL
    if prod.get("halal"):
        draw.rectangle([20, 175, 72, 192], fill="#1A5C2A")
        draw.text((24, 178), "HALAL", fill="white", font=font_xs)

    draw.rectangle([78, 175, 116, 192], fill="#3E2000")
    draw.text((82, 178), "PIRT", fill="white", font=font_xs)

    # QR label
    draw.text((W - 150, 172), "Scan untuk info", fill="#7A5C3A", font=font_xs)

    return label


def build_product_url(prod: dict) -> str:
    pid = prod["id"].lower()
    return f"https://ceciliasnack.id/produk/{pid}"


def build_wa_url(prod: dict) -> str:
    msg = f"Halo Cecilia Snack! Saya ingin memesan *{prod['name']}* ({prod['weight']}) — Rp {prod['price']:,}".replace(",", ".")
    return f"https://wa.me/{prod['wa']}?text={urllib.parse.quote(msg)}"
    
    

# ─── HERO ─────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="hero">
  <div class="hero-badge">🍟 INDI 4.0 — Digitalisasi UMKM</div>
  <h1>Cecilia Snack<br><span>QR & Barcode Generator</span></h1>
  <p>Buat QR Code yang bisa di-scan langsung oleh konsumen, lengkap dengan Barcode dan label kemasan digital.</p>
</div>
""", unsafe_allow_html=True)


# ─── INIT SESSION STATE ───────────────────────────────────────────────────────
if "tab" not in st.session_state:
    st.session_state.tab = "generator"
if "selected_product" not in st.session_state:
    st.session_state.selected_product = None
if "generated" not in st.session_state:
    st.session_state.generated = False


# ─── TAB NAVIGATION ───────────────────────────────────────────────────────────
col_t1, col_t2 = st.columns(2)
with col_t1:
    if st.button("🎨  Buat QR & Barcode", use_container_width=True,
                 type="primary" if st.session_state.tab == "generator" else "secondary"):
        st.session_state.tab = "generator"
        st.session_state.generated = False
with col_t2:
    if st.button("📱  Simulasi Scan Konsumen", use_container_width=True,
                 type="primary" if st.session_state.tab == "scanner" else "secondary"):
        st.session_state.tab = "scanner"

st.markdown("<hr style='border:1px solid #F0E6D6;margin:16px 0 28px'>", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# TAB: GENERATOR
# ══════════════════════════════════════════════════════════════════════════════
if st.session_state.tab == "generator":

    st.markdown("""
    <div class="section-tag">Langkah 1</div>
    <div class="divider"></div>
    <div class="section-title">Pilih atau Isi Data Produk</div>
    <div class="section-sub">Pilih salah satu produk Cecilia Snack, atau isi data produk custom di bawah.</div>
    """, unsafe_allow_html=True)

    left_col, right_col = st.columns([1, 1], gap="large")

    with left_col:
        st.markdown("**Produk Cecilia Snack:**")
        for i, p in enumerate(PRODUCTS):
            selected = st.session_state.selected_product == i
            border = "2px solid #E8650A" if selected else "2px solid #F0E6D6"
            bg = "#FFF3E0" if selected else "white"

            clicked = st.button(
                f"{p['emoji']}  **{p['name']}** — {p['weight']} · Rp {p['price']:,}".replace(",", "."),
                key=f"prod_{i}",
                use_container_width=True,
                type="primary" if selected else "secondary",
            )
            if clicked:
                st.session_state.selected_product = i
                st.session_state.generated = False
                st.rerun()

    with right_col:
        st.markdown("**Atau isi produk custom:**")
        custom_name  = st.text_input("Nama Produk", placeholder="cth: Keripik Tempe Pedas")
        c1, c2 = st.columns(2)
        custom_price = c1.text_input("Harga (Rp)", placeholder="15000")
        custom_weight = c2.text_input("Berat / Ukuran", placeholder="200g")
        custom_desc  = st.text_area("Deskripsi Singkat", placeholder="Keripik tempe renyah...", height=70)
        custom_bc    = st.text_input("Nomor Barcode (12–13 digit)", placeholder="8993012200188")
        custom_wa    = st.text_input("No. WhatsApp (62xxx)", value="6281234567890")
        custom_halal = st.checkbox("✅ Sudah bersertifikat HALAL", value=False)
        custom_pirt  = st.text_input("Nomor PIRT (opsional)", placeholder="P-IRT No. ...")

    st.markdown("<br>", unsafe_allow_html=True)

    # Tentukan produk aktif
    using_custom = bool(custom_name)
    if using_custom:
        active_prod = {
            "id": "CUSTOM",
            "name": custom_name,
            "weight": custom_weight or "-",
            "price": int(custom_price) if custom_price.isdigit() else 0,
            "price_ori": int(custom_price) if custom_price.isdigit() else 0,
            "emoji": "🍿",
            "halal": custom_halal,
            "pirt": custom_pirt or "-",
            "expired": "-",
            "ingredients": "-",
            "desc": custom_desc or "-",
            "barcode": custom_bc or "8993012200100",
            "wa": custom_wa or "6281234567890",
            "bg_color": (255, 243, 224),
        }
    elif st.session_state.selected_product is not None:
        active_prod = PRODUCTS[st.session_state.selected_product]
    else:
        active_prod = None

    # Tombol Generate
    can_generate = active_prod is not None
    if st.button("🎯  Generate QR Code & Barcode", use_container_width=True,
                 type="primary", disabled=not can_generate):
        st.session_state.generated = True

    # ── HASIL ──
    if st.session_state.generated and active_prod:
        product_url = build_product_url(active_prod)
        wa_url      = build_wa_url(active_prod)

        st.markdown("---")
        st.markdown("""
        <div class="section-tag">Hasil Generate</div>
        <div class="divider"></div>
        <div class="section-title">QR Code & Barcode Siap!</div>
        """, unsafe_allow_html=True)

        with st.spinner("Generating..."):
            qr_img  = generate_qr(product_url, box_size=10)
            bc_img  = generate_barcode(active_prod["barcode"])
            lbl_img = make_label_image(active_prod, generate_qr(product_url, box_size=4))

        res_col1, res_col2, res_col3 = st.columns(3, gap="medium")

        # QR Code
        with res_col1:
            st.markdown("""
            <div style='text-align:center;background:white;border-radius:14px;padding:20px;
            box-shadow:0 4px 20px rgba(62,32,0,0.10);'>
            <div style='font-family:Space Mono,monospace;font-size:10px;letter-spacing:2px;
            color:#E8650A;font-weight:700;margin-bottom:10px;'>📱 QR CODE</div>
            """, unsafe_allow_html=True)
            st.image(qr_img, use_container_width=True, caption="Bisa di-scan langsung!")
            qr_bytes = img_to_bytes(qr_img, "PNG")
            st.download_button(
                "⬇️ Download QR Code", data=qr_bytes,
                file_name=f"qr_{active_prod['id']}.png", mime="image/png",
                use_container_width=True,
            )
            st.markdown("</div>", unsafe_allow_html=True)
            st.markdown(f"""
            <div style='background:#E8F5E9;border-radius:10px;padding:10px;margin-top:10px;
            font-size:11px;color:#1A5C2A;text-align:center;font-weight:600;'>
            ✅ URL: <code style='font-size:10px;'>{product_url}</code>
            </div>
            """, unsafe_allow_html=True)

        # Barcode
        with res_col2:
            st.markdown("""
            <div style='text-align:center;background:white;border-radius:14px;padding:20px;
            box-shadow:0 4px 20px rgba(62,32,0,0.10);'>
            <div style='font-family:Space Mono,monospace;font-size:10px;letter-spacing:2px;
            color:#E8650A;font-weight:700;margin-bottom:10px;'>📊 BARCODE</div>
            """, unsafe_allow_html=True)
            st.image(bc_img, use_container_width=True, caption=f"EAN-13: {active_prod['barcode']}")
            bc_bytes = img_to_bytes(bc_img, "PNG")
            st.download_button(
                "⬇️ Download Barcode", data=bc_bytes,
                file_name=f"barcode_{active_prod['id']}.png", mime="image/png",
                use_container_width=True,
            )
            st.markdown("</div>", unsafe_allow_html=True)

        # Label Kemasan
        with res_col3:
            st.markdown("""
            <div style='text-align:center;background:white;border-radius:14px;padding:20px;
            box-shadow:0 4px 20px rgba(62,32,0,0.10);'>
            <div style='font-family:Space Mono,monospace;font-size:10px;letter-spacing:2px;
            color:#E8650A;font-weight:700;margin-bottom:10px;'>🏷️ LABEL KEMASAN</div>
            """, unsafe_allow_html=True)
            st.image(lbl_img, use_container_width=True, caption="Preview label siap cetak")
            lbl_bytes = img_to_bytes(lbl_img, "PNG")
            st.download_button(
                "⬇️ Download Label", data=lbl_bytes,
                file_name=f"label_{active_prod['id']}.png", mime="image/png",
                use_container_width=True,
            )
            st.markdown("</div>", unsafe_allow_html=True)

        # Info Produk Lengkap
        st.markdown("<br>", unsafe_allow_html=True)
        with st.expander("📋 Lihat Info Produk Lengkap (Preview Halaman Konsumen)", expanded=True):
            discount = round((1 - active_prod["price"] / active_prod["price_ori"]) * 100) if active_prod["price_ori"] else 0
            i1, i2 = st.columns([1, 2])
            with i1:
                st.markdown(f"<div style='font-size:80px;text-align:center'>{active_prod['emoji']}</div>", unsafe_allow_html=True)
                st.image(qr_img, width=140, caption="Scan ini!")
            with i2:
                badges = ""
                if active_prod.get("halal"):
                    badges += '<span class="badge-halal">✓ HALAL</span>'
                badges += '<span class="badge-pirt">PIRT</span>'
                st.markdown(f"""
                <div style='padding:4px 0'>{badges}</div>
                <div style='font-family:Georgia,serif;font-size:24px;font-weight:900;color:#3E2000;margin:8px 0 2px'>
                  {active_prod['name']}
                </div>
                <div style='font-size:11px;color:#E8650A;font-weight:700;letter-spacing:2px;margin-bottom:10px'>
                  CECILIA SNACK • {active_prod['weight']}
                </div>
                <div style='font-size:13px;color:#7A5C3A;margin-bottom:12px'>{active_prod['desc']}</div>
                <div style='background:white;border-radius:10px;padding:12px 16px;
                box-shadow:0 4px 16px rgba(62,32,0,0.10);display:inline-block;'>
                  <span style='font-size:26px;font-weight:900;color:#3E2000'>
                    Rp {active_prod['price']:,}
                  </span>
                  {'<span style="font-size:20px;font-weight:700;color:#E8650A;margin-left:12px">-' + str(discount) + '%</span>' if discount > 0 else ""}
                </div>
                """.replace(",", "."), unsafe_allow_html=True)

                st.markdown("<br>", unsafe_allow_html=True)
                info_rows = [
                    ("🌿 Bahan", active_prod["ingredients"]),
                    ("📅 Masa Simpan", active_prod["expired"]),
                    ("📋 PIRT", active_prod["pirt"]),
                    ("🔗 URL Produk", product_url),
                ]
                for label, val in info_rows:
                    st.markdown(f"""
                    <div style='display:flex;gap:12px;padding:7px 0;border-bottom:1px solid #F0E6D6;font-size:13px'>
                      <span style='min-width:120px;color:#7A5C3A'>{label}</span>
                      <span style='color:#3E2000;font-weight:500'>{val}</span>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown(f"""
                <a href="{wa_url}" target="_blank" style='
                  display:inline-block;margin-top:14px;
                  background:#25D366;color:white;text-decoration:none;
                  padding:12px 24px;border-radius:10px;font-weight:800;font-size:14px;
                '>💬 Pesan via WhatsApp</a>
                """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-box">
        <p>
        📌 <strong>Cara pakai:</strong><br>
        1. Download QR Code & Barcode di atas<br>
        2. Print dan tempel ke kemasan produk<br>
        3. Konsumen scan QR → langsung melihat halaman produk digital<br>
        4. Konsumen bisa pesan via WhatsApp dengan 1 klik!
        </p>
        </div>
        """, unsafe_allow_html=True)
            


# ══════════════════════════════════════════════════════════════════════════════
# TAB: SCANNER SIMULATOR
# ══════════════════════════════════════════════════════════════════════════════
elif st.session_state.tab == "scanner":

    st.markdown("""
    <div class="section-tag">Simulasi Scan</div>
    <div class="divider"></div>
    <div class="section-title">Tampilan Saat Konsumen Scan QR</div>
    <div class="section-sub">
      Pilih produk untuk melihat halaman yang muncul ketika konsumen scan QR Code di kemasan.
    </div>
    """, unsafe_allow_html=True)

    for i, p in enumerate(PRODUCTS):
        with st.expander(f"{p['emoji']}  {p['name']} — {p['weight']} · Rp {p['price']:,}".replace(",", "."), expanded=(i == 0)):
            product_url = build_product_url(p)
            wa_url      = build_wa_url(p)

            col_qr, col_bc, col_info = st.columns([1, 1, 2], gap="medium")

            with col_qr:
                st.markdown("""
                <div style='text-align:center;font-family:Space Mono,monospace;
                font-size:9px;letter-spacing:2px;color:#E8650A;font-weight:700;margin-bottom:6px'>
                QR CODE — SCAN INI!</div>
                """, unsafe_allow_html=True)
                with st.spinner("Membuat QR..."):
                    qr_img = generate_qr(product_url, box_size=7)
                st.image(qr_img, use_container_width=True)
                st.caption(f"🔗 {product_url}")

            with col_bc:
                st.markdown("""
                <div style='text-align:center;font-family:Space Mono,monospace;
                font-size:9px;letter-spacing:2px;color:#E8650A;font-weight:700;margin-bottom:6px'>
                BARCODE PRODUK</div>
                """, unsafe_allow_html=True)
                with st.spinner("Membuat Barcode..."):
                    bc_img = generate_barcode(p["barcode"])
                st.image(bc_img, use_container_width=True)
                st.caption(f"EAN-13: {p['barcode']}")

            with col_info:
                discount = round((1 - p["price"] / p["price_ori"]) * 100)
                badges = ""
                if p.get("halal"):
                    badges += '<span class="badge-halal">✓ HALAL</span> '
                badges += '<span class="badge-pirt">PIRT</span>'

                st.markdown(f"""
                <div style='background:#FFF8EE;border-radius:12px;padding:16px;'>
                  <div>{badges}</div>
                  <div style='font-family:Georgia,serif;font-size:20px;font-weight:900;
                  color:#3E2000;margin:8px 0 2px'>{p['name']}</div>
                  <div style='font-size:11px;color:#E8650A;font-weight:700;
                  letter-spacing:2px;margin-bottom:6px'>CECILIA SNACK • {p['weight']}</div>
                  <div style='font-size:13px;color:#7A5C3A;margin-bottom:10px'>{p['desc']}</div>

                  <div style='display:flex;align-items:center;gap:12px;margin-bottom:10px'>
                    <span style='font-size:22px;font-weight:900;color:#3E2000'>
                      Rp {p['price']:,}
                    </span>
                    <span style='font-size:16px;font-weight:700;color:#E8650A'>-{discount}%</span>
                    <span style='font-size:12px;color:#999;text-decoration:line-through'>
                      Rp {p['price_ori']:,}
                    </span>
                  </div>
                  {''.join([f"<div style='font-size:12px;color:#7A5C3A;padding:4px 0;border-bottom:1px solid #F0E6D6'><b>{l}</b>: {v}</div>" for l, v in [('🌿 Bahan', p['ingredients']), ('📅 Masa Simpan', p['expired']), ('📋 PIRT', p['pirt'])]])}
                </div>
                """.replace(",", "."), unsafe_allow_html=True)

                st.markdown(f"""
                <a href="{wa_url}" target="_blank" style='
                  display:inline-block;margin-top:10px;
                  background:#25D366;color:white;text-decoration:none;
                  padding:10px 20px;border-radius:9px;font-weight:800;font-size:13px;
                '>💬 Pesan via WhatsApp</a>
                """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box" style="margin-top:24px;">
    <p>
    💡 <strong>Tips:</strong> QR Code di atas bisa langsung di-scan menggunakan kamera HP!
    Coba arahkan kamera ke QR Code salah satu produk untuk melihat halaman produk digital Cecilia Snack.
    </p>
    </div>
    """, unsafe_allow_html=True)


# ─── FOOTER ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
  <span>Cecilia Snack × INDI 4.0</span>
  <p>Digitalisasi UMKM • QR Code & Barcode Generator<br>
  Proyek Teknologi Informasi — Peningkatan Indeks INDI 4.0</p>
</div>
""", unsafe_allow_html=True)
