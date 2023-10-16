# quantidade de alunos 

quantidade_alunos = int(input("Informe a quantidade de alunos na turma: "))

soma_idades = 0

# laço FOR para receber as idades dos alunos
for i in range(quantidade_alunos):
    idade = int(input(f"Informe a idade do aluno {i + 1}: "))
    soma_idades += idade

# média das idades
media_idades = soma_idades / quantidade_alunos

print(f"A média de idade da turma é: {media_idades}")






