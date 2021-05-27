# penggabungan
angka = [2, 4, 6, 8]
huruf = ['P', 'Y', 'T', 'H', 'O', 'N']
gabung = angka + huruf
print(gabung)

# replikasi
learn = ['P', 'Y', 'T', 'H', 'O', 'N']
replikasi = learn * 2
print(replikasi)

tujuh = [7]*7
print(len(tujuh))
print(tujuh)

# perulangan
for i in range(5):
    print(i)

print()
# perulangan dari 1 - 6
for i in range(1,7):
    print(i)

print()
# perulangan dari 0 - 20 step 5
for i in range(0,21,5):
    print(i)

print([_ for _ in range(0,20,5)])

# buat ngelihat apa ada kalimat nya atau engga
print()
kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

# memberikan nilai utk multiple variable
data = ['shirt', 'white', 'L'] # From List
apparel, color, size = data
data = ('shirt', 'white', 'L')  # From Tuple
apparel, color, size = data