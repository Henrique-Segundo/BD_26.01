import psycopg2
from LivroGenero import LivroGenero

# Classe DAO da entidade livroGenero
class LivroGeneroDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="livros")

    # Criar um objeto livroGenero a partir da linha de dados
    def criar_livroGenero(self, linha):
        lg = LivroGenero()
        lg.livro_id = linha[0]
        lg.genero_id = linha[1]
        return lg

    # Lista todas os livroGenero
    def listar_todas(self):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT livro_id, genero_id, login, senha FROM livroGenero")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_livroGenero(linha))
        except Exception as erro:
            print(f"Erro ao listar livroGenero: {erro}")
        return resultado

    # Busca um livroGenero pelo id do livro
    def listar(self, livro_id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT livro_id, genero_id FROM livroGenero WHERE livro_id = %s", 
                        (livro_id,)
                    )
                    linha = cursor.fetchone()
                    if linha:
                        return self.criar_livroGenero(linha)
        except Exception as erro:
            print(f"Erro ao buscar livroGenero: {erro}")
        return None

    # Insere uma nova livroGenero
    def inserir(self, livro_id, genero_id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO livroGenero (livro_id, genero_id) VALUES (%s, %s)",
                        (livro_id, genero_id)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao inserir livroGenero: {erro}")
        return False

    # Atualiza uma livroGenero existente
    def atualizar(self, livro_id, genero_id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE livroGenero SET livro_id = %s, genero_id = %s WHERE livro_id = %s",
                        (livro_id, genero_id)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao atualizar livroGenero: {erro}")
        return False

    # Remove uma livroGenero
    def remover(self, livro_id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM livroGenero WHERE livro_id = %s", 
                        (livro_id,)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover livroGenero: {erro}")
        return False