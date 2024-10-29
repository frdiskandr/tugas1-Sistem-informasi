# Muhammad Faried Iskandar (054474913)
# Sistem Informasi

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

# Mengonversi data ke DataFrame
df_penjualan = pd.DataFrame(data_penjualan)
df_penjualan["Total Penjualan"] = df_penjualan["Hitam"] + df_penjualan["Putih"] + df_penjualan["Biru"]

# Plot Grafik Penjualan Bulanan per Warna
plt.figure(figsize=(12, 6))
plt.plot(df_penjualan["Bulan"], df_penjualan["Hitam"], marker='o', color='black', label='Hitam')
plt.plot(df_penjualan["Bulan"], df_penjualan["Putih"], marker='o', color='gray', label='Putih')
plt.plot(df_penjualan["Bulan"], df_penjualan["Biru"], marker='o', color='blue', label='Biru')

# Tambahkan label dan judul
plt.title("Grafik Penjualan Bulanan Sepatu Niki per Warna")
plt.xlabel("Bulan")
plt.ylabel("Jumlah Penjualan")
plt.legend()
plt.xticks(rotation=45)
plt.grid(True)

# Tampilkan grafik
plt.tight_layout()
plt.show()

# Grafik Stok Akhir
stok_akhir = {
    'Hitam': 21500 - df_penjualan["Hitam"].sum(),
    'Putih': 15000 - df_penjualan["Putih"].sum(),
    'Biru': 13500 - df_penjualan["Biru"].sum()
}

# Data untuk Pie Chart Stok Akhir
labels = stok_akhir.keys()
sizes = stok_akhir.values()
colors = ['black', 'gray', 'blue']

# Plot Pie Chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Persentase Stok Akhir Sepatu Niki per Warna")

# Tampilkan grafik
plt.show()
