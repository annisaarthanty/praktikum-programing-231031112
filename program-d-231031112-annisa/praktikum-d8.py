pwd_benar = 'si23d'
pwd_benar2 = 'SI23D'
pwd_benar3 = 's123d'
a = True
limit = 3
i = 0

while a:
    i += 1
    pwd = input('Masukkan Password= ')
    if pwd == pwd_benar:
        print('Password Benar, Selamat Datang di halaman 1')
        a = True
        pwd2 = input('Masukkan Password 2= ')
        if pwd2 == pwd_benar2:
            print('Password Benar, Selamat Datang di halaman 2')
            a = True       
            pwd3 = input('Masukkan Password 3= ')
            if pwd3 == pwd_benar3:
                print('Password Benar, Selamat Anda Berhasil Login')
                a = True
            else :
                print('Password salah, anda gagal pada halaman 3')
                a = True
    else:
        if i == limit:
            print('Kesempatan Anda Habis!')
            a = False
        else:
            print(f'Kesempatan anda tersisa {limit-i} kali')
            a = True
           

            
            

# Tugas: Buat Password Berlapis 3
# jika Salah pertama: Password salah, anda gagal pada halaman 1
# jika Salah ke-2: Password salah, anda gagal pada halaman 2
# jika Salah ke-3: Password salah, anda gagal pada halaman 3

# jika Benar Pertama: Password Benar, Selamat Datang di halaman 1
# jika Benar ke-2: Password Benar, Selamat Datang di halaman 2
# jika Benar ke-3: Password Benar, Selamat Anda Berhasil Login

# Tiap halaman, memiliki kesempatan 3 kali masukkan password

