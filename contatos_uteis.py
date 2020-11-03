import csv, pickle, json
from contato import Contato


def csv_para_contatos(caminho, encoding):
    contatos = []

    with open(caminho, encoding=encoding) as file:
        leitor = csv.reader(file)

        for i in leitor:
            id = i[0]
            nome = i[1]
            email = i[2]

            # ou id, nome, email = i

            contato = Contato(id, nome, email)
            contatos.append(contato)
    return contatos


def contatos_para_pickle(contatos, caminho):
    with open(caminho, mode='wb') as file:
        pickle.dump(contatos, file)


def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as file:
        contatos = pickle.load(file)

    return contatos


def contatos_para_json(contatos, caminho):
    with open(caminho, mode='w') as file:
        json.dump(contatos, file, default=_contato_para_json)


def _contato_para_json(contato):
    return contato.__dict__


def json_para_contatos(caminho):
    with open(caminho) as file:
        contatos = []

        contatos_json = json.load(file)

        for i in contatos_json:
            contato = Contato(i['id'], i['nome'], i['email'])
            contatos.append(contato)
        return contatos
