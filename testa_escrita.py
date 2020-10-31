arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')

contato = '11,Henrique,henrique@henrique.com\n'

arquivo_contatos.write(contato)
