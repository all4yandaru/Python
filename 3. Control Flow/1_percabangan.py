tinggi = int(input("Masukkan tinggi badan : "))
if tinggi < 160:
    print("anda pendek")
elif tinggi < 180:
    print("tinggi anda {}, anda tinggi".format(tinggi))
else:
    print("tinggi anda {}, anda tinggi sekali".format(tinggi))

# Ternary
lulus = True
kata = "selamat" if lulus else "perbaiki"
kata = ("perbaiki", "selamat")[lulus]
print(kata)

# ShortHand Ternary
hasil = None
pesan = hasil or "Tidak ada pesan"
print(pesan)