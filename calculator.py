from rates import PROMO_RATE_GRATIS_ONGKIR, PROMO_RATE_PROMO_XTRA, PAYMENT_RATE_MALL, BIAYA_PROSES_ORDER, BIAYA_PEMBAYARAN_MALL_MAX

def hitung_biaya(tarif_admin, modal, target_profit_rp, tarif_promo, is_mall):
    tarif_biaya_pembayaran = PAYMENT_RATE_MALL if is_mall else 0
    rate_total_potongan = tarif_admin + tarif_promo + tarif_biaya_pembayaran
    
    if rate_total_potongan >= 1:
        return None
    
    harga_jual = (modal + target_profit_rp + BIAYA_PROSES_ORDER) / (1 - rate_total_potongan)
    biaya_admin = harga_jual * tarif_admin
    biaya_promo = harga_jual * tarif_promo
    biaya_pembayaran_raw = harga_jual * tarif_biaya_pembayaran
    biaya_pembayaran = min(biaya_pembayaran_raw, BIAYA_PEMBAYARAN_MALL_MAX) if is_mall else 0
    total_biaya = biaya_admin + biaya_promo + biaya_pembayaran + BIAYA_PROSES_ORDER
    pendapatan_bersih = harga_jual - total_biaya
    actual_total_potongan = total_biaya / harga_jual
    
    return {
        'harga_jual': harga_jual,
        'biaya_admin': biaya_admin,
        'biaya_promo': biaya_promo,
        'biaya_pembayaran': biaya_pembayaran,
        'total_biaya': total_biaya,
        'pendapatan_bersih': pendapatan_bersih,
        'actual_total_potongan': actual_total_potongan
    }

def hitung_tarif_promo(ikut_gratis_ongkir, ikut_promo_xtra):
    tarif_promo = 0.0
    if ikut_gratis_ongkir:
        tarif_promo += PROMO_RATE_GRATIS_ONGKIR
    if ikut_promo_xtra:
        tarif_promo += PROMO_RATE_PROMO_XTRA
    return tarif_promo

def format_rupiah(value):
    return f"Rp {round(value):,}"
