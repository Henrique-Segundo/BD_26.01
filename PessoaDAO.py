import psycopg2
from Pessoa import Pessoa

# Classe DAO da entidade pessoa
class PessoaDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")

    # Criar um objeto pessoa a partir da linha de dados
    def criar_pessoa(self, linha):
        p = Pessoa()
        p.codigo = linha[0]
        p.nome = linha[1]
        p.login = linha[2]
        p.senha = linha[3]
        return p

    # Lista todas as pessoas
    def listar_todas(self):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT codigo, nome, login, senha FROM pessoa")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_pessoa(linha))
        except Exception as erro:
            print(f"Erro ao listar pessoas: {erro}")
        return resultado

    # Busca uma pessoa pelo código
    def listar(self, codigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT codigo, nome, login, senha FROM pessoa WHERE codigo = %s", 
                        (codigo,)
                    )
                    linha = cursor.fetchone()
                    if linha:
                        return self.criar_pessoa(linha)
        except Exception as erro:
            print(f"Erro ao buscar pessoa: {erro}")
        return None

    # Insere uma nova pessoa
    def inserir(self, nome, login, senha):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO pessoa (nome, login, senha) VALUES (%s, %s, %s)",
                        (nome, login, senha)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao inserir pessoa: {erro}")
        return False

    # Atualiza uma pessoa existente
    def atualizar(self, nome, login, senha, codigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE pessoa SET nome = %s, login = %s, senha = %s WHERE codigo = %s",
                        (nome, login, senha, codigo)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao atualizar pessoa: {erro}")
        return False

    # Remove uma pessoa
    def remover(self, codigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM pessoa WHERE codigo = %s", 
                        (codigo,)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover pessoa: {erro}")
        return False