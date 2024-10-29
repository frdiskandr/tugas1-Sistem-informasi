import pandas as pd
import matplotlib.pyplot as plt

# Data penjualan bulanan
data_penjualan = {
    "Bulan": [
        "Januari", "Februari", "Maret", "April", "Mei", "Juni",
        "Juli", "Agustus", "September", "Oktober", "November", "Desember"
    ],
    "Hitam": [900, 975, 1150, 1325, 1500, 1675, 1850, 2025, 2200, 2375, 2550, 2725],
    "Putih": [1500, 1100, 1200, 1300, 1400, 1450, 1350, 1200, 1050, 900, 750, 600],
    "Biru": [1000, 750, 725, 710, 700, 775, 720, 710, 760, 740, 730, 705]
}

# Mengonversi data penjualan bulanan ke DataFrame
df_penjualan = pd.DataFrame(data_penjualan)
df_penjualan["Total Penjualan"] = df_penjualan["Hitam"] + df_penjualan["Putih"] + df_penjualan["Biru"]

# Total penjualan tahunan per warna
total_penjualan_hitam = df_penjualan["Hitam"].sum()
total_penjualan_putih = df_penjualan["Putih"].sum()
total_penjualan_biru = df_penjualan["Biru"].sum()

# Total penjualan keseluruhan
total_penjualan_keseluruhan = total_penjualan_hitam + total_penjualan_putih + total_penjualan_biru

# Menampilkan laporan penjualan tahunan
print("Laporan Penjualan Tahunan Sepatu Niki")
print("=====================================")
print(f"Total Penjualan Hitam: {total_penjualan_hitam} pasang")
print(f"Total Penjualan Putih: {total_penjualan_putih} pasang")
print(f"Total Penjualan Biru: {total_penjualan_biru} pasang")
print(f"Total Penjualan Keseluruhan: {total_penjualan_keseluruhan} pasang")

# Visualisasi dalam bentuk Grafik Batang
warna = ['Hitam', 'Putih', 'Biru']
penjualan = [total_penjualan_hitam, total_penjualan_putih, total_penjualan_biru]

plt.figure(figsize=(10, 6))
plt.bar(warna, penjualan, color=['black', 'gray', 'blue'])
plt.title("Grafik Penjualan Tahunan Sepatu Niki per Warna")
plt.xlabel("Warna")
plt.ylabel("Total Penjualan (Pasang)")
plt.show()
