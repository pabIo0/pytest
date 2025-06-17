from adaptado_sis_banc import deposito, saque, extrato, sair

def test_deposito_valido():
    saldo = 0
    historico = []
    novo_saldo, novo_historico, mensagem = deposito(saldo, historico, 100)
    assert novo_saldo == 100
    assert "Depósito: R$ 100.00" in novo_historico
    assert mensagem == "Depósito realizado!"

def test_deposito_invalido():
    saldo = 0
    historico = []
    novo_saldo, novo_historico, mensagem = deposito(saldo, historico, -10)
    assert novo_saldo == 0
    assert len(novo_historico) == 0
    assert mensagem == "Erro: valor inválido para depósito."

def test_saque_valido():
    saldo = 200
    historico = []
    quantidade_saques = 0
    novo_saldo, novo_historico, novo_quantidade, mensagem = (
    saque(saldo, historico, 100, quantidade_saques, 3, 500)
    )
    assert novo_saldo == 100
    assert "Saque: R$ 100.00" in novo_historico
    assert novo_quantidade == 1
    assert mensagem == "Saque realizado!"

def test_saque_saldo_insuficiente():
    saldo = 50
    historico = []
    quantidade_saques = 0
    novo_saldo, novo_historico, novo_quantidade, mensagem = (
    saque(saldo, historico, 100, quantidade_saques, 3, 500)
    )
    assert novo_saldo == 50
    assert len(novo_historico) == 0
    assert novo_quantidade == 0
    assert mensagem == "Erro: saldo insuficiente."

def test_saque_limite_excedido():
    saldo = 1000
    historico = []
    quantidade_saques = 0
    novo_saldo, novo_historico, novo_quantidade, mensagem = (
        saque(saldo, historico, 600, quantidade_saques, 3, 500)
    )
    assert novo_saldo == 1000
    assert len(novo_historico) == 0
    assert novo_quantidade == 0
    assert mensagem == "Erro: o valor excede o limite permitido por saque."

def test_saque_numero_maximo_excedido():
    saldo = 1000
    historico = []
    quantidade_saques = 3
    novo_saldo, novo_historico, novo_quantidade, mensagem = (
    saque(saldo, historico, 100, quantidade_saques, 3, 500)
    )
    assert novo_saldo == 1000
    assert len(novo_historico) == 0
    assert novo_quantidade == 3
    assert mensagem == "Erro: número de saques diários excedido."

def test_extrato_sem_movimentacoes():
    saldo = 0
    historico = []
    resultado = extrato(saldo, historico)
    assert "Nenhuma movimentação registrada." in resultado
    assert "Saldo disponível: R$ 0.00" in resultado

def test_extrato_com_movimentacoes():
    saldo = 150
    historico = ["Depósito: R$ 100.00", "Depósito: R$ 50.00"]
    resultado = extrato(saldo, historico)
    assert "Depósito: R$ 100.00" in resultado
    assert "Depósito: R$ 50.00" in resultado
    assert "Saldo disponível: R$ 150.00" in resultado

def test_sair():
    valor = ""

    if valor != "0":
        assert sair(valor) is False
    else:
        assert sair(valor) is True