import psycopg2
from Livros import Livros

# Classe DAO da entidade livros
class LivrosDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="livros")

    # Criar um objeto livros a partir da linha de dados
    def criar_livro(self, linha):
        l = Livros()
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
                    cursor.execute("SELECT id, nome, descricao, data_de_publicacao FROM livros")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_livro(linha))
        except Exception as erro:
            print(f"Erro ao listar livros: {erro}")
        return resultado

    # Busca uma livros pelo id
    def listar(self, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id, nome, descricao, data_de_publicacao FROM livros WHERE id = %s", 
                        (id,)
                    )
                    linha = cursor.fetchone()
                    if linha:
                        return self.criar_livro(linha)
        except Exception as erro:
            print(f"Erro ao buscar livros: {erro}")
        return None

    # Insere uma nova livros
    def inserir(self, nome, descricao, data_de_publicacao):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO livros (nome, descricao, data_de_publicacao) VALUES (%s, %s, %s)",
                        (nome, descricao, data_de_publicacao)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao inserir livros: {erro}")
        return False

    # Atualiza um livros existente
    def atualizar(self, nome, descricao, data_de_publicacao, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE livros SET nome = %s, descricao = %s, data_de_publicacao = %s WHERE id = %s",
                        (nome, descricao, data_de_publicacao, id)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao atualizar livros: {erro}")
        return False

    # Remove uma livros
    def remover(self, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM livros WHERE id = %s", 
                        (id,)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover livros: {erro}")
        return False