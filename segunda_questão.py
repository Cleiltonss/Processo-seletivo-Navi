from math import factorial, log
x = []
for i in range(1, 11):
    if i % 2 == 0:
        x.append((3 ** i) + (7 * (factorial(i))))
    else:
        x.append((2 ** i) + (4 * (log(i))))
soma = 0
for c in range(0 , len(x)):
    soma += x[c]
    if x[c] == max(x):
        indice_max = c
media = round(soma / len(x), 2)
print(f'O valor da média é {media} e o índice do maior elemento é {indice_max}')