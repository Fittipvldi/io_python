arquivo_contatos = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w+')

contatos = ['11,Henrique,henrique@henrique.com\n'
           '12,Guilherme,guilherme@guilherme.com\n']

for i in contatos:
    arquivo_contatos.write(i)

arquivo_contatos.flush()

arquivo_contatos.seek(0)
arquivo_contatos.write('11,Henrique,henrique@henrique.com\n'.upper())
arquivo_contatos.flush()
arquivo_contatos.seek(0)

for i in arquivo_contatos:
    print(i)
