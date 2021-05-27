def printinfo(*args, **kwargs):
    for a in args:
        print('argumen posisi {}'.format(a))
    for key, value in kwargs.items():
        print('argumen kata kunci {}:{}'.format(key, value))


# Panggil printinfo
printinfo()
printinfo(1, 2, 3)
printinfo(i=7, j=8, k=9)
printinfo(1, 2, j=8, k=9)
printinfo(*(2, 3), **{'i': 7, 'j': 8})

# lambda
kali = lambda nilai1, nilai2: nilai1 * nilai2;
print("Hasil : ", kali(11, 21))
print("Hasil : ", kali(2, 2))
