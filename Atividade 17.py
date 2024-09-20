choose = input("Digte o turno que você estuda (M para matutino, V para vespertino, N para noturno): ")

while (choose != "M" and choose != "m") and (choose != "V" and choose != "v") and (choose != "N" and choose != "n"):
    choose = input(f"{choose} não é um valor válido!")

if choose == "M" or choose == "m":
    print("Bom dia!")
    
elif choose == "V" or choose == "v":
    print("Boa tarde!")

elif choose == "N" or choose == "n":
    print("Boa noite!")
    