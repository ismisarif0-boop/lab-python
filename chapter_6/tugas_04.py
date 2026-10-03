"""
==========================================================
 TUGAS 4 - Proyek Mini: End-to-End ML Pipeline
 Chapter 6: Machine Learning & AI
 Laboratorium Python & Dasar AI
 Universitas Muhammadiyah Makassar
==========================================================

 Instruksi:
 Pilih SALAH SATU dari dua opsi proyek di bawah ini.
 Implementasikan pipeline ML lengkap dari awal hingga akhir.

 === OPSI A: Klasifikasi Kelayakan Beasiswa ===
 - Dataset: 200 mahasiswa
 - Fitur: IPK (2.0-4.0), penghasilan_ortu (1-20 juta),
   semester (1-8), tanggungan_ortu (1-6), prestasi (0-10)
 - Target: Layak / Tidak Layak (binary classification)
 - Pipeline: preprocessing -> 2+ model -> evaluasi -> prediksi

 === OPSI B: Regresi Prediksi Biaya Kos ===
 - Dataset: 200 data kos
 - Fitur: kota (encoded), tipe_kos (1-3), jarak_kampus (0.5-15 km),
   fasilitas (1-10), luas_kamar (9-30 m²)
 - Target: biaya_kos (500rb - 5juta / bulan)
 - Pipeline: preprocessing -> 2+ model -> evaluasi -> prediksi

 Kedua opsi harus mencakup:
 1. Buat dataset sintetis (200 sampel)
 2. Preprocessing (scaling, encoding jika perlu)
 3. Train/test split 80:20
 4. Train minimal 2 model berbeda
 5. Evaluasi dan perbandingan model
 6. Prediksi untuk data baru
 7. Kesimpulan dan rekomendasi
==========================================================
"""

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

# Opsi B (regresi) tidak dikerjakan; instruksi: pilih SALAH SATU opsi.
# Import untuk Opsi B bila dikerjakan:
# from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
# from sklearn.linear_model import LinearRegression
# from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor


# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                    OPSI A: KLASIFIKASI KELAYAKAN BEASISWA                ║
# ╚════════════════════════════════════════════════════════════════════════════╝


# ============================================
# A1. Buat Dataset Beasiswa
# ============================================
def buat_dataset_beasiswa(n_samples=200, random_state=42):
    """Buat dataset sintetis klasifikasi kelayakan beasiswa.

    Fitur:
    - ipk: 2.0 - 4.0
    - penghasilan_ortu: 1_000_000 - 20_000_000 (Rp/bulan)
    - semester: 1 - 8
    - tanggungan_ortu: 1 - 6 orang
    - prestasi: 0 - 10 (skor prestasi non-akademik)

    Target: 1 = Layak, 0 = Tidak Layak

    Args:
        n_samples (int): Jumlah sampel.
        random_state (int): Random seed.

    Returns:
        tuple: (X, y, feature_names)
    """
    np.random.seed(random_state)

    ipk = np.random.uniform(2.0, 4.0, n_samples)
    penghasilan = np.random.uniform(1_000_000, 20_000_000, n_samples)
    semester = np.random.randint(1, 9, n_samples).astype(float)
    tanggungan = np.random.randint(1, 7, n_samples).astype(float)
    prestasi = np.random.uniform(0, 10, n_samples)

    # Skor kelayakan = fungsi dari semua fitur (aturan beasiswa + noise)
    skor = (
        (ipk - 2.0) / 2.0 * 30          # IPK tinggi -> skor tinggi (max 30)
        + (1 - penghasilan / 20_000_000) * 25  # Penghasilan rendah -> skor tinggi (max 25)
        + tanggungan / 6.0 * 15          # Tanggungan banyak -> skor tinggi (max 15)
        + prestasi / 10.0 * 20           # Prestasi tinggi -> skor tinggi (max 20)
        + np.random.normal(0, 5, n_samples)  # noise
    )
    target = (skor > 45).astype(int)  # Threshold: skor > 45 = Layak

    X = np.column_stack([ipk, penghasilan, semester, tanggungan, prestasi])
    feature_names = ["IPK", "Penghasilan Ortu (Rp)", "Semester",
                     "Tanggungan Ortu", "Skor Prestasi"]

    print(f"Jumlah sampel       : {n_samples}")
    print(f"Jumlah fitur        : {len(feature_names)}")
    print("Distribusi target   :")
    print(f"  Layak (1)         : {np.sum(target == 1)} ({np.sum(target == 1)/n_samples*100:.1f}%)")
    print(f"  Tidak Layak (0)   : {np.sum(target == 0)} ({np.sum(target == 0)/n_samples*100:.1f}%)")
    print("\nStatistik fitur:")
    for i, name in enumerate(feature_names):
        print(f"  {name:25s}: min={X[:, i].min():.2f}, max={X[:, i].max():.2f}")

    return X, target, feature_names


# ============================================
# A2. Preprocessing Beasiswa
# ============================================
def preprocessing_beasiswa(X, y):
    """Preprocessing untuk klasifikasi beasiswa.

    Args:
        X (ndarray): Feature matrix.
        y (ndarray): Target array.

    Returns:
        tuple: (X_train, X_test, y_train, y_test,
                X_train_scaled, X_test_scaled, scaler)
    """
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # Handling outlier: clip ke [Q1 - 1.5*IQR, Q3 + 1.5*IQR] dari data training
    q1, q3 = np.percentile(X_train, [25, 75], axis=0)
    iqr = q3 - q1
    batas_bawah, batas_atas = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    n_outlier = int(np.sum((X_train < batas_bawah) | (X_train > batas_atas)))
    X_train = np.clip(X_train, batas_bawah, batas_atas)
    X_test = np.clip(X_test, batas_bawah, batas_atas)
    print(f"Outlier (aturan IQR) pada data training: {n_outlier} nilai di-clip")

    # Scaler hanya di-fit pada data training agar tidak terjadi data leakage
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print(f"Training : {len(X_train)} sampel")
    print(f"Testing  : {len(X_test)} sampel")
    print(f"Train - Layak: {np.sum(y_train == 1)}, Tidak: {np.sum(y_train == 0)}")
    print(f"Test  - Layak: {np.sum(y_test == 1)}, Tidak: {np.sum(y_test == 0)}")

    return X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler


# ============================================
# A3. Train & Evaluasi Model Klasifikasi
# ============================================
def train_model_klasifikasi(X_train, X_test, y_train, y_test):
    """Train minimal 2 model klasifikasi dan evaluasi.

    Args:
        X_train (ndarray): Training features (scaled).
        X_test (ndarray): Testing features (scaled).
        y_train (ndarray): Training target.
        y_test (ndarray): Testing target.

    Returns:
        dict: {nama_model: (model, accuracy, y_pred)}
    """
    nama_kelas = ["Tidak Layak", "Layak"]

    print("--- Model 1: Random Forest ---")
    rf = RandomForestClassifier(n_estimators=100, random_state=42)
    rf.fit(X_train, y_train)
    y_pred_rf = rf.predict(X_test)
    acc_rf = accuracy_score(y_test, y_pred_rf)
    print(f"Accuracy: {acc_rf:.4f} ({acc_rf*100:.1f}%)")
    laporan_rf = classification_report(y_test, y_pred_rf, target_names=nama_kelas)
    print(f"Classification Report:\n{laporan_rf}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred_rf)}\n")

    print("--- Model 2: Logistic Regression ---")
    lr = LogisticRegression(random_state=42, max_iter=1000)
    lr.fit(X_train, y_train)
    y_pred_lr = lr.predict(X_test)
    acc_lr = accuracy_score(y_test, y_pred_lr)
    print(f"Accuracy: {acc_lr:.4f} ({acc_lr*100:.1f}%)")
    laporan_lr = classification_report(y_test, y_pred_lr, target_names=nama_kelas)
    print(f"Classification Report:\n{laporan_lr}")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred_lr)}\n")

    print("--- Model 3: KNN (k=5) ---")
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit(X_train, y_train)
    y_pred_knn = knn.predict(X_test)
    acc_knn = accuracy_score(y_test, y_pred_knn)
    print(f"Accuracy: {acc_knn:.4f} ({acc_knn*100:.1f}%)")
    print(f"Confusion Matrix:\n{confusion_matrix(y_test, y_pred_knn)}")

    return {
        "Random Forest": (rf, acc_rf, y_pred_rf),
        "Logistic Regression": (lr, acc_lr, y_pred_lr),
        "KNN (k=5)": (knn, acc_knn, y_pred_knn),
    }


# ============================================
# A4. Perbandingan & Prediksi (Klasifikasi)
# ============================================
def perbandingan_dan_prediksi_klasifikasi(hasil_models, scaler, feature_names):
    """Buat tabel perbandingan dan prediksi data baru.

    Args:
        hasil_models (dict): Hasil dari train_model_klasifikasi().
        scaler: StandardScaler.
        feature_names (list): Nama fitur.
    """
    print("--- Perbandingan Model ---")
    print(f"{'No':>2} | {'Model':<25} | {'Accuracy':>10} | Visualisasi")
    print("-" * 60)
    sorted_models = sorted(hasil_models.items(), key=lambda x: x[1][1], reverse=True)
    for i, (name, (model, acc, _)) in enumerate(sorted_models, 1):
        bar = "#" * int(acc * 30)
        marker = " <- TERBAIK" if i == 1 else ""
        print(f"{i:>2} | {name:<25} | {acc:>9.1%} | {bar}{marker}")

    best_name, (best_model, best_acc, _) = sorted_models[0]
    print(f"\nModel terbaik: {best_name} ({best_acc:.1%})")

    print("\n--- Prediksi Kelayakan Beasiswa ---")
    mahasiswa_baru = np.array([
        [3.8, 3_000_000, 5, 4, 8],    # IPK tinggi, penghasilan rendah
        [2.5, 15_000_000, 3, 1, 2],   # IPK rendah, penghasilan tinggi
        [3.2, 8_000_000, 6, 3, 6],    # Menengah
        [3.9, 2_000_000, 4, 5, 9],    # Sangat layak
        [2.1, 18_000_000, 2, 1, 1],   # Sangat tidak layak
    ])

    mhs_scaled = scaler.transform(mahasiswa_baru)
    prediksi = best_model.predict(mhs_scaled)

    label_map = {0: "Tidak Layak", 1: "Layak"}
    print(f"{'No':>2} | {'IPK':>4} | {'Penghasilan':>14} | {'Smt':>3} | "
          f"{'Tgg':>3} | {'Pres':>4} | {'Hasil':<12}")
    print("-" * 65)
    for i, (mhs, pred) in enumerate(zip(mahasiswa_baru, prediksi), 1):
        print(f"{i:>2} | {mhs[0]:>4.1f} | Rp{mhs[1]:>11,.0f} | {mhs[2]:>3.0f} | "
              f"{mhs[3]:>3.0f} | {mhs[4]:>4.1f} | {label_map[pred]:<12}")

    if hasattr(best_model, "predict_proba"):
        probas = best_model.predict_proba(mhs_scaled)
        print("\nProbabilitas:")
        for i, (pred, prob) in enumerate(zip(prediksi, probas), 1):
            print(f"  Mahasiswa {i}: Tidak Layak={prob[0]:.1%}, Layak={prob[1]:.1%}")


# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                    OPSI B: REGRESI PREDIKSI BIAYA KOS                    ║
# ╚════════════════════════════════════════════════════════════════════════════╝


# ============================================
# B1. Buat Dataset Biaya Kos
# ============================================
def buat_dataset_kos(n_samples=200, random_state=42):
    """Buat dataset sintetis prediksi biaya kos.

    Fitur:
    - kota: 0=kota kecil, 1=kota sedang, 2=kota besar (encoded)
    - tipe_kos: 1=kos biasa, 2=kos AC, 3=kos eksklusif
    - jarak_kampus: 0.5 - 15.0 km
    - fasilitas: 1 - 10 (skor kelengkapan fasilitas)
    - luas_kamar: 9 - 30 m²

    Target: biaya_kos (500_000 - 5_000_000 Rp/bulan)

    Args:
        n_samples (int): Jumlah sampel.
        random_state (int): Random seed.

    Returns:
        tuple: (X, y, feature_names)
    """
    # TODO: Set random seed
    # np.random.seed(random_state)
    #
    # TODO: Generate fitur-fitur
    # kota = np.random.choice([0, 1, 2], n_samples, p=[0.3, 0.4, 0.3])
    # tipe_kos = np.random.choice([1, 2, 3], n_samples, p=[0.4, 0.35, 0.25])
    # jarak_kampus = np.random.uniform(0.5, 15.0, n_samples)
    # fasilitas = np.random.uniform(1, 10, n_samples)
    # luas_kamar = np.random.uniform(9, 30, n_samples)
    #
    # TODO: Buat target (biaya kos) berdasarkan fitur
    # biaya_kos = (
    #     500_000                            # Biaya dasar
    #     + kota * 400_000                   # Kota besar lebih mahal
    #     + tipe_kos * 350_000               # Tipe eksklusif lebih mahal
    #     - jarak_kampus * 30_000            # Jauh dari kampus lebih murah
    #     + fasilitas * 80_000               # Fasilitas lebih lengkap lebih mahal
    #     + luas_kamar * 25_000              # Kamar lebih luas lebih mahal
    #     + np.random.normal(0, 100_000, n_samples)  # noise
    # )
    # biaya_kos = np.clip(biaya_kos, 500_000, 5_000_000)
    #
    # TODO: Buat feature matrix
    # X = np.column_stack([kota.astype(float), tipe_kos.astype(float),
    #                      jarak_kampus, fasilitas, luas_kamar])
    # feature_names = ["Kota (0/1/2)", "Tipe Kos (1/2/3)",
    #                  "Jarak Kampus (km)", "Skor Fasilitas", "Luas Kamar (m²)"]
    #
    # TODO: Tampilkan info dataset
    # print(f"Jumlah sampel : {n_samples}")
    # print(f"Jumlah fitur  : {len(feature_names)}")
    # print(f"\nDistribusi kota   : kecil={np.sum(kota==0)}, sedang={np.sum(kota==1)}, besar={np.sum(kota==2)}")
    # print(f"Distribusi tipe   : biasa={np.sum(tipe_kos==1)}, AC={np.sum(tipe_kos==2)}, eksklusif={np.sum(tipe_kos==3)}")
    # print(f"Range biaya kos   : Rp{biaya_kos.min():,.0f} - Rp{biaya_kos.max():,.0f}")
    # print(f"Rata-rata biaya   : Rp{biaya_kos.mean():,.0f}")
    #
    # return X, biaya_kos, feature_names
    ...


# ============================================
# B2. Preprocessing Biaya Kos
# ============================================
def preprocessing_kos(X, y):
    """Preprocessing untuk regresi biaya kos.

    Args:
        X (ndarray): Feature matrix.
        y (ndarray): Target array (biaya kos).

    Returns:
        tuple: (X_train, X_test, y_train, y_test,
                X_train_scaled, X_test_scaled, scaler)
    """
    # TODO: Train/test split 80:20, random_state=42
    # X_train, X_test, y_train, y_test = train_test_split(
    #     X, y, test_size=0.2, random_state=42
    # )
    #
    # TODO: Scaling
    # scaler = StandardScaler()
    # X_train_scaled = scaler.fit_transform(X_train)
    # X_test_scaled = scaler.transform(X_test)
    #
    # TODO: Tampilkan info
    # print(f"Training : {len(X_train)} sampel")
    # print(f"Testing  : {len(X_test)} sampel")
    # print(f"Rata-rata biaya train: Rp{y_train.mean():,.0f}")
    # print(f"Rata-rata biaya test : Rp{y_test.mean():,.0f}")
    #
    # return X_train, X_test, y_train, y_test, X_train_scaled, X_test_scaled, scaler
    ...


# ============================================
# B3. Train & Evaluasi Model Regresi
# ============================================
def train_model_regresi(X_train, X_test, y_train, y_test, feature_names):
    """Train minimal 2 model regresi dan evaluasi.

    Args:
        X_train (ndarray): Training features (scaled).
        X_test (ndarray): Testing features (scaled).
        y_train (ndarray): Training target.
        y_test (ndarray): Testing target.
        feature_names (list): Nama fitur.

    Returns:
        dict: {nama_model: (model, r2, rmse, y_pred)}
    """
    # TODO: Train Model 1 - Linear Regression
    # print("--- Model 1: Linear Regression ---")
    # lr = LinearRegression()
    # lr.fit(X_train, y_train)
    # y_pred_lr = lr.predict(X_test)
    # r2_lr = r2_score(y_test, y_pred_lr)
    # rmse_lr = np.sqrt(mean_squared_error(y_test, y_pred_lr))
    # mae_lr = mean_absolute_error(y_test, y_pred_lr)
    # print(f"R²   : {r2_lr:.4f} ({r2_lr*100:.1f}%)")
    # print(f"RMSE : Rp{rmse_lr:,.0f}")
    # print(f"MAE  : Rp{mae_lr:,.0f}")
    #
    # print("\nKoefisien:")
    # for name, coef in zip(feature_names, lr.coef_):
    #     print(f"  {name:25s}: Rp{coef:+,.0f}")
    # print(f"  {'Intercept':25s}: Rp{lr.intercept_:,.0f}")
    #
    # TODO: Train Model 2 - Random Forest Regressor
    # print("\n--- Model 2: Random Forest Regressor ---")
    # rfr = RandomForestRegressor(n_estimators=100, random_state=42)
    # rfr.fit(X_train, y_train)
    # y_pred_rfr = rfr.predict(X_test)
    # r2_rfr = r2_score(y_test, y_pred_rfr)
    # rmse_rfr = np.sqrt(mean_squared_error(y_test, y_pred_rfr))
    # mae_rfr = mean_absolute_error(y_test, y_pred_rfr)
    # print(f"R²   : {r2_rfr:.4f} ({r2_rfr*100:.1f}%)")
    # print(f"RMSE : Rp{rmse_rfr:,.0f}")
    # print(f"MAE  : Rp{mae_rfr:,.0f}")
    #
    # print("\nFeature Importance:")
    # for name, imp in sorted(zip(feature_names, rfr.feature_importances_),
    #                          key=lambda x: x[1], reverse=True):
    #     bar = "#" * int(imp * 40)
    #     print(f"  {name:25s}: {imp:.4f} {bar}")
    #
    # TODO: (Opsional) Train Model 3 - Gradient Boosting
    # print("\n--- Model 3: Gradient Boosting Regressor ---")
    # gbr = GradientBoostingRegressor(n_estimators=100, random_state=42)
    # gbr.fit(X_train, y_train)
    # y_pred_gbr = gbr.predict(X_test)
    # r2_gbr = r2_score(y_test, y_pred_gbr)
    # rmse_gbr = np.sqrt(mean_squared_error(y_test, y_pred_gbr))
    # print(f"R²   : {r2_gbr:.4f} ({r2_gbr*100:.1f}%)")
    # print(f"RMSE : Rp{rmse_gbr:,.0f}")
    #
    # return {
    #     "Linear Regression": (lr, r2_lr, rmse_lr, y_pred_lr),
    #     "Random Forest": (rfr, r2_rfr, rmse_rfr, y_pred_rfr),
    #     "Gradient Boosting": (gbr, r2_gbr, rmse_gbr, y_pred_gbr),
    # }
    ...


# ============================================
# B4. Perbandingan & Prediksi (Regresi)
# ============================================
def perbandingan_dan_prediksi_regresi(hasil_models, scaler, feature_names):
    """Buat tabel perbandingan dan prediksi data baru.

    Args:
        hasil_models (dict): Hasil dari train_model_regresi().
        scaler: StandardScaler.
        feature_names (list): Nama fitur.
    """
    # TODO: Tabel perbandingan
    # print("--- Perbandingan Model ---")
    # print(f"{'No':>2} | {'Model':<25} | {'R²':>10} | {'RMSE':>15} | Visualisasi")
    # print("-" * 75)
    # sorted_models = sorted(hasil_models.items(), key=lambda x: x[1][1], reverse=True)
    # for i, (name, (model, r2, rmse, _)) in enumerate(sorted_models, 1):
    #     bar = "#" * int(r2 * 25)
    #     marker = " <- TERBAIK" if i == 1 else ""
    #     print(f"{i:>2} | {name:<25} | {r2:>9.4f} | Rp{rmse:>12,.0f} | {bar}{marker}")
    #
    # TODO: Prediksi dengan model terbaik
    # best_name, (best_model, best_r2, _, _) = sorted_models[0]
    # print(f"\nModel terbaik: {best_name} (R²={best_r2:.4f})")
    #
    # TODO: Prediksi kos baru
    # print("\n--- Prediksi Biaya Kos ---")
    # kos_baru = np.array([
    #     [2, 3, 1.0, 9, 25],   # Kota besar, eksklusif, dekat kampus
    #     [0, 1, 10.0, 3, 12],  # Kota kecil, biasa, jauh
    #     [1, 2, 3.0, 6, 18],   # Kota sedang, AC, cukup dekat
    #     [2, 2, 5.0, 7, 20],   # Kota besar, AC
    #     [0, 1, 8.0, 2, 9],    # Kota kecil, biasa, minimal
    # ])
    #
    # kota_map = {0: "Kecil", 1: "Sedang", 2: "Besar"}
    # tipe_map = {1: "Biasa", 2: "AC", 3: "Eksklusif"}
    #
    # kos_scaled = scaler.transform(kos_baru)
    # prediksi = best_model.predict(kos_scaled)
    #
    # print(f"{'No':>2} | {'Kota':<7} | {'Tipe':<10} | {'Jarak':>6} | {'Fas':>3} | {'Luas':>5} | {'Prediksi Biaya':>16}")
    # print("-" * 70)
    # for i, (kos, pred) in enumerate(zip(kos_baru, prediksi), 1):
    #     print(f"{i:>2} | {kota_map[int(kos[0])]:<7} | {tipe_map[int(kos[1])]:<10} | {kos[2]:>5.1f}km | {kos[3]:>3.0f} | {kos[4]:>4.0f}m² | Rp{pred:>14,.0f}")
    ...


# ╔════════════════════════════════════════════════════════════════════════════╗
# ║                           KESIMPULAN                                      ║
# ╚════════════════════════════════════════════════════════════════════════════╝


def kesimpulan():
    """Tulis kesimpulan proyek ML pipeline."""
    # Berdasarkan hasil run (random_state=42, 160 data latih, 40 data uji):
    #   KNN (k=5) 0.8750 | Logistic Regression 0.8500 | Random Forest 0.8250
    print("=" * 50)
    print("KESIMPULAN PROYEK ML PIPELINE")
    print("=" * 50)
    print("""
1. Proyek yang dikerjakan: Opsi A (klasifikasi kelayakan beasiswa).

2. Model terbaik: KNN (k=5), accuracy 87.5% pada 40 data uji.
   Alasan: accuracy tertinggi dan hanya 5 salah prediksi (2 Tidak Layak
   dikira Layak, 3 Layak dikira Tidak Layak). Perbedaan antar model hanya
   1-2 sampel (2.5%-5%), jadi ketiganya setara secara praktis. Logistic
   Regression (85.0%) layak dipilih bila butuh model yang mudah dijelaskan.
   Random Forest paling rendah accuracy-nya (82.5%) tetapi recall kelas Layak
   tertinggi (0.89): bila prioritas adalah tidak melewatkan calon penerima,
   Random Forest bisa menjadi pilihan.

3. Insight menarik:
   - Kelas cukup seimbang (46% Layak, 54% Tidak Layak), sehingga accuracy
     cukup representatif sebagai metrik.
   - Target dibuat dari IPK (30 poin), penghasilan ortu (25), prestasi (20)
     dan tanggungan (15); semester tidak berpengaruh pada aturan kelayakan.
   - Data baru dengan IPK tinggi dan penghasilan rendah diprediksi Layak
     (probabilitas 100%), sedangkan IPK rendah dengan penghasilan tinggi
     Tidak Layak. Profil menengah (mahasiswa 3) paling tidak pasti
     (Layak 60%), sehingga cocok ditinjau manual.
   - Tahap outlier (aturan IQR) tidak mengubah data (0 nilai) karena fitur
     simulasi berdistribusi seragam tanpa pencilan.

4. Limitasi model:
   - Dataset sintetis (bukan data real) dan ada noise acak pada target
   - Data uji hanya 40 sampel, hasil bisa berubah jika random_state berbeda
   - Belum ada cross-validation maupun hyperparameter tuning
   - KNN sensitif terhadap scaling dan lambat bila data sangat besar

5. Saran pengembangan:
   - Gunakan dataset real dan tambah fitur yang relevan
   - Coba cross-validation untuk estimasi performa yang lebih stabil
   - Coba hyperparameter tuning (GridSearch)
   - Tambahkan visualisasi (matplotlib)
""")


# ── Main Program ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Opsi A dipilih; Opsi B (regresi biaya kos) tidak dikerjakan.
    print("=" * 60)
    print("TUGAS 4 - OPSI A: KLASIFIKASI KELAYAKAN BEASISWA")
    print("=" * 60)

    print("\n=== 1. Membuat Dataset ===")
    X, y, feature_names = buat_dataset_beasiswa()

    print("\n=== 2. Preprocessing ===")
    X_train, X_test, y_train, y_test, X_train_s, X_test_s, scaler = preprocessing_beasiswa(X, y)

    print("\n=== 3. Training & Evaluasi Model ===")
    hasil = train_model_klasifikasi(X_train_s, X_test_s, y_train, y_test)

    print("\n=== 4. Perbandingan & Prediksi ===")
    perbandingan_dan_prediksi_klasifikasi(hasil, scaler, feature_names)

    print("\n=== 5. Kesimpulan ===")
    kesimpulan()
    # --- OPSI B: Regresi Prediksi Biaya Kos ---
    # print("=" * 60)
    # print("TUGAS 4 - OPSI B: REGRESI PREDIKSI BIAYA KOS")
    # print("=" * 60)
    #
    # # B1. Buat dataset
    # print("\n=== 1. Membuat Dataset ===")
    # X, y, feature_names = buat_dataset_kos()
    #
    # # B2. Preprocessing
    # print("\n=== 2. Preprocessing ===")
    # X_train, X_test, y_train, y_test, X_train_s, X_test_s, scaler = preprocessing_kos(X, y)
    #
    # # B3. Train model
    # print("\n=== 3. Training & Evaluasi Model ===")
    # hasil = train_model_regresi(X_train_s, X_test_s, y_train, y_test, feature_names)
    #
    # # B4. Perbandingan dan prediksi
    # print("\n=== 4. Perbandingan & Prediksi ===")
    # perbandingan_dan_prediksi_regresi(hasil, scaler, feature_names)
    #
    # # Kesimpulan
    # print("\n=== 5. Kesimpulan ===")
    # kesimpulan()

    pass
