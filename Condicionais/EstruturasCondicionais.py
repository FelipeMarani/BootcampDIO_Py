# saldo = 2000.0
# saque = float(input("Informe o valor do saque: "))

# if saldo >= saque:
#     print("Saque realizado com sucesso!")
# elif saldo < saque:
#     print("Saldo insuficiente, não será possível realizar o saque!")
saldo = 2000.0
saque = float(input("Informe o valor do saque: "))

if saldo >= saque:
    print("Saque realizado com sucesso!")
else:
    print("Saldo insuficiente, não será possível realizar o saque!")


opc = {"SACAR": 1, "DEPOSITAR": 2, "EXTRATO": 3}
select = str(input("Digite qual função gostaria de executar: ")).upper()
if select in opc :
    if opc == 1:
        valor = float(input("Quanto deseja sacar?: "))
        if valor <= saldo:
            print("As notas estão sendo contadas...Saque liberado com sucesso!")
        else:
            print("Saldo Insuficiente!")
    elif opc == 2:
        valor = float(input("Digite a quantidade que deseja depositar: "))
        saldo += valor
        print("Valor depositado com sucesso")
        print(f"Saldo atual é: {saldo}")
    else:
        print(saldo)