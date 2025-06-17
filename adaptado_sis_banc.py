def deposito(saldo, historico, valor):
    if valor > 0:
        saldo += valor
        historico.append(f"Depósito: R$ {valor:.2f}")
        return saldo, historico, "Depósito realizado!"
    else:
        return saldo, historico, "Erro: valor inválido para depósito."

def saque(saldo, historico, valor, quantidade_saques, max_saques, limite_saque):
    if valor > saldo:
        return saldo, historico, quantidade_saques, "Erro: saldo insuficiente."
    elif valor > limite_saque:
        return saldo, historico, quantidade_saques, "Erro: o valor excede o limite permitido por saque."
    elif quantidade_saques >= max_saques:
        return saldo, historico, quantidade_saques, "Erro: número de saques diários excedido."
    elif valor > 0:
        saldo -= valor
        historico.append(f"Saque: R$ {valor:.2f}")
        quantidade_saques += 1
        return saldo, historico, quantidade_saques, "Saque realizado!"
    else:
        return saldo, historico, quantidade_saques, "Erro: valor inválido para saque."

def extrato(saldo, historico):
    if not historico:
        extrato = "Nenhuma movimentação registrada."
    else:
        extrato = "\n".join(historico)
    
    saldo_formatado = f"\nSaldo disponível: R$ {saldo:.2f}"
    return extrato + saldo_formatado

def sair(escolha):
    return escolha == "0"