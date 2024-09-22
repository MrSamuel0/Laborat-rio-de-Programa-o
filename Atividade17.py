#1 - Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

choose = input("Digte o turno que você estuda (M para matutino, V para vespertino, N para noturno): ")

while (choose != "M" and choose != "m") and (choose != "V" and choose != "v") and (choose != "N" and choose != "n"):
    choose = input(f"{choose} não é um valor válido!")

if choose == "M" or choose == "m":
    print("Bom dia!")
    
elif choose == "V" or choose == "v":
    print("Boa tarde!")

elif choose == "N" or choose == "n":
    print("Boa noite!")

#2 – Programa para permitir que as Organizações Tabajara deem um aumento de salário aos seus colaboradores

#  O programa recebe o salário de um colaborador e  calcula o reajuste segundo o seguinte critério, baseado no   salário atual:

#•salários até R$ 280,00 (incluindo) : aumento de 20%
#•salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#•salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#•salários de R$ 1500,00 em diante : aumento de 5%
#Após o aumento ser realizado, informe na tela:

#•o salário antes do reajuste;
#•o percentual de aumento aplicado;
#•o valor do aumento;
#•o novo salário, após o aumento.

salario = float(input("Digite o seu salário atual: "))

reajuste = ""
aumento = 0

if salario <= 280:
    reajuste = "20%"
    aumento = salario * 0.20
    salarioNovo = salario + aumento
    
    
elif (salario > 280) and (salario <= 700):
    reajuste = "15%"
    aumento = salario * 0.15
    salarioNovo = salario + aumento
    
elif (salario > 700) and (salario <= 1500):
    reajuste = "10%"
    aumento = salario * 0.10
    salarioNovo = salario + aumento
    
elif salario > 1500:
    reajuste = "5%"
    aumento = salario * 0.05
    salarioNovo = salario + aumento
    
print(f"O reajuste do salario de {salario} ficou em {salarioNovo}, teve um aumento de  {aumento} com reajuste de {reajuste} do salário anterior.")

#3 - Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

semana = ["domingo", "segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado"]

resposta = int(input("Digite um número de 1 a 7: "))

match resposta:
    case 1:
        print(f"O dia da semana correspondente ao número 1 é: {semana[0]}")

    case 2:
        print(f"O dia da semana correspondente ao número 2 é: {semana[1]}")

    case 3:
        print(f"O dia da semana correspondente ao número 3 é: {semana[2]}")

    case 4:
        print(f"O dia da semana correspondente ao número 4 é: {semana[3]}")

    case 5:
        print(f"O dia da semana correspondente ao número 5 é: {semana[4]}")

    case 6:
        print(f"O dia da semana correspondente ao número 6 é: {semana[5]}")

    case 7:
        print(f"O dia da semana correspondente ao número 7 é: {semana[6]}")

    case _:
        print(f"{resposta} não corresponde a nenhum dia da semana!")

#4 - Programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua

#        média. A atribuição de conceitos obedece à tabela abaixo:

#  Média de Aproveitamento    Conceito

#•  Entre 9.0 e 10.0                A
#•  Entre 7.5 e 9.0                 B
#•  Entre 6.0 e 7.5                 C
#•  Entre 4.0 e 6.0               D
#•  Entre 4.0 e zero               E
#       O programa deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o

#        conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

while (nota1 > 10) or (nota2 > 10):
    print(f"Não é possível ter uma nota maior que 10")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
conceito = ""
mensagem = ""

if media > 9.0:
    conceito = "A"
    mensagem = "Aprovado"

elif (media > 7.5) and (media <= 9.0):
    conceito = "B"
    mensagem = "Aprovado"

elif (media > 6.0) and (media <= 7.5):
    conceito = "C"
    mensagem = "Aprovado"

elif (media > 4.0) and (media <= 6.0):
    conceito = "D"
    mensagem = "Reprovado"

elif media <= 4.0:
    conceito = "E"
    mensagem = "Reprovado"


print(f"A sua média é {media}, você obteve um conceito {conceito} de aproveitamento na matéria. Você está {mensagem}")    
