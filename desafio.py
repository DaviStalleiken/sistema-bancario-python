menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
    
        else:
            print("Operação cancelada deivdo a valor inválido. Tente novamente.")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        saldo_excedido = valor > saldo
        limite_excedido = valor > limite
        saque_excedido = numero_saques >= LIMITE_SAQUES

        if saldo_excedido:
            print("Operação inválida. Não há saldo suficiente.")
        
        elif limite_excedido:
            print("Operação inválida. Seu limite foi ultrapassado.")

        elif saque_excedido:
            print("Operação inválida. O número de saques foi excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação inválida. O valor informado é inválido.") 
    
    elif opcao == "e":
        print("Não foi realizada nenhuma movimentação." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida. Por favor, selecione novamente a opção desejada.")
