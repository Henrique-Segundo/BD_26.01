import psycopg2
from LivroGenero import LivroGenero

# Classe DAO da entidade livro_genero
class LivroGeneroDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="livros")

    # Criar um objeto livro_genero a partir da linha de dados
    def criar_livroGenero(self, linha):
        lg = LivroGenero()
        lg.livro_id = linha[0]
        lg.genero_id = linha[1]
        return lg

    # Lista todas os livro_genero
    def listar_todas(self):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT livro_id, genero_id FROM livro_genero")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_livroGenero(linha))
        except Exception as erro:
            print(f"Erro ao listar livro_genero: {erro}")
        return resultado

    def listar_por_livro(self, livro_id):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT livro_id, genero_id FROM livro_genero WHERE livro_id = %s", 
                        (livro_id,)
                    )
                    for linha in cursor.fetchall():
                        resultado.append(self.livro_genero(linha))
        except Exception as erro:
            print(f"Erro ao buscar livro_genero: {erro}")
        return resultado

    # Insere uma nova relação livro_genero
    def inserir(self, livro_id, genero_id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO livro_genero (livro_id, genero_id) VALUES (%s, %s)",
                        (livro_id, genero_id)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao inserir livro_genero: {erro}")
        return False

    # Remove uma relação específica (por livro_id e genero_id)
    def remover_por_livro_genero(self, livro_id, genero_id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM livro_genero WHERE livro_id = %s AND genero_id = %s", 
                        (livro_id, genero_id)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover livro_genero: {erro}")
        return False

    # Remove todas as relações de um livro
    def remover_por_livro(self, livro_id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM livro_genero WHERE livro_id = %s", 
                        (livro_id,)
                    )
                    return cursor.rowcount > 0
        except Exception as erro:
            print(f"Erro ao remover livro_genero: {erro}")
        return False