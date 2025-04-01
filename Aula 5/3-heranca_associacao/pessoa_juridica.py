from pessoa import Pessoa


#Para herdar, importa a classe pessoa e chama a Pessoa. Após passa como parâmetro dentro da classe que estende:
class PessoaJuridica(Pessoa):

    def __init__(self, nome, endereco,  cnpj):
        super().__init__(nome,  endereco)
        self._cnpj = cnpj

    def validar_cnpj(cnpj=None):
        if cnpj is not None:
            return True
        
        return False