import psycopg2
from Genero import Genero

# Classe DAO da entidade Genero
class GeneroDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="livros")

    # Criar um objeto Genero a partir da linha de dados
    def criar_genero(self, linha):
        g = Genero()
        g.id = linha[0]
        g.nome = linha[1]
        g.descricao = linha[2]
        return g

    # Lista todos os genero
    def listar_todas(self):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id, nome, descricao FROM Genero")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_genero(linha))
        except Exception as erro:
            print(f"Erro ao listar genero: {erro}")
        return resultado

    # Busca uma Genero pelo id
    def listar(self, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id, nome, descricao FROM Genero WHERE id = %s",
                        (id,)
                    )
                    linha = cursor.fetchone()
                    if linha:
                        return self.criar_genero(linha)
        except Exception as erro:
            print(f"Erro ao buscar Genero: {erro}")
        return None

    # Insere uma nova Genero
    def inserir(self, nome, descricao):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Genero (nome, descricao) VALUES (%s, %s)",
                        (nome, descricao)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao inserir Genero: {erro}")
        return False

    # Atualiza uma Genero existente
    def atualizar(self, nome, descricao, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE Genero SET nome = %s, descricao = %s WHERE id = %s",
                        (nome, descricao, id)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao atualizar Genero: {erro}")
        return False

    # Remove uma Genero
    def remover(self, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM Genero WHERE id = %s", 
                        (id,)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover Genero: {erro}")
        return False