def menu():
    menu = f"""

        Bem vindo ao nosso sistema!!
        
        Escolha qual das operações deseja realizar:
    
    [1]Deposito
    [2]Saque
    [3]Extrato
    [0]Fechar sistema
    """

def sacar(*, sacar, valueSaques, quantSaque, saldo, Saldo, retiradaSaque, limiteSaque):
    LimiteSaque = 0
    while LimiteSaque < 3 and Saque <= 500.00:
            QuantSaque = float(input("Qual valor deseja sacar?: "))
            QuantSaque = round(QuantSaque,2)
            if quantSaque > 500.00:
                print("Quantidade inválida, só é permitido saques até R$ 500,00, com limite de três saques diários.")
                continue
            elif quantSaque > saldo:
                print("Quantidade indisponível na saldo.")
                option = None
                while option == None:
                    option = int(input("Deseja continuar[1] ou encerrar a seção[0]"))
                    if option == 1:
                        continue
                    elif option == 0:
                        print("Obrigado por usar nosso sistema!")
                        break
            elif quantSaque < 0:
                print("Não é possível sacar valores negativos.")
                continue
            else:
                print("saldondo as notas... Saque no valor de R$ {} efetuado com sucesso! :)".format(quantSaque))
                Saldo -= quantSaque
                ValuesSaques.append("R$"+ str(quantSaque))
                Saque += quantSaque
                RetiradasSaques += 1
                LimiteSaque += 1
    return sacar, valueSaques

def depositar(deposito, saldo, extrato, lisdeposito, /):
        if deposito < 0 :
            print("Valor inválido, digite um valor maior que 0")
        else:
            saldo += deposito
            LisDeposito.append("R$ " + str(deposito))
            quantDeposito += 1
        return saldo, extrato

def extrato(saldo, /, *, extrato):
            
     print("Valor em saldo: R$ {:.2f}".format(saldo))
     print("Quantidade de deposito efetuados: {},  e valores depositados: {}".format(quantDeposito, lisDeposito))
     print("Quantidade de saques realizados: {} e seus respectivos valores: {}".format(RetiradasSaques, ValuesSaques))

def main():
    saldo = 0
    RetiradasSaques = 0
    ValuesSaques = []
    saque = 0
    lisDeposito = []
    quantDeposito = 0
    Agencia = 00001
    
    while True:
        option = menu()
        
        if option == 1:
            deposito = float(input("Qual valor deseja depositar?: "))
            deposito = round(deposito)
            saldo, extrato, lisdeposito = depositar(deposito, saldo, extrato, lisDeposito)