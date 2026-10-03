"""
==========================================================
 TUGAS 3 - Kalkulator Serbaguna
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat fungsi kalkulator(a, b, operasi="+") dengan default param
 2. Tangani pembagian dengan nol
 3. Buat fungsi statistik(*args) -> dict {min, max, sum, mean, count}
 4. Buat fungsi format_output(**kwargs) -> cetak key: value
 5. Demonstrasikan lambda dengan map() (kuadrat)
 6. Demonstrasikan lambda dengan filter() (bilangan genap)
 7. Demonstrasikan lambda dengan sorted() (sort list of tuple)
==========================================================
"""


def kalkulator(a, b, operasi="+"):
    """Kalkulator dasar dengan default parameter.

    Args:
        a (float): Bilangan pertama.
        b (float): Bilangan kedua.
        operasi (str): Operator (+, -, *, /, //, %, **). Default: "+".

    Returns:
        float: Hasil perhitungan, atau None jika operasi tidak valid.
    """
    if operasi == "+":
        return a + b
    elif operasi == "-":
        return a - b
    elif operasi == "*":
        return a * b
    elif operasi in ("/", "//", "%"):
        if b == 0:
            print("Error: pembagian dengan nol!")
            return None
        if operasi == "/":
            return a / b
        elif operasi == "//":
            return a // b
        return a % b
    elif operasi == "**":
        return a ** b
    print(f"Error: operasi '{operasi}' tidak dikenal")
    return None


def statistik(*args):
    """Menghitung statistik dari sekumpulan angka.

    Args:
        *args: Bilangan-bilangan yang akan dihitung statistiknya.

    Returns:
        dict: {"min": ..., "max": ..., "sum": ..., "mean": ..., "count": ...}
    """
    return {
        "min": min(args),
        "max": max(args),
        "sum": sum(args),
        "mean": sum(args) / len(args),
        "count": len(args),
    }


def format_output(**kwargs):
    """Mencetak data dalam format key: value yang rapi.

    Args:
        **kwargs: Pasangan key-value yang akan dicetak.
    """
    for key, value in kwargs.items():
        print(f"  {key:<15}: {value}")


# ── Demonstrasi ──────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Kalkulator ===")
    for op in ("+", "-", "*", "/", "//", "%", "**"):
        print(f"10 {op} 3 = {kalkulator(10, 3, op)}")
    print(f"10 (default) 3 = {kalkulator(10, 3)}")
    print(f"10 / 0 = {kalkulator(10, 0, '/')}")

    print("\n=== Statistik ===")
    hasil = statistik(85, 90, 78, 92, 65, 88, 73)
    print(hasil)

    print("\n=== Format Output ===")
    format_output(nama="Ahmad", nim="105841100123", jurusan="Informatika")

    angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    kuadrat = list(map(lambda x: x ** 2, angka))
    print(f"\nKuadrat: {kuadrat}")

    genap = list(filter(lambda x: x % 2 == 0, angka))
    print(f"Genap  : {genap}")

    mahasiswa = [("Ahmad", 85), ("Siti", 92), ("Budi", 78), ("Dewi", 90)]
    by_nilai = sorted(mahasiswa, key=lambda x: x[1], reverse=True)
    print(f"\nUrut by nilai: {by_nilai}")
