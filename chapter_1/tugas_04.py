"""
==========================================================
 TUGAS 4 - Menghitung Luas & Keliling Bangun Datar
 Chapter 1: Dasar Python
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat variabel untuk dimensi: persegi, persegi panjang,
    lingkaran, dan segitiga
 2. Hitung luas dan keliling masing-masing bangun datar
 3. Gunakan konstanta PI = 3.14159 untuk lingkaran
 4. Tampilkan hasil dalam format tabel yang rapi
 5. Gunakan operator assignment (+=) untuk menghitung total luas

 Contoh Output:
 ============ LUAS & KELILING BANGUN DATAR ============
 Bangun            |    Luas   |  Keliling
 --------------------------------------------------
 Persegi           |     25.00 |     20.00
 Persegi Panjang   |     40.00 |     26.00
 Lingkaran         |     78.54 |     31.42
 Segitiga          |     24.00 |     24.00
 --------------------------------------------------
 Total Luas        |    167.54
 ======================================================
==========================================================
"""

# ── Konstanta ─────────────────────────────────────────────────────────────────
PI = 3.14159

# ── Dimensi Bangun Datar ─────────────────────────────────────────────────────

# Persegi
sisi_persegi = 5

# Persegi Panjang
panjang = 8
lebar = 5

# Lingkaran
jari_jari = 5

# Segitiga siku-siku 6-8-10 (alas 8, tinggi 6)
sisi_a = 6
sisi_b = 8
sisi_c = 10
tinggi_segitiga = 6
alas_segitiga = 8


# ── Perhitungan Luas ─────────────────────────────────────────────────────────
# Rumus:
#   Persegi         : sisi * sisi
#   Persegi Panjang : panjang * lebar
#   Lingkaran       : PI * jari_jari ** 2
#   Segitiga        : 0.5 * alas * tinggi

luas_persegi = sisi_persegi * sisi_persegi
luas_persegi_panjang = panjang * lebar
luas_lingkaran = PI * jari_jari ** 2
luas_segitiga = 0.5 * alas_segitiga * tinggi_segitiga


# ── Perhitungan Keliling ─────────────────────────────────────────────────────
# Rumus:
#   Persegi         : 4 * sisi
#   Persegi Panjang : 2 * (panjang + lebar)
#   Lingkaran       : 2 * PI * jari_jari
#   Segitiga        : sisi_a + sisi_b + sisi_c

keliling_persegi = 4 * sisi_persegi
keliling_persegi_panjang = 2 * (panjang + lebar)
keliling_lingkaran = 2 * PI * jari_jari
keliling_segitiga = sisi_a + sisi_b + sisi_c


# ── Total Luas (gunakan operator +=) ─────────────────────────────────────────
total_luas = 0
total_luas += luas_persegi
total_luas += luas_persegi_panjang
total_luas += luas_lingkaran
total_luas += luas_segitiga


# ── Tampilkan Hasil dalam Format Tabel ───────────────────────────────────────
print("============ LUAS & KELILING BANGUN DATAR ============")
print(f"{'Bangun':<18}| {'Luas':>9} | {'Keliling':>9}")
print("-" * 50)
print(f"{'Persegi':<18}| {luas_persegi:>9.2f} | {keliling_persegi:>9.2f}")
print(f"{'Persegi Panjang':<18}| {luas_persegi_panjang:>9.2f} | {keliling_persegi_panjang:>9.2f}")
print(f"{'Lingkaran':<18}| {luas_lingkaran:>9.2f} | {keliling_lingkaran:>9.2f}")
print(f"{'Segitiga':<18}| {luas_segitiga:>9.2f} | {keliling_segitiga:>9.2f}")
print("-" * 50)
print(f"{'Total Luas':<18}| {total_luas:>9.2f}")
print("=" * 54)
