"""
==========================================================
 TUGAS 2 - Sistem Akademik dengan Inheritance
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat class Orang (parent) dengan atribut: nama, umur, alamat
 2. Buat class Mahasiswa(Orang) dengan atribut: nim, jurusan, semester,
    daftar_mk; method: tambah_mk, hitung_ipk, info (override)
 3. Buat class Dosen(Orang) dengan atribut: nidn, bidang_keahlian,
    daftar_mk_diampu; method: tambah_mk_diampu, info (override)
 4. Buat class Asisten(Mahasiswa) dengan atribut: lab, dosen_pembimbing
 5. Demonstrasikan polymorphism, isinstance(), dan issubclass()

 Konsep yang dipelajari:
 - Inheritance (pewarisan) single & multilevel
 - Method overriding
 - super() untuk memanggil parent constructor
 - Polymorphism (method yang sama, perilaku berbeda)
 - isinstance() dan issubclass()
==========================================================
"""


class Orang:
    """Class dasar untuk merepresentasikan seseorang.

    Attributes:
        nama (str): Nama lengkap.
        umur (int): Umur dalam tahun.
        alamat (str): Alamat tempat tinggal.
    """

    def __init__(self, nama, umur, alamat):
        """Inisialisasi objek Orang.

        Args:
            nama (str): Nama lengkap.
            umur (int): Umur dalam tahun.
            alamat (str): Alamat tempat tinggal.
        """
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def info(self):
        """Menampilkan informasi dasar seseorang.

        Returns:
            str: Informasi dalam format "Nama: ..., Umur: ..., Alamat: ..."
        """
        return f"Nama: {self.nama}, Umur: {self.umur}, Alamat: {self.alamat}"

    def __str__(self):
        """Representasi string.

        Returns:
            str: Nama orang tersebut.
        """
        return self.nama


class Mahasiswa(Orang):
    """Representasi mahasiswa, turunan dari Orang.

    Attributes:
        nim (str): Nomor Induk Mahasiswa.
        jurusan (str): Program studi.
        semester (int): Semester saat ini.
        daftar_mk (list): Daftar mata kuliah berupa list of dict.
            Contoh: [{"nama": "Kalkulus", "sks": 3, "nilai": "A"}, ...]
    """

    def __init__(self, nama, umur, alamat, nim, jurusan, semester):
        """Inisialisasi objek Mahasiswa.

        Args:
            nama (str): Nama lengkap.
            umur (int): Umur dalam tahun.
            alamat (str): Alamat tempat tinggal.
            nim (str): Nomor Induk Mahasiswa.
            jurusan (str): Program studi.
            semester (int): Semester saat ini.
        """
        super().__init__(nama, umur, alamat)
        self.nim = nim
        self.jurusan = jurusan
        self.semester = semester
        self.daftar_mk = []

    def tambah_mk(self, nama_mk, sks, nilai):
        """Menambahkan mata kuliah ke daftar.

        Args:
            nama_mk (str): Nama mata kuliah.
            sks (int): Jumlah SKS.
            nilai (str): Nilai huruf (A/B/C/D/E).
        """
        self.daftar_mk.append({"nama": nama_mk, "sks": sks, "nilai": nilai})

    def hitung_ipk(self):
        """Menghitung IPK berdasarkan daftar mata kuliah.

        Bobot nilai: A=4, B=3, C=2, D=1, E=0
        IPK = sum(bobot * sks) / sum(sks)

        Returns:
            float: IPK mahasiswa (0.0 - 4.0), atau 0.0 jika belum ada MK.
        """
        bobot = {"A": 4, "B": 3, "C": 2, "D": 1, "E": 0}
        total_sks = sum(mk["sks"] for mk in self.daftar_mk)
        if total_sks == 0:
            return 0.0
        total_bobot = sum(bobot[mk["nilai"]] * mk["sks"] for mk in self.daftar_mk)
        return total_bobot / total_sks

    def info(self):
        """Override method info() dari parent.

        Returns:
            str: Informasi lengkap mahasiswa termasuk NIM, jurusan, IPK.
        """
        return (
            f"{super().info()}\n"
            f"  NIM: {self.nim}, Jurusan: {self.jurusan}, Semester: {self.semester}, "
            f"IPK: {self.hitung_ipk():.2f}"
        )


class Dosen(Orang):
    """Representasi dosen, turunan dari Orang.

    Attributes:
        nidn (str): Nomor Induk Dosen Nasional.
        bidang_keahlian (str): Bidang keahlian utama.
        daftar_mk_diampu (list): Daftar nama mata kuliah yang diampu.
    """

    def __init__(self, nama, umur, alamat, nidn, bidang_keahlian):
        """Inisialisasi objek Dosen.

        Args:
            nama (str): Nama lengkap.
            umur (int): Umur dalam tahun.
            alamat (str): Alamat tempat tinggal.
            nidn (str): Nomor Induk Dosen Nasional.
            bidang_keahlian (str): Bidang keahlian.
        """
        super().__init__(nama, umur, alamat)
        self.nidn = nidn
        self.bidang_keahlian = bidang_keahlian
        self.daftar_mk_diampu = []

    def tambah_mk_diampu(self, nama_mk):
        """Menambahkan mata kuliah yang diampu.

        Args:
            nama_mk (str): Nama mata kuliah.
        """
        self.daftar_mk_diampu.append(nama_mk)

    def info(self):
        """Override method info() dari parent.

        Returns:
            str: Informasi lengkap dosen termasuk NIDN dan bidang keahlian.
        """
        mk_diampu = ", ".join(self.daftar_mk_diampu) or "-"
        return (
            f"{super().info()}\n"
            f"  NIDN: {self.nidn}, Keahlian: {self.bidang_keahlian}\n"
            f"  MK diampu: {mk_diampu}"
        )


class Asisten(Mahasiswa):
    """Representasi asisten laboratorium, turunan dari Mahasiswa.

    Contoh multilevel inheritance: Asisten -> Mahasiswa -> Orang.

    Attributes:
        lab (str): Nama laboratorium tempat bertugas.
        dosen_pembimbing (str): Nama dosen pembimbing.
    """

    def __init__(
        self, nama, umur, alamat, nim, jurusan, semester, lab, dosen_pembimbing
    ):
        """Inisialisasi objek Asisten.

        Args:
            nama (str): Nama lengkap.
            umur (int): Umur dalam tahun.
            alamat (str): Alamat tempat tinggal.
            nim (str): NIM.
            jurusan (str): Program studi.
            semester (int): Semester saat ini.
            lab (str): Nama laboratorium.
            dosen_pembimbing (str): Nama dosen pembimbing.
        """
        super().__init__(nama, umur, alamat, nim, jurusan, semester)
        self.lab = lab
        self.dosen_pembimbing = dosen_pembimbing

    def info(self):
        """Override method info() dari parent.

        Returns:
            str: Informasi lengkap asisten termasuk lab dan dosen pembimbing.
        """
        return (
            f"{super().info()}\n"
            f"  Asisten di: {self.lab}, Pembimbing: {self.dosen_pembimbing}"
        )


# ── Demonstrasi ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    dosen1 = Dosen("Dr. Ahmad", 45, "Makassar", "001122", "Machine Learning")
    dosen1.tambah_mk_diampu("Kecerdasan Buatan")
    dosen1.tambah_mk_diampu("Data Mining")

    mhs1 = Mahasiswa("Siti Aisyah", 20, "Makassar", "105841100123", "Informatika", 5)
    mhs1.tambah_mk("Kalkulus", 3, "A")
    mhs1.tambah_mk("Pemrograman Dasar", 4, "A")
    mhs1.tambah_mk("Basis Data", 3, "B")

    mhs2 = Mahasiswa("Budi Santoso", 21, "Gowa", "105841100456", "Informatika", 5)
    mhs2.tambah_mk("Kalkulus", 3, "B")
    mhs2.tambah_mk("Pemrograman Dasar", 4, "A")
    mhs2.tambah_mk("Basis Data", 3, "C")

    asisten1 = Asisten("Dewi Lestari", 22, "Makassar", "105841100789",
                       "Informatika", 7, "Lab AI", "Dr. Ahmad")
    asisten1.tambah_mk("Kecerdasan Buatan", 3, "A")
    asisten1.tambah_mk("Machine Learning", 3, "A")

    # Polymorphism: info() berperilaku berbeda di setiap class
    print("=== POLYMORPHISM ===")
    semua_orang = [dosen1, mhs1, mhs2, asisten1]
    for orang in semua_orang:
        print(f"\n[{type(orang).__name__}]")
        print(orang.info())
        print("-" * 50)

    print("\n=== ISINSTANCE ===")
    for orang in semua_orang:
        print(f"{orang.nama}:")
        print(f"  isinstance(Orang)     = {isinstance(orang, Orang)}")
        print(f"  isinstance(Mahasiswa) = {isinstance(orang, Mahasiswa)}")
        print(f"  isinstance(Dosen)     = {isinstance(orang, Dosen)}")
        print(f"  isinstance(Asisten)   = {isinstance(orang, Asisten)}")

    print("\n=== ISSUBCLASS ===")
    print(f"Mahasiswa subclass Orang?   {issubclass(Mahasiswa, Orang)}")
    print(f"Dosen subclass Orang?       {issubclass(Dosen, Orang)}")
    print(f"Asisten subclass Mahasiswa? {issubclass(Asisten, Mahasiswa)}")
    print(f"Asisten subclass Orang?     {issubclass(Asisten, Orang)}")
    print(f"Dosen subclass Mahasiswa?   {issubclass(Dosen, Mahasiswa)}")

    print("\n=== MRO (Method Resolution Order) ===")
    print(f"Asisten MRO: {[c.__name__ for c in Asisten.__mro__]}")
