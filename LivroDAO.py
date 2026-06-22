import psycopg2
from Livro import Livro

# Classe DAO da entidade livro
class LivroDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="livros")

    # Criar um objeto livro a partir da linha de dados
    def criar_livro(self, linha):
        l = Livro()
        l.id = linha[0]
        l.nome = linha[1]
        l.descricao = linha[2]
        l.data_de_publicacao = linha[3]
        return l

    # Lista todos os livros
    def listar_todas(self):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id, nome, descricao, data_de_publicacao FROM livro")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_livro(linha))
        except Exception as erro:
            print(f"Erro ao listar livros: {erro}")
        return resultado

    # Busca uma livro pelo id
    def listar(self, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id, nome, descricao, data_de_publicacao FROM livro WHERE id = %s", 
                        (id,)
                    )
                    linha = cursor.fetchone()
                    if linha:
                        return self.criar_livro(linha)
        except Exception as erro:
            print(f"Erro ao buscar livro: {erro}")
        return None

    # Insere uma nova livro
    def inserir(self, nome, descricao, data_de_publicacao):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO livro (nome, descricao, data_de_publicacao) VALUES (%s, %s, %s)",
                        (nome, descricao, data_de_publicacao)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao inserir livro: {erro}")
        return False

    # Atualiza um livro existente
    def atualizar(self, nome, descricao, data_de_publicacao, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE livro SET nome = %s, descricao = %s, data_de_publicacao = %s WHERE id = %s",
                        (nome, descricao, data_de_publicacao, id)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao atualizar livro: {erro}")
        return False

    # Remove uma livro
    def remover(self, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM livro WHERE id = %s", 
                        (id,)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover livro: {erro}")
        return False