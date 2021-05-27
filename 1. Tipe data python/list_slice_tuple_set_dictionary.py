# 2 List, Slicing, Tuple, Set, dan Dictionary
a = [1, 2.2, 'python']  # list [ ... ]

# List
x = [5, 10, 15, 20, 25, 30, 35, 40]
print(x[5])
print(x[-2])  # paling belakang ke-2
print(x[3:5])  # index ke 3 sampe sebelum index 5
print(x[:5])  # index 0-4
print(x[-3:])  # 3 angka paling belakang
print(x[1:7:2])  # index 1-6 step 2

# ===============================
x.append(5)
print(x)
del x[0]
print(x)

# Slicing " ... "
s = "Hello World!"
print(s[4], type(s))  # ambil karakter kelima dari string s
print(s[6:11])  # ambil karakter index 6-10
# s[5] = "d"  # ubah karakter keenam dari string s menjadi "d", seharusnya gagal karena immutable
s = "Halo Dunia!"  # ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
print(s)

# tuple ( ... )
t = (5, 'program', 1 + 3j)
print(t[1], type(t))
print(t[0:3])
# print(t[0]=10)

# set { ... }
a = {1,2,2,3,3,3}
print(a)


# dictionary key : value
d = {1:'value','key':2}
print(type(d))
print("d[1] = ", d[1]);
print("d['key'] = ", d['key']);
