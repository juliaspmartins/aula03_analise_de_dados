salarioBruto = float(input("Salário: ").replace(",","."))
if salarioBruto >= 2000:
    desconto = salarioBruto * 0.11
else:
    desconto = salarioBruto * 0.9
slarioFinal = salarioBruto - desconto
print(f"Salário: {salarioBruto:.2f}")
print(f"Desconto: {desconto:.2f}")
print(f"Salário Final: {salarioFinal:.2f}")
