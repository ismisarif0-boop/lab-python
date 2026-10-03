"""
==========================================================
 TUGAS 4 - Permainan Tebak Angka
 Chapter 3: Control Flow & Fungsi
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat fungsi yang menghasilkan angka acak 1-100 (import random)
 2. Buat while loop untuk tebak angka (gunakan input())
 3. Berikan petunjuk "Terlalu besar!" / "Terlalu kecil!"
 4. Hitung dan tampilkan jumlah percobaan saat berhasil
 5. Gunakan break untuk keluar saat tebakan benar
 6. Batas maksimal 10 percobaan, tampilkan "Game Over" jika gagal
 7. Buat fungsi rekursif tebak_rekursif sebagai alternatif

 Catatan: Tugas ini interaktif (menggunakan input()).
          Sertakan screenshot saat menjalankan program.
==========================================================
"""

import random


def generate_angka(batas_bawah=1, batas_atas=100):
    """Generate angka acak dalam rentang tertentu.

    Args:
        batas_bawah (int): Batas bawah (default 1).
        batas_atas (int): Batas atas (default 100).

    Returns:
        int: Angka acak.
    """
    return random.randint(batas_bawah, batas_atas)


def main_tebak_angka():
    """Permainan tebak angka dengan while loop.

    - Batas percobaan: 10 kali
    - Berikan petunjuk di setiap tebakan salah
    - Gunakan break saat tebakan benar
    """
    target = generate_angka()
    maks_percobaan = 10
    percobaan = 0

    print("=== PERMAINAN TEBAK ANGKA ===")
    print(f"Tebak angka antara 1 sampai 100 (maksimal {maks_percobaan} percobaan)")

    while percobaan < maks_percobaan:
        try:
            tebakan = int(input(f"Percobaan {percobaan + 1}: "))
        except ValueError:
            print("Masukkan angka bulat!")
            continue  # input tidak valid tidak dihitung sebagai percobaan
        percobaan += 1

        if tebakan == target:
            print(f"BENAR! Angkanya adalah {target}")
            print(f"Anda berhasil dalam {percobaan} percobaan!")
            break
        elif tebakan > target:
            print("Terlalu besar!")
        else:
            print("Terlalu kecil!")
    else:
        print(f"\nGame Over! Angka yang benar adalah {target}")


def tebak_rekursif(target, percobaan=1, maks=10):
    """Versi rekursif dari permainan tebak angka.

    Args:
        target (int): Angka yang harus ditebak.
        percobaan (int): Nomor percobaan saat ini.
        maks (int): Batas maksimal percobaan.
    """
    if percobaan > maks:
        print(f"\nGame Over! Angka yang benar adalah {target}")
        return

    try:
        tebakan = int(input(f"Percobaan {percobaan}: "))
    except ValueError:
        print("Masukkan angka bulat!")
        tebak_rekursif(target, percobaan, maks)  # input tidak valid tidak dihitung
        return

    if tebakan == target:
        print(f"BENAR! Angkanya adalah {target}")
        print(f"Anda berhasil dalam {percobaan} percobaan!")
        return

    print("Terlalu besar!" if tebakan > target else "Terlalu kecil!")
    tebak_rekursif(target, percobaan + 1, maks)


# ── Main Program ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== VERSI ITERATIF (while loop) ===")
    main_tebak_angka()

    print("\n=== VERSI REKURSIF ===")
    target = generate_angka()
    tebak_rekursif(target)
