# solucoes.py
def sao_anagramas(string1, string2):
    """
    Verifica se duas strings são anagramas, ignorando espaços e case.
    Args:
        string1 (str): A primeira string para comparação.
        string2 (str): A segunda string para comparação.
    Returns:
        bool: True se forem anagramas, False caso contrário.
    """
    from collections import Counter
    # 1. Normalização: remover espaços e converter para minúsculas
    s1 = string1.replace(" ", "").lower()
    s2 = string2.replace(" ", "").lower()
    # Compara as contagens de caracteres
    return Counter(s1) == Counter(s2)

def cifra_de_cesar(texto: str, deslocamento: int) -> str:
    """Aplica a cifra de César ao texto com o deslocamento dado.
    Args:
        texto (str): O texto para ser cifrado
        deslocamento (int): O número de posições para deslocar cada letra (pode ser positivo ou negativo)
    Returns:
        str: O texto cifrado
    """
    resultado = ""
    for caractere in texto:
        if caractere.isalpha():
            # Determina o código ASCII base (97 para minúsculas, 65 para maiúsculas)
            ascii_base = 65 if caractere.isupper() else 97
            # Converte o caractere para número (0-25), aplica o deslocamento e volta para letra
            novo_caractere = chr((ord(caractere) - ascii_base + deslocamento) % 26 + ascii_base)
            resultado += novo_caractere
        else:
            # Mantém caracteres não alfabéticos inalterados
            resultado += caractere
    return resultado

def encontrar_maior_palavra(frase: str) -> str:
    """Retorna a maior palavra na frase (pontuação ignorada)."""
    raise NotImplementedError

#criado um seletor para tipo da fuçao
def selecionar_funcao(tipo: str):

    if tipo == "anagrama":
        # 1. Pede as strings ao utilizador
        print("\n--- Verificador Interativo de Anagramas ---")
        entrada1 = input("Por favor, insira a primeira palavra ou frase: ")
        entrada2 = input("Por favor, insira a segunda palavra ou frase: ")

        # 2. Chama a tua função com as entradas do utilizador
        resultado_usuario = sao_anagramas(entrada1, entrada2)

        # 3. Apresenta o resultado de forma clara
        print("\n--- Resultado ---")
        if resultado_usuario:
            print(f'SIM! "{entrada1}" e "{entrada2}" SÃO anagramas.')
        else:
            print(f'NÃO! "{entrada1}" e "{entrada2}" NÃO são anagramas.')

    elif tipo == "cifra":
        print("\n--- Cifra de César Interativa ---")
        entrada = input("Por favor, insira a palavra ou frase a ser cifrada: ")
        #faz a conversao para inteiro
        deslocamento = int(input("Por favor, insira o deslocamento (número inteiro): "))

        # 2. Chama a tua função com as entradas do utilizador
        resultado_usuario = cifra_de_cesar(entrada, deslocamento)

        # 3. Apresenta o resultado de forma clara
        print("\n--- Resultado ---")
        print(f'Texto original: {entrada}')
        print(f'Deslocamento: {deslocamento}')
        print(f'Texto cifrado: {resultado_usuario}')

          
    elif tipo == "maior_palavra":
        return encontrar_maior_palavra
    else:
        raise ValueError("Tipo de função desconhecido.")


# --- Secção de Interação com o Utilizador ---
# Solicitando o tipo de função
tipo_funcao = input("Qual tipo de função você deseja usar? (anagrama/cifra/maior_palavra): ")
funcao_selecionada = selecionar_funcao(tipo_funcao)





