print("boas vindas ao calculador de inteiros")

primeiro_valor = int(input("Por favor, informe o primeiro valor: "))
segundo_valor = int(input("Por favor, informe o segundo valor"))

print(type(primeiro_valor))

soma = primeiro_valor + segundo_valor
subtracao = primeiro_valor - segundo_valor
divisao = primeiro_valor / segundo_valor
multiplicacao = primeiro_valor * segundo_valor

print("O resultado da soma foi: {}".format(soma))

print(f"o resultado da soma foi: {soma}")
print(f"o resultado da subtracao foi: {subtracao}")
print(f"o resultado da divisao foi: {divisao}")
print(f"o resultado da multiplicacao foi: {multiplicacao}")