# zfill
# Contoh 1: Penggunaan zfill 5 pada angka satuan
angka = 5
print(str(angka).zfill(5));
# Contoh 2: Penggunaan zfill 5 pada angka ratusan
angka = 300
print(str(angka).zfill(5));
# Contoh 3: Penggunaan zfill 5 pada angka desimal negatif (memiliki koma)
angka = -0.45
print(str(angka).zfill(5));
# Contoh 4: Penggunaan zfill 7 pada angka desimal negatif (memiliki koma)
angka = -0.45
print(str(angka).zfill(7));

# Contoh 1
kata = 'aku'
print(kata.zfill(5));
# Contoh 2
kata = 'kamu'
print(kata.zfill(5));
# Contoh 3
kata = 'dirinya'
print(kata.zfill(5));

# rjust, ljust, center
print('Dicoding'.rjust(20))  # rata kanan
print('Dicoding'.ljust(20))  # rata kiri
print('Dicoding'.center(20))  # rata tengah
print('Dicoding'.center(20, '-'))  # rata tengah

# string literah
st1 = "jum'at"
st1 = 'Jum\'at'

# raw string
print('Dicoding\tIndonesia')
print(r'Dicoding\tIndonesia')