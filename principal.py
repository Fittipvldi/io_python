import contatos_uteis


try:
    contatos = contatos_uteis.csv_para_contatos('dados/contatos.csv', 'latin_1')

    for i in contatos:
        print(f'{i.id} - {i.nome} - {i.email}')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão')
