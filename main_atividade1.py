"""
Demonstração que 4 divide (2m - 2n) quando n é impar
4 | (2m - 2n) ⟺ 2m - 2n ≡ 0 (mod 4)
                ⟺ 2(m - n) ≡ 0 (mod 4)
                ⟺ m - n ≡ 0 (mod 2)
                ⟺ m - n é par

Quando n é impar, m deve ser par ou impar:
- Se m é par: m - n é ímpar - ímpar = par ✓
- Se m é impar: não funciona para todos os casos

Vamos verificar que 4 | (2m - 2n) quando n é impar
"""

def verificar_divisibilidade(m, n):
    """
    Verifica se 4 divide (2m - 2n) quando n é impar
    """
    if n % 2 == 0:
        return False, "n deve ser ímpar"
    
    resultado = 2 * m - 2 * n
    divisivel = resultado % 4 == 0
    
    return divisivel, resultado


# Testando com vários valores onde n é impar
print("Demonstração: 4 | (2m - 2n) quando n é impar\n")
print("-" * 60)

testes = [
    (1, 1),   # m=1, n=1 (ímpar)
    (2, 1),   # m=2, n=1 (ímpar)
    (3, 1),   # m=3, n=1 (ímpar)
    (4, 3),   # m=4, n=3 (ímpar)
    (5, 3),   # m=5, n=3 (ímpar)
    (10, 5),  # m=10, n=5 (ímpar)
    (7, 1),   # m=7, n=1 (ímpar)
]

for m, n in testes:
    resultado = 2 * m - 2 * n
    divisivel = resultado % 4 == 0
    status = "✓ VERDADE" if divisivel else "✗ FALSO"
    print(f"m={m:2d}, n={n:2d} (n ímpar): 2m - 2n = {resultado:3d}, 4|{resultado:3d}? {status}")

print("-" * 60)

# Prova algébrica
print("\nProva algébrica:")
print("Se n é ímpar, podemos escrever n = 2k + 1 para algum inteiro k")
print("Então: 2m - 2n = 2m - 2(2k + 1) = 2m - 4k - 2 = 2(m - 2k - 1)")
print("\nPara 4 | (2m - 2n), precisamos que (m - 2k - 1) seja par")
print("Isto acontece quando m é ímpar (pois ímpar - par - ímpar = par) ✓")
print("\nOu quando m = 2j para algum inteiro j:")
print("2(2j - 2k - 1) = 4j - 4k - 2 = 2(2(j-k) - 1)")
print("Neste caso, 4 não divide sempre, depende de m e n específicos.")
