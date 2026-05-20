import streamlit as st

# Product categories
PRODUCT_CATEGORIES = [
    "Fashion",
    "Electronics",
    "Beauty & Personal Care",
    "Home & Living",
    "Mom & Baby",
    "Sports & Outdoors",
    "Food & Beverages",
    "Hobbies & Collections",
    "Health",
    "Pets"
]

# Promo program rates
PROMO_RATE_GRATIS_ONGKIR = 0.04  # 4%
PROMO_RATE_CASHBACK = 0.02       # 2%
PROMO_RATE_PROMO_XTRA = 0.06       # 6%

# Category-based admin rates (seller type -> product category -> rate)
# TODO: Replace with official Shopee rates from Seller Center documentation
CATEGORY_RATES = {
    "Shopee Mall": {
        "Fashion": 0.085,
        "Electronics": 0.090,
        "Beauty & Personal Care": 0.080,
        "Home & Living": 0.082,
        "Mom & Baby": 0.087,
        "Sports & Outdoors": 0.084,
        "Food & Beverages": 0.078,
        "Hobbies & Collections": 0.083,
        "Health": 0.086,
        "Pets": 0.081,
    },
    "Star / Star+ Seller": {
        "Fashion": 0.065,
        "Electronics": 0.070,
        "Beauty & Personal Care": 0.060,
        "Home & Living": 0.062,
        "Mom & Baby": 0.067,
        "Sports & Outdoors": 0.064,
        "Food & Beverages": 0.058,
        "Hobbies & Collections": 0.063,
        "Health": 0.066,
        "Pets": 0.061,
    },
    "Non-Star Seller": {
        "Fashion": 0.050,
        "Electronics": 0.055,
        "Beauty & Personal Care": 0.045,
        "Home & Living": 0.047,
        "Mom & Baby": 0.052,
        "Sports & Outdoors": 0.049,
        "Food & Beverages": 0.043,
        "Hobbies & Collections": 0.048,
        "Health": 0.051,
        "Pets": 0.046,
    },
}

# Konfigurasi halaman utama web app
st.set_page_config(page_title="Kalkulator Harga Shopee", page_icon="🛍️", layout="centered")

st.title("🛍️ Shopee Pricing Calculator")
st.write("Hitung harga jual produkmu di Shopee agar tidak boncos terpotong biaya admin!")
st.write("---")

# --- INPUT SECTION (Kolom Kiri) ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Input Data")
    modal = st.number_input("Modal Produk (Rp)", min_value=0, value=50000, step=1000)
    profit_persen = st.number_input("Target Profit (% dari modal)", min_value=0.0, value=20.0, step=5.0)

with col2:
    st.subheader("⚙️ Pengaturan Toko")
    tipe_penjual = st.selectbox(
        "Tipe Penjual Shopee",
        options=["Non-Star Seller", "Star / Star+ Seller", "Shopee Mall"]
    )
    kategori_produk = st.selectbox(
        "Kategori Produk Shopee",
        options=PRODUCT_CATEGORIES
    )
    
    # Checkbox untuk program promo
    ikut_gratis_ongkir = st.checkbox("Ikut Program Gratis Ongkir XTRA")
    ikut_cashback = st.checkbox("Ikut Program Cashback XTRA")
    ikut_promo_xtra = st.checkbox("Ikut Program Promo XTRA")

# --- LOGIKA PERHITUNGAN ---
# Tentukan tarif admin berdasarkan pilihan
tarif_admin = CATEGORY_RATES[tipe_penjual][kategori_produk]

# Tambahkan tarif promo tambahan jika dicentang
tarif_promo = 0.0
if ikut_gratis_ongkir:
    tarif_promo += PROMO_RATE_GRATIS_ONGKIR
if ikut_cashback:
    tarif_promo += PROMO_RATE_CASHBACK
if ikut_promo_xtra:
    tarif_promo += PROMO_RATE_PROMO_XTRA

# Hitung nominal profit rupiah yang diinginkan
target_profit_rp = modal * (profit_persen / 100)

# Total persentase potongan Shopee
total_potongan_persen = tarif_admin + tarif_promo

# Rumus sakti agar harga jual menutup semua biaya admin
if total_potongan_persen < 1:
    harga_jual = (modal + target_profit_rp) / (1 - total_potongan_persen)
else:
    harga_jual = 0

# Hitung rincian biaya
biaya_admin_rp = harga_jual * tarif_admin
biaya_promo_rp = harga_jual * tarif_promo
total_biaya_shopee = biaya_admin_rp + biaya_promo_rp
pendapatan_bersih = harga_jual - total_biaya_shopee

# --- OUTPUT SECTION ---
st.write("---")
st.subheader("📊 Hasil Analisis Harga Jual")

if harga_jual > 0:
    # Tampilkan rekomendasi harga dengan ukuran besar
    st.success(f"### Rekomendasi Harga Jual: **Rp {round(harga_jual):,}**")
    
    # Tampilkan detail rincian dalam bentuk kolom informasi
    c1, c2, c3 = st.columns(3)
    c1.metric("Target Profit", f"Rp {round(target_profit_rp):,}")
    c2.metric("Total Potongan Shopee", f"Rp {round(total_biaya_shopee):,}", delta=f"-{total_potongan_persen*100}%", delta_color="inverse")
    c3.metric("Bersih ke Dompet", f"Rp {round(pendapatan_bersih):,}")

    # Breakdown detail dalam bentuk list ekspander yang rapi
    with st.expander("Lihat Rincian Potongan Lebih Detail"):
        st.write(f"• **Biaya Admin ({tipe_penjual} - {kategori_produk}):** Rp {round(biaya_admin_rp):,}")
        st.write(f"• **Biaya Program XTRA (Gratis Ongkir/Cashback/Promo XTRA):** Rp {round(biaya_promo_rp):,}")
        st.write(f"• **Total Modal Awal:** Rp {modal:,}")
else:
    st.error("Terjadi kesalahan dalam perhitungan persentase biaya anda.")