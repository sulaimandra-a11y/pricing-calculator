import streamlit as st
from rates import CATEGORY_RATES, PRODUCT_CATEGORIES
from calculator import hitung_biaya, hitung_tarif_promo, format_rupiah

st.set_page_config(page_title="Kalkulator Harga Shopee", page_icon="🛍️", layout="centered")

st.title("🛍️ Shopee Pricing Calculator")
st.write("Hitung harga jual produkmu di Shopee agar tidak boncos terpotong biaya admin!")
st.write("---")

# --- INPUT SECTION ---
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("📥 Input Data")
    modal = st.number_input("Modal Produk (Rp)", min_value=0, value=50000, step=1000)
    profit_persen = st.number_input("Target Profit (% dari modal)", min_value=0.0, value=20.0, step=5.0)

with col2:
    st.subheader("⚙️ Pengaturan Toko")
    tipe_penjual = st.selectbox("Tipe Penjual Shopee", options=list(CATEGORY_RATES.keys()))
    kategori_produk = st.selectbox("Kategori Produk Shopee", options=PRODUCT_CATEGORIES)
    ikut_gratis_ongkir = st.checkbox("Ikut Program Gratis Ongkir XTRA")
    ikut_promo_xtra = st.checkbox("Ikut Program Promo XTRA")

# --- CALCULATION ---
tarif_admin_dict = CATEGORY_RATES[tipe_penjual][kategori_produk]
is_mall = tipe_penjual == "Shopee Mall"
target_profit_rp = modal * (profit_persen / 100)
tarif_promo = hitung_tarif_promo(ikut_gratis_ongkir, ikut_promo_xtra)

hasil = hitung_biaya(tarif_admin_dict['max'], modal, target_profit_rp, tarif_promo, is_mall)

# --- OUTPUT SECTION ---
st.write("---")
st.subheader("📊 Hasil Analisis Harga Jual")

if hasil:
    st.markdown(f"## 💰 Rekomendasi Harga Jual: {format_rupiah(hasil['harga_jual'])}")
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Target Profit", format_rupiah(target_profit_rp))
    with col_b:
        st.metric(
            "Total Potongan Shopee",
            format_rupiah(hasil['total_biaya']),
            delta=f"-{hasil['actual_total_potongan']*100:.1f}%",
            delta_color="inverse"
        )
    with col_c:
        st.metric("Bersih ke Dompet", format_rupiah(hasil['pendapatan_bersih']))

    with st.expander("Lihat Rincian Potongan Lebih Detail"):
        st.write(f"**Biaya Admin ({tipe_penjual} - {kategori_produk}):** {format_rupiah(hasil['biaya_admin'])}")
        st.write(f"**Biaya Program Promo XTRA:** {format_rupiah(hasil['biaya_promo'])}")
        if is_mall:
            st.write(f"**Biaya Pembayaran Mall:** {format_rupiah(hasil['biaya_pembayaran'])}")
        st.write(f"**Biaya Proses Order:** {format_rupiah(1250)}")
        st.write(f"**Total Potongan:** {format_rupiah(hasil['total_biaya'])}")
        st.write(f"**Total Modal Awal:** {format_rupiah(modal)}")
else:
    st.error("Terjadi kesalahan dalam perhitungan persentase biaya anda.")
