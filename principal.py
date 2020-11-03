import contatos_uteis


try:
    # contatos = contatos_uteis.csv_para_contatos('dados/contatos.csv', 'latin_1')
    # contatos_uteis.contatos_para_pickle(contatos, 'dados/contatos.p')

    contatos = contatos_uteis.pickle_para_contatos('dados/contatos.p')

    for i in contatos:
        print(f'{i.id} - {i.nome} - {i.email}')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão')
