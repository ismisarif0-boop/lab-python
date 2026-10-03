"""
==========================================================
 TUGAS 3 - Handling Missing Data
 Chapter 5: NumPy & Pandas
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 1. Buat DataFrame dengan data yang sengaja memiliki NaN
    (minimal 3 kolom, 10-15 baris)
 2. Deteksi missing values: isnull().sum() per kolom
 3. Hitung persentase missing per kolom
 4. Buat 3 versi penanganan:
    - Versi 1: dropna() — hapus baris yang memiliki NaN
    - Versi 2: fillna() — isi numerik dengan mean,
               kategorikal dengan mode
    - Versi 3: fillna(method="ffill") — forward fill
 5. Bandingkan jumlah baris ketiga versi
 6. Berikan komentar kapan metode mana yang tepat digunakan

 Catatan:
 - Gunakan np.nan untuk membuat missing values
 - Buat data yang realistis (misal: data survei/kuesioner)
==========================================================
"""

import pandas as pd
import numpy as np


def buat_data_dengan_missing():
    """Membuat DataFrame dengan data yang memiliki missing values.

    Buat data realistis (misal: survei mahasiswa) dengan 10-15 baris
    dan minimal 3 kolom. Sisipkan np.nan di beberapa posisi.

    Returns:
        pd.DataFrame: DataFrame dengan missing values.
    """
    data = {
        "Nama": ["Ahmad", "Budi", "Citra", "Dewi", "Eko",
                 "Fitri", "Gilang", "Hana", "Irfan", "Jasmine",
                 "Kamal", "Lina"],
        "Usia": [20, 21, np.nan, 22, 20, np.nan, 23, 21, 20, np.nan, 22, 21],
        "IPK": [3.5, np.nan, 3.2, 3.8, np.nan, 3.1, 3.6, np.nan, 3.4, 3.7, np.nan, 3.3],
        "Jurusan": ["Informatika", "SI", np.nan, "Informatika", "Elektro",
                    "SI", np.nan, "Informatika", "Elektro", np.nan,
                    "SI", "Informatika"],
        "Skor_Survei": [85, 90, 78, np.nan, 88, 92, np.nan, 75, np.nan, 80, 95, np.nan],
    }

    return pd.DataFrame(data)


def deteksi_missing(df):
    """Mendeteksi dan menampilkan informasi missing values.

    Args:
        df (pd.DataFrame): DataFrame yang mungkin memiliki NaN.

    Returns:
        tuple: (jumlah_missing_per_kolom, persen_missing_per_kolom)
    """
    jumlah = df.isnull().sum()
    persen = (df.isnull().sum() / len(df)) * 100
    return jumlah, persen


def versi_dropna(df):
    """Versi 1: Menghapus baris yang mengandung NaN.

    Args:
        df (pd.DataFrame): DataFrame asli.

    Returns:
        pd.DataFrame: DataFrame tanpa baris yang memiliki NaN.
    """
    return df.dropna()


def versi_fillna_statistik(df):
    """Versi 2: Mengisi NaN — numerik dengan mean, kategorikal dengan mode.

    Args:
        df (pd.DataFrame): DataFrame asli.

    Returns:
        pd.DataFrame: DataFrame dengan NaN terisi.
    """
    df_filled = df.copy()

    for col in df_filled.select_dtypes(include=["number"]).columns:
        df_filled[col] = df_filled[col].fillna(df_filled[col].mean())

    # exclude=number (bukan include=object) karena pandas 3 memakai dtype str
    for col in df_filled.select_dtypes(exclude=["number"]).columns:
        df_filled[col] = df_filled[col].fillna(df_filled[col].mode()[0])

    return df_filled


def versi_fillna_ffill(df):
    """Versi 3: Mengisi NaN dengan forward fill (nilai sebelumnya).

    Args:
        df (pd.DataFrame): DataFrame asli.

    Returns:
        pd.DataFrame: DataFrame dengan NaN terisi (ffill).
    """
    # ffill() setara fillna(method="ffill"); argumen method dihapus di pandas 3
    return df.ffill()


def bandingkan_hasil(df_asli, df_dropna, df_fillna_stat, df_fillna_ffill):
    """Membandingkan jumlah baris dan sisa NaN dari ketiga versi.

    Args:
        df_asli (pd.DataFrame): DataFrame asli.
        df_dropna (pd.DataFrame): Hasil dropna.
        df_fillna_stat (pd.DataFrame): Hasil fillna statistik.
        df_fillna_ffill (pd.DataFrame): Hasil fillna ffill.
    """
    print(f"{'Metode':<25} | {'Baris':>5} | {'NaN Tersisa':>11}")
    print("-" * 48)
    print(f"{'Data Asli':<25} | {len(df_asli):>5} | {df_asli.isnull().sum().sum():>11}")
    print(f"{'dropna()':<25} | {len(df_dropna):>5} | {df_dropna.isnull().sum().sum():>11}")
    print(f"{'fillna (mean/mode)':<25} | {len(df_fillna_stat):>5} | "
          f"{df_fillna_stat.isnull().sum().sum():>11}")
    print(f"{'fillna (ffill)':<25} | {len(df_fillna_ffill):>5} | "
          f"{df_fillna_ffill.isnull().sum().sum():>11}")


# ── Kapan Menggunakan Metode Mana? ──────────────────────────────────────────
#
# dropna():
#   - Gunakan ketika: data yang hilang sedikit dan acak, sehingga sisa baris
#     masih cukup banyak untuk dianalisis.
#   - Risiko: kehilangan banyak data dan bisa menimbulkan bias bila
#     missing-nya tidak acak (di data ini hanya sebagian baris yang lengkap).
#   - Contoh kasus: dataset besar dengan < 5% baris yang tidak lengkap.
#
# fillna(mean/mode):
#   - Gunakan ketika: jumlah baris perlu dipertahankan dan data tidak
#     berurutan; mean untuk numerik, mode untuk kategorikal.
#   - Risiko: variansi mengecil dan hubungan antar kolom bisa terdistorsi;
#     mean sensitif terhadap outlier (pakai median bila ada outlier).
#   - Contoh kasus: kolom IPK atau skor survei yang sebagian kosong.
#
# fillna(ffill):
#   - Gunakan ketika: data berurutan (deret waktu) dan nilai cenderung tetap
#     dari satu baris ke baris berikutnya.
#   - Risiko: tidak masuk akal untuk data tak berurutan (nilai mahasiswa
#     lain ikut tersalin) dan NaN di baris pertama tidak terisi.
#   - Contoh kasus: suhu harian atau harga saham yang tidak tercatat di akhir pekan.


# ── Main Program ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    df = buat_data_dengan_missing()

    print("=" * 55)
    print(" HANDLING MISSING DATA")
    print("=" * 55)

    print("\n── Data Asli ──")
    print(df)

    print("\n── Deteksi Missing Values ──")
    jumlah, persen = deteksi_missing(df)
    print(f"Jumlah NaN per kolom:\n{jumlah}")
    print(f"\nPersentase NaN per kolom:\n{persen.round(1)}")

    print("\n── Versi 1: dropna() ──")
    df_v1 = versi_dropna(df)
    print(df_v1)

    print("\n── Versi 2: fillna (mean/mode) ──")
    df_v2 = versi_fillna_statistik(df)
    print(df_v2)

    print("\n── Versi 3: fillna (ffill) ──")
    df_v3 = versi_fillna_ffill(df)
    print(df_v3)

    print("\n── Perbandingan Hasil ──")
    bandingkan_hasil(df, df_v1, df_v2, df_v3)
