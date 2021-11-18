dicionario = {}
for c in range(0, 5):
    nome = input('Qual o nome do aluno(a)? ')
    nota = float(input('Qual a nota dele(a)? '))
    dicionario[nome] = nota
maior = -1
for nome, nota in dicionario.items():
    if maior < nota:
        maior = nota
        nome_maior = nome
print(f'O aluno com a maior nota foi {nome_maior} com nota {maior}')