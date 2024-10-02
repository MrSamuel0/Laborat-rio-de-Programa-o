#1 - Programa que imprima a tabuada do 13.

i = 0

while i <= 10:
    print(f"13 x {i} = {13 * i}")
    i += 1

#2 - Programa que leia do teclado uma lista com 15 inteiros e imprima o menor valor.

i = 0
numero = int(input("Digite um número: "))
menor = numero

while i <= 14:
    if numero < menor:
        menor = numero
    
    numero = int(input("Digite outro número: "))
    i += 1
    
print(f"O menor número é {menor}")

#3 - Programa que leia do teclado uma lista com 5 inteiros e imprima “True” se a lista estiver ordenada de forma crescente ou “False” caso contrário.

crescente = False
anterior = 0
atual = int(input("Digite um número: "))
i = 0

while i <= 4:
    if atual < anterior:
        crescente = False
        
        print(crescente)
        
    elif atual > anterior:
        crescente = True
        
        print(crescente)
        
    elif atual == anterior:
        crescente = False
        
        print(crescente)
        
    anterior = atual
    atual = int(input("Digite outro número: "))

#4 - Programa para imprimir em ordem decrescente todos os números de 500 até 10.

i = 500

while i >= 10:
    print(i)
    
    i -= 1

#5 - Programa para ler do teclado 10 números e imprima a quantidade de números entre 10 e 50.

lista = []
i = 1

while i <= 10:
    numero = int(input("Digite um número: "))
    
    if (numero >= 10) and (numero <=50):
        lista.append(numero)
        
    i += 1
    
print(f"Os números digitados que estão entre 10 e 50 são: {lista}")

#6 - Programa Ler do teclado a idade e o sexo de 10 pessoas, calcule e imprima:
#•idade média das mulheres
#•idade média dos homens
#•idade média do grupo

i = 0
homens = []
mulheres = []
geral = []
somaHomens = 0
somaMulheres = 0
somaGeral = 0

while i <= 9:
    sexo = int(input("Qual o seu sexo (1 para masculino, 2 para feminino): "))
    
    while (sexo != 1) and (sexo != 2):
        sexo = int(input("Qual o seu sexo (1 para masculino, 2 para feminino): "))
    
    idade = int(input("Qual é a sua idade? "))
    
    if sexo == 1:
        homens.append(idade)
        geral.append(idade)
        
    elif sexo == 2:
        mulheres.append(idade)
        geral.append(idade)
        
    i += 1
    
for idade in homens:
    somaHomens += idade
    
for age in mulheres:
    somaMulheres += age 
    
for edad in geral:
    somaGeral += edad 
    
mediaHomens = somaHomens / len(homens)
mediaMulheres = somaMulheres / len(mulheres)
mediaGeral = somaGeral / len(geral)

print(f"A média da idade dos homens é: {mediaHomens}, das mulheres: {mediaMulheres}, e a média geral: {mediaGeral}")

#7 – Programa que calcule o somatório dos números de 1 a 100 e imprima o resultado.



#8 – Programa que leia vários conjuntos de dois números inteiros correspondentes à largura e altura de um retângulo  e, para cada um deles, calcule a  respectiva área do retângulo e imprima a as medidas das áreas e dos lados. O conjunto de números acaba quando aparece o primeiro lado igual a 99.



#9 – Programa para ler do teclado um conjunto de números inteiros e imprima apenas os números primos. O conjunto acaba quando aparece o numero 1000.


#10 – Programa para controlar a capacidade máxima de um restaurante. Primeiro leia um numero inteiro que significa a capacidade máxima do restaurante. Depois o programa vai lendo vários números inteiros que significam os números dos clientes que entraram. Após o restaurante ficar cheio, imprima a mensagem “atingiu a capacidade máxima”.


