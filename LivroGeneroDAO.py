import psycopg2
from LivroGenero import LivroGenero

# Classe DAO da entidade livroGenero
class LivroGeneroDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")

    # Criar um objeto livroGenero a partir da linha de dados
    def criar_livroGenero(self, linha):
        lg = LivroGenero()
        lg.livroCodigo = linha[0]
        lg.generoCodigo = linha[1]
        return lg

    # Lista todas os livroGenero
    def listar_todas(self):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT livroCodigo, generoCodigo, login, senha FROM livroGenero")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_livroGenero(linha))
        except Exception as erro:
            print(f"Erro ao listar livroGenero: {erro}")
        return resultado

    # Busca um livroGenero pelo código do livro
    def listar(self, livroCodigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT livroCodigo, generoCodigo FROM livroGenero WHERE livroCodigo = %s", 
                        (livroCodigo,)
                    )
                    linha = cursor.fetchone()
                    if linha:
                        return self.criar_livroGenero(linha)
        except Exception as erro:
            print(f"Erro ao buscar livroGenero: {erro}")
        return None

    # Insere uma nova livroGenero
    def inserir(self, livroCodigo, generoCodigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO livroGenero (livrocodigo, generoCodigo) VALUES (%s, %s)",
                        (livroCodigo, generoCodigo)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao inserir livroGenero: {erro}")
        return False

    # Atualiza uma livroGenero existente
    def atualizar(self, livroCodigo, generoCodigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE livroGenero SET livroCodigo = %s, generoCodigo = %s WHERE livroCodigo = %s",
                        (livroCodigo, generoCodigo)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao atualizar livroGenero: {erro}")
        return False

    # Remove uma livroGenero
    def remover(self, livroCodigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM livroGenero WHERE livroCodigo = %s", 
                        (livroCodigo,)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover livroGenero: {erro}")
        return False