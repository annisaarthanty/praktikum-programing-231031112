from datetime import datetime, timedelta

# Fungsi untuk menambahkan waktu
def tambah_waktu(waktu1, waktu2):
    total_detik = waktu1 + waktu2
    jam = total_detik // 3600
    sisa_detik = total_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return jam, menit, detik

# Input waktu pertama
jam1 = int(input("Masukkan jam pertama: "))
menit1 = int(input("Masukkan menit pertama: "))
detik1 = int(input("Masukkan detik pertama: "))
# Input waktu kedua
jam2 = int(input("Masukkan jam kedua: "))
menit2 = int(input("Masukkan menit kedua: "))
detik2 = int(input("Masukkan detik kedua: "))

# Hitung total waktu
total_jam, total_menit, total_detik = tambah_waktu((jam1 * 3600 + menit1 * 60 + detik1),
                                                   (jam2 * 3600 + menit2 * 60 + detik2))

# Tampilkan hasil penjumlahan waktu
print(f"Total waktu: {total_jam} jam, {total_menit} menit, {total_detik} detik")

# Fungsi untuk menghitung selisih waktu
def selisih_waktu(waktu1, waktu2):
    selisih_detik = abs(waktu1 - waktu2)
    jam = selisih_detik // 3600
    sisa_detik = selisih_detik % 3600
    menit = sisa_detik // 60
    detik = sisa_detik % 60
    return jam, menit, detik

# Input waktu pertama
jam1 = int(input("Masukkan jam pertama: "))
menit1 = int(input("Masukkan menit pertama: "))
detik1 = int(input("Masukkan detik pertama: "))

# Input waktu kedua
jam2 = int(input("Masukkan jam kedua: "))
menit2 = int(input("Masukkan menit kedua: "))
detik2 = int(input("Masukkan detik kedua: "))

# Hitung selisih waktu
selisih_jam, selisih_menit, selisih_detik = selisih_waktu((jam1 * 3600 + menit1 * 60 + detik1),
                                                         (jam2 * 3600 + menit2 * 60 + detik2))

# Tampilkan hasil selisih waktu
print(f"Selisih waktu: {selisih_jam} jam, {selisih_menit} menit, {selisih_detik} detik")
