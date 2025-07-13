# Sistem Pakar Diagnosa Gangguan Mental Remaja dengan Certainty Factor

# Daftar gejala dan bobot dari pakar
gejala = {
    "G01": ("Tidak bisa menikmati aktivitas", 0.5),
    "G02": ("Putus asa dan hilang harapan", 0.5),
    "G03": ("Tidak antusias", 0.4),
    "G04": ("Merasa tidak berharga", 0.6),
    "G05": ("Tidak ada harapan masa depan", 0.7),
    "G06": ("Hidup tidak berarti", 1.0),
    "G07": ("Sulit inisiatif", 0.33),
    "G08": ("Tidak lihat sisi positif", 0.5),
    "G09": ("Tidak kuat beraktivitas", 0.7),
    "G10": ("Tidak ada hal yang diharapkan", 0.9),
    "G11": ("Sedih dan tertekan", 0.33),
    "G12": ("Kehilangan minat", 0.6),
    "G13": ("Merasa tidak layak", 0.6),
    "G14": ("Hidup tidak bermanfaat", 0.8)
}

cf_list = []
print("=== SISTEM PAKAR DIAGNOSA DEPRESI REMAJA ===")
print("Masukkan nilai gejala berikut (0=Tidak Pernah, 1=Kadang, 2=Sering, 3=Selalu):")

# Input gejala dan hitung CF tiap gejala
for kode, (desc, bobot) in gejala.items():
    while True:
        try:
            nilai = int(input(f"{kode} - {desc}: "))
            if nilai < 0 or nilai > 3:
                raise ValueError
            break
        except ValueError:
            print("Masukkan angka antara 0 - 3")

    cf_user = nilai / 3
    cf = cf_user * bobot
    cf_list.append(cf)

# Proses penggabungan CF
cf_total = cf_list[0]
for i in range(1, len(cf_list)):
    cf_total = cf_total + cf_list[i] * (1 - cf_total)

# Menentukan hasil diagnosa
if cf_total >= 0.7:
    hasil = "Depresi Berat"
elif cf_total >= 0.5:
    hasil = "Depresi Sedang"
elif cf_total >= 0.3:
    hasil = "Depresi Ringan"
else:
    hasil = "Normal"

# Tampilkan hasil
print("\n=== HASIL DIAGNOSA ===")
print(f"Tingkat Depresi: {hasil}")
print(f"Nilai CF Total: {cf_total:.2f}")