texto = "Este texto quebra de linha  aqui.\n \tPorem aqui temos uma tabulação"
print(texto )

texto = "texto em minuscula AINDA é texto "
print(texto.capitalize())

print(texto.upper())
print(texto.lower())

print(texto.startswith("Tex"))
print(texto.endswith(" "))


print(texto.count("t"))
print("em" in texto)

print(texto.replace("AINDA" , "com certeza"))