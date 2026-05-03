import streamlit as st
import os

st.set_page_config(
    page_title="Cecilia Snack × INDI 4.0",
    page_icon="🍟",
    layout="wide"
)

# Load HTML file
html_path = os.path.join(os.path.dirname(__file__), "index.html")

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Tampilkan HTML di Streamlit
st.components.v1.html(html_content, height=4000, scrolling=True)

<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Cecilia Snack and INDI 4.0</title>

<style>
  :root {
    --brown: #3E2000;
    --orange: #E8650A;
    --cream: #FFF8EE;
  }

  body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: var(--cream);
    color: var(--brown);
  }

  .hero {
    background: linear-gradient(135deg, var(--brown) 0%, #6B3500 60%, var(--orange) 100%);
    color: white;
    padding: 60px 20px;
    text-align: center;
  }

  .hero h1 {
    font-size: 40px;
    margin-bottom: 10px;
  }

  .hero p {
    opacity: 0.8;
  }

  .section {
    padding: 40px 20px;
    max-width: 1000px;
    margin: auto;
  }

  .card {
    background: white;
    padding: 20px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  }

  .product {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 20px;
  }

  .product-card {
    background: white;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    box-shadow: 0 4px 16px rgba(0,0,0,0.1);
  }

  .product-card h3 {
    margin: 10px 0;
  }

</style>
</head>

<body>

<!-- HERO -->
<div class="hero">
  <h1>Cecilia Snack</h1>
  <p>Digitalisasi UMKM menuju INDI 4.0</p>
</div>

<!-- BEFORE AFTER -->
<div class="section">
  <div class="card">
    <h2>Sebelum</h2>
    <ul>
      <li>Kemasan polos</li>
      <li>Tidak ada QR Code</li>
      <li>Pencatatan manual</li>
    </ul>
  </div>

  <div class="card">
    <h2>Sesudah</h2>
    <ul>
      <li>QR Code di kemasan</li>
      <li>Harga digital</li>
      <li>Terhubung ke WhatsApp</li>
    </ul>
  </div>
</div>

<!-- PRODUK -->
<div class="section">
  <h2>Produk</h2>

  <div class="product">
    
    <div class="product-card">
      <h3>Keripik Singkong</h3>
      <p>Rp 10.000</p>
    </div>

    <div class="product-card">
      <h3>Keripik Pisang</h3>
      <p>Rp 12.000</p>
    </div>

    <div class="product-card">
      <h3>Keripik Kentang</h3>
      <p>Rp 15.000</p>
    </div>

    <div class="product-card">
      <h3>Keripik Ubi</h3>
      <p>Rp 11.000</p>
    </div>

  </div>
</div>

</body>
</html>
