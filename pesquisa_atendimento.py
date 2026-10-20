
excelente = 0
ruim = 0

for i in range(50):
    print(f"\nEntrevistado {i + 1}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = input("Digite sua opinião: ")

    if opiniao == "1":
        excelente += 1
    elif opiniao == "2":
        print("Opinião: BOM")
    elif opiniao == "3":
        ruim += 1
    else:
        print("Opção inválida")

print("\n=== RESULTADO FINAL ===")
print("Respostas EXCELENTE:", excelente)
print("Respostas RUIM:", ruim)
