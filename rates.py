# Promo program rates
PROMO_RATE_GRATIS_ONGKIR = 0.04  # 4%
PROMO_RATE_PROMO_XTRA = 0.06     # 6%
PAYMENT_RATE_MALL = 0.018
BIAYA_PROSES_ORDER = 1250  # Fixed cost per order in Rp
BIAYA_PEMBAYARAN_MALL_MAX = 50000  # Maximum payment fee for Shopee Mall in Rp

# Category-based admin rates (seller type -> product category -> rate)
# TODO: Replace with official Shopee rates from Seller Center documentation
CATEGORY_RATES = {
    "Shopee Mall": {
        'Aksesoris Fashion':{'min':0.032,'max':0.1045},
        'Audio':{'min':0.072,'max':0.0995},
        'Buku & Alat Tulis':{'min':0.072,'max':0.117},
        'Buku & Majalah':{'min':0.072,'max':0.117},
        'Elektronik':{'min':0.042,'max':0.102},
        'Fashion Bayi & Anak':{'min':0.0995,'max':0.102},
        'Fashion Muslim':{'min':0.0995,'max':0.117},
        'Gaming & Konsol':{'min':0.072,'max':0.077},
        'Handphone & Aksesoris':{'min':0.047,'max':0.102},
        'Hewan Peliharaan':{'min':0.077,'max':0.077},
        'Hobi & Koleksi':{'min':0.077,'max':0.1045},
        'Ibu & Bayi':{'min':0.072,'max':0.117},
        'Jam Tangan':{'min':0.102,'max':0.102},
        'Kamera & Drone':{'min':0.072,'max':0.102},
        'Kesehatan':{'min':0.072,'max':0.102},
        'Komputer & Aksesoris':{'min':0.042,'max':0.102},
        'Koper & Tas Travel':{'min':0.102,'max':0.117},
        'Makanan & Minuman':{'min':0.062,'max':0.102},
        'Mobil':{'min':0.025,'max':0.1045},
        'Olahraga & Outdoor':{'min':0.1045,'max':0.117},
        'Pakaian Pria':{'min':0.0995,'max':0.102},
        'Pakaian Wanita':{'min':0.0995,'max':0.102},
        'Perawatan & Kecantikan':{'min':0.0995,'max':0.0995},
        'Perlengkapan Rumah':{'min':0.072,'max':0.117},
        'Sepatu Pria':{'min':0.102,'max':0.102},
        'Sepatu Wanita':{'min':0.102,'max':0.102},
        'Sepeda Motor':{'min':0.025,'max':0.1045},
        'Tas Pria':{'min':0.102,'max':0.102},
        'Tas Wanita':{'min':0.102,'max':0.102},
        'Tiket, Voucher, & Layanan':{'min':0.072,'max':0.077},
    },
    "Non-Star / Star / Star+ Seller": {
        'Aksesoris Fashion':{'min':0.0425,'max':0.09},
        'Audio':{'min':0.0675,'max':0.095},
        'Buku & Alat Tulis':{'min':0.09,'max':0.1},
        'Buku & Majalah':{'min':0.0825,'max':0.1},
        'Elektronik':{'min':0.0525,'max':0.1},
        'Fashion Bayi & Anak':{'min':0.0425,'max':0.09},
        'Fashion Muslim':{'min':0.0825,'max':0.1},
        'Gaming & Konsol':{'min':0.0525,'max':0.1},
        'Hewan Peliharaan':{'min':0.095,'max':0.095},
        'Hobi & Koleksi':{'min':0.09,'max':0.095},
        'Ibu & Bayi':{'min':0.065,'max':0.1},
        'Jam Tangan':{'min':0.09,'max':0.09},
        'Kamera & Drone':{'min':0.065,'max':0.095},
        'Kesehatan':{'min':0.09,'max':0.1},
        'Komputer & Aksesoris':{'min':0.0525,'max':0.0675},
        'Koper & Tas Travel':{'min':0.09,'max':0.1},
        'Makanan & Minuman':{'min':0.065,'max':0.1},
        'Mobil':{'min':0.025,'max':0.095},
        'Olahraga & Outdoor':{'min':0.0825,'max':0.1},
        'Pakaian Pria':{'min':0.0825,'max':0.1},
        'Pakaian Wanita':{'min':0.0825,'max':0.1},
        'Perawatan & Kecantikan':{'min':0.0825,'max':0.0825},
        'Perlengkapan Rumah':{'min':0.065,'max':0.1},
        'Sepatu Pria':{'min':0.09,'max':0.09},
        'Sepatu Wanita':{'min':0.09,'max':0.09},
        'Sepeda Motor':{'min':0.025,'max':0.0825},
        'Tas Pria':{'min':0.09,'max':0.09},
        'Tas Wanita':{'min':0.09,'max':0.09},
        'Tiket, Voucher, & Layanan':{'min':0.0825,'max':0.095},
    },
}

# Product categories (matches keys in CATEGORY_RATES)
PRODUCT_CATEGORIES = list(CATEGORY_RATES["Shopee Mall"].keys())
