class Pessoa: # início da classe - "projeto" para criar objetos
    # Atributos
    id = None
    nome = None

    # Método Construtor
    def __init__(self, id, nome): # parâmetros
        self.id = id
        self.nome = nome
    # Método para ajudar na exibição
    def __str__(self):
        return (f"{self.nome} ({ self.id})")



# self parâmetro é uma referência à instância atual da classe e é usado
# para acessar as variávei pertencentes à classe.
