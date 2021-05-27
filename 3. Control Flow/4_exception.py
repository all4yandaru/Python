z = 0
try:
    x = 1 / z
except ZeroDivisionError:
    print('tidak bisa membagi angka dengan nilai nol')

try:
    with open('contoh_tidak_ada.py') as file:
        print(file.read())
except:
    print('file tidak ditemukan')

# KeyError
# ValueError
# except (ValueError, TypeError):
# except (ValueError, TypeError) as e:


d = {'ratarata': '10.0'}
if 'ratarata' not in d:
    raise KeyError('harus memiliki total')
else:
    print(d['total'])