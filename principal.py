import contatos_uteis


try:
    # contatos = contatos_uteis.csv_para_contatos('dados/contatos.csv', 'latin_1')
    # contatos_uteis.contatos_para_pickle(contatos, 'dados/contatos.p')

    # contatos = contatos_uteis.pickle_para_contatos('dados/contatos.p')

    # contatos_uteis.contatos_para_json(contatos, 'dados/contatos.json')

    contatos = contatos_uteis.json_para_contatos('dados/contatos.json')

    for i in contatos:
        print(f'{i.id} - {i.nome} - {i.email}')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão')
