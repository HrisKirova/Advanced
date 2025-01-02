x = list(range(7, 16))
y = list(range(1, 18, 2))

x_reversed = x[::-1]
z = list(zip(x_reversed, y))

for index, (i, j) in enumerate(z):
    if index == 0:
        print(' ' * i + '\033[93m' + '*' * j + '\033[0m')
    else:
        print(' ' * i + '\033[32m' + '*' * j)

for r in range(3):
    print(' ' * 13 + '\033[33m || \033[0m')

print(' ' * 12, end='\\=====/')
print('')