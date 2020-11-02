try:
    with open('dados/contatos.csv', encoding='latin_1') as file:
        for i in file:
            print(i, end='')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão')
