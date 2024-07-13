def calc(numeros):
    return sum(numeros)

def ent_suc(numero):
    sucessor  = numero + 1
    ant = numero -1
    return sucessor, ant

print(calc([15, 3, 7, 98, 45, 7, 665]))
print(ent_suc(int(input("Digite um numero: "))))