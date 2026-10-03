"""
==========================================================
 TUGAS 1 - Biodata Mahasiswa
 Chapter 1: Dasar Python
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat variabel yang menyimpan: nama lengkap, NIM, jurusan,
    semester (int), IPK (float), dan status aktif (bool)
 2. Tampilkan semua data menggunakan f-string dengan format rapi
 3. Tampilkan tipe data dari setiap variabel menggunakan type()
 4. Gunakan isinstance() untuk memeriksa apakah NIM bertipe str
    dan semester bertipe int

 Contoh Output:
 ===== BIODATA MAHASISWA =====
 Nama    : Ahmad Fauzi
 NIM     : 105841100123
 Jurusan : Informatika
 Semester: 4
 IPK     : 3.75
 Aktif   : True
 =============================
 Tipe 'nama'    : <class 'str'>
 Tipe 'semester': <class 'int'>
 ...
==========================================================
"""

# ── Deklarasi Variabel ────────────────────────────────────────────────────────
nama_lengkap = "Ahmad Fauzi"  # str: nama lengkap mahasiswa
nim = "105841100123"  # str: Nomor Induk Mahasiswa
jurusan = "Informatika"  # str: nama jurusan
semester = 4  # int: semester saat ini
ipk = 3.75  # float: Indeks Prestasi Kumulatif
status_aktif = True  # bool: apakah masih aktif kuliah


# ── Tampilkan Biodata ─────────────────────────────────────────────────────────
print("===== BIODATA MAHASISWA =====")
print(f"Nama    : {nama_lengkap}")
print(f"NIM     : {nim}")
print(f"Jurusan : {jurusan}")
print(f"Semester: {semester}")
print(f"IPK     : {ipk:.2f}")
print(f"Aktif   : {status_aktif}")
print("=============================")


# ── Tampilkan Tipe Data ──────────────────────────────────────────────────────
print(f"Tipe 'nama'    : {type(nama_lengkap)}")
print(f"Tipe 'nim'     : {type(nim)}")
print(f"Tipe 'jurusan' : {type(jurusan)}")
print(f"Tipe 'semester': {type(semester)}")
print(f"Tipe 'ipk'     : {type(ipk)}")
print(f"Tipe 'aktif'   : {type(status_aktif)}")


# ── Pemeriksaan isinstance() ─────────────────────────────────────────────────
print(f"NIM adalah str?     {isinstance(nim, str)}")
print(f"Semester adalah int? {isinstance(semester, int)}")
