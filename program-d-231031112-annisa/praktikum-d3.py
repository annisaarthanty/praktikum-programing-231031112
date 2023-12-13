nama  = 'ANNISA ARTHANTY'
nim   = '231031112'
prodi = 'Sistem Informasi D'
meet  = 'Praktikum 3'
email = 'annisaarthanty21@gmail.com'

sp = 40
# print(len(nama))
print('-'.center(sp,'-'))
print(nama.center(sp))
print(nim.center(sp))
print('\n'*2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp))
print('-'.center(sp,'-'))

paragraf = '''\t Halo, selamat datang perkenalkan nama saya {} dengan NIM {} dari prodi {}. Ini adalah file {}.'''

p = paragraf.format(nama,nim,prodi,meet)
print(p)

# ----------5++++++++++9----------
#1. Input nilai 
x = int(input('Masukkan Nilai --5++9--='))
#2. cek1 apakah x>5 true
cek1 = x>=5
#3. cek2 apakah x<9 true
cek2 = x<=9
#4. status = cek1 and cek2
status = cek1 and cek2
#5. cetak status
print('Hasilnya adalah',status)

# +++++++++5-----------9++++++++++++
#1. Input nilai 
x = int(input('Masukkan Nilai ++5--9++='))
#2. cek1 apakah x<=5 true
cek1 = x<=5
#3. cek2 apakah x=>9 false
cek2 = x>=9
#4. status = cek1 or cek2
status = cek1 or cek2
#5. cetak status
print('Hasilnya adalah',status)

#++++++5-------9+++++13------
#1. Input nilai 
x = int(input('Masukkan Nilai ++5--9++13--='))
#2. cek1 apakah x<5 true
cek1 = x<5
#3. cek2 apakah x>9 false
cek2 = x>9
#4. cek3 apakah x<13
cek3 = x<13
#5. status = cek1 or cek2 and cek3
status = cek1 or cek2 and cek3
#6. cetak status
print('Hasilnya adalah',status)

#-----5+++++9------13++++++16------
#1. Input nilai 
x = int(input('Masukkan Nilai --5++9--13++16--='))
#2. cek1 apakah x>5 
cek1 = x>5
#3. cek2 apakah x<9 
cek2 = x<9
#4. cek3 apakah x>13
cek3 = x>13
#5. cek4 apakah x<16
cek4 = x<16
#5. status = cek1 and cek2 or cek3 and cek4
status = cek1 and cek2 or cek3 and cek4
#6. cetak status
print('Hasilnya adalah',status)

#++++5-----9++++++13-----16++++++
#1. Input nilai 
x = int(input('Masukkan Nilai ++5--9++13--16++='))
#2. cek1 apakah x<5 
cek1 = x<5
#3. cek2 apakah x>9 
cek2 = x>9
#4. cek3 apakah x<13
cek3 = x<13
#5. cek4 apakah x>16
cek4 = x>16
#5. status = cek1 or cek2 and cek3 or cek4
status = cek1 or cek2 and cek3 or cek4
#6. cetak status
print('Hasilnya adalah',status)

#-----5+++++9-----13+++++16-----20+++++24----
#1. Input nilai 
x = int(input('Masukkan Nilai --5++9--13++16--20++24--='))
#2. cek1 apakah x>5 
cek1 = x>5
#3. cek2 apakah x<9 
cek2 = x<9
#4. cek3 apakah x>13
cek3 = x>13
#5. cek4 apakah x<16
cek4 = x<16
#6. cek5 apakah x>20
cek5 = x>20
#7. cek6 apakah x<24
cek6 = x<24
#8. status = cek1 and cek2 or cek3 and cek4 or cek5 and cek6
status = cek1 and cek2 or cek3 and cek4 or cek5 and cek6
#9. cetak status
print('Hasilnya adalah',status)

#+++++5-----9+++++13------16++++20-----24++++
#1. Input nilai 
x = int(input('Masukkan Nilai ++5--9++13--16++20--24++='))
#2. cek1 apakah x<5 
cek1 = x<5
#3. cek2 apakah x>9 
cek2 = x>9
#4. cek3 apakah x<13
cek3 = x<13
#5. cek4 apakah x>16
cek4 = x>16
#6. cek5 apakah x<20
cek5 = x<20
#7. cek6 apakah x>24
cek6 = x>24
#8. status = cek1 or cek2 and cek3 or cek4 and cek5 or cek6
status = cek1 or cek2 and cek3 or cek4 and cek5 or cek6
#9. cetak status
print('Hasilnya adalah',status)
