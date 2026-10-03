"""
==========================================================
 TUGAS 1 - Manajemen Nilai Mahasiswa
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat sebuah list berisi 10 nilai ujian (integer, range 0-100)
 2. Tampilkan: nilai tertinggi, terendah, rata-rata (hitung manual)
 3. Urutkan list dari terkecil ke terbesar
 4. Gunakan list comprehension untuk filter nilai >= 70 (lulus)
 5. Hitung jumlah mahasiswa lulus dan tidak lulus
 6. Tambahkan 2 nilai baru (append), hapus nilai terkecil (remove)
==========================================================
"""

# ── Data Nilai ────────────────────────────────────────────────────────────────
nilai = [85, 60, 92, 45, 78, 55, 90, 73, 68, 88]


# ── Statistik Dasar (hitung manual, tanpa library) ───────────────────────────
# Hitung manual dengan loop (tanpa max/min/sum)
nilai_tertinggi = nilai[0]
nilai_terendah = nilai[0]
total = 0
for n in nilai:
    if n > nilai_tertinggi:
        nilai_tertinggi = n
    if n < nilai_terendah:
        nilai_terendah = n
    total += n
rata_rata = total / len(nilai)


# ── Pengurutan ────────────────────────────────────────────────────────────────
nilai_urut = sorted(nilai)


# ── List Comprehension: Filter Nilai Lulus ────────────────────────────────────
nilai_lulus = [n for n in nilai if n >= 70]


# ── Hitung Lulus & Tidak Lulus ────────────────────────────────────────────────
jumlah_lulus = len(nilai_lulus)
jumlah_tidak_lulus = len(nilai) - jumlah_lulus


# ── Manipulasi List ──────────────────────────────────────────────────────────
nilai_akhir = nilai.copy()  # salinan agar tampilan "nilai awal" tidak berubah
nilai_akhir.append(81)
nilai_akhir.append(95)
nilai_terkecil = nilai_akhir[0]
for n in nilai_akhir:
    if n < nilai_terkecil:
        nilai_terkecil = n
nilai_akhir.remove(nilai_terkecil)  # remove() hanya menghapus kemunculan pertama


# ── Tampilkan Hasil ──────────────────────────────────────────────────────────
print("===== MANAJEMEN NILAI MAHASISWA =====")
print(f"Nilai awal   : {nilai}")
print(f"Tertinggi    : {nilai_tertinggi}")
print(f"Terendah     : {nilai_terendah}")
print(f"Rata-rata    : {rata_rata:.1f}")
print(f"Nilai sorted : {nilai_urut}")
print(f"Nilai lulus  : {nilai_lulus}")
print(f"Lulus: {jumlah_lulus} | Tidak lulus: {jumlah_tidak_lulus}")
print(f"Setelah append 81 & 95, remove {nilai_terkecil}: {nilai_akhir}")
