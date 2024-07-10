conta = 0
LimiteSaque = 0
RetiradasSaques = 0
ValuesSaques = []
saque = 0
lisDeposito = []
quantDeposito = 0

menu = f"""

        Bem vindo ao nosso sistema!!
        
        Escolha qual das operações deseja realizar:
    
    [1]Deposito
    [2]Saque
    [3]Extrato
    [0]Fechar sistema

"""
print(menu)

while True:
    option = int(input(": "))
    
    if option == 1:
        deposito = float(input("Qual valor deseja depositar?: "))
        if deposito < 0 :
            print("Valor inválido, digite um valor maior que 0")
            continue
        else:
            conta += deposito
            lisDeposito.append(deposito)
            quantDeposito += 1
    elif option == 2:
        while LimiteSaque < 3 and saque <= 500.00:
            quantSaque = float(input("Qual valor deseja sacar?: "))
            if quantSaque > 500.00:
                print("Quantidade inválida, só é permitido saques até R$ 500,00, com limite de três saques diários.")
                continue
            elif quantSaque > conta:
                print("Quantidade indisponível na conta.")
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
                print("Contando as notas... Saque efetuado com sucesso! :)")
                conta -= quantSaque
                ValuesSaques.append(quantSaque)
                saque += quantSaque
                RetiradasSaques += 1
                LimiteSaque += 1
    elif option == 3:
        print("Valor em conta: R$ {}".format(conta))
        print("Quantidade de deposito efetuados: {},  e valores depositados: {}".format(quantDeposito, lisDeposito))
        print("Quantidade de saques realizados: {} e seus respectivos valores: {}".format(RetiradasSaques, ValuesSaques))
    elif option == 0:
        print("Obrigado por usar nosso sistema! :)")
        break
    else:
        print("Operação Inválida, tente novamente")
        continue