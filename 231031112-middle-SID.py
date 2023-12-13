'''
Misalkan anda diberikan tugas untuk membuat program struk pembelian pada kasir di perusahaan alat-alat komputer. Pilih 5 barang Alat Komputer dengan harga masing-masing barang kemudian buatkan program dan ouputnya seperti berikut.

- Buat list data perusahaan
mdata = [PT. ABC DESIGN,
        JL. BALAIKOTA NO.1,
        Kota Parepare,
        Nama Lengkap,
        mahasiswa@ith.ac.id,
        Nama Kasir,
        25 Oktober 2023]
(NOTED: ubah Nama Lengkap, e-mail, Nama Kasir, Tanggal-Bulan-Tahun Lahir)

- Buat Nested list untuk 5 barang:

djual = [['D0001','D0002','D0003','D0004','D0005'],
        ['Barang1','Barang2','Barang3','Barang4','Barang5'],
        [15,5,75,3,10],
        [2,2,2,2,2]]
(NOTED: ubah nama barang dan harga barang sesuai keinginan)

- Hasil Runing
                                 PT. ABC DESIGN
                          JL. BALAIKOTA NO.1 KOTA PAREPARE
                             e-Mail: mahasiswa@ith.ac.id


MANAJER           : Nama Lengkap
KASIR             : Nama Kasir
Tanggal Pembelian : 25 Oktober 2023
|--     16    --|--       19      --|--     15    --|--  8 --|--    14    --| 
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  
No. Kode Barang |    Nama Barang    |   H. Satuan   | Jumlah |     Total    |
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
1   D0001       | Barang1           |      Rp15000,-|    2  |     Rp45000,-|
2   D0002       | Barang2           |       Rp5000,-|    2   |     Rp15000,-|
3   D0003       | Barang3           |      Rp50000,-|    2  |    Rp150000,-|
4   D0004       | Barang4           |       Rp3000,-|    2  |     Rp15000,-|
5   D0005       | Barang5           |      Rp10000,-|    2   |     Rp30000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
                                    SUBTOTAL:           15   |    Rp245000,-|
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
Summary:
Harga tertinggi adalah    : Rp50000,-  (D0003 - Barang3)
Harga terendah  adalah    : Rp3000,-   (D0004 - Barang4)
Harga rata-rata pembelian : Rp ,-
                                                   Parepare, 25 Oktober 2023
                                          



                                                         NAMA LENGKAP      
                                                         ------------
                                                            MANAJER

'''


# Write your code in below!

print('''
Nama\t\t: Annisa Arthanty
NIM\t\t: 231031112
Nomor Komputer\t: 17
Kelas\t\t: Sistem Informasi D''')

#Answer in below
mdata = ['PT. ABC DESIGN',
        'JL. BALAIKOTA NO.1 PAREPARE',
        'Annisa Arthanty',
        'annisaarthanty21@gmail.com',
        'Heyzel',
        '16 Januari 2003']
print()
ps = 120
PT = (mdata[0])
Alamat = (mdata[1])
email = (mdata[3])

print(PT.center(ps))
print(Alamat.center(ps))
print(email.center(ps))

djual = [['D0001','D0002','D0003','D0004','D0005'],
        ['pulpen','pensil','penggaris','penghapus','peraut'],
        [3000,5000,7000,4000,8000],
        [2,2,2,2,2]]

print('\n')
print(f'''MANAGER           : {mdata[2]}
KASIR             : {mdata[4]}
Tanggal Pembelian : {mdata[-1]}''')

print('-' * (77))
print('No. Kode Barang'.ljust(16) + '|' + 'Nama Barang'.center(19) + '|' + 'H. Satuan'.center(15) + '|' + 'Jumlah'.center(8) + '|'+'Total'.center(14)+'|')
print('-' * (77))

# Membuat loop untuk mencetak data barang
subtotal = 0  # Menyimpan total harga
for i in range(len(djual[0])):
    nama_barang = djual[0][i]
    kode_barang = djual[1][i]
    harga_satuan = djual[2][i]
    jumlah = djual[3][i]
    total = harga_satuan*3
    subtotal += total  # Menambahkan total harga barang ke subtotal
    print(f'{i + 1}.  {kode_barang}'.ljust(16) + '|' + f' {nama_barang}'.ljust(19) + '|' +
          f'Rp{harga_satuan},-'.rjust(15) + '|' + f'{jumlah}'.center(8) + '|' +
        f'Rp{total},-'.center(14) + '|')

# Menambahkan subtotal ke akhir
print('-' * (77))
print(f'SUBTOTAL:'.ljust(63) + f'Rp{subtotal},-'.center(14) + '|')
print('-' * (77))

print('Summary:')
# Menghitung harga tertinggi dan terendah
harga_tertinggi = max(djual[2])
harga_terendah = min(djual[2])

# Mencari indeks item dengan harga tertinggi dan terendah
indeks_tertinggi = djual[2].index(harga_tertinggi)
indeks_terendah = djual[2].index(harga_terendah)

# Menampilkan harga tertinggi dan terendah beserta barangnya
print(f'Harga tertinggi adalah    : Rp{harga_tertinggi},- ({djual[1][indeks_tertinggi]} - {djual[0][indeks_tertinggi]})')
print(f'Harga terendah  adalah    : Rp{harga_terendah},- ({djual[1][indeks_terendah]} - {djual[0][indeks_terendah]})')

# Menambahkan informasi tambahan
total_pembelian = sum(djual[2])
rata_rata_pembelian = total_pembelian / len(djual[2])
print(f"Harga rata-rata pembelian : Rp{rata_rata_pembelian},-\n")
print('Parepare, 16 januari 2003'.rjust(79))
print('\n')
print('Annisa Arthanty'.rjust(77))
print('--------------------'.rjust(79))
print('MANAGER'.rjust(72))