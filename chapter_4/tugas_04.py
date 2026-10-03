"""
==========================================================
 TUGAS 4 - Class Bangun Ruang
 Chapter 4: Object-Oriented Programming
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat class BangunRuang (parent) dengan method abstract:
    volume(), luas_permukaan(), info()
 2. Buat subclass: Kubus, Balok, Tabung, Bola
 3. Implementasikan @classmethod sebagai alternative constructor
    (contoh: Kubus.dari_volume(vol) -> buat Kubus dari volume)
 4. Implementasikan @staticmethod untuk validasi
    (contoh: Kubus.is_valid(sisi) -> True jika sisi > 0)
 5. Overload operator __gt__ (>) untuk perbandingan volume
 6. Urutkan list campuran bangun ruang berdasarkan volume
    menggunakan sorted() + lambda

 Konsep yang dipelajari:
 - Abstract class dan method (tanpa ABC, gunakan raise)
 - @classmethod dan @staticmethod
 - Operator overloading (__gt__, __eq__, __lt__)
 - Polymorphism dalam sorted() + lambda
 - Rumus: pi = 3.14159265358979

 Rumus Bangun Ruang:
 | Bangun | Volume              | Luas Permukaan          |
 |--------|---------------------|-------------------------|
 | Kubus  | s^3                 | 6 * s^2                 |
 | Balok  | p * l * t           | 2 * (pl + pt + lt)      |
 | Tabung | pi * r^2 * t        | 2 * pi * r * (r + t)    |
 | Bola   | 4/3 * pi * r^3      | 4 * pi * r^2            |
==========================================================
"""

import math


class BangunRuang:
    """Class dasar (abstract) untuk bangun ruang.

    Class ini tidak dimaksudkan untuk diinstansiasi secara langsung.
    Subclass harus mengoverride semua method.

    Attributes:
        nama (str): Nama bangun ruang.
    """

    def __init__(self, nama):
        """Inisialisasi bangun ruang.

        Args:
            nama (str): Nama bangun ruang.
        """
        self.nama = nama

    def volume(self):
        """Menghitung volume bangun ruang (abstract).

        Raises:
            NotImplementedError: Harus diimplementasikan oleh subclass.
        """
        raise NotImplementedError("Subclass harus mengimplementasikan volume()")

    def luas_permukaan(self):
        """Menghitung luas permukaan bangun ruang (abstract).

        Raises:
            NotImplementedError: Harus diimplementasikan oleh subclass.
        """
        raise NotImplementedError("Subclass harus mengimplementasikan luas_permukaan()")

    def info(self):
        """Menampilkan informasi lengkap bangun ruang (abstract).

        Returns:
            str: Informasi meliputi nama, dimensi, volume, luas permukaan.
        """
        raise NotImplementedError("Subclass harus mengimplementasikan info()")

    def __gt__(self, other):
        """Overload operator > untuk membandingkan volume.

        Args:
            other (BangunRuang): Bangun ruang lain.

        Returns:
            bool: True jika volume self > volume other.
        """
        return self.volume() > other.volume()

    def __eq__(self, other):
        """Overload operator == untuk membandingkan volume.

        Args:
            other (BangunRuang): Bangun ruang lain.

        Returns:
            bool: True jika volume sama (toleransi 0.01).
        """
        return abs(self.volume() - other.volume()) < 0.01

    def __lt__(self, other):
        """Overload operator < untuk membandingkan volume.

        Args:
            other (BangunRuang): Bangun ruang lain.

        Returns:
            bool: True jika volume self < volume other.
        """
        return self.volume() < other.volume()

    def __str__(self):
        """Representasi string.

        Returns:
            str: Contoh -> "Kubus (V=125.00)"
        """
        return f"{self.nama} (V={self.volume():.2f})"


class Kubus(BangunRuang):
    """Bangun ruang Kubus.

    Attributes:
        sisi (float): Panjang sisi kubus.
    """

    def __init__(self, sisi):
        """Inisialisasi Kubus.

        Args:
            sisi (float): Panjang sisi kubus.
        """
        super().__init__("Kubus")
        self.sisi = sisi

    def volume(self):
        """Menghitung volume kubus.

        Returns:
            float: Volume = sisi^3
        """
        return self.sisi ** 3

    def luas_permukaan(self):
        """Menghitung luas permukaan kubus.

        Returns:
            float: Luas = 6 * sisi^2
        """
        return 6 * self.sisi ** 2

    def info(self):
        """Informasi lengkap kubus.

        Returns:
            str: Informasi meliputi sisi, volume, luas permukaan.
        """
        return (
            f"Kubus [sisi={self.sisi:g}]\n"
            f"  Volume         : {self.volume():.2f}\n"
            f"  Luas Permukaan : {self.luas_permukaan():.2f}"
        )

    @classmethod
    def dari_volume(cls, vol):
        """Alternative constructor: buat Kubus dari volume.

        Args:
            vol (float): Volume yang diinginkan.

        Returns:
            Kubus: Objek Kubus dengan sisi yang sesuai.
        """
        return cls(vol ** (1 / 3))

    @staticmethod
    def is_valid(sisi):
        """Validasi apakah sisi valid untuk membuat kubus.

        Args:
            sisi (float): Panjang sisi yang akan divalidasi.

        Returns:
            bool: True jika sisi > 0 dan bertipe numerik.
        """
        return isinstance(sisi, (int, float)) and sisi > 0


class Balok(BangunRuang):
    """Bangun ruang Balok.

    Attributes:
        panjang (float): Panjang balok.
        lebar (float): Lebar balok.
        tinggi (float): Tinggi balok.
    """

    def __init__(self, panjang, lebar, tinggi):
        """Inisialisasi Balok.

        Args:
            panjang (float): Panjang balok.
            lebar (float): Lebar balok.
            tinggi (float): Tinggi balok.
        """
        super().__init__("Balok")
        self.panjang = panjang
        self.lebar = lebar
        self.tinggi = tinggi

    def volume(self):
        """Menghitung volume balok.

        Returns:
            float: Volume = panjang * lebar * tinggi
        """
        return self.panjang * self.lebar * self.tinggi

    def luas_permukaan(self):
        """Menghitung luas permukaan balok.

        Returns:
            float: Luas = 2 * (pl + pt + lt)
        """
        p, l, t = self.panjang, self.lebar, self.tinggi
        return 2 * (p * l + p * t + l * t)

    def info(self):
        """Informasi lengkap balok.

        Returns:
            str: Informasi meliputi dimensi, volume, luas permukaan.
        """
        return (
            f"Balok [p={self.panjang:g}, l={self.lebar:g}, t={self.tinggi:g}]\n"
            f"  Volume         : {self.volume():.2f}\n"
            f"  Luas Permukaan : {self.luas_permukaan():.2f}"
        )

    @classmethod
    def dari_kubus(cls, sisi):
        """Alternative constructor: buat Balok dari kubus (semua sisi sama).

        Args:
            sisi (float): Panjang sisi.

        Returns:
            Balok: Objek Balok dengan p=l=t=sisi.
        """
        return cls(sisi, sisi, sisi)

    @staticmethod
    def is_valid(panjang, lebar, tinggi):
        """Validasi dimensi balok.

        Returns:
            bool: True jika semua dimensi > 0.
        """
        return all(isinstance(d, (int, float)) and d > 0
                   for d in (panjang, lebar, tinggi))


class Tabung(BangunRuang):
    """Bangun ruang Tabung (Silinder).

    Attributes:
        jari_jari (float): Jari-jari alas tabung.
        tinggi (float): Tinggi tabung.
    """

    def __init__(self, jari_jari, tinggi):
        """Inisialisasi Tabung.

        Args:
            jari_jari (float): Jari-jari alas.
            tinggi (float): Tinggi tabung.
        """
        super().__init__("Tabung")
        self.jari_jari = jari_jari
        self.tinggi = tinggi

    def volume(self):
        """Menghitung volume tabung.

        Returns:
            float: Volume = pi * r^2 * t
        """
        return math.pi * self.jari_jari ** 2 * self.tinggi

    def luas_permukaan(self):
        """Menghitung luas permukaan tabung.

        Returns:
            float: Luas = 2 * pi * r * (r + t)
        """
        return 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)

    def info(self):
        """Informasi lengkap tabung.

        Returns:
            str: Informasi meliputi jari-jari, tinggi, volume, luas permukaan.
        """
        return (
            f"Tabung [r={self.jari_jari:g}, t={self.tinggi:g}]\n"
            f"  Volume         : {self.volume():.2f}\n"
            f"  Luas Permukaan : {self.luas_permukaan():.2f}"
        )

    @classmethod
    def dari_volume(cls, vol, tinggi):
        """Alternative constructor: buat Tabung dari volume dan tinggi.

        Args:
            vol (float): Volume yang diinginkan.
            tinggi (float): Tinggi tabung.

        Returns:
            Tabung: Objek Tabung dengan jari-jari yang sesuai.
        """
        r = math.sqrt(vol / (math.pi * tinggi))
        return cls(r, tinggi)

    @staticmethod
    def is_valid(jari_jari, tinggi):
        """Validasi dimensi tabung.

        Returns:
            bool: True jika jari_jari > 0 dan tinggi > 0.
        """
        return all(isinstance(d, (int, float)) and d > 0
                   for d in (jari_jari, tinggi))


class Bola(BangunRuang):
    """Bangun ruang Bola.

    Attributes:
        jari_jari (float): Jari-jari bola.
    """

    def __init__(self, jari_jari):
        """Inisialisasi Bola.

        Args:
            jari_jari (float): Jari-jari bola.
        """
        super().__init__("Bola")
        self.jari_jari = jari_jari

    def volume(self):
        """Menghitung volume bola.

        Returns:
            float: Volume = 4/3 * pi * r^3
        """
        return (4 / 3) * math.pi * self.jari_jari ** 3

    def luas_permukaan(self):
        """Menghitung luas permukaan bola.

        Returns:
            float: Luas = 4 * pi * r^2
        """
        return 4 * math.pi * self.jari_jari ** 2

    def info(self):
        """Informasi lengkap bola.

        Returns:
            str: Informasi meliputi jari-jari, volume, luas permukaan.
        """
        return (
            f"Bola [r={self.jari_jari:g}]\n"
            f"  Volume         : {self.volume():.2f}\n"
            f"  Luas Permukaan : {self.luas_permukaan():.2f}"
        )

    @classmethod
    def dari_volume(cls, vol):
        """Alternative constructor: buat Bola dari volume.

        Args:
            vol (float): Volume yang diinginkan.

        Returns:
            Bola: Objek Bola dengan jari-jari yang sesuai.
        """
        r = ((3 * vol) / (4 * math.pi)) ** (1 / 3)
        return cls(r)

    @staticmethod
    def is_valid(jari_jari):
        """Validasi jari-jari bola.

        Returns:
            bool: True jika jari_jari > 0.
        """
        return isinstance(jari_jari, (int, float)) and jari_jari > 0


# ── Demonstrasi ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    kubus = Kubus(5)
    balok = Balok(8, 4, 3)
    tabung = Tabung(7, 10)
    bola = Bola(6)

    # Polymorphism: info() dipanggil pada tiap objek tanpa peduli class-nya
    print("=== INFO BANGUN RUANG ===")
    bangun_list = [kubus, balok, tabung, bola]
    for bangun in bangun_list:
        print(bangun.info())
        print()

    print("=== ALTERNATIVE CONSTRUCTOR (@classmethod) ===")
    kubus2 = Kubus.dari_volume(125)
    print(f"Kubus dari volume 125: sisi = {kubus2.sisi:.2f}")
    print(kubus2.info())

    tabung2 = Tabung.dari_volume(1000, 10)
    print(f"\nTabung dari volume 1000 (t=10): r = {tabung2.jari_jari:.2f}")
    print(tabung2.info())

    bola2 = Bola.dari_volume(1000)
    print(f"\nBola dari volume 1000: r = {bola2.jari_jari:.2f}")
    print(f"Balok.dari_kubus(3): {Balok.dari_kubus(3).info()}")

    print("\n=== VALIDASI (@staticmethod) ===")
    print(f"Kubus.is_valid(5)      = {Kubus.is_valid(5)}")
    print(f"Kubus.is_valid(-3)     = {Kubus.is_valid(-3)}")
    print(f"Kubus.is_valid('a')    = {Kubus.is_valid('a')}")
    print(f"Balok.is_valid(1, 2, 3) = {Balok.is_valid(1, 2, 3)}")
    print(f"Tabung.is_valid(7, 10) = {Tabung.is_valid(7, 10)}")
    print(f"Tabung.is_valid(-1, 5) = {Tabung.is_valid(-1, 5)}")
    print(f"Bola.is_valid(0)       = {Bola.is_valid(0)}")

    print("\n=== OPERATOR OVERLOADING ===")
    print(f"{kubus} > {balok}  ? {kubus > balok}")
    print(f"{tabung} > {bola}  ? {tabung > bola}")
    print(f"{kubus} == {kubus2} ? {kubus == kubus2}")
    print(f"{kubus} < {bola}   ? {kubus < bola}")

    print("\n=== URUTAN BERDASARKAN VOLUME ===")
    bangun_list = [kubus, balok, tabung, bola]
    urut_volume = sorted(bangun_list, key=lambda b: b.volume())
    print("Kecil -> Besar:")
    for i, b in enumerate(urut_volume, 1):
        print(f"  {i}. {b.nama:<8} -> Volume: {b.volume():>10.2f}")

    print("\nBesar -> Kecil:")
    urut_desc = sorted(bangun_list, key=lambda b: b.volume(), reverse=True)
    for i, b in enumerate(urut_desc, 1):
        print(f"  {i}. {b.nama:<8} -> Volume: {b.volume():>10.2f}")

    print("\n=== TABEL BANGUN RUANG ===")
    print(f"{'Bangun':<8} | {'Volume':>10} | {'Luas Permukaan':>14}")
    print("-" * 38)
    for b in urut_volume:
        print(f"{b.nama:<8} | {b.volume():>10.2f} | {b.luas_permukaan():>14.2f}")

    print("\n=== TEST ABSTRACT (NotImplementedError) ===")
    try:
        br = BangunRuang("Test")
        br.volume()
    except NotImplementedError as e:
        print(f"Error: {e}")
