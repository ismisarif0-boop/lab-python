"""
==========================================================
 TUGAS 2 - Kalkulator Konversi Suhu
 Chapter 1: Dasar Python
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Definisikan variabel celsius dengan nilai tertentu
 2. Hitung konversi ke Fahrenheit: F = (C x 9/5) + 32
 3. Hitung konversi ke Reamur:     R = C x 4/5
 4. Hitung konversi ke Kelvin:     K = C + 273.15
 5. Tampilkan semua hasil konversi dengan 2 angka desimal
 6. Uji dengan minimal 3 nilai celsius berbeda
==========================================================
"""

# ── Rumus Konversi ────────────────────────────────────────────────────────────
# Fahrenheit = (Celsius * 9/5) + 32
# Reamur     = Celsius * 4/5
# Kelvin     = Celsius + 273.15


def konversi_suhu(celsius):
    """Konversi suhu dari Celsius ke Fahrenheit, Reamur, dan Kelvin.

    Args:
        celsius (float): Suhu dalam Celsius.

    Returns:
        tuple: (fahrenheit, reamur, kelvin)
    """
    fahrenheit = (celsius * 9 / 5) + 32
    reamur = celsius * 4 / 5
    kelvin = celsius + 273.15
    return fahrenheit, reamur, kelvin


# ── Tampilkan Hasil Konversi ─────────────────────────────────────────────────
nilai_celsius = [0, 100, 37.5, -10]
for c in nilai_celsius:
    f, r, k = konversi_suhu(c)
    print(f"{c:.2f}°C = {f:.2f}°F = {r:.2f}°R = {k:.2f}K")
