name = str(input("Digite seu nome: "))

print(f"Seu nome em maiúsculo: {name.upper()}")
print(f"Seu nome em minúsculo: {name.lower()}")
print(f"Seu nome em Título: {name.title()}")

txt = str(input("Digite um texto ou palavra por favor: "))

print(txt.strip())
print(txt.rstrip())
print(txt.lstrip())

menu = str(input("Digite um conteúdo para o menu: "))

print('###' + menu + '###')
print(menu.center(14))
print(menu.center(14, '#'))
print("-".join(menu))