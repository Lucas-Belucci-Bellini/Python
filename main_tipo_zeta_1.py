def soma_digitos(numero_str: str) -> int:
    return sum(int(digito) for digito in numero_str if digito.isdigit())


def dois_ultimos_digitos(numero_str: str) -> int:
    return int(numero_str[-2:]) if len(numero_str) >= 2 else int(numero_str)


def tres_ultimos_digitos(numero_str: str) -> int:
    return int(numero_str[-3:]) if len(numero_str) >= 3 else int(numero_str)


def eh_divisivel_por_2(numero_str: str) -> bool:
    return numero_str[-1] in "02468"


def eh_divisivel_por_3(numero_str: str) -> bool:
    return soma_digitos(numero_str) % 3 == 0


def eh_divisivel_por_4(numero_str: str) -> bool:
    return dois_ultimos_digitos(numero_str) % 4 == 0


def eh_divisivel_por_5(numero_str: str) -> bool:
    return numero_str[-1] in "05"


def eh_divisivel_por_6(numero_str: str) -> bool:
    return eh_divisivel_por_2(numero_str) and eh_divisivel_por_3(numero_str)


def eh_divisivel_por_8(numero_str: str) -> bool:
    return tres_ultimos_digitos(numero_str) % 8 == 0


def eh_divisivel_por_9(numero_str: str) -> bool:
    return soma_digitos(numero_str) % 9 == 0


def eh_divisivel_por_10(numero_str: str) -> bool:
    return numero_str[-1] == "0"


def resultado_divisibilidade(numero: str) -> dict:
    numero_limpo = numero.strip()
    if numero_limpo.startswith(('+', '-')):
        numero_limpo = numero_limpo[1:]

    if not numero_limpo.isdigit():
        raise ValueError("Entrada deve ser um número inteiro.")

    return {
        2: eh_divisivel_por_2(numero_limpo),
        3: eh_divisivel_por_3(numero_limpo),
        4: eh_divisivel_por_4(numero_limpo),
        5: eh_divisivel_por_5(numero_limpo),
        6: eh_divisivel_por_6(numero_limpo),
        8: eh_divisivel_por_8(numero_limpo),
        9: eh_divisivel_por_9(numero_limpo),
        10: eh_divisivel_por_10(numero_limpo),
    }


def main() -> None:
    numero = input().strip()
    if not numero:
        return

    try:
        resultados = resultado_divisibilidade(numero)
    except ValueError:
        print("Entrada inválida")
        return

    for divisor in [2, 3, 4, 5, 6, 8, 9, 10]:
        print(f"Divisível por {divisor}: {'Sim' if resultados[divisor] else 'Não'}")


if __name__ == '__main__':
    main()
