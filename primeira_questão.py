d = 0
for c in range(1, 5000001):
    if c % 49 == 0 and c % 37 and c %  2 == 0:
        d += 1
print(f'O número de pares multiplos de 37 e 49, entre 1 e 5.000.000, é: {d}')