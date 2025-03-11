from pessoa_fisica import PessoaFisica
from pessoa_juridica import PessoaJuridica

# Importa as classes para utilizar no main:

def main():
    pf1 = PessoaFisica('Guilherme Silva', 'Rua tal 3',888888,  '11/06/2013')
    pf2 = PessoaFisica('Antonio Silva', 'Rua tal 4',999999, '10/10/2005')
    pj1 = PessoaJuridica('Google', 'Rua tal 333',3213123)
    pj2 = PessoaJuridica('Antonio Silva', 'Rua tal 4',423424)
    print("Cliente: %s - Data de nascimeto: %s " % (pf1._nome , pf1._data_nascimento))
    print(pj2._cnpj)


# Compara o nome da classe para executar o método.
if __name__ == "__main__": 
    main()

