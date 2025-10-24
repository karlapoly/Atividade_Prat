# Atividade: Code Review e Colaboração com Git & GitHub
Grupo: Karla Polyanna, Marcelo Sabaris
Descrição: Implementar 3 funções em Python:

Desenvolvedor 1: Verificador de anagramas
Tarefa: Crie uma função sao_anagramas(string1, string2) que receba duas strings e retorne True se elas forem anagramas uma da outra, e False caso contrário.
Definição: Um anagrama é uma palavra ou frase formada pelo rearranjo das letras de outra palavra ou frase. Espaços e diferenças entre maiúsculas e minúsculas devem ser ignorados.
Exemplos:
sao_anagramas("amor", "roma") → True
sao_anagramas("A gentleman", "Elegant man") → True
sao_anagramas("gato", "cabra") → False

Desenvolvedor 2: Cifra de César
Tarefa: Crie uma função cifra_de_cesar(texto, deslocamento) que aplique a Cifra de César a uma string.
Definição: A Cifra de César é uma técnica de criptografia simples onde cada letra do texto original é substituída por outra letra que se encontra a um número fixo de posições (deslocamento) à frente no alfabeto. A função deve preservar maiúsculas/minúsculas e não alterar caracteres que não sejam letras (números, espaços, pontuação). O alfabeto deve ser considerado circular (depois de 'z' vem 'a').
Exemplos:
cifra_de_cesar("abc", 2) → "cde"
cifra_de_cesar("xyz", 3) → "abc"
cifra_de_cesar("Ataque ao Amanhecer!", 5) → "Fyfvzj ft Frfsmjhmjw!"

Desenvolvedor 3: Encontrar a maior palavra em uma frase
Tarefa: Crie uma função encontrar_maior_palavra(frase) que receba uma string contendo uma frase e retorne a maior palavra encontrada nela.
Definição: As palavras são separadas por espaços. Se houver duas ou mais palavras com o mesmo comprimento máximo, a função deve retornar a primeira que aparecer. A pontuação anexada às palavras (como vírgulas ou pontos finais) deve ser ignorada na contagem do comprimento.
Exemplos:
encontrar_maior_palavra("O rato roeu a roupa do rei de Roma") → "roupa"
encontrar_maior_palavra("A jornada de mil milhas começa com um único passo.") → "jornada"
encontrar_maior_palavra("Seja forte e corajoso") → "forte" (retorna a primeira de tamanho 5)

Como testar:
$ python3 tests.py
