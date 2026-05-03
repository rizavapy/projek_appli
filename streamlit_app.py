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

import { useState, useRef, useEffect } from "react";

const PRODUCTS = [
  {
    id: "CS001",
    name: "Keripik Singkong",
    brand: "Cecilia Snack",
    weight: "250g",
    price: 12000,
    priceOri: 15000,
    emoji: "🥔",
    bg: "linear-gradient(135deg,#FFF3E0,#FFE0B2)",
    halal: true,
    pirt: "P-IRT No. 2153578010488-22",
    expired: "12 bulan",
    ingredients: "Singkong, Minyak Nabati, Garam, Bumbu",
    desc: "Keripik singkong renyah dengan bumbu gurih khas Jawa.",
    barcode: "8993012200140",
    wa: "6285776126900",
  },
  {
    id: "CS002",
    name: "Keripik Pisang",
    brand: "Cecilia Snack",
    weight: "200g",
    price: 10000,
    priceOri: 13000,
    emoji: "🍌",
    bg: "linear-gradient(135deg,#FFFDE7,#FFF9C4)",
    halal: true,
    pirt: "P-IRT No. 2153578010488-23",
    expired: "10 bulan",
    ingredients: "Pisang, Minyak Nabati, Gula, Garam",
    desc: "Keripik pisang manis legit, dibuat dari pisang pilihan.",
    barcode: "8993012200157",
    wa: "6285776126900",
  },
  {
    id: "CS003",
    name: "Kue Bawang",
    brand: "Cecilia Snack",
    weight: "150g",
    price: 8000,
    priceOri: 10000,
    emoji: "🧅",
    bg: "linear-gradient(135deg,#F3E5F5,#EDE7F6)",
    halal: true,
    pirt: "P-IRT No. 2153578010488-24",
    expired: "8 bulan",
    ingredients: "Tepung Terigu, Bawang Putih, Telur, Minyak, Garam",
    desc: "Kue bawang gurih dan renyah, cocok untuk cemilan keluarga.",
    barcode: "8993012200164",
    wa: "6285776126900",
  },
  {
    id: "CS004",
    name: "Rempeyek Kacang",
    brand: "Cecilia Snack",
    weight: "180g",
    price: 11000,
    priceOri: 14000,
    emoji: "🥜",
    bg: "linear-gradient(135deg,#E8F5E9,#C8E6C9)",
    halal: true,
    pirt: "P-IRT No. 2153578010488-25",
    expired: "9 bulan",
    ingredients: "Tepung Beras, Kacang Tanah, Santan, Bumbu Rempah",
    desc: "Rempeyek kacang tanah renyah dengan aroma rempah yang khas.",
    barcode: "8993012200171",
    wa: "6285776126900",
  },
];

// ---- Mini QR Matrix Generator (visual only, functional via URL) ----
function generateQRMatrix(size = 21) {
  // Deterministic pseudorandom for visual QR-like pattern
  const matrix = Array.from({ length: size }, () => Array(size).fill(0));
  // Finder patterns
  const finder = (r, c) => {
    for (let i = 0; i < 7; i++) for (let j = 0; j < 7; j++) {
      const v = (i === 0 || i === 6 || j === 0 || j === 6) ? 1 : (i >= 2 && i <= 4 && j >= 2 && j <= 4) ? 1 : 0;
      if (r + i < size && c + j < size) matrix[r + i][c + j] = v;
    }
  };
  finder(0, 0); finder(0, size - 7); finder(size - 7, 0);
  // Fill rest with pattern
  for (let i = 0; i < size; i++) for (let j = 0; j < size; j++) {
    if (matrix[i][j] === 0) matrix[i][j] = ((i * 3 + j * 7 + i * j) % 5 < 2) ? 1 : 0;
  }
  return matrix;
}

const QR_MATRIX = generateQRMatrix(21);

function QRCode({ url, size = 120, product }) {
  // Use Google Charts API for real scannable QR
  const qrUrl = `https://api.qrserver.com/v1/create-qr-code/?size=${size}x${size}&data=${encodeURIComponent(url)}&color=3E2000&bgcolor=FFFDF8`;
  return (
    <div style={{ textAlign: "center" }}>
      <img
        src={qrUrl}
        alt="QR Code"
        width={size}
        height={size}
        style={{ borderRadius: 8, border: "2px solid #3E2000", display: "block", margin: "0 auto" }}
        onError={(e) => {
          // Fallback visual QR
          e.target.style.display = "none";
        }}
      />
    </div>
  );
}

function Barcode({ code, width = 200, height = 60 }) {
  const canvasRef = useRef(null);
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    ctx.fillStyle = "#FFFDF8";
    ctx.fillRect(0, 0, width, height);

    // EAN-13 like visual barcode
    const digits = code.slice(0, 13).padEnd(13, "0");
    const bars = [];
    // Encode digits to bars (simplified visual)
    const enc = [
      [3,2,1,1],[2,2,2,1],[2,1,2,2],[1,4,1,1],[1,1,3,2],
      [1,2,3,1],[1,1,1,4],[1,3,1,2],[1,2,1,3],[3,1,1,2]
    ];
    bars.push(1,0,1); // start
    for (let i = 1; i < 7; i++) {
      const d = parseInt(digits[i]);
      enc[d].forEach((w, idx) => {
        for (let k = 0; k < w; k++) bars.push(idx % 2 === 0 ? 1 : 0);
      });
    }
    bars.push(0,1,0,1,0); // middle
    for (let i = 7; i < 13; i++) {
      const d = parseInt(digits[i]);
      enc[d].forEach((w, idx) => {
        for (let k = 0; k < w; k++) bars.push(idx % 2 === 0 ? 0 : 1);
      });
    }
    bars.push(1,0,1); // end

    const barW = (width - 20) / bars.length;
    bars.forEach((b, i) => {
      if (b) {
        ctx.fillStyle = "#3E2000";
        ctx.fillRect(10 + i * barW, 5, Math.max(barW - 0.3, 0.7), height - 18);
      }
    });

    // Digit text
    ctx.fillStyle = "#3E2000";
    ctx.font = `bold ${Math.floor(height * 0.18)}px 'Courier New', monospace`;
    ctx.textAlign = "center";
    const spacing = (width - 20) / 13;
    for (let i = 0; i < 13; i++) {
      ctx.fillText(digits[i], 10 + (i + 0.5) * spacing, height - 2);
    }
  }, [code, width, height]);

  return <canvas ref={canvasRef} width={width} height={height} style={{ display: "block", margin: "0 auto" }} />;
}

function ProductPage({ product, onBack }) {
  const waMsg = encodeURIComponent(`Halo Cecilia Snack! Saya ingin memesan *${product.name}* (${product.weight}) Rp ${product.price.toLocaleString("id-ID")}`);
  const waUrl = `https://wa.me/${product.wa}?text=${waMsg}`;
  const productUrl = `https://ceciliasnack.id/produk/${product.id.toLowerCase()}`;

  return (
    <div style={{
      minHeight: "100vh",
      background: "#FFF8EE",
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      padding: "0 0 40px",
      fontFamily: "'DM Sans', sans-serif",
    }}>
      {/* Header */}
      <div style={{
        width: "100%",
        background: "linear-gradient(135deg,#3E2000,#E8650A)",
        color: "white",
        padding: "20px 24px 16px",
        display: "flex",
        alignItems: "center",
        gap: 12,
      }}>
        <button onClick={onBack} style={{
          background: "rgba(255,255,255,0.2)", border: "none", color: "white",
          borderRadius: 8, padding: "6px 12px", cursor: "pointer", fontSize: 14, fontWeight: 700,
        }}>← Kembali</button>
        <div>
          <div style={{ fontSize: 18, fontWeight: 900, fontFamily: "Georgia, serif" }}>Cecilia Snack</div>
          <div style={{ fontSize: 11, opacity: 0.8 }}>Halaman Produk Digital</div>
        </div>
      </div>

      {/* Product Image Area */}
      <div style={{
        width: "100%", maxWidth: 420,
        background: product.bg,
        display: "flex", alignItems: "center", justifyContent: "center",
        fontSize: 96, padding: "32px 0",
      }}>
        {product.emoji}
      </div>

      {/* Info */}
      <div style={{ width: "100%", maxWidth: 420, padding: "0 20px" }}>
        {/* Badges */}
        <div style={{ display: "flex", gap: 8, marginTop: 16, marginBottom: 12 }}>
          {product.halal && (
            <span style={{ background: "#1A5C2A", color: "white", fontSize: 11, fontWeight: 700, padding: "4px 10px", borderRadius: 4 }}>✓ HALAL</span>
          )}
          <span style={{ background: "#3E2000", color: "white", fontSize: 11, fontWeight: 700, padding: "4px 10px", borderRadius: 4 }}>PIRT</span>
          <span style={{ background: "#E8650A", color: "white", fontSize: 11, fontWeight: 700, padding: "4px 10px", borderRadius: 4 }}>UMKM</span>
        </div>

        <h1 style={{ fontFamily: "Georgia, serif", fontSize: 28, fontWeight: 900, color: "#3E2000", margin: "0 0 4px" }}>{product.name}</h1>
        <div style={{ color: "#E8650A", fontSize: 12, fontWeight: 700, letterSpacing: 2, marginBottom: 8 }}>{product.brand} • {product.weight}</div>
        <p style={{ color: "#7A5C3A", fontSize: 14, lineHeight: 1.7, marginBottom: 16 }}>{product.desc}</p>

        {/* Price */}
        <div style={{
          background: "white", borderRadius: 12, padding: "16px 20px",
          display: "flex", alignItems: "center", justifyContent: "space-between",
          boxShadow: "0 4px 20px rgba(62,32,0,0.12)", marginBottom: 16,
        }}>
          <div>
            <div style={{ fontSize: 11, color: "#7A5C3A", marginBottom: 4 }}>Harga Promo</div>
            <div style={{ fontSize: 26, fontWeight: 900, color: "#3E2000" }}>Rp {product.price.toLocaleString("id-ID")}</div>
            <div style={{ fontSize: 12, color: "#999", textDecoration: "line-through" }}>Rp {product.priceOri.toLocaleString("id-ID")}</div>
          </div>
          <div style={{ textAlign: "right" }}>
            <div style={{ fontSize: 20, fontWeight: 900, color: "#E8650A" }}>
              -{Math.round((1 - product.price / product.priceOri) * 100)}%
            </div>
            <div style={{ fontSize: 11, color: "#7A5C3A" }}>Hemat Rp {(product.priceOri - product.price).toLocaleString("id-ID")}</div>
          </div>
        </div>

        {/* Details */}
        <div style={{ background: "white", borderRadius: 12, padding: "16px 20px", marginBottom: 16, boxShadow: "0 4px 20px rgba(62,32,0,0.08)" }}>
          <div style={{ fontWeight: 700, fontSize: 13, color: "#3E2000", marginBottom: 12 }}>Informasi Produk</div>
          {[
            ["🏷️ Kode Produk", product.id],
            ["🌿 Bahan", product.ingredients],
            ["📅 Masa Simpan", product.expired],
            ["📋 Sertifikasi", product.pirt],
          ].map(([label, val]) => (
            <div key={label} style={{ display: "flex", gap: 10, padding: "8px 0", borderBottom: "1px solid #F0E6D6", fontSize: 13 }}>
              <span style={{ minWidth: 110, color: "#7A5C3A" }}>{label}</span>
              <span style={{ color: "#3E2000", fontWeight: 500 }}>{val}</span>
            </div>
          ))}
        </div>

        {/* Barcode display */}
        <div style={{ background: "white", borderRadius: 12, padding: "16px", marginBottom: 16, textAlign: "center", boxShadow: "0 4px 20px rgba(62,32,0,0.08)" }}>
          <div style={{ fontSize: 11, color: "#7A5C3A", marginBottom: 8 }}>Barcode Produk</div>
          <Barcode code={product.barcode} width={240} height={52} />
        </div>

        {/* Order Button */}
        <a href={waUrl} target="_blank" rel="noopener noreferrer" style={{
          display: "block", background: "#25D366", color: "white",
          textAlign: "center", padding: "16px", borderRadius: 12,
          fontWeight: 800, fontSize: 15, textDecoration: "none",
          marginBottom: 10, boxShadow: "0 4px 20px rgba(37,211,102,0.4)",
        }}>
          💬 Pesan via WhatsApp
        </a>
      </div>
    </div>
  );
}// ---- MAIN APP ----
export default function CeciliaQRApp() {
  const [tab, setTab] = useState("generator"); // generator | scanner-sim | product
  const [selected, setSelected] = useState(null);
  const [scannedProduct, setScannedProduct] = useState(null);
  const [customProduct, setCustomProduct] = useState({
    name: "", price: "", weight: "", desc: "", barcode: "", wa: "6281234567890",
  });
  const [qrGenerated, setQrGenerated] = useState(false);
  const [activeScan, setActiveScan] = useState(null);

  // If viewing a product page (simulating QR scan result)
  if (scannedProduct) {
    return <ProductPage product={scannedProduct} onBack={() => setScannedProduct(null)} />;
  }

  const handleGenerateQR = () => {
    if (!selected && !customProduct.name) return;
    setQrGenerated(true);
  };

  const currentProduct = selected !== null ? PRODUCTS[selected] : null;
  const productUrl = currentProduct
    ? `https://ceciliasnack.id/produk/${currentProduct.id.toLowerCase()}`
    : customProduct.name
    ? `https://ceciliasnack.id/produk/custom-${customProduct.name.toLowerCase().replace(/\s+/g, "-")}`
    : "";

  return (
    <div style={{ minHeight: "100vh", background: "#FFF8EE", fontFamily: "'DM Sans', sans-serif", color: "#3E2000" }}>
      {/* Header */}
      <div style={{
        background: "linear-gradient(135deg,#3E2000 0%,#6B3500 60%,#E8650A 100%)",
        color: "white", padding: "28px 24px 24px", textAlign: "center",
      }}>
        <div style={{
          display: "inline-block", background: "#E8650A", fontSize: 10, letterSpacing: 3,
          padding: "5px 16px", borderRadius: 2, marginBottom: 12, fontWeight: 700,
        }}>INDI 4.0 — CECILIA SNACK</div>
        <h1 style={{ fontFamily: "Georgia, serif", fontSize: 32, fontWeight: 900, margin: "0 0 8px" }}>
          🍟 Generator QR & Barcode
        </h1>
        <p style={{ fontSize: 14, opacity: 0.85 }}>Buat QR Code yang bisa di-scan, tampilkan info produk langsung</p>
      </div>

      {/* Tabs */}
      <div style={{ display: "flex", background: "white", borderBottom: "2px solid #F0E6D6" }}>
        {[
          { key: "generator", label: "🎨 Buat QR/Barcode" },
          { key: "scanner", label: "📱 Simulasi Scan" },
        ].map(t => (
          <button key={t.key} onClick={() => { setTab(t.key); setQrGenerated(false); }}
            style={{
              flex: 1, padding: "14px 8px", border: "none", cursor: "pointer",
              fontWeight: 700, fontSize: 13,
              background: tab === t.key ? "#FFF8EE" : "white",
              color: tab === t.key ? "#E8650A" : "#7A5C3A",
              borderBottom: tab === t.key ? "3px solid #E8650A" : "3px solid transparent",
            }}>
            {t.label}
          </button>
        ))}
      </div>

      {/* TAB: GENERATOR */}
      {tab === "generator" && (
        <div style={{ padding: "24px 20px", maxWidth: 700, margin: "0 auto" }}>
          <h2 style={{ fontFamily: "Georgia, serif", fontSize: 20, marginBottom: 6 }}>Pilih Produk</h2>
          <p style={{ fontSize: 13, color: "#7A5C3A", marginBottom: 16 }}>Pilih produk Cecilia Snack atau isi data custom</p>

          {/* Product Selector */}
          <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 12, marginBottom: 20 }}>
            {PRODUCTS.map((p, i) => (
              <div key={p.id} onClick={() => { setSelected(i); setCustomProduct({ name: "", price: "", weight: "", desc: "", barcode: "", wa: "6281234567890" }); setQrGenerated(false); }}
                style={{
                  background: selected === i ? "#FFF3E0" : "white",
                  border: selected === i ? "2px solid #E8650A" : "2px solid #F0E6D6",
                  borderRadius: 12, padding: "14px", cursor: "pointer",
                  display: "flex", alignItems: "center", gap: 10,
                  transition: "all 0.2s",
                }}>
                <span style={{ fontSize: 32 }}>{p.emoji}</span>
                <div>
                  <div style={{ fontWeight: 700, fontSize: 14 }}>{p.name}</div>
                  <div style={{ fontSize: 12, color: "#7A5C3A" }}>{p.weight} • Rp {p.price.toLocaleString("id-ID")}</div>
                </div>
              </div>
            ))}
          </div>

          {/* Custom Product Form */}
          <div style={{ background: "white", borderRadius: 14, padding: "20px", marginBottom: 20, border: "2px solid #F0E6D6" }}>
            <div style={{ fontWeight: 700, fontSize: 14, marginBottom: 14, color: "#3E2000" }}>✏️ Atau Isi Produk Custom</div>
            {[
              { key: "name", label: "Nama Produk", placeholder: "cth: Keripik Tempe Pedas" },
              { key: "price", label: "Harga (Rp)", placeholder: "cth: 15000" },
              { key: "weight", label: "Berat / Ukuran", placeholder: "cth: 200g" },
              { key: "desc", label: "Deskripsi Singkat", placeholder: "cth: Keripik tempe renyah..." },
              { key: "barcode", label: "Nomor Barcode (13 digit)", placeholder: "cth: 8993012200188" },
              { key: "wa", label: "No. WhatsApp (62xxx)", placeholder: "6281234567890" },
            ].map(f => (
              <div key={f.key} style={{ marginBottom: 12 }}>
                <label style={{ fontSize: 12, fontWeight: 600, color: "#7A5C3A", display: "block", marginBottom: 4 }}>{f.label}</label>
                <input
                  type="text"
                  placeholder={f.placeholder}
                  value={customProduct[f.key]}
                  onChange={e => { setSelected(null); setCustomProduct(p => ({ ...p, [f.key]: e.target.value })); setQrGenerated(false); }}
                  style={{
                    width: "100%", padding: "10px 12px", borderRadius: 8,
                    border: "1.5px solid #E8DDD0", fontSize: 14, outline: "none",
                    fontFamily: "inherit", color: "#3E2000", background: "#FFFDF8",
                    boxSizing: "border-box",
                  }}
                />
              </div>
            ))}
          </div>

          {/* Generate Button */}
          <button onClick={handleGenerateQR}
            disabled={!selected && selected !== 0 && !customProduct.name}
            style={{
              width: "100%", padding: "16px", background: "#E8650A", color: "white",
              border: "none", borderRadius: 12, fontWeight: 800, fontSize: 16,
              cursor: "pointer", marginBottom: 24,
              opacity: (!selected && selected !== 0 && !customProduct.name) ? 0.5 : 1,
            }}>
            🎯 Generate QR Code & Barcode
          </button>

          {/* Generated Output */}
          {qrGenerated && (currentProduct || customProduct.name) && (() => {
            const prod = currentProduct || {
              id: "CUSTOM",
              name: customProduct.name,
              price: parseInt(customProduct.price) || 0,
              priceOri: parseInt(customProduct.price) || 0,
              weight: customProduct.weight,
              desc: customProduct.desc,
              emoji: "🍿",
              bg: "linear-gradient(135deg,#FFF3E0,#FFE0B2)",
              halal: false,
              pirt: "-",
              expired: "-",
              ingredients: "-",
              barcode: customProduct.barcode || "8993012200100",
              wa: customProduct.wa,
            };
            const url = `https://ceciliasnack.id/produk/${prod.id.toLowerCase()}`;

            return (
              <div style={{ background: "white", borderRadius: 16, padding: "24px", boxShadow: "0 8px 32px rgba(62,32,0,0.12)" }}>
                <div style={{ textAlign: "center", marginBottom: 20 }}>
                  <div style={{ fontSize: 11, letterSpacing: 3, color: "#E8650A", fontWeight: 700, marginBottom: 8 }}>HASIL GENERATE</div>
                  <h3 style={{ fontFamily: "Georgia, serif", fontSize: 22, margin: "0 0 4px" }}>{prod.name}</h3>
                  <div style={{ fontSize: 13, color: "#7A5C3A" }}>{prod.weight} • Rp {prod.price.toLocaleString("id-ID")}</div>
                </div>

                {/* QR Code */}
                <div style={{ textAlign: "center", marginBottom: 20, background: "#FFFDF8", borderRadius: 12, padding: 20 }}>
                  <div style={{ fontSize: 12, fontWeight: 700, color: "#7A5C3A", marginBottom: 12, letterSpacing: 1 }}>📱 QR CODE — BISA DI-SCAN!</div>
                  <QRCode url={url} size={160} product={prod} />
                  <div style={{ fontSize: 11, color: "#7A5C3A", marginTop: 10, wordBreak: "break-all", padding: "0 10px" }}>
                    🔗 {url}
                  </div>
                  <div style={{ marginTop: 10, fontSize: 12, background: "#E8F5E9", color: "#1A5C2A", padding: "8px 12px", borderRadius: 8, fontWeight: 600 }}>
                    ✅ Scan QR di atas untuk melihat halaman produk
                  </div>
                </div>

                {/* Barcode */}
                <div style={{ textAlign: "center", background: "#FFFDF8", borderRadius: 12, padding: "16px", marginBottom: 16 }}>
                  <div style={{ fontSize: 12, fontWeight: 700, color: "#7A5C3A", marginBottom: 10, letterSpacing: 1 }}>📊 BARCODE PRODUK</div>
                  <div style={{ background: "white", display: "inline-block", padding: "12px 16px", borderRadius: 8, border: "1.5px solid #E8DDD0" }}>
                    <Barcode code={prod.barcode} width={220} height={56} />
                  </div>
                </div>

                {/* Label Preview */}
                <div style={{ border: "2px dashed #E8650A", borderRadius: 12, padding: 16, marginBottom: 16 }}>
                  <div style={{ fontSize: 11, letterSpacing: 2, color: "#E8650A", fontWeight: 700, marginBottom: 10 }}>🏷️ PREVIEW LABEL KEMASAN</div>
                  <div style={{
                    background: prod.bg, borderRadius: 10, padding: "16px",
                    display: "flex", gap: 14, alignItems: "center",
                  }}>
                    <span style={{ fontSize: 48 }}>{prod.emoji}</span>
                    <div style={{ flex: 1 }}>
                      <div style={{ fontFamily: "Georgia, serif", fontWeight: 900, fontSize: 16, color: "#3E2000" }}>{prod.name}</div>
                      <div style={{ fontSize: 11, color: "#E8650A", fontWeight: 700, letterSpacing: 1 }}>CECILIA SNACK</div>
                      <div style={{ fontSize: 20, fontWeight: 900, color: "#3E2000", margin: "4px 0" }}>Rp {prod.price.toLocaleString("id-ID")}</div>
                      <div style={{ display: "flex", gap: 6 }}>
                        {prod.halal && <span style={{ background: "#1A5C2A", color: "white", fontSize: 9, fontWeight: 700, padding: "2px 6px", borderRadius: 3 }}>HALAL</span>}
                        <span style={{ background: "#3E2000", color: "white", fontSize: 9, fontWeight: 700, padding: "2px 6px", borderRadius: 3 }}>PIRT</span>
                      </div>
                    </div>
                    <div>
                      <QRCode url={url} size={70} product={prod} />
                      <div style={{ fontSize: 8, color: "#7A5C3A", textAlign: "center", marginTop: 3 }}>Scan untuk info</div>
                    </div>
                  </div>
                </div>

                {/* Simulate scan button */}
                <button onClick={() => setScannedProduct(currentProduct || { ...prod, id: "CUSTOM" })}
                  style={{
                    width: "100%", padding: "14px", background: "#3E2000", color: "white",
                    border: "none", borderRadius: 12, fontWeight: 800, fontSize: 14, cursor: "pointer",
                  }}>
                  📱 Simulasikan Hasil Scan QR →
                </button>
              </div>
            );
          })()}
        </div>
      )}

      {/* TAB: SCANNER SIMULATOR */}
      {tab === "scanner" && (
        <div style={{ padding: "24px 20px", maxWidth: 700, margin: "0 auto" }}>
          <h2 style={{ fontFamily: "Georgia, serif", fontSize: 20, marginBottom: 6 }}>Simulasi Scan QR</h2>
          <p style={{ fontSize: 13, color: "#7A5C3A", marginBottom: 20 }}>
            Tap produk untuk melihat tampilan halaman yang muncul saat QR di-scan konsumen
          </p>

          <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
            {PRODUCTS.map((p, i) => {
              const url = `https://ceciliasnack.id/produk/${p.id.toLowerCase()}`;
              return (
                <div key={p.id} style={{
                  background: "white", borderRadius: 14, overflow: "hidden",
                  boxShadow: "0 4px 20px rgba(62,32,0,0.10)", border: "1.5px solid #F0E6D6",
                }}>
                  <div style={{ display: "flex", gap: 0 }}>
                    {/* Product Info */}
                    <div style={{ flex: 1, padding: "16px 16px" }}>
                      <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 10 }}>
                        <span style={{ fontSize: 36 }}>{p.emoji}</span>
                        <div>
                          <div style={{ fontWeight: 800, fontSize: 15 }}>{p.name}</div>
                          <div style={{ fontSize: 12, color: "#E8650A", fontWeight: 600 }}>{p.weight} • Rp {p.price.toLocaleString("id-ID")}</div>
                        </div>
                      </div>
                      <div style={{ marginBottom: 10 }}>
                        <QRCode url={url} size={90} product={p} />
                        <div style={{ fontSize: 9, color: "#7A5C3A", textAlign: "center", marginTop: 4 }}>QR Bisa Di-scan Langsung</div>
                      </div>
                      <div style={{ background: "#F5E6C8", borderRadius: 8, padding: "6px 10px", marginBottom: 8 }}>
                        <Barcode code={p.barcode} width={160} height={36} />
                      </div>
                      <button onClick={() => setScannedProduct(p)}
                        style={{
                          width: "100%", padding: "10px", background: "#E8650A", color: "white",
                          border: "none", borderRadius: 8, fontWeight: 700, fontSize: 12, cursor: "pointer",
                        }}>
                        📱 Lihat Halaman Produk →
                      </button>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          <div style={{
            marginTop: 24, background: "#E8F5E9", borderRadius: 12, padding: "16px",
            border: "1.5px solid #A5D6A7",
          }}>
            <div style={{ fontWeight: 700, fontSize: 13, color: "#1A5C2A", marginBottom: 6 }}>💡 Cara Pakai QR Code Asli</div>
            <ol style={{ fontSize: 12, color: "#3E2000", paddingLeft: 16, lineHeight: 2 }}>
              <li>Generate QR di tab "Buat QR/Barcode"</li>
              <li>Screenshot atau download gambar QR</li>
              <li>Print dan tempel ke kemasan produk</li>
              <li>Konsumen scan → langsung dapat info produk!</li>
            </ol>
          </div>
        </div>
      )}

      {/* Footer */}
      <div style={{
        background: "#3E2000", color: "rgba(255,255,255,0.7)",
        padding: "24px", textAlign: "center", marginTop: 40,
      }}>
        <div style={{ color: "#FFD580", fontFamily: "Georgia, serif", fontSize: 18, marginBottom: 4 }}>Cecilia Snack × INDI 4.0</div>
        <div style={{ fontSize: 12 }}>Digitalisasi UMKM • QR Code & Barcode Generator</div>
      </div>
    </div>
  );
}
