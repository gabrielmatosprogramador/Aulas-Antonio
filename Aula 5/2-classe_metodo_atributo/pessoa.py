class Pessoa:
    
    def __init__(self, nome, endereco):
        self._nome = nome 
        self._endereco = endereco  

# To Sting
    def __str__(self):
        return f"{self._nome} - {self._endereco}"
    


objeto_pessoa = Pessoa("Gabriel Matos", "Rua 123 4")

print(f"{objeto_pessoa._nome} - {objeto_pessoa._endereco}")