uas = float(input("Masukkan nilai uas: "))
absen = float(input("Masukkan nilai absen: "))
uts = float(input("Masukkan nilai uts: "))

batas_nilai = 60

jumlah = absen + uts + uas
rata = jumlah / 3

print("Jumlah nilai rata-rata anda:", rata)

print("======= Grade nilai mahasiswa *******")
print("")

if rata >= 95:
    print("Grade anda: A")
elif rata >= 80:
    print("Grade anda: B")
elif rata >= 75:
    print("Grade anda: C")
elif rata >= 55:
    print("Grade anda: D")
else:
    print("Grade anda: E")