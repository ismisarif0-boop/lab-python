"""
==========================================================
 TUGAS 3 - Sistem Keuangan dengan Encapsulation
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat class Rekening dengan access modifier:
    - Private: __saldo, __pin, __riwayat_transaksi
    - Protected: _nomor_rekening, _pemilik
    - Public: bank
 2. Implementasikan @property untuk saldo (read-only)
    dan pemilik (dengan setter validation)
 3. Implementasikan method: setor, tarik, transfer,
    cek_riwayat, ganti_pin (semua memerlukan verifikasi PIN)
 4. Demonstrasikan error saat mengakses atribut private
 5. Buat minimal 2 objek Rekening dan lakukan transaksi

 Konsep yang dipelajari:
 - Access modifier (public, protected, private)
 - Name mangling (double underscore)
 - Property decorator (@property, @setter)
 - Data validation dalam setter
 - Encapsulation untuk keamanan data
==========================================================
"""

from datetime import date


class Rekening:
    """Rekening bank dengan encapsulation.

    Access Modifier:
        Private (__)  : __saldo, __pin, __riwayat_transaksi
        Protected (_) : _nomor_rekening, _pemilik
        Public        : bank

    Attributes:
        bank (str): Nama bank.
    """

    def __init__(self, nomor_rekening, pemilik, pin, saldo_awal=0, bank="Bank Unismuh"):
        """Inisialisasi rekening baru.

        Args:
            nomor_rekening (str): Nomor rekening.
            pemilik (str): Nama pemilik rekening.
            pin (str): PIN 6 digit untuk verifikasi.
            saldo_awal (float): Saldo awal (default 0).
            bank (str): Nama bank (default "Bank Unismuh").
        """
        self.bank = bank

        # Protected (konvensi: satu underscore)
        self._nomor_rekening = nomor_rekening
        self._pemilik = pemilik

        # Private (name mangling: dua underscore)
        self.__saldo = saldo_awal
        self.__pin = pin
        self.__riwayat_transaksi = []
        self.__catat_transaksi("SALDO AWAL", saldo_awal, "Saldo awal")

    # ── Property: saldo (read-only) ─────────────────────────────────────────
    @property
    def saldo(self):
        """Getter untuk saldo (read-only, tanpa setter).

        Returns:
            float: Saldo saat ini.
        """
        return self.__saldo

    # ── Property: pemilik (dengan setter dan validasi) ──────────────────────
    @property
    def pemilik(self):
        """Getter untuk nama pemilik.

        Returns:
            str: Nama pemilik rekening.
        """
        return self._pemilik

    @pemilik.setter
    def pemilik(self, nama_baru):
        """Setter untuk nama pemilik dengan validasi.

        Args:
            nama_baru (str): Nama baru pemilik.

        Raises:
            ValueError: Jika nama kosong atau kurang dari 3 karakter.
        """
        if not nama_baru or len(nama_baru) < 3:
            raise ValueError("Nama harus minimal 3 karakter")
        self._pemilik = nama_baru

    def __verifikasi_pin(self, pin):
        """Verifikasi PIN (method private).

        Args:
            pin (str): PIN yang dimasukkan.

        Returns:
            bool: True jika PIN benar.
        """
        return pin == self.__pin

    def __catat_transaksi(self, jenis, jumlah, keterangan=""):
        """Mencatat transaksi ke riwayat (method private).

        Args:
            jenis (str): Jenis transaksi (SETOR/TARIK/TRANSFER).
            jumlah (float): Jumlah uang.
            keterangan (str): Keterangan tambahan.
        """
        self.__riwayat_transaksi.append({
            "tanggal": date.today().isoformat(),
            "jenis": jenis,
            "jumlah": jumlah,
            "keterangan": keterangan,
            "saldo_setelah": self.__saldo,
        })

    def __terima_transfer(self, jumlah, keterangan):
        """Menambah saldo dari transfer rekening lain (method private).

        Args:
            jumlah (float): Jumlah uang yang diterima.
            keterangan (str): Keterangan transaksi.
        """
        self.__saldo += jumlah
        self.__catat_transaksi("TERIMA", jumlah, keterangan)

    def setor(self, jumlah, pin):
        """Menyetor uang ke rekening.

        Args:
            jumlah (float): Jumlah uang yang disetor (harus > 0).
            pin (str): PIN untuk verifikasi.

        Returns:
            str: Pesan berhasil/gagal.
        """
        if not self.__verifikasi_pin(pin):
            return "Gagal: PIN salah."
        if jumlah <= 0:
            return "Gagal: jumlah setor harus lebih dari 0."
        self.__saldo += jumlah
        self.__catat_transaksi("SETOR", jumlah, "Setor tunai")
        return f"Berhasil! Setor Rp{jumlah:,.0f}. Saldo: Rp{self.__saldo:,.0f}"

    def tarik(self, jumlah, pin):
        """Menarik uang dari rekening.

        Args:
            jumlah (float): Jumlah uang yang ditarik (harus > 0).
            pin (str): PIN untuk verifikasi.

        Returns:
            str: Pesan berhasil/gagal.
        """
        if not self.__verifikasi_pin(pin):
            return "Gagal: PIN salah."
        if jumlah <= 0:
            return "Gagal: jumlah tarik harus lebih dari 0."
        if jumlah > self.__saldo:
            return "Gagal: saldo tidak cukup."
        self.__saldo -= jumlah
        self.__catat_transaksi("TARIK", jumlah, "Tarik tunai")
        return f"Berhasil! Tarik Rp{jumlah:,.0f}. Saldo: Rp{self.__saldo:,.0f}"

    def transfer(self, tujuan, jumlah, pin):
        """Transfer uang ke rekening lain.

        Args:
            tujuan (Rekening): Objek Rekening tujuan.
            jumlah (float): Jumlah uang yang ditransfer.
            pin (str): PIN pengirim untuk verifikasi.

        Returns:
            str: Pesan berhasil/gagal.
        """
        if not self.__verifikasi_pin(pin):
            return "Gagal: PIN salah."
        if jumlah <= 0:
            return "Gagal: jumlah transfer harus lebih dari 0."
        if jumlah > self.__saldo:
            return "Gagal: saldo tidak cukup."
        self.__saldo -= jumlah
        self.__catat_transaksi(
            "TRANSFER", jumlah, f"Transfer ke {tujuan._nomor_rekening}"
        )
        # Name mangling berlaku untuk objek lain dari class yang sama
        tujuan.__terima_transfer(jumlah, f"Dari {self._nomor_rekening}")
        return (f"Berhasil! Transfer ke {tujuan._nomor_rekening} "
                f"Rp{jumlah:,.0f}. Saldo: Rp{self.__saldo:,.0f}")

    def cek_riwayat(self, pin):
        """Menampilkan riwayat transaksi.

        Args:
            pin (str): PIN untuk verifikasi.

        Returns:
            str: Riwayat transaksi dalam format tabel, atau pesan error.
        """
        if not self.__verifikasi_pin(pin):
            return "Gagal: PIN salah."
        baris = [f"--- Riwayat Transaksi {self._nomor_rekening} ---"]
        for t in self.__riwayat_transaksi:
            baris.append(
                f"  [{t['tanggal']}] {t['jenis']:<10} | Rp {t['jumlah']:>12,.0f} "
                f"| {t['keterangan']}"
            )
        return "\n".join(baris)

    def ganti_pin(self, pin_lama, pin_baru):
        """Mengganti PIN rekening.

        Args:
            pin_lama (str): PIN lama untuk verifikasi.
            pin_baru (str): PIN baru (harus 6 digit angka).

        Returns:
            str: Pesan berhasil/gagal.
        """
        if not self.__verifikasi_pin(pin_lama):
            return "Gagal: PIN lama salah."
        if not (len(pin_baru) == 6 and pin_baru.isdigit()):
            return "Gagal: PIN baru harus 6 digit angka."
        self.__pin = pin_baru
        return "Berhasil! PIN telah diganti."

    def __str__(self):
        """Representasi string rekening.

        Returns:
            str: Contoh -> "[Bank Unismuh] 001 - Ahmad (Saldo: Rp 1,000,000)"
        """
        return (f"[{self.bank}] {self._nomor_rekening} - {self._pemilik} "
                f"(Saldo: Rp {self.__saldo:,.0f})")


# ── Demonstrasi ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    rek1 = Rekening("001", "Ahmad Dahlan", "123456", 5_000_000)
    rek2 = Rekening("002", "Siti Rahmah", "654321", 3_000_000)

    print("=== INFO REKENING ===")
    print(rek1)
    print(rek2)

    print("\n=== SETOR ===")
    print(rek1.setor(1_000_000, "123456"))
    print(rek1.setor(1_000_000, "000000"))  # PIN salah

    print("\n=== TARIK ===")
    print(rek1.tarik(500_000, "123456"))
    print(rek1.tarik(99_000_000, "123456"))  # saldo tidak cukup

    print("\n=== TRANSFER ===")
    print(rek1.transfer(rek2, 2_000_000, "123456"))

    print("\n=== CEK SALDO (property) ===")
    print(f"Saldo Ahmad: Rp {rek1.saldo:,.0f}")
    print(f"Saldo Siti : Rp {rek2.saldo:,.0f}")

    print("\n=== TEST AKSES PRIVATE ===")
    try:
        rek1.saldo = 999_999_999  # AttributeError (tanpa setter)
    except AttributeError as e:
        print(f"Error saldo: {e}")

    try:
        print(rek1.__saldo)  # AttributeError (name mangling)
    except AttributeError as e:
        print(f"Error __saldo: {e}")

    # Bisa diakses lewat name mangling (tidak disarankan!)
    print(f"Name mangling: rek1._Rekening__saldo = {rek1._Rekening__saldo}")

    print("\n=== TEST PROPERTY SETTER ===")
    rek1.pemilik = "Ahmad Dahlan Syamsuddin"
    print(f"Pemilik baru: {rek1.pemilik}")
    try:
        rek1.pemilik = "AB"  # ValueError (kurang dari 3 karakter)
    except ValueError as e:
        print(f"Error setter: {e}")

    print("\n=== RIWAYAT TRANSAKSI ===")
    print(rek1.cek_riwayat("123456"))
    print(rek2.cek_riwayat("654321"))
    print(rek1.cek_riwayat("000000"))  # PIN salah

    print("\n=== GANTI PIN ===")
    print(rek1.ganti_pin("123456", "111111"))
    print(rek1.ganti_pin("111111", "abc"))  # gagal: bukan 6 digit angka
    print(rek1.ganti_pin("999999", "222222"))  # gagal: PIN lama salah
