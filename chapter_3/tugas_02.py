"""
==========================================================
 TUGAS 2 - Pola & Deret
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat fungsi pola_segitiga(n) -> cetak segitiga bintang
 2. Buat fungsi pola_segitiga_terbalik(n) -> cetak segitiga terbalik
 3. Buat fungsi pola_diamond(n) -> cetak pola diamond/berlian
 4. Buat fungsi deret_fibonacci(n) -> list n bilangan Fibonacci
 5. Buat fungsi is_prima(n) -> True jika n bilangan prima
 6. Tampilkan bilangan prima 1-100 menggunakan filter() + is_prima
==========================================================
"""


def pola_segitiga(n):
    """Mencetak pola segitiga bintang dengan tinggi n.

    Args:
        n (int): Tinggi segitiga.

    Contoh (n=4):
       *
      **
     ***
    ****
    """
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


def pola_segitiga_terbalik(n):
    """Mencetak pola segitiga terbalik dengan tinggi n.

    Args:
        n (int): Tinggi segitiga.

    Contoh (n=4):
    ****
     ***
      **
       *
    """
    for i in range(n, 0, -1):
        print(" " * (n - i) + "*" * i)


def pola_diamond(n):
    """Mencetak pola diamond/berlian.

    Args:
        n (int): Setengah tinggi diamond (jumlah baris bagian atas).

    Contoh (n=5):
        *
       ***
      *****
     *******
    *********
     *******
      *****
       ***
        *
    """
    # Bagian atas membesar, bagian bawah mengecil tanpa mengulang baris tengah
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * (2 * i - 1))
    for i in range(n - 1, 0, -1):
        print(" " * (n - i) + "*" * (2 * i - 1))


def deret_fibonacci(n):
    """Mengembalikan list berisi n bilangan Fibonacci pertama.

    Args:
        n (int): Jumlah bilangan Fibonacci yang diinginkan.

    Returns:
        list: Deret Fibonacci. Contoh (n=8): [0, 1, 1, 2, 3, 5, 8, 13]
    """
    deret = []
    a, b = 0, 1
    for _ in range(n):
        deret.append(a)
        a, b = b, a + b
    return deret


def is_prima(n):
    """Memeriksa apakah n adalah bilangan prima.

    Args:
        n (int): Bilangan yang diperiksa.

    Returns:
        bool: True jika prima, False jika bukan.
    """
    if n < 2:
        return False
    for pembagi in range(2, int(n ** 0.5) + 1):
        if n % pembagi == 0:
            return False
    return True


# ── Demonstrasi ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Pola Segitiga (n=5) ===")
    pola_segitiga(5)

    print("\n=== Pola Segitiga Terbalik (n=5) ===")
    pola_segitiga_terbalik(5)

    print("\n=== Pola Diamond (n=5) ===")
    pola_diamond(5)

    print(f"\nFibonacci (15): {deret_fibonacci(15)}")

    bilangan_prima = list(filter(is_prima, range(1, 101)))
    print(f"\nBilangan prima (1-100): {bilangan_prima}")
    print(f"Jumlah: {len(bilangan_prima)}")
