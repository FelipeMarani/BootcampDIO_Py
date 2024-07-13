contact = {
        "john.doe@gmai.com"   : {"Name": "John", "Telefone": "55 11 91234-5678"},
        "jane.smith@gmai.com" : {"Name": "Jane", "Telefone": "55 11 92345-6789"},
        "robert.brown@gmai.com" : {"Name": "Robert", "Telefone": "55 11 93456-7890"},
        "emily.jones@gmai.com" : {"Name": "Emily", "Telefone": "55 11 94567-8901"},
}

for chave in contact:
    print(chave, contact[chave])
print("=" * 10)

reserva = contact.copy()


