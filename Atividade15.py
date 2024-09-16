# 1 - Média de Notas: Crie um programa que solicite ao usuário que insira as cinco notas de um aluno em diferentes disciplinas. Em seguida, calcule e exiba a média das notas inseridas.

print("Programa que calcula a média de várias notas.")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a seginda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a querta nota: "))
nota5 = float(input("Digite a quintaa nota: "))

media = float((nota1 + nota2 + nota3 + nota4 + nota5) / 5)

print(f"A média das notas é: {media}")

# 2 - Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

print("Programa que recebe o valor ganhado por hora e quantas horas foram trabalhadas e retorna o salário.")

recebHora = float(input("Digite quanto você ganha por hora: "))
horasTrab = int(input("Digite a quantidade de horas trabalhadas: "))

salario = recebHora * horasTrab

print(f"O salário total é: {salario}")

# 3 - Calculadora Simples: Escreva um programa que solicite ao usuário que insira dois números e, em seguida, peça que ele escolha uma operação matemática (adição, subtração, multiplicação ou divisão). O programa deve realizar a operação escolhida e exibir o resultado.

def sum (num1, num2):
    return num1 + num2
    
def times (num1, num2):
    return num1 * num2
    
def divide (num1, num2):
    return num1 / num2
    
def minus (num1, num2):
    return num1 - num2

print("Calculadora simples.")
print("Digite 1 para soma, 2 para subtração, 3 para multiplicação e 4 para divisão.")

choose = int(input("Digite a operação: "))

while choose != 1 and choose != 2 and choose != 3 and choose != 4:
    print("Você digitou um valor inválido!")
    choose = int(input("Digite a opção novamente: "))

firstNum = int(input("Digite o primeiro número: "))
secondNum = int(input("Digite o segundo número: "))



if choose == 1:
    res = sum(firstNum, secondNum)
    print(f"A soma de {firstNum} com {secondNum} é: {res}")

if choose == 2:
    res = minus(firstNum, secondNum)
    print(f"A subtração de {firstNum} com {secondNum} é: {res}")
    
if choose == 3:
    res = times(firstNum, secondNum)
    print(f"A multiplicação de {firstNum} com {secondNum} é: {res}")
    
if choose == 4:
    res = divide(firstNum, secondNum)
    print(f"A divisão de {firstNum} com {secondNum} é: {res}")

#  4 - Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

# C = 5 * ((F-32) / 9).

print("Programa que converte de fahrenheit para celsius")

fahrenheit = int(input("Digite a temperatura em fahrenheit: "))

def celsiusFahrenheit (temperature):
    return 5 * ((temperature - 32) / 9)
    
celsius = celsiusFahrenheit(fahrenheit)

print(f"{fahrenheit}º em fahrenheit são {celsius}º celsius.")

# 5 - Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# •o produto do dobro do primeiro com metade do segundo .

# •a soma do triplo do primeiro com o terceiro.

# •o terceiro elevado ao cubo.

int1 = int(input("Digite o primeiro número inteiro: "))
int2 = int(input("Digite o segundo número inteiro: "))
flo = float(input("Digite o número real: "))

ans1 = (int1 * 2) * (int2 / 2)
ans2 = (int1 * 3) + flo
ans3 = flo ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {ans1}")
print(f"A soma do triplo do primeiro com o terceiro é: {ans2}")
print(f"O terceiro elevado ao cubo é: {ans3}")

# 6  - Tendo como dados de entrada a altura de uma pessoa, construa um programa que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58



# 7 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um programa que calcule seu peso ideal, utilizando

#  as seguintes fórmulas:

# •Para homens: (72.7*h) - 58

# •Para mulheres: (62.1*h) - 44.7



# 8.João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.



# 9.Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o se salario liquido, salario bruto e os descontos no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# 1.salário bruto.

# 2.quanto pagou ao INSS.

# 3.quanto pagou ao sindicato.

# 4.o salário líquido.

# calcule os descontos e o salário líquido, conforme a tabela abaixo:

# + Salário Bruto : R$

# - IR (11%) : R$

# - INSS (8%) : R$

# - Sindicato ( 5%) : R$

# = Salário Liquido : R$

# Obs.: Salário Bruto - Descontos = Salário Líquido.



# 10.Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.



# 11.Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

#       Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

 

#   a) comprar apenas latas de 18 litros;

#   b) comprar apenas galões de 3,6 litros;

#   c)misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre   arredonde os valores para cima, isto é, considere latas cheias.



# 12.Programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).