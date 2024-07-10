name = str(input("Digite seu nome: "))
age = int(input("Digite sua idade: "))
profession = str(input("Digite sua profissão atual: "))
lenguage = str(input("Caso se indendifique como profissional na área de TI, digite sua liinguagem de domínio: "))

if lenguage == None:
    lenguage = "ainda não possuo conhecimento firmes em linguagens de programação, mas estou buscando me aperfeiçoar!"
else:
    lenguage = lenguage

print("Nome: {}, idade: {}".format(name, age))