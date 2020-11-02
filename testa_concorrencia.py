arquivo1 = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')
arquivo2 = open('dados/contatos-escrita.csv', encoding='latin_1', mode='w')

contato_juliana = '11,Juliana,juliana@juliana.com\n'
contato_raquel = '12,Raquel,raquel@raquel.com\n'

arquivo1.write(contato_juliana)
arquivo2.write(contato_raquel)

arquivo1.close()
arquivo2.close()
