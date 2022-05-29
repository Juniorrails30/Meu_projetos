quantas_nota = int(input("Quantas notas você vai somar: "))
soma_nota = 0
for x in range((quantas_nota)):
    nota_aluno = float(input(f'Digite a {x+1} nota: '))
    soma_nota = soma_nota + nota_aluno

print(f'A média do aluno foi {soma_nota / 5:.2f}')