"""
==========================================================
 TUGAS 1 - Sistem Penilaian Akademik
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat fungsi hitung_grade(nilai) -> grade (A/B/C/D/E)
 2. Buat fungsi status_kelulusan(grade) -> "LULUS"/"TIDAK LULUS"
 3. Buat list 10 mahasiswa (nama, nilai) sebagai list of tuple
 4. Proses semua mahasiswa, tampilkan dalam format tabel
 5. Hitung jumlah lulus, tidak lulus, dan persentasenya
 6. Gunakan ternary operator minimal 1 kali

 Tabel Grade:
 | 90-100 | A | Sangat Baik    |
 | 80-89  | B | Baik           |
 | 70-79  | C | Cukup          |
 | 60-69  | D | Kurang         |
 | 0-59   | E | Sangat Kurang  |
==========================================================
"""


def hitung_grade(nilai):
    """Menentukan grade berdasarkan nilai angka (0-100).

    Args:
        nilai (int): Nilai angka mahasiswa (0-100).

    Returns:
        tuple: (grade, keterangan) misal ("A", "Sangat Baik")
    """
    if nilai >= 90:
        return ("A", "Sangat Baik")
    elif nilai >= 80:
        return ("B", "Baik")
    elif nilai >= 70:
        return ("C", "Cukup")
    elif nilai >= 60:
        return ("D", "Kurang")
    else:
        return ("E", "Sangat Kurang")


def status_kelulusan(grade):
    """Menentukan status kelulusan berdasarkan grade.

    Args:
        grade (str): Grade mahasiswa (A/B/C/D/E).

    Returns:
        str: "LULUS" jika A/B/C, "TIDAK LULUS" jika D/E.
    """
    # Ternary operator
    return "LULUS" if grade in ("A", "B", "C") else "TIDAK LULUS"


# ── Data Mahasiswa ────────────────────────────────────────────────────────────
data_mahasiswa = [
    ("Ahmad Fauzi", 85),
    ("Siti Rahma", 92),
    ("Budi Santoso", 55),
    ("Dewi Lestari", 78),
    ("Rizky Ramadhan", 66),
    ("Hana Pertiwi", 73),
    ("Irfan Hakim", 88),
    ("Lina Marlina", 45),
    ("Naufal Akbar", 95),
    ("Putri Ayu", 70),
]


# ── Proses & Tampilkan ───────────────────────────────────────────────────────
print("=" * 65)
print(f"{'No':>2} | {'Nama':<18} | {'Nilai':>5} | {'Grade':>5} | {'Keterangan':<14} | {'Status'}")
print("-" * 65)
jumlah_lulus = 0
jumlah_tidak_lulus = 0
for i, (nama, nilai) in enumerate(data_mahasiswa, 1):
    grade, keterangan = hitung_grade(nilai)
    status = status_kelulusan(grade)
    if status == "LULUS":
        jumlah_lulus += 1
    else:
        jumlah_tidak_lulus += 1
    print(f"{i:>2} | {nama:<18} | {nilai:>5} | {grade:>5} | {keterangan:<14} | {status}")
print("=" * 65)


# ── Statistik ────────────────────────────────────────────────────────────────
total = len(data_mahasiswa)
persen_lulus = jumlah_lulus / total * 100
persen_tidak_lulus = jumlah_tidak_lulus / total * 100
print(f"Lulus: {jumlah_lulus} ({persen_lulus:.1f}%) | "
      f"Tidak Lulus: {jumlah_tidak_lulus} ({persen_tidak_lulus:.1f}%)")
