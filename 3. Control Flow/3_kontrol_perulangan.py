# else for
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n / x)
            break
    else:  # else dijalankan saat if di dalam for tidak pernah bernilai True
        # loop fell through without finding a factor
        print(n, ' adalah bilangan prima')

# else while
n = 10
while n > 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:  # else dijalankan setiap while bernilai false
    print("Loop selesai")

# pass
import sys

data = ''
while (data != 'exit'):
    try:
        data = input('Please enter an integer (type exit to exit): ')
        print('got integer: {}'.format(int(data)))
    except:
        if data == 'exit':
            pass  # exit gracefully without prompt any error
        else:
            print('error: {}'.format(sys.exc_info()[0]))
