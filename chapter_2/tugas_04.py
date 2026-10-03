"""
==========================================================
 TUGAS 4 - Tuple untuk Data Koordinat
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat list berisi 5 tuple koordinat (x, y) sebagai lokasi
 2. Gunakan tuple unpacking untuk menampilkan setiap koordinat
 3. Hitung jarak Euclidean antar dua titik:
    d = sqrt((x2-x1)^2 + (y2-y1)^2)  (gunakan ** 0.5, tanpa math)
 4. Cari pasangan titik yang paling dekat jaraknya
 5. Buat dictionary dengan tuple sebagai key, nama lokasi sebagai value
 6. Buktikan tuple bisa jadi key dict tapi list tidak (try-except)
==========================================================
"""

# ── Data Koordinat ───────────────────────────────────────────────────────────
koordinat = [
    (0, 0),
    (3, 4),
    (6, 8),
    (2, 1),
    (10, 10),
]


# ── Tuple Unpacking ──────────────────────────────────────────────────────────
print("===== DATA KOORDINAT =====")
for i, (x, y) in enumerate(koordinat, 1):
    print(f"Titik {i}: x={x}, y={y}")


# ── Fungsi Jarak Euclidean ───────────────────────────────────────────────────
def hitung_jarak(titik_1, titik_2):
    """Hitung jarak Euclidean antara dua titik.

    Args:
        titik_1 (tuple): Koordinat titik pertama (x, y).
        titik_2 (tuple): Koordinat titik kedua (x, y).

    Returns:
        float: Jarak antara kedua titik.
    """
    x1, y1 = titik_1
    x2, y2 = titik_2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


# ── Cari Pasangan Titik Terdekat ─────────────────────────────────────────────
jarak_min = float("inf")
pasangan_terdekat = None
for i in range(len(koordinat)):
    for j in range(i + 1, len(koordinat)):
        jarak = hitung_jarak(koordinat[i], koordinat[j])
        if jarak < jarak_min:
            jarak_min = jarak
            pasangan_terdekat = (i, j)

i, j = pasangan_terdekat
print(f"\nJarak Titik 1 ke Titik 2: {hitung_jarak(koordinat[0], koordinat[1]):.2f}")
print(f"Pasangan terdekat: Titik {i + 1} {koordinat[i]} dan "
      f"Titik {j + 1} {koordinat[j]} (jarak {jarak_min:.2f})")


# ── Tuple sebagai Key Dictionary ─────────────────────────────────────────────
lokasi = {
    (0, 0): "Kampus Unismuh",
    (3, 4): "Perpustakaan",
    (6, 8): "Laboratorium",
    (2, 1): "Kantin",
    (10, 10): "Gerbang Utama",
}
print("\n--- Dictionary Lokasi ---")
for (x, y), nama in lokasi.items():
    print(f"({x}, {y}) -> {nama}")


# ── Buktikan List Tidak Bisa Jadi Key ────────────────────────────────────────
print("\n--- Tuple vs List sebagai Key ---")
try:
    valid_dict = {(1, 2): "tuple bisa jadi key"}
    print(f"Tuple sebagai key: berhasil -> {valid_dict}")
    invalid_dict = {[1, 2]: "ini akan error"}
except TypeError as e:
    print(f"Error: {e}")
    print("List tidak bisa menjadi key dictionary karena mutable!")
