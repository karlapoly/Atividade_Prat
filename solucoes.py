# solucoes.py
def sao_anagramas(string1, string2):
    # 1. Normalização: remover espaços e converter para minúsculas
    # O que achas de usar o método replace() para remover espaços e lower() para minúsculas?
    string1_limpa = string1.replace(" ", "").lower()
    string2_limpa = string2.replace(" ", "").lower()
    
    # 2. Ordenação: converter a string limpa numa lista de caracteres e ordená-la
    # O que achas de usar a função sorted() do Python?
    lista_ordenada_1 = sorted(string1_limpa)
    lista_ordenada_2 = sorted(string2_limpa)
    
    # 3. Comparação
    # Como podes verificar se estas duas listas ordenadas são iguais?
    
    return lista_ordenada_1 == lista_ordenada_2

def cifra_de_cesar(texto: str, deslocamento: int) -> str:
    """Aplica a cifra de César ao texto com o deslocamento dado."""
    raise NotImplementedError

def encontrar_maior_palavra(frase: str) -> str:
    """Retorna a maior palavra na frase (pontuação ignorada)."""
    raise NotImplementedError

# --- Secção de Interação com o Utilizador ---

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