saldo = 500


def sacar(valor):
    global saldo
    if saldo >= valor:
        print("Valor sacado")
        print("Retire seu dinheiro na boca do caixa.")
        
    print("Obrigado pela preferência")


def despositar(valor):
    global saldo
    saldo = valor


despositar(50)
sacar(100)