interface = """

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair

=> """

saldo_atual = 0
valor_maximo_saque = 500
historico = ""
quantidade_saques = 0
MAX_SAQUES_DIARIOS = 3

while True:
    escolha = input(interface)

    if escolha == "1":
        deposito = float(input("Digite o valor para depósito: "))

        if deposito > 0:
            saldo_atual += deposito
            historico += f"Depósito: R$ {deposito:.2f}\n"
        else:
            print("Erro: valor inválido para depósito.")

    elif escolha == "2":
        saque = float(input("Digite o valor para saque: "))

        saldo_insuficiente = saque > saldo_atual
        limite_excedido = saque > valor_maximo_saque
        saques_excedidos = quantidade_saques >= MAX_SAQUES_DIARIOS

        if saldo_insuficiente:
            print("Erro: saldo insuficiente.")

        elif limite_excedido:
            print("Erro: o valor excede o limite permitido por saque.")

        elif saques_excedidos:
            print("Erro: número de saques diários excedido.")

        elif saque > 0:
            saldo_atual -= saque
            historico += f"Saque: R$ {saque:.2f}\n"
            print(f"\nSaque de R$ {saque:.2f} realizado!")
            print(f"Saldo restante: R$ {saldo_atual:.2f}\n")
            quantidade_saques += 1
        else:
            print("Erro: valor inválido para saque.")

    elif escolha == "3":
        print("\n========= MOVIMENTAÇÕES =========")
        print("Nenhuma movimentação registrada." if not historico else historico)
        print(f"\nSaldo disponível: R$ {saldo_atual:.2f}")
        print("=================================")

    elif escolha == "0":
        print("Sessão encerrada.")
        break

    else:
        print("Opção inválida. Tente novamente.")
