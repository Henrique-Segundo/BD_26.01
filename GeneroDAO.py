import psycopg2
from Genero import Genero

# Classe DAO da entidade Genero
class GeneroDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")

    # Criar um objeto Genero a partir da linha de dados
    def criar_genero(self, linha):
        g = Genero()
        g.codigo = linha[0]
        g.nome = linha[1]
        g.descricao = linha[2]
        return g

    # Lista todos os genero
    def listar_todas(self):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT codigo, nome, descricao FROM Genero")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_pessoa(linha))
        except Exception as erro:
            print(f"Erro ao listar genero: {erro}")
        return resultado

    # Busca uma Genero pelo código
    def listar(self, codigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT codigo, nome, descricao, senha FROM Genero WHERE codigo = %s", 
                        (codigo,)
                    )
                    linha = cursor.fetchone()
                    if linha:
                        return self.criar_pessoa(linha)
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
    def atualizar(self, nome, descricao, codigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE Genero SET nome = %s, descricao = %s WHERE codigo = %s",
                        (nome, descricao, codigo)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao atualizar Genero: {erro}")
        return False

    # Remove uma Genero
    def remover(self, codigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM Genero WHERE codigo = %s", 
                        (codigo,)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover Genero: {erro}")
        return False