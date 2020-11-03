import csv
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
