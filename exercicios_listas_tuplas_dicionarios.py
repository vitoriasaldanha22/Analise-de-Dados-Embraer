# 2. Lista: Acessar elementos por índice
lista_nomes = ["Ana", "Bruno", "Carla", "Daniel", "Elisa"]
print(f"2. Segundo nome: {lista_nomes[1]}, Quarto nome: {lista_nomes[3]}")

# 3. Dicionário: Acessar valor por chave
dicionario_cores = {"vermelho": "#FF0000", "verde": "#00FF00", "azul": "#0000FF"}
print(f"3. Valor da chave 'vermelho': {dicionario_cores['vermelho']}")

# 4. Lista: Média de números
lista_numeros = [10, 20, 30, 40, 50, 60]
media_lista = sum(lista_numeros) / len(lista_numeros)
print(f"4. Média da lista: {media_lista}")

# 5. Dicionário: Adicionar novo par chave-valor
dicionario_cidades = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"}
dicionario_cidades["ES"] = "Vitória"
print(f"5. Dicionário atualizado: {dicionario_cidades}")

# 6. Tupla, lista e adição de elemento
tupla_numeros2 = (1, 2, 3, 4)
lista_numeros2 = list(tupla_numeros2)
lista_numeros2.append(5)
print(f"6. Lista após conversão e adição: {lista_numeros2}")

# 7. Lista: Remover elemento por índice
lista_numeros3 = [1, 2, 3, 4, 5, 6, 7]
del lista_numeros3[3]
print(f"7. Lista após remoção: {lista_numeros3}")

# 8. Dicionário: Alterar valor de chave
dicionario_frutas = {"maçã": 1.50, "banana": 2.00, "laranja": 1.75}
dicionario_frutas["banana"] = 2.20
print(f"8. Dicionário com valor alterado: {dicionario_frutas}")

# 9. Tupla: Acessar último elemento
tupla_cores = ("vermelho", "verde", "azul", "amarelo", "preto")
print(f"9. Último elemento da tupla: {tupla_cores[-1]}")

# 10. Lista: Combinar listas
lista1 = [1, 2, 3, 4]
lista2 = [5, 6, 7, 8]
lista_combinada = lista1 + lista2
print(f"10. Lista combinada: {lista_combinada}")

# 11. Lista e If: Verificar se elemento existe
lista_verificacao = [5, 10, 15, 20, 25]
if 10 in lista_verificacao:
    print("11. O número 10 está na lista.")
else:
    print("11. O número 10 não está na lista.")

# 12. Dicionário e If: Verificar chave
dicionario_verifica_chave = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
if "idade" in dicionario_verifica_chave:
    print("12. A chave 'idade' existe no dicionário.")
else:
    print("12. A chave 'idade' não existe no dicionário.")

# 13. Input e If: Verificar número maior que 10
numero_input = int(input("13. Digite um número: "))
if numero_input > 10:
    print("13. O número é maior que 10.")
else:
    print("13. O número não é maior que 10.")

# 14. Lista e If: Verificar números negativos
lista_numeros_negativos = [1, -2, 3, -4, 5]
tem_negativo = False
for numero in lista_numeros_negativos:
    if numero < 0:
        tem_negativo = True
        break
if tem_negativo:
    print("14. A lista possui um número negativo.")
else:
    print("14. A lista não possui um número negativo.")

# 15. Tupla e If: Verificar primeiro e segundo elemento
tupla_comparacao = (15, 10, 5)
if tupla_comparacao[0] > tupla_comparacao[1]:
    print("15. O primeiro número é maior que o segundo.")
else:
    print("15. O primeiro número não é maior que o segundo.")

# 16. Dicionário e Input: Acessar valor por chave digitada
dicionario_input_chave = {"a": 100, "b": 200, "c": 300}
chave_desejada = input("16. Digite a chave (a, b ou c): ")
if chave_desejada in dicionario_input_chave:
    print(f"16. Valor da chave '{chave_desejada}': {dicionario_input_chave[chave_desejada]}")
else:
    print("16. Chave não encontrada.")

# 17. Input e Lista: Adicionar números a lista
lista_input_numeros = []
for _ in range(5):
    numero_digitado = int(input("17. Digite um número: "))
    lista_input_numeros.append(numero_digitado)
print(f"17. Lista de números digitados: {lista_input_numeros}")

# 18. Tupla e If: Verificar primeiro e último elemento
tupla_igualdade = (5, 10, 15, 5)
if tupla_igualdade[0] == tupla_igualdade[-1]:
    print("18. O primeiro e o último elemento são iguais.")
else:
    print("18. O primeiro e o último elemento são diferentes.")

# 19. Lista e If: Verificar se nome existe
lista_nomes_maria = ["João", "Maria", "José"]
if "Maria" in lista_nomes_maria:
    print("19. Maria está na lista.")
else:
    print("19. Maria não está na lista.")

# 20. Dicionário e If: Verificar valor da chave 'idade'
dicionario_idades = {"nome": "Carlos", "idade": 25, "cidade": "Recife", "profissao": "Programador"}
if "idade" in dicionario_idades and dicionario_idades["idade"] > 18:
    print("20. A idade é maior que 18.")
else:
    print("20. A idade não é maior que 18 ou a chave 'idade' não existe.")