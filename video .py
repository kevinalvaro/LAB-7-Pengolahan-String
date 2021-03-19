#by Kevin Alvaro Adianto

file=input("Masukkan Nama File: ")
nim,nama=file.split("_")

tahun="20"

nama=nama.upper()
prodi=nim[0]+nim[1]
angkatan=nim[2]+nim[3]
nomor=nim[4]+nim[5]+nim[6]+nim[7]
angkatan=tahun+angkatan
print()
print("Prodi: ",end='')
if prodi == "01":
    print("Filsafat Keilahian")
elif prodi == "11":
    print("Mangement")
elif prodi == "12":
    print("Akuntansi")
elif prodi == "61":
    print("Arsitektur dan Desain")
elif prodi == "71":
    print("Informatika")
elif prodi == "72":
    print("Sistem Informasi")
elif prodi == "11":
    print("Desain Produk")
elif prodi == "11":
    print("Biologi")
elif prodi == "11":
    print("Kedokteran")
else:
    print("maaf prodi tidak terdafatar dalam sistem")

print("Angkatan :",angkatan)
print("Nomor    :",nomor)
print("Nama     :",nama)