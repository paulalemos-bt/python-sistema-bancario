menu * """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3
  

while true:

    opcao = input(menu)

# não pode depositar valores negativos, tem colocar todos os valores de extrato

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R${valor:.2f}\n"

        else:
            print("Operação falhou! o valor informado é inválido.")

#valores ate 3 saques diários, verificar se tem saldo, e o limite diário é ate 500

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite

        excedeu_saque = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        
        elif excedeu_saque:
            print("Operação falhou! Número maximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

        
       #tem que apresentar todos os valores depositados e sacados

    elif opcao == "e":
        print("\n ################ EXTRATO #################")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("#############################################")

    elif opcao == "q":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada")