"""
==========================================================
 TUGAS 3 - Analisis Teks dengan Set
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Definisikan 2 string kalimat (minimal 10 kata per kalimat)
 2. Konversi setiap kalimat menjadi set kata unik (lowercase)
 3. Tampilkan intersection (kata di kedua kalimat)
 4. Tampilkan difference (kata hanya di kalimat 1 / kalimat 2)
 5. Tampilkan union (semua kata unik)
 6. Tampilkan symmetric difference (kata di salah satu saja)
 7. Hitung jumlah kata unik total
==========================================================
"""

# ── Data Kalimat ─────────────────────────────────────────────────────────────
kalimat_1 = (
    "Belajar python di laboratorium informatika sangat menyenangkan "
    "karena banyak praktik langsung setiap pekan"
)
kalimat_2 = (
    "Mahasiswa informatika wajib belajar python dan machine learning "
    "agar siap menghadapi dunia kerja yang kompetitif"
)


# ── Konversi ke Set ──────────────────────────────────────────────────────────
kata_set_1 = set(kalimat_1.lower().split())
kata_set_2 = set(kalimat_2.lower().split())


# ── Intersection (kata yang muncul di KEDUA kalimat) ─────────────────────────
kata_sama = kata_set_1 & kata_set_2


# ── Difference (kata HANYA di kalimat 1) ─────────────────────────────────────
hanya_kalimat_1 = kata_set_1 - kata_set_2


# ── Difference (kata HANYA di kalimat 2) ─────────────────────────────────────
hanya_kalimat_2 = kata_set_2 - kata_set_1


# ── Union (SEMUA kata unik dari kedua kalimat) ──────────────────────────────
semua_kata = kata_set_1 | kata_set_2


# ── Symmetric Difference (kata di SALAH SATU saja) ──────────────────────────
kata_unik_masing = kata_set_1 ^ kata_set_2


# ── Tampilkan Hasil ──────────────────────────────────────────────────────────
print("===== ANALISIS TEKS DENGAN SET =====")
print(f"Kalimat 1: {kalimat_1}")
print(f"Kalimat 2: {kalimat_2}")
print(f"\nKata unik kalimat 1 : {len(kata_set_1)}")
print(f"Kata unik kalimat 2 : {len(kata_set_2)}")
print(f"\nKata di kedua kalimat (intersection) : {sorted(kata_sama)}")
print(f"Hanya di kalimat 1 (difference)      : {sorted(hanya_kalimat_1)}")
print(f"Hanya di kalimat 2 (difference)      : {sorted(hanya_kalimat_2)}")
print(f"Semua kata unik (union)              : {sorted(semua_kata)}")
print(f"Salah satu saja (symmetric diff.)    : {sorted(kata_unik_masing)}")
print(f"\nJumlah kata unik total: {len(semua_kata)}")
