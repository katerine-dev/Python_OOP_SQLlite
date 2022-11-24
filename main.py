# Importar nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa # mencionar o diretório
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

# Exemplo de uso
witkoski = Pessoa(1, "Katerine Witkoski")
#print(witkoski.nome) # acessando o nome (segundo parâmetro)
print(witkoski)
print("Daqui para frente é acesso ao banco...\n")
# Chama o objeto de banco de dados
db = Database()

# Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

# Quero carregar uma lista com o que veio do benco de dados

pessoas = pessoaDAO.getAll(orderByName=True)
for pessoa in pessoas:
    print(pessoa)

# Criar um objeto com qualquer ator/atriz/diretor
novo_ator = Pessoa(0, "Denzel Washington")
#olha que simples:
novo_ator = pessoaDAO.save(novo_ator)

# Consulta o banco de novo
pessoas = pessoaDAO.getAll(orderByName=True)
for pessoa in pessoas:
    print(pessoa)

#desafios:

#1) consertar meu inserir no banco
#2) faça o atualizar e apagar também!!

#desafio mega zord (ranger verde, RIP) 2.0
#3) faz o model/Filme.py, dao/FilmeDAO.py e coloca em prática!!