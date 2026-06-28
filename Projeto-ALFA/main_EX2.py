a = int(input("Digite a: "))
b = int(input("Digite b: "))

if b == 0:
    print("Divisao por zero nao e definida.")
else:
    quociente = a // b
    resto = a % b
    print("a div b =", quociente)
    print("a mod b =", resto)