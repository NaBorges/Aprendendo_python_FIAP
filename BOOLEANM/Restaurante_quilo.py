print("Quilão do Reinaldao")

preco_quilo = float(input("Informe o valor cobrado por quilo" ))
peso_prato = float(input("Informe o peso do prato do cliente(em kg)"))

preco_prato = preco_quilo* peso_prato

print(f"O valor do prato é{preco_prato: .2f}")