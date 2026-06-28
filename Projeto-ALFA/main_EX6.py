n = int(input("Digite um numero: "))

if n % 3 == 0 and n % 5 != 0:
    print(n, "e divisivel por 3 e NAO por 5")
else:
    print(n, "nao satisfaz a condicao")