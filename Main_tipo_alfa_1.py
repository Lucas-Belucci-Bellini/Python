# Código Python para conceitos de Divisibilidade em Matemática Discreta

# --- Definição 1: Divisibilidade ---
# Diz-se que o número inteiro 'a' é divisor do número inteiro 'b'
# ou que o número 'b' é divisível por 'a' se é possível encontrar c ∈ Z tal que b = ac.
# Nesse caso, pode-se dizer também que b é múltiplo de a.
# Para indicar que a divide b, usaremos a notação a | b.

def is_divisible(a: int, b: int) -> bool:
    """
    Verifica se 'a' divide 'b' (a | b).
    Retorna True se 'b' é divisível por 'a', False caso contrário.
    Considera o caso especial de 0 | 0.
    """
    if a == 0:
        return b == 0  # 0 divide 0, mas 0 não divide nenhum outro número
    return b % a == 0

def get_quotient_if_divisible(a: int, b: int) -> int | None:
    """
    Se 'a' divide 'b' e a != 0, retorna o quociente b/a.
    Caso contrário, retorna None.
    """
    if a == 0:
        # Se a é 0, a divisão b/a não é bem definida para b != 0.
        # Se b é 0, 0/0 é indefinido, mas a definição 1 diz 0 = 0*c para qualquer c.
        # Para fins práticos de "quociente", evitamos 0/0.
        return None
    if is_divisible(a, b):
        return b // a
    return None

print("--- Exemplo 2 e 3: Verificação de Divisibilidade e Quociente ---")
a_ex2 = int(input("Digite o primeiro inteiro (a): "))
b_ex2 = int(input("Digite o segundo inteiro (b): "))

if is_divisible(a_ex2, b_ex2):
    print(f"{a_ex2} divide {b_ex2}.")
    quotient_c = get_quotient_if_divisible(a_ex2, b_ex2)
    if quotient_c is not None:
        print(f"O valor de c (quociente) é: {quotient_c}")
    else:
        print("Não foi possível determinar o quociente (provavelmente a=0 e b!=0).")
else:
    print(f"{a_ex2} NÃO divide {b_ex2}.")

print("\n--- Exemplo: -2 divide 6 ---")
print(f"-2 divide 6? {is_divisible(-2, 6)}")
print(f"Quociente: {get_quotient_if_divisible(-2, 6)}") # Saída: -3
print(f"0 divide 0? {is_divisible(0, 0)}") # Saída: True
print(f"0 divide 5? {is_divisible(0, 5)}") # Saída: False


# --- Proposição 1: Propriedades da Divisibilidade ---
# Implementando a propriedade iv: Se a | b e a | c, então a | (bx + cy)
def check_linear_combination_divisibility(a: int, b: int, c: int, x: int, y: int) -> bool:
    """
    Verifica se a | (bx + cy) dado que a | b e a | c.
    Retorna True se a propriedade se mantém, False caso contrário.
    """
    if is_divisible(a, b) and is_divisible(a, c):
        return is_divisible(a, (b * x + c * y))
    return False # A premissa (a|b e a|c) não foi satisfeita

print("\n--- Proposição 1 (iv): a | (bx + cy) ---")
# Exemplo: a=2, b=4, c=6. Sabemos que 2|4 e 2|6.
# Então 2 deve dividir (4*x + 6*y) para quaisquer x, y.
# Vamos testar com x=3, y=2
a_prop = 2
b_prop = 4
c_prop = 6
x_prop = 3
y_prop = 2
result_prop = check_linear_combination_divisibility(a_prop, b_prop, c_prop, x_prop, y_prop)
print(f"Dados a={a_prop}, b={b_prop}, c={c_prop}, x={x_prop}, y={y_prop}:")
print(f"a | b é {is_divisible(a_prop, b_prop)}")
print(f"a | c é {is_divisible(a_prop, c_prop)}")
print(f"a | (bx + cy) é {result_prop}") # Deve ser True


# --- Divisão Inteira e Resto da Divisão (Página 6) ---
print("\n--- Divisão Inteira e Resto da Divisão ---")
num = 35
divisor = 3
quotient = num // divisor  # Divisão inteira
remainder = num % divisor  # Resto da divisão
print(f"Dividindo {num} por {divisor}:")
print(f"Quociente (divisão inteira): {quotient}") # Saída: 11
print(f"Resto da divisão: {remainder}") # Saída: 2


# --- Proposição 2: Regras de Divisibilidade ---
def is_divisible_by_2(n: int) -> bool:
    """Um número é divisível por 2 se seu último dígito for par."""
    return n % 2 == 0

def is_divisible_by_3(n: int) -> bool:
    """Um número é divisível por 3 se a soma dos seus dígitos for múltipla de 3."""
    return sum(int(digit) for digit in str(n)) % 3 == 0

def is_divisible_by_4(n: int) -> bool:
    """Um número é divisível por 4 se os seus dois últimos dígitos formarem um número divisível por 4."""
    if n < 0: n = abs(n) # Regra se aplica ao valor absoluto
    if n < 100: # Para números menores que 100, o próprio número é o "últimos dois dígitos"
        return n % 4 == 0
    return int(str(n)[-2:]) % 4 == 0

def is_divisible_by_5(n: int) -> bool:
    """Um número é divisível por 5 se seu último dígito for 0 ou 5."""
    return n % 5 == 0

def is_divisible_by_6(n: int) -> bool:
    """Um número é divisível por 6 se for divisível por 2 e por 3 ao mesmo tempo."""
    return is_divisible_by_2(n) and is_divisible_by_3(n)

def is_divisible_by_8(n: int) -> bool:
    """Um número é divisível por 8 se os seus três últimos dígitos formarem um número divisível por 8."""
    if n < 0: n = abs(n)
    if n < 1000:
        return n % 8 == 0
    return int(str(n)[-3:]) % 8 == 0

def is_divisible_by_9(n: int) -> bool:
    """Um número é divisível por 9 se a soma dos seus dígitos for múltipla de 9."""
    return sum(int(digit) for digit in str(n)) % 9 == 0

def is_divisible_by_10(n: int) -> bool:
    """Um número é divisível por 10 se seu último dígito for 0."""
    return n % 10 == 0

print("\n--- Proposição 2: Regras de Divisibilidade ---")
test_num = 1234567890
print(f"Testando o número: {test_num}")
print(f"Divisível por 2: {is_divisible_by_2(test_num)}")
print(f"Divisível por 3: {is_divisible_by_3(test_num)}")
print(f"Divisível por 4: {is_divisible_by_4(test_num)}")
print(f"Divisível por 5: {is_divisible_by_5(test_num)}")
print(f"Divisível por 6: {is_divisible_by_6(test_num)}")
print(f"Divisível por 8: {is_divisible_by_8(test_num)}")
print(f"Divisível por 9: {is_divisible_by_9(test_num)}")
print(f"Divisível por 10: {is_divisible_by_10(test_num)}")

test_num_2 = 72
print(f"\nTestando o número: {test_num_2}")
print(f"Divisível por 2: {is_divisible_by_2(test_num_2)}") # True
print(f"Divisível por 3: {is_divisible_by_3(test_num_2)}") # True (7+2=9)
print(f"Divisível por 4: {is_divisible_by_4(test_num_2)}") # True
print(f"Divisível por 6: {is_divisible_by_6(test_num_2)}") # True (por 2 e 3)
print(f"Divisível por 8: {is_divisible_by_8(test_num_2)}") # True
print(f"Divisível por 9: {is_divisible_by_9(test_num_2)}") # True (7+2=9)


# --- Teorema 1: Algoritmo da Divisão (Página 9) ---
# Sejam a e b inteiros, com b > 0. Então, existem únicos inteiros q e r tais que:
# a = bq + r com 0 ≤ r < b.
# Aqui, q é chamado de quociente da divisão de a por b, e r é o resto dessa divisão.

def division_algorithm(a: int, b: int) -> tuple[int, int]:
    """
    Implementa o Algoritmo da Divisão.
    Retorna uma tupla (q, r) onde q é o quociente e r é o resto,
    tal que a = bq + r e 0 <= r < b.
    Assume b > 0.
    """
    if b <= 0:
        raise ValueError("O divisor 'b' deve ser um inteiro positivo (b > 0).")
    q = a // b  # Quociente
    r = a % b   # Resto
    return q, r

print("\n--- Teorema 1: Algoritmo da Divisão ---")
# Exemplo 4:
a_ex4_1 = 35
b_ex4_1 = 3
q1, r1 = division_algorithm(a_ex4_1, b_ex4_1)
print(f"{a_ex4_1} = {b_ex4_1} * {q1} + {r1}") # Saída: 35 = 3 * 11 + 2

a_ex4_2 = 33
b_ex4_2 = 3
q2, r2 = division_algorithm(a_ex4_2, b_ex4_2)
print(f"{a_ex4_2} = {b_ex4_2} * {q2} + {r2}") # Saída: 33 = 3 * 11 + 0

a_ex4_3 = -17
b_ex4_3 = 5
q3, r3 = division_algorithm(a_ex4_3, b_ex4_3)
print(f"{a_ex4_3} = {b_ex4_3} * {q3} + {r3}") # Saída: -17 = 5 * -4 + 3 (Python lida com resto positivo)


# --- Exemplo 5: Cálculo de Notas ---
def calculate_banknotes(amount: float) -> dict[int, int]:
    """
    Calcula a quantidade de notas de 100, 50, 20, 10, 5, 2 necessárias
    para um dado valor em reais.
    """
    notes = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0}
    # Convertendo para centavos para evitar problemas de ponto flutuante
    remaining_amount = int(amount * 100)

    # Apenas notas de 2, 5, 10, 20, 50, 100.
    # Se houver centavos ou notas de 1 real, eles não serão considerados.
    # Para simplificar, vamos assumir que o valor de entrada já é um número inteiro de reais.
    # Se o valor de entrada puder ter centavos, a lógica precisaria ser ajustada
    # para lidar com moedas ou arredondamento.
    if remaining_amount % 100 != 0:
        print("Atenção: O cálculo de notas considera apenas valores inteiros de reais.")
        print("Centavos serão ignorados ou arredondados para baixo.")
    
    remaining_reais = remaining_amount // 100

    for note_value in sorted(notes.keys(), reverse=True):
        if remaining_reais >= note_value:
            count = remaining_reais // note_value
            notes[note_value] = count
            remaining_reais %= note_value
    
    return notes

print("\n--- Exemplo 5: Cálculo de Notas ---")
value_input = float(input("Digite o valor em reais (ex: 378.50): "))
banknotes_needed = calculate_banknotes(value_input)

print(f"Para R$ {value_input:.2f}, as notas necessárias são:")
for note, count in banknotes_needed.items():
    if count > 0:
        print(f"  {count} nota(s) de R$ {note:.2f}")

# Exemplo com um valor específico
print("\nExemplo com R$ 378.00:")
banknotes_378 = calculate_banknotes(378.00)
for note, count in banknotes_378.items():
    if count > 0:
        print(f"  {count} nota(s) de R$ {note:.2f}")
# Saída esperada:
#   3 nota(s) de R$ 100.00
#   1 nota(s) de R$ 50.00
#   1 nota(s) de R$ 20.00
#   1 nota(s) de R$ 5.00
#   1 nota(s) de R$ 2.00
```