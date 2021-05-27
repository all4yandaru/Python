kata = 'dicoding'
kata = kata.upper()
print(kata)

kata = kata.lower()
print(kata)

# strip
print('     Dicoding    '.rstrip())  # menghapus whitespace di kanan
print('     Dicoding    '.lstrip())  # menghapus whitespace di kiri
print('     Dicoding    '.strip())  # menghapus whitespace di kanan kiri

kata = 'CodeADicodingCodeCode'
print(kata.strip('Code'))  # menghapus kata 'Code'

# startswith & endswith
print('Dicoding Indonesia'.startswith('Dicoding'))
print('Dicoding Indonesia'.endswith('Indonesia'))

# join
print(' '.join(['Dicoding', 'Indonesia', '!']))
print('123'.join(['Dicoding', 'Indonesia', '!']))

# split
print('Dicoding Indonesia !'.split())
print('Dicoding123Indonesia123!'.split('123'))
print('''Halo,
aku ikan,
aku suka sekali menyelam
aku tinggal di perairan.
Badanku licin dan renangku cepat.
Senang berkenalan denganmu.'''.split('\n'))

# replace
string = "Ayo belajar Coding di Dicoding karena Coding adalah bahasa masa depan"
print(string.replace("Coding", "Pemrograman"))
print(string.replace("Coding", "Pemrograman", 1))

# isupper & islower
kata = "DICODING"
print(kata.isupper())
print(kata.islower())

# isalpha & isalnum & isdecimal
print("dicoding".isalpha())  # semua huruf
print("dicoding123".isalnum())  # gabungan huruf dan angka
print("123".isdecimal())  # semua angka

# isspace & istitle
print('      '.isspace())  # whitespace semua
print('Dicoding Indonesia'.istitle())  # format penulisan judul
