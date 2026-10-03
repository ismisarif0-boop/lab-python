"""
==========================================================
 TUGAS 1 - Sistem Perpustakaan
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat class Buku dengan atribut: judul, penulis, tahun, isbn, tersedia
 2. Implementasikan __str__ dan __repr__ pada class Buku
 3. Buat class Perpustakaan dengan atribut: nama, daftar_buku
 4. Implementasikan method: tambah_buku, cari_buku (pencarian parsial),
    pinjam_buku (by isbn), kembalikan_buku (by isbn), tampilkan_semua
 5. Buat minimal 5 objek Buku dan demonstrasikan semua method

 Konsep yang dipelajari:
 - Membuat class dan __init__
 - Method __str__ dan __repr__
 - Atribut instance dan default value
 - Interaksi antar objek (Perpustakaan memiliki list Buku)
==========================================================
"""


class Buku:
    """Representasi sebuah buku di perpustakaan.

    Attributes:
        judul (str): Judul buku.
        penulis (str): Nama penulis buku.
        tahun (int): Tahun terbit buku.
        isbn (str): Nomor ISBN buku (unik).
        tersedia (bool): Status ketersediaan buku (default True).
    """

    def __init__(self, judul, penulis, tahun, isbn):
        """Inisialisasi objek Buku.

        Args:
            judul (str): Judul buku.
            penulis (str): Nama penulis.
            tahun (int): Tahun terbit.
            isbn (str): Nomor ISBN.
        """
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.isbn = isbn
        self.tersedia = True  # buku baru selalu tersedia

    def __str__(self):
        """Representasi string yang mudah dibaca.

        Returns:
            str: Contoh -> "Python Dasar oleh John (2023) [Tersedia]"
        """
        status = "Tersedia" if self.tersedia else "Dipinjam"
        return f"{self.judul} oleh {self.penulis} ({self.tahun}) [{status}]"

    def __repr__(self):
        """Representasi resmi untuk debugging.

        Returns:
            str: Contoh -> "Buku('Python Dasar', 'John', 2023, '978-123')"
        """
        return f"Buku('{self.judul}', '{self.penulis}', {self.tahun}, '{self.isbn}')"


class Perpustakaan:
    """Sistem manajemen perpustakaan sederhana.

    Attributes:
        nama (str): Nama perpustakaan.
        daftar_buku (list): Koleksi objek Buku.
    """

    def __init__(self, nama):
        """Inisialisasi perpustakaan.

        Args:
            nama (str): Nama perpustakaan.
        """
        self.nama = nama
        self.daftar_buku = []

    def tambah_buku(self, buku):
        """Menambahkan buku ke koleksi perpustakaan.

        Args:
            buku (Buku): Objek Buku yang akan ditambahkan.
        """
        if self._temukan(buku.isbn) is not None:
            print(f"Buku dengan ISBN {buku.isbn} sudah ada, dilewati.")
            return
        self.daftar_buku.append(buku)

    def _temukan(self, isbn):
        """Mencari buku berdasarkan ISBN.

        Returns:
            Buku | None: Objek Buku, atau None jika tidak ditemukan.
        """
        for buku in self.daftar_buku:
            if buku.isbn == isbn:
                return buku
        return None

    def cari_buku(self, kata_kunci):
        """Mencari buku berdasarkan kata kunci (pencarian parsial).

        Pencarian dilakukan pada judul dan penulis (case-insensitive).

        Args:
            kata_kunci (str): Kata kunci pencarian.

        Returns:
            list: Daftar objek Buku yang cocok.
        """
        kunci = kata_kunci.lower()
        return [
            b for b in self.daftar_buku
            if kunci in b.judul.lower() or kunci in b.penulis.lower()
        ]

    def pinjam_buku(self, isbn):
        """Meminjam buku berdasarkan ISBN.

        Args:
            isbn (str): Nomor ISBN buku yang akan dipinjam.

        Returns:
            str: Pesan berhasil/gagal meminjam.
        """
        buku = self._temukan(isbn)
        if buku is None:
            return f"Gagal: buku dengan ISBN {isbn} tidak ditemukan."
        if not buku.tersedia:
            return f"Gagal: '{buku.judul}' sedang dipinjam."
        buku.tersedia = False
        return f"Berhasil meminjam '{buku.judul}'."

    def kembalikan_buku(self, isbn):
        """Mengembalikan buku berdasarkan ISBN.

        Args:
            isbn (str): Nomor ISBN buku yang akan dikembalikan.

        Returns:
            str: Pesan berhasil/gagal mengembalikan.
        """
        buku = self._temukan(isbn)
        if buku is None:
            return f"Gagal: buku dengan ISBN {isbn} tidak ditemukan."
        if buku.tersedia:
            return f"Gagal: '{buku.judul}' sudah tersedia (tidak sedang dipinjam)."
        buku.tersedia = True
        return f"Berhasil mengembalikan '{buku.judul}'."

    def tampilkan_semua(self):
        """Menampilkan semua buku dalam format tabel.

        Contoh output:
        ============================================================
        No | Judul               | Penulis        | Tahun | Status
        ------------------------------------------------------------
         1 | Python Dasar        | John Doe       |  2023 | Tersedia
         2 | Data Science        | Jane Smith     |  2022 | Dipinjam
        ============================================================
        """
        print(f"{'=' * 12} {self.nama.upper()} {'=' * 12}")
        print(f"{'No':>2} | {'Judul':<26} | {'Penulis':<17} | {'Tahun':>5} | Status")
        print("-" * 75)
        for i, b in enumerate(self.daftar_buku, 1):
            status = "Tersedia" if b.tersedia else "Dipinjam"
            print(f"{i:>2} | {b.judul:<26} | {b.penulis:<17} | {b.tahun:>5} | {status}")
        print("=" * 75)
        tersedia = sum(1 for b in self.daftar_buku if b.tersedia)
        total = len(self.daftar_buku)
        print(f"Total: {total} buku | Tersedia: {tersedia} | Dipinjam: {total - tersedia}")


# ── Demonstrasi ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    buku1 = Buku("Python Dasar", "Guido van Rossum", 2023, "978-001")
    buku2 = Buku("Data Science dengan Python", "Jake VanderPlas", 2022, "978-002")
    buku3 = Buku("Machine Learning", "Andrew Ng", 2021, "978-003")
    buku4 = Buku("Algoritma & Pemrograman", "Thomas Cormen", 2020, "978-004")
    buku5 = Buku("Artificial Intelligence", "Stuart Russell", 2019, "978-005")

    perpus = Perpustakaan("Perpustakaan Unismuh Makassar")

    for buku in [buku1, buku2, buku3, buku4, buku5]:
        perpus.tambah_buku(buku)
    perpus.tambah_buku(buku1)  # ISBN duplikat, harus ditolak

    print("=== DAFTAR BUKU ===")
    perpus.tampilkan_semua()

    print("\n=== CARI BUKU: 'python' ===")
    for buku in perpus.cari_buku("python"):
        print(f"  - {buku}")

    print("\n=== PINJAM BUKU ===")
    print(perpus.pinjam_buku("978-001"))
    print(perpus.pinjam_buku("978-001"))  # sudah dipinjam
    print(perpus.pinjam_buku("999-999"))  # tidak ditemukan

    print("\n=== DAFTAR BUKU (setelah peminjaman) ===")
    perpus.tampilkan_semua()

    print("\n=== KEMBALIKAN BUKU ===")
    print(perpus.kembalikan_buku("978-001"))
    print(perpus.kembalikan_buku("978-001"))  # sudah tersedia

    print("\n=== REPR ===")
    print(repr(buku1))
