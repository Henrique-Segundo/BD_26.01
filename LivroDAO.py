import psycopg2
from Livro import Livro

# Classe DAO da entidade livro
class livroDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")

    # Criar um objeto livro a partir da linha de dados
    def criar_livro(self, linha):
        l = Livro()
        l.codigo = linha[0]
        l.nome = linha[1]
        l.descricao = linha[2]
        l.dataPublicao = linha[3]
        return l

    # Lista todos os livros
    def listar_todas(self):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT codigo, nome, descricao, dataPublicacao FROM livro")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_livro(linha))
        except Exception as erro:
            print(f"Erro ao listar livros: {erro}")
        return resultado

    # Busca uma livro pelo código
    def listar(self, codigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT codigo, nome, descricao, dataPublicacao FROM livro WHERE codigo = %s", 
                        (codigo,)
                    )
                    linha = cursor.fetchone()
                    if linha:
                        return self.criar_livro(linha)
        except Exception as erro:
            print(f"Erro ao buscar livro: {erro}")
        return None

    # Insere uma nova livro
    def inserir(self, nome, descricao, dataPublicacao):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO livro (nome, descricao, dataPublicacao) VALUES (%s, %s, %s)",
                        (nome, descricao, dataPublicacao)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao inserir livro: {erro}")
        return False

    # Atualiza um livro existente
    def atualizar(self, nome, descricao, dataPublicacao, codigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE livro SET nome = %s, descricao = %s, dataPublicacao = %s WHERE codigo = %s",
                        (nome, descricao, dataPublicacao, codigo)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao atualizar livro: {erro}")
        return False

    # Remove uma livro
    def remover(self, codigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM livro WHERE codigo = %s", 
                        (codigo,)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover livro: {erro}")
        return False