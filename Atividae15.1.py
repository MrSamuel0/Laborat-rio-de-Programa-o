print("Programa que converte de fahrenheit para celsius")

fahrenheit = int(input("Digite a temperatura em fahrenheit: "))

def celsiusFahrenheit (temperature):
    return 5 * ((temperature - 32) / 9)
    
celsius = celsiusFahrenheit(fahrenheit)

print(f"{fahrenheit}º em fahrenheit são {celsius}º celsius.")