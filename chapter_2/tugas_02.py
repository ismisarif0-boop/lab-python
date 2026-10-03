"""
==========================================================
 TUGAS 2 - Sistem Data Mahasiswa
 Chapter 2: Struktur Data
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat dictionary berisi data 5 mahasiswa, setiap mahasiswa
    memiliki: nama, nim, jurusan, dan nilai (dict mata kuliah)
 2. Tampilkan seluruh data mahasiswa dalam format tabel rapi
 3. Hitung rata-rata nilai setiap mahasiswa
 4. Cari mahasiswa dengan rata-rata tertinggi
 5. Tambahkan 1 mahasiswa baru ke dictionary
 6. Gunakan dict comprehension untuk {nama: rata_rata_nilai}

 Contoh Struktur:
 mahasiswa = {
     "MHS001": {
         "nama": "Ahmad",
         "jurusan": "Informatika",
         "nilai": {"Algoritma": 85, "Basis Data": 90, "Jaringan": 78}
     },
     ...
 }
==========================================================
"""

# ── Data Mahasiswa ────────────────────────────────────────────────────────────
mahasiswa = {
    "MHS001": {
        "nama": "Ahmad",
        "nim": "105841100121",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 85, "Basis Data": 90, "Jaringan": 78},
    },
    "MHS002": {
        "nama": "Siti",
        "nim": "105841100122",
        "jurusan": "Informatika",
        "nilai": {"Algoritma": 92, "Basis Data": 88, "Jaringan": 95},
    },
    "MHS003": {
        "nama": "Budi",
        "nim": "105841100123",
        "jurusan": "Sistem Informasi",
        "nilai": {"Algoritma": 70, "Basis Data": 75, "Jaringan": 68},
    },
    "MHS004": {
        "nama": "Dewi",
        "nim": "105841100124",
        "jurusan": "Teknik Elektro",
        "nilai": {"Algoritma": 80, "Basis Data": 82, "Jaringan": 79},
    },
    "MHS005": {
        "nama": "Rizky",
        "nim": "105841100125",
        "jurusan": "Sistem Informasi",
        "nilai": {"Algoritma": 60, "Basis Data": 65, "Jaringan": 72},
    },
}


# ── Tampilkan Data dalam Format Tabel ─────────────────────────────────────────
def rata_rata_nilai(data):
    """Hitung rata-rata nilai satu mahasiswa."""
    return sum(data["nilai"].values()) / len(data["nilai"])


def tampilkan_tabel(daftar):
    """Cetak seluruh data mahasiswa dalam format tabel."""
    print(f"{'ID':<7}| {'Nama':<8}| {'NIM':<13}| {'Jurusan':<17}| "
          f"{'Algoritma':>9} | {'Basis Data':>10} | {'Jaringan':>8} | {'Rata-rata':>9}")
    print("-" * 100)
    for id_mhs, data in daftar.items():
        n = data["nilai"]
        print(f"{id_mhs:<7}| {data['nama']:<8}| {data['nim']:<13}| {data['jurusan']:<17}| "
              f"{n['Algoritma']:>9} | {n['Basis Data']:>10} | {n['Jaringan']:>8} | "
              f"{rata_rata_nilai(data):>9.2f}")


print("===== SISTEM DATA MAHASISWA =====")
tampilkan_tabel(mahasiswa)


# ── Hitung Rata-rata Nilai Setiap Mahasiswa ──────────────────────────────────
print("\n--- Rata-rata Nilai ---")
for id_mhs, data in mahasiswa.items():
    print(f"{data['nama']:<8}: {rata_rata_nilai(data):.2f}")


# ── Cari Mahasiswa dengan Rata-rata Tertinggi ────────────────────────────────
id_terbaik = max(mahasiswa, key=lambda k: rata_rata_nilai(mahasiswa[k]))
terbaik = mahasiswa[id_terbaik]
print(f"\nRata-rata tertinggi: {terbaik['nama']} ({id_terbaik}) "
      f"= {rata_rata_nilai(terbaik):.2f}")


# ── Tambahkan Mahasiswa Baru ─────────────────────────────────────────────────
mahasiswa["MHS006"] = {
    "nama": "Hana",
    "nim": "105841100126",
    "jurusan": "Informatika",
    "nilai": {"Algoritma": 88, "Basis Data": 84, "Jaringan": 90},
}
print(f"\nMahasiswa baru ditambahkan. Total sekarang: {len(mahasiswa)}")
tampilkan_tabel({"MHS006": mahasiswa["MHS006"]})


# ── Dictionary Comprehension ─────────────────────────────────────────────────
ringkasan = {
    data["nama"]: round(rata_rata_nilai(data), 2)
    for data in mahasiswa.values()
}
print(f"\nRingkasan {{nama: rata-rata}}: {ringkasan}")
