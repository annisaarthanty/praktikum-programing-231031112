
print('\n')
biodata = { 'nama'  : 'Annisa Arthanty',
'nim'   : '231031112',
'kelas' : 'S123D',
'tempat,tanggal lahir' : 'surabaya,16 januari 2003',
'jenis kelamin' : 'perempuan',
'agama' : 'islam',
'alamat': 'jalan haji andi abu bakar',
'email' : 'annisaarthanty21@gmail.com'
}

print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:3])
print(selected_biodata)





