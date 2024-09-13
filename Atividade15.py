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