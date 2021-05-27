# for
for huruf in "Dicoding":
    print("Huruf {}".format(huruf))

print("=========")
flowers = ['mawar', 'melati', 'anggrek']
for bunga in flowers:
    print("flower : {}".format(bunga))

print("=========")
for index in range(len(flowers)):
    print('Flowers [{}]: {}'.format(index, flowers[index]))

for i in range(3, 1, -1):  # dari 3 sampai 2, step -1
    print(i)

for i in range(5, -1, -1):
    for j in range(i):
        print("*", end="")
    print()

# while
count = 0
while count < 7:
    print('Hitungannya adalah: {}'.format(count))
    count += 2
