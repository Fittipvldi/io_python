contato_juliana = '11,Juliana,juliana@juliana.com\n'
contato_raquel = '12,Raquel,raquel@raquel.com\n'

with open('dados/contatos-escrita.csv', encoding='latin_1', mode='w') as file:
    file.write(contato_juliana)

with open('dados/contatos-escrita.csv', encoding='latin_1', mode='a') as file:
    file.write(contato_raquel)
