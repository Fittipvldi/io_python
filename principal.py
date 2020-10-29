arquivo_contatos = open('dados/contatos.csv', encoding='latin_1')

conteudo = arquivo_contatos.readlines()

for i in conteudo:
    print(i, end='')
