import psycopg2
from Diario import Diario

# Classe DAO da entidade Diario
class DiarioDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="cadastro")

    # Criar um objeto Diario a partir da linha de dados
    def criar_diario(self, linha):
        d = Diario()
        d.LivroCodigo = linha[0]
        d.UsuarioCodigo = linha[1]
        d.nota = linha[2]
        d.review = linha[3]
        d.dataVisualizacao = linha[4]
        return d

    # Lista todas as Diario
    def listar_todas(self):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT LivroCodigo, UsuarioCodigo, nota, review, dataVisualizacao FROM Diario")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_pessoa(linha))
        except Exception as erro:
            print(f"Erro ao listar Diario: {erro}")
        return resultado

    # Busca uma Diario pelo código do usuario
    def listar(self, codigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT LivroCodigo, UsuarioCodigo, nota, review, dataVisualizacao FROM Diario WHERE UsuarioCodigo = %s", 
                        (codigo,)
                    )
                    linha = cursor.fetchone()
                    if linha:
                        return self.criar_pessoa(linha)
        except Exception as erro:
            print(f"Erro ao buscar Diario: {erro}")
        return None

    # Insere uma nova Diario
    def inserir(self, LivroCodigo, UsuarioCodigo, nota, review, dataVisualizacao):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Diario (LivroCodigo, UsuarioCodigo, nota, review, dataVisualizacao) VALUES (%s, %s, %s, %s, %s)",
                        (LivroCodigo, UsuarioCodigo, nota, review, dataVisualizacao)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao inserir Diario: {erro}")
        return False

    # Atualiza uma Diario existente
    def atualizar(self, LivroCodigo, nota, review, dataVisualizacao,UsuarioCodigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE Diario SET LivroCodigo = %s, nota = %s, review = %s, dataVisualizacao = %s WHERE UsuarioCodigo = %s",
                        (LivroCodigo, nota, review, dataVisualizacao,UsuarioCodigo)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao atualizar Diario: {erro}")
        return False

    # Remove uma Diario
    def remover(self, UsuarioCodigo):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM Diario WHERE UsuarioCodigo = %s", 
                        (UsuarioCodigo,)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover Diario: {erro}")
        return False