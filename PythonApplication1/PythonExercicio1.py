print("Digite sua idade")

idade = input()

result = int(idade)

if result <= 5:
        print("NAO PAGA PASSAGEM")
elif result >= 65:
        print("ISENTO DE PAGAMENTO DE PASSAGEM")
else:
        print("PAGAM PASSAGEM")
