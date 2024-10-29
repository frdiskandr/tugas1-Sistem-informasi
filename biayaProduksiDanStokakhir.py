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

# Konversi data ke DataFrame
df_penjualan = pd.DataFrame(data_penjualan)
df_penjualan["Total Penjualan"] = df_penjualan["Hitam"] + df_penjualan["Putih"] + df_penjualan["Biru"]

# Data produksi dan harga
total_produksi = 50000
produksi_hitam = 21500
produksi_putih = 15000
produksi_biru = 13500
harga_jual = 100000
biaya_total_produksi = 5000000000

# Biaya per pasang sepatu
biaya_per_pasang = biaya_total_produksi / total_produksi

# Total penjualan per warna
total_penjualan_hitam = df_penjualan["Hitam"].sum()
total_penjualan_putih = df_penjualan["Putih"].sum()
total_penjualan_biru = df_penjualan["Biru"].sum()

# Stok akhir per warna
stok_akhir = {
    'Hitam': produksi_hitam - total_penjualan_hitam,
    'Putih': produksi_putih - total_penjualan_putih,
    'Biru': produksi_biru - total_penjualan_biru
}

# Nilai Stok Akhir
nilai_stok_akhir = {
    warna: jumlah * biaya_per_pasang for warna, jumlah in stok_akhir.items()
}

# Total nilai stok akhir
total_nilai_stok_akhir = sum(nilai_stok_akhir.values())

# Laporan Persediaan dan Biaya dalam Grafik

# Grafik Batang untuk Stok Akhir per Warna
plt.figure(figsize=(10, 6))
plt.bar(stok_akhir.keys(), stok_akhir.values(), color=['black', 'gray', 'blue'])
plt.title("Grafik Stok Akhir Sepatu Niki per Warna")
plt.xlabel("Warna")
plt.ylabel("Jumlah Stok Akhir (Pasang)")
plt.show()

# Pie Chart untuk Biaya Produksi dan Nilai Stok Akhir
biaya_data = [biaya_total_produksi, total_nilai_stok_akhir]
labels = ['Biaya Produksi', 'Nilai Stok Akhir']
colors = ['skyblue', 'lightgreen']

plt.figure(figsize=(8, 8))
plt.pie(biaya_data, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title("Persentase Biaya Produksi dan Nilai Stok Akhir")
plt.show()
