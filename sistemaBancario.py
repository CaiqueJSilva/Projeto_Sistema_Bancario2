menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu).strip().lower()


    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R${valor_deposito:.2f}\n"
            print(f"Depósito de R${valor_deposito:.2f} realizado. Saldo atual: R${saldo:.2f}")
        else:
            print("Valor inválido para depósito. O valor deve ser maior que zero.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor do saque: "))
            if valor_saque > 0 and valor_saque <= 500 and saldo >= valor_saque:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque de R${valor_saque:.2f}\n"
                print(f"Saque de R${valor_saque:.2f} realizado. Saldo atual: R${saldo:.2f}")
            elif valor_saque > 500:
                print("Valor inválido para saque. O valor máximo por saque é de R$ 500,00.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Limite de saques diários atingido.")

    elif opcao == "e":
        print("Extrato:")
        print(extrato)
        print(f"Saldo atual: R${saldo:.2f}")

    elif opcao == "q":
        print("Saindo do sistema...  Obrigado por usar os nossos canais de atendimento.")
        break


    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
