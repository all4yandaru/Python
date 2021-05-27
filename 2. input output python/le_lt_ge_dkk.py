from operator import *
hijau = 5
kuning = 10
print('Kelereng Hijau = {}'.format(hijau))
print('Kelereng Kuning = {}'.format(kuning))
for func in (lt, le, eq, ne, ge, gt):
    print('{}(hijau, kuning): {}'.format(func.__name__, func(hijau, kuning)))

'''
lt, less than   <
le, less equal  <=
eq, equal       ==
ne, not equal   !=
ge, greater equal   >=
gt, greater than    >
'''