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

# --- Secção de Interação com o Utilizador ---

def menu_interativo():
    """Menu interativo para testar as funções"""
    while True:
        print("\n=== MENU INTERATIVO ===")
        print("Escolha uma opção:")
        print("1 - Verificar Anagramas")
        print("2 - Encontrar Maior Palavra")
        print("3 - Ver Exemplos")
        print("4 - Sair")
        
        try:
            opcao = input("\nDigite sua opção (1, 2, 3 ou 4): ")
            
            if opcao == "1":
                # Verificador de Anagramas
                print("\n--- Verificador Interativo de Anagramas ---")
                entrada1 = input("Por favor, insira a primeira palavra ou frase: ")
                entrada2 = input("Por favor, insira a segunda palavra ou frase: ")
                
                resultado_usuario = sao_anagramas(entrada1, entrada2)
                
                print("\n--- Resultado ---")
                if resultado_usuario:
                    print(f'SIM! "{entrada1}" e "{entrada2}" SÃO anagramas.')
                else:
                    print(f'NÃO! "{entrada1}" e "{entrada2}" NÃO são anagramas.')
            
            elif opcao == "2":
                # Encontrador de Maior Palavra
                print("\n--- Encontrador de Maior Palavra ---")
                frase_usuario = input("Por favor, insira uma frase: ")
                
                maior_palavra = encontrar_maior_palavra(frase_usuario)
                
                print("\n--- Resultado ---")
                print(f'A maior palavra na frase é: "{maior_palavra}"')
                print(f'Comprimento: {len(maior_palavra)} caracteres')
            
            elif opcao == "3":
                # Mostrar exemplos
                print("\n--- EXEMPLOS DAS FUNÇÕES ---")
                
                print("\n1. Exemplos de Anagramas:")
                exemplos_anagramas = [
                    ("amor", "roma"),
                    ("listen", "silent"),
                    ("a gentleman", "elegant man"),
                    ("python", "typhon")
                ]
                
                for palavra1, palavra2 in exemplos_anagramas:
                    resultado = sao_anagramas(palavra1, palavra2)
                    status = "SÃO" if resultado else "NÃO são"
                    print(f'   "{palavra1}" e "{palavra2}" {status} anagramas')
                
                print("\n2. Exemplos de Maior Palavra:")
                exemplos_maior = [
                    "O rato roeu a roupa do rei de Roma",
                    "A jornada de mil milhas começa com um único passo.",
                    "Seja forte e corajoso",
                    "Python é uma linguagem incrível!"
                ]
                
                for frase in exemplos_maior:
                    maior = encontrar_maior_palavra(frase)
                    print(f'   Frase: "{frase}"')
                    print(f'   Maior palavra: "{maior}" ({len(maior)} caracteres)')
                    print()
            
            elif opcao == "4":
                print("\nObrigado por usar o programa! Até logo!")
                break
                
            else:
                print("\nOpção inválida! Por favor, escolha 1, 2, 3 ou 4.")
                
        except KeyboardInterrupt:
            print("\n\nPrograma interrompido pelo usuário. Até logo!")
            break
        except EOFError:
            print("\n\nEntrada encerrada. Até logo!")
            break

# Executa o menu se o arquivo for executado diretamente
if __name__ == "__main__":
    menu_interativo()
