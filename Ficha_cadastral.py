#Nome
#Peso
#Altura
#Idade
#Tem peso minimo para doar
#Tem idade minima para doar

print("Cadastro de doadores de sangue")
nome = input("Por favor, informe o seu nome completo: ")
peso = float(input("Por favor, informe o seu peso em Kg: "))
altura = int(input("Por favor, informe a sua altura em cm: "))
ano_nascimento = int(input("Por favor, informe seu ano de nascimento"))


idade = 2025 - ano_nascimento
tem_peso_minimo = peso > 50
tem_idade_minima = idade >= 16

texto_saida = f"\tnome: {nome}\n\tPeso: {peso} kg\n\tALTURA: {altura} cm\n\tIDADE:{idade}\n\tTEM PESO MINIMO PARA DOAR: {tem_peso_minimo}\n\t Tem idade minima para doar:  {tem_idade_minima}"

print(texto_saida)

print("termino do projeto")

print("salvando no github")