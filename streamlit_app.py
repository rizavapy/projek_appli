import streamlit as st

st.set_page_config(
    page_title="Cecilia Snack - Proyek Solusi QR Label",
    page_icon="🍟",
    layout="wide"
)

html_content = """<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;0,900;1,700&family=DM+Sans:wght@300;400;500;600&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
  :root {
    --cream: #FDF6EC;
    --warm-brown: #5C3D1E;
    --orange: #E8722A;
    --orange-light: #F2A35A;
    --gold: #C9963A;
    --green: #3A6B35;
    --green-light: #5A9E52;
    --red: #C0392B;
    --dark: #1A0F05;
    --text-mid: #4A3020;
  }
  * { margin: 0; padding: 0; box-sizing: border-box; }
  body {
    font-family: 'DM Sans', sans-serif;
    background: #1a0f05;
    color: var(--cream);
    overflow-x: hidden;
  }
  .tabs {
    position: sticky;
    top: 0;
    z-index: 100;
    display: flex;
    background: rgba(28, 15, 5, 0.95);
    backdrop-filter: blur(12px);
    border-bottom: 1px solid rgba(201,150,58,0.3);
    padding: 0 2rem;
  }
  .tab-btn {
    padding: 1rem 1.5rem;
    background: none;
    border: none;
    color: rgba(253,246,236,0.5);
    font-family: 'DM Sans', sans-serif;
    font-size: 0.85rem;
    font-weight: 500;
    cursor: pointer;
    letter-spacing: 0.05em;
    border-bottom: 2px solid transparent;
    transition: all 0.3s;
    text-transform: uppercase;
  }
  .tab-btn.active, .tab-btn:hover { color: var(--gold); border-bottom-color: var(--gold); }
  .page { display: none; min-height: 100vh; }
  .page.active { display: block; }

  /* PAGE 1 */
  #poster { background: var(--cream); color: var(--dark); min-height: 100vh; position: relative; overflow: hidden; }
  .poster-inner { max-width: 800px; margin: 0 auto; padding: 3rem 2rem; position: relative; z-index: 2; }
  .poster-badge { display: inline-flex; align-items: center; gap: 0.5rem; background: var(--green); color: white; padding: 0.4rem 1rem; border-radius: 99px; font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 1.5rem; }
  .poster-eyebrow { font-family: 'Space Mono', monospace; font-size: 0.7rem; letter-spacing: 0.2em; color: var(--orange); text-transform: uppercase; margin-bottom: 0.5rem; }
  .poster-headline { font-family: 'Playfair Display', serif; font-size: clamp(2.5rem, 6vw, 4rem); font-weight: 900; line-height: 1.1; color: var(--warm-brown); }
  .poster-headline span { color: var(--orange); font-style: italic; }
  .poster-sub { font-size: 1.05rem; color: var(--text-mid); margin-top: 1rem; line-height: 1.6; max-width: 560px; }
  .poster-divider { width: 60px; height: 3px; background: linear-gradient(90deg, var(--orange), var(--gold)); margin: 1.5rem 0; border-radius: 2px; }
  .problem-solution { display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin: 2rem 0; }
  .ps-box { padding: 1.5rem; border-radius: 12px; }
  .ps-box.problem { background: #FDE8E8; border-left: 4px solid var(--red); }
  .ps-box.solution { background: #E8F5E8; border-left: 4px solid var(--green); }
  .ps-label { font-family: 'Space Mono', monospace; font-size: 0.65rem; letter-spacing: 0.15em; text-transform: uppercase; font-weight: 700; margin-bottom: 0.75rem; }
  .ps-box.problem .ps-label { color: var(--red); }
  .ps-box.solution .ps-label { color: var(--green); }
  .ps-items { list-style: none; }
  .ps-items li { font-size: 0.88rem; color: var(--text-mid); padding: 0.3rem 0; display: flex; align-items: flex-start; gap: 0.5rem; line-height: 1.4; }
  .ps-items li::before { flex-shrink: 0; margin-top: 2px; }
  .ps-box.problem .ps-items li::before { content: "✗"; color: var(--red); font-weight: 700; }
  .ps-box.solution .ps-items li::before { content: "✓"; color: var(--green); font-weight: 700; }
  .qr-section { background: var(--warm-brown); color: var(--cream); border-radius: 16px; padding: 2rem; margin: 2rem 0; display: grid; grid-template-columns: auto 1fr; gap: 2rem; align-items: center; }
  .qr-box { width: 120px; height: 120px; background: white; border-radius: 8px; display: flex; align-items: center; justify-content: center; flex-direction: column; gap: 0.25rem; flex-shrink: 0; }
  .qr-pattern { display: grid; grid-template-columns: repeat(7, 1fr); gap: 1.5px; width: 80px; height: 80px; }
  .qr-cell { background: #000; border-radius: 0.5px; }
  .qr-cell.white { background: white; }
  .qr-label-text { font-size: 0.55rem; color: #333; font-family: 'Space Mono', monospace; letter-spacing: 0.05em; }
  .qr-info h3 { font-family: 'Playfair Display', serif; font-size: 1.4rem; margin-bottom: 0.5rem; color: var(--gold); }
  .qr-info p { font-size: 0.88rem; line-height: 1.6; color: rgba(253,246,236,0.8); margin-bottom: 1rem; }
  .qr-features { display: flex; flex-wrap: wrap; gap: 0.5rem; }
  .qr-tag { background: rgba(201,150,58,0.2); border: 1px solid rgba(201,150,58,0.4); color: var(--gold); padding: 0.3rem 0.8rem; border-radius: 99px; font-size: 0.72rem; font-weight: 500; letter-spacing: 0.05em; }
  .info-flow { margin: 2rem 0; }
  .info-flow h3 { font-family: 'Playfair Display', serif; font-size: 1.3rem; color: var(--warm-brown); margin-bottom: 1rem; }
  .flow-steps { display: flex; align-items: center; flex-wrap: wrap; gap: 0.5rem; }
  .flow-step { flex: 1; min-width: 140px; background: white; border: 1px solid rgba(92,61,30,0.15); border-radius: 10px; padding: 1rem; text-align: center; box-shadow: 0 2px 8px rgba(92,61,30,0.08); }
  .step-num { width: 28px; height: 28px; background: var(--orange); color: white; border-radius: 50%; font-size: 0.75rem; font-weight: 700; display: flex; align-items: center; justify-content: center; margin: 0 auto 0.5rem; font-family: 'Space Mono', monospace; }
  .step-icon { font-size: 1.5rem; margin-bottom: 0.3rem; }
  .step-title { font-size: 0.8rem; font-weight: 600; color: var(--warm-brown); margin-bottom: 0.25rem; }
  .step-desc { font-size: 0.72rem; color: var(--text-mid); line-height: 1.4; }
  .flow-arrow { color: var(--orange-light); font-size: 1.2rem; flex-shrink: 0; }
  .indi-section { margin: 2rem 0; }
  .indi-section h3 { font-family: 'Playfair Display', serif; font-size: 1.3rem; color: var(--warm-brown); margin-bottom: 1rem; }
  .indi-bars { display: flex; flex-direction: column; gap: 0.75rem; }
  .indi-bar-row { display: grid; grid-template-columns: 160px 1fr 60px; align-items: center; gap: 0.75rem; }
  .indi-bar-label { font-size: 0.78rem; color: var(--text-mid); font-weight: 500; }
  .indi-bar-track { height: 10px; background: #EDE0CF; border-radius: 99px; overflow: hidden; }
  .indi-bar-fill { height: 100%; border-radius: 99px; }
  .bar-after { background: linear-gradient(90deg, var(--green), var(--green-light)); }
  .indi-bar-val { font-family: 'Space Mono', monospace; font-size: 0.75rem; font-weight: 700; text-align: right; }
  .bar-after-val { color: var(--green); }
  .indi-legend { display: flex; gap: 1.5rem; margin-bottom: 1rem; }
  .legend-item { display: flex; align-items: center; gap: 0.4rem; font-size: 0.75rem; color: var(--text-mid); }
  .legend-dot { width: 10px; height: 10px; border-radius: 50%; }
  .poster-footer { background: var(--warm-brown); color: var(--cream); padding: 1.5rem 2rem; border-radius: 12px; display: flex; justify-content: space-between; align-items: center; margin-top: 2rem; flex-wrap: wrap; gap: 1rem; }
  .footer-brand { font-family: 'Playfair Display', serif; font-size: 1.2rem; color: var(--gold); }
  .footer-brand span { display: block; font-family: 'DM Sans', sans-serif; font-size: 0.75rem; color: rgba(253,246,236,0.6); font-style: normal; margin-top: 0.1rem; }
  .footer-tag { font-family: 'Space Mono', monospace; font-size: 0.7rem; letter-spacing: 0.1em; color: var(--orange-light); text-transform: uppercase; }
  .bg-deco { position: absolute; border-radius: 50%; opacity: 0.04; pointer-events: none; }
  .bg-deco-1 { width: 400px; height: 400px; background: var(--orange); top: -100px; right: -100px; }
  .bg-deco-2 { width: 300px; height: 300px; background: var(--green); bottom: 50px; left: -80px; }

  /* PAGE 2 */
  #kemasan { background: #2C1A0A; padding: 3rem 1rem; min-height: 100vh; }
  .kemasan-title { text-align: center; margin-bottom: 3rem; }
  .kemasan-title h2 { font-family: 'Playfair Display', serif; font-size: 2.2rem; color: var(--gold); margin-bottom: 0.5rem; }
  .kemasan-title p { color: rgba(253,246,236,0.6); font-size: 0.9rem; }
  .packaging-grid { display: flex; justify-content: center; flex-wrap: wrap; gap: 2rem; max-width: 1100px; margin: 0 auto; }
  .pack-card { width: 220px; background: white; border-radius: 16px; overflow: hidden; box-shadow: 0 20px 60px rgba(0,0,0,0.5); transition: transform 0.3s; cursor: pointer; }
  .pack-card:hover { transform: translateY(-8px) rotate(1deg); }
  .pack-header { padding: 1rem; text-align: center; }
  .pack-brand { font-family: 'Playfair Display', serif; font-size: 1.1rem; font-weight: 900; color: white; letter-spacing: 0.05em; }
  .pack-tagline { font-size: 0.6rem; color: rgba(255,255,255,0.8); letter-spacing: 0.1em; text-transform: uppercase; margin-top: 0.1rem; }
  .pack-singkong .pack-header { background: linear-gradient(135deg, #8B4513, #C0763A); }
  .pack-pisang .pack-header { background: linear-gradient(135deg, #DAA520, #F4C842); }
  .pack-coco .pack-header { background: linear-gradient(135deg, #2C5F2E, #4A9650); }
  .pack-roti .pack-header { background: linear-gradient(135deg, #C0392B, #E74C3C); }
  .pack-emoji { font-size: 2.5rem; display: block; margin: 0.5rem 0; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.2)); }
  .pack-body { padding: 0.75rem; background: white; }
  .pack-product-name { font-family: 'Playfair Display', serif; font-size: 1rem; color: #222; font-weight: 700; margin-bottom: 0.2rem; }
  .pack-variant { font-size: 0.7rem; color: #888; margin-bottom: 0.75rem; font-style: italic; }
  .pack-info-row { display: flex; justify-content: space-between; align-items: flex-start; gap: 0.5rem; margin-bottom: 0.75rem; }
  .pack-details { flex: 1; }
  .pack-detail-item { display: flex; justify-content: space-between; font-size: 0.65rem; color: #555; padding: 0.2rem 0; border-bottom: 1px solid #f0f0f0; }
  .pack-detail-item:last-child { border-bottom: none; }
  .pack-detail-item strong { color: #222; }
  .pack-qr-mini { width: 65px; height: 65px; background: white; border: 1px solid #ddd; border-radius: 6px; display: flex; flex-direction: column; align-items: center; justify-content: center; flex-shrink: 0; gap: 3px; padding: 4px; }
  .mini-qr-grid { display: grid; grid-template-columns: repeat(5,1fr); gap: 1px; width: 48px; height: 48px; }
  .mq { background: #000; border-radius: 0.5px; }
  .mq.w { background: white; }
  .pack-qr-label { font-size: 0.45rem; color: #666; font-family: 'Space Mono', monospace; text-align: center; line-height: 1.2; }
  .pack-price { background: #f8f8f8; border-radius: 6px; padding: 0.4rem 0.6rem; display: flex; justify-content: space-between; align-items: center; margin-top: 0.5rem; }
  .pack-price-label { font-size: 0.6rem; color: #888; }
  .pack-price-val { font-family: 'Space Mono', monospace; font-size: 0.85rem; font-weight: 700; color: #222; }
  .pack-footer { background: #f5f5f5; padding: 0.5rem 0.75rem; display: flex; align-items: center; justify-content: space-between; }
  .pack-cert { display: flex; gap: 4px; align-items: center; }
  .cert-badge { background: #e8f5e8; border: 1px solid #3A6B35; color: #3A6B35; font-size: 0.5rem; padding: 1px 5px; border-radius: 3px; font-weight: 700; letter-spacing: 0.05em; }
  .pack-barcode { display: flex; flex-direction: column; align-items: center; gap: 1px; }
  .barcode-lines { display: flex; gap: 1px; height: 18px; align-items: flex-end; }
  .bl { width: 1px; background: #222; }
  .bl.t { height: 100%; }
  .bl.m { height: 70%; }
  .bl.s { height: 50%; }
  .barcode-num { font-size: 0.45rem; font-family: 'Space Mono', monospace; color: #555; }

  /* PAGE 3 */
  #digital { background: #0D1117; min-height: 100vh; padding: 2rem 1rem 4rem; }
  .digital-header { text-align: center; padding: 2rem 0 3rem; }
  .digital-header h2 { font-family: 'Playfair Display', serif; font-size: 2.2rem; color: white; margin-bottom: 0.5rem; }
  .digital-header p { color: rgba(255,255,255,0.5); font-size: 0.9rem; }
  .phone-section { display: flex; justify-content: center; align-items: flex-start; gap: 4rem; flex-wrap: wrap; max-width: 900px; margin: 0 auto; }
  .phone-frame { width: 260px; height: 520px; background: #1C1C1E; border-radius: 40px; padding: 12px; box-shadow: 0 40px 100px rgba(0,0,0,0.6), inset 0 0 0 1px rgba(255,255,255,0.1); position: relative; }
  .phone-screen { width: 100%; height: 100%; background: var(--cream); border-radius: 30px; overflow: hidden; position: relative; }
  .phone-notch { position: absolute; top: 0; left: 50%; transform: translateX(-50%); width: 80px; height: 25px; background: #1C1C1E; border-radius: 0 0 20px 20px; z-index: 10; }
  .landing-header-phone { background: linear-gradient(135deg, #5C3D1E, #8B5E35); padding: 2rem 1rem 1.5rem; text-align: center; }
  .landing-brand-phone { font-family: 'Playfair Display', serif; font-size: 1.1rem; color: var(--gold); font-weight: 700; }
  .landing-sub-phone { font-size: 0.55rem; color: rgba(253,246,236,0.7); letter-spacing: 0.1em; text-transform: uppercase; }
  .landing-emoji-phone { font-size: 2rem; display: block; margin: 0.5rem 0 0.25rem; }
  .landing-product-phone { font-size: 0.8rem; color: white; font-weight: 600; }
  .landing-body-phone { padding: 0.75rem; display: flex; flex-direction: column; gap: 0.5rem; }
  .lbp-card { background: white; border-radius: 8px; padding: 0.6rem; box-shadow: 0 1px 4px rgba(0,0,0,0.08); }
  .lbp-label { font-size: 0.5rem; color: var(--orange); font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; margin-bottom: 0.25rem; font-family: 'Space Mono', monospace; }
  .lbp-value { font-size: 0.72rem; color: var(--dark); font-weight: 500; }
  .lbp-row { display: flex; gap: 0.4rem; }
  .lbp-row .lbp-card { flex: 1; }
  .contact-btn-phone { background: var(--green); color: white; border: none; border-radius: 8px; padding: 0.6rem; font-size: 0.7rem; font-weight: 600; width: 100%; cursor: pointer; font-family: 'DM Sans', sans-serif; }
  .digital-explain { flex: 1; min-width: 280px; max-width: 360px; }
  .explain-title { font-family: 'Playfair Display', serif; font-size: 1.5rem; color: white; margin-bottom: 0.5rem; }
  .explain-sub { color: rgba(255,255,255,0.5); font-size: 0.85rem; line-height: 1.6; margin-bottom: 1.5rem; }
  .explain-cards { display: flex; flex-direction: column; gap: 0.75rem; }
  .exp-card { background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.08); border-radius: 12px; padding: 1rem 1.25rem; display: flex; gap: 1rem; align-items: flex-start; transition: background 0.3s; }
  .exp-card:hover { background: rgba(255,255,255,0.08); }
  .exp-icon { width: 36px; height: 36px; border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 1.1rem; flex-shrink: 0; }
  .icon-orange { background: rgba(232,114,42,0.2); }
  .icon-green { background: rgba(58,107,53,0.2); }
  .icon-gold { background: rgba(201,150,58,0.2); }
  .icon-blue { background: rgba(52,152,219,0.2); }
  .exp-text h4 { font-size: 0.88rem; color: white; font-weight: 600; margin-bottom: 0.25rem; }
  .exp-text p { font-size: 0.78rem; color: rgba(255,255,255,0.55); line-height: 1.5; }
  .indi-connection { max-width: 900px; margin: 3rem auto 0; background: rgba(201,150,58,0.08); border: 1px solid rgba(201,150,58,0.2); border-radius: 16px; padding: 2rem; }
  .indi-conn-title { font-family: 'Playfair Display', serif; font-size: 1.4rem; color: var(--gold); margin-bottom: 1rem; }
  .indi-conn-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1rem; }
  .indi-conn-item { background: rgba(255,255,255,0.04); border-radius: 10px; padding: 1rem; }
  .indi-conn-item h4 { font-size: 0.82rem; color: var(--gold); font-weight: 600; margin-bottom: 0.4rem; font-family: 'Space Mono', monospace; }
  .indi-conn-item p { font-size: 0.78rem; color: rgba(255,255,255,0.6); line-height: 1.5; }
</style>
</head>
<body>
<nav class="tabs">
  <button class="tab-btn active" onclick="showPage('poster', this)">📋 Poster Pameran</button>
  <button class="tab-btn" onclick="showPage('kemasan', this)">📦 Mockup Kemasan</button>
  <button class="tab-btn" onclick="showPage('digital', this)">📱 Konsep Digital</button>
</nav>

<div id="poster" class="page active">
  <div class="poster-inner">
    <div class="bg-deco bg-deco-1"></div>
    <div class="bg-deco bg-deco-2"></div>
    <div class="poster-badge">🏆 Proyek Solusi INDI 4.0</div>
    <div class="poster-title-block">
      <p class="poster-eyebrow">Transformasi Digital UMKM</p>
      <h1 class="poster-headline">Digitalisasi Label<br><span>QR Code</span> pada<br>Kemasan Produk</h1>
      <p class="poster-sub">Solusi berbasis teknologi untuk meningkatkan identitas produk, transparansi informasi, dan daya saing UMKM <strong>Cecilia Snack</strong> menuju era Industri 4.0.</p>
    </div>
    <div class="poster-divider"></div>
    <div class="problem-solution">
      <div class="ps-box problem">
        <div class="ps-label">⚠ Kondisi Saat Ini</div>
        <ul class="ps-items">
          <li>Tidak ada barcode/QR di kemasan</li>
          <li>Harga ditempel manual, mudah lepas</li>
          <li>Info produk tidak tersedia digital</li>
          <li>Stok tidak bisa dilacak otomatis</li>
          <li>Kemasan tidak profesional</li>
        </ul>
      </div>
      <div class="ps-box solution">
        <div class="ps-label">✅ Solusi yang Ditawarkan</div>
        <ul class="ps-items">
          <li>QR code terintegrasi di setiap kemasan</li>
          <li>Harga & info produk digital & akurat</li>
          <li>Halaman produk bisa diakses konsumen</li>
          <li>Potensi tracking distribusi produk</li>
          <li>Kemasan lebih rapi & profesional</li>
        </ul>
      </div>
    </div>
    <div class="qr-section">
      <div class="qr-box">
        <div class="qr-pattern">
          <div class="qr-cell"></div><div class="qr-cell"></div><div class="qr-cell"></div><div class="qr-cell"></div><div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell"></div>
          <div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell white"></div><div class="qr-cell white"></div><div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell"></div>
          <div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell"></div>
          <div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell white"></div><div class="qr-cell white"></div><div class="qr-cell"></div><div class="qr-cell"></div><div class="qr-cell"></div>
          <div class="qr-cell"></div><div class="qr-cell"></div><div class="qr-cell"></div><div class="qr-cell"></div><div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell"></div>
          <div class="qr-cell white"></div><div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell"></div><div class="qr-cell white"></div>
          <div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell"></div><div class="qr-cell white"></div><div class="qr-cell"></div>
        </div>
        <div class="qr-label-text">SCAN ME</div>
      </div>
      <div class="qr-info">
        <h3>Informasi dalam QR Code</h3>
        <p>Setiap kemasan Cecilia Snack akan dilengkapi QR Code unik yang dapat di-scan konsumen untuk mengakses i
