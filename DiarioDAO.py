import psycopg2
from Diario import Diario

# Classe DAO da entidade Diario
class DiarioDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="livros")

    # Criar um objeto Diario a partir da linha de dados
    def criar_diario(self, linha):
        d = Diario()
        d.livro_id = linha[0]
        d.usuario_id = linha[1]
        d.nota = linha[2]
        d.review = linha[3]
        d.data = linha[4]
        return d

    # Lista todas as Diario
    def listar_todas(self):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT livro_id, usuario_id, nota, review, data FROM Diario")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_diario(linha))
        except Exception as erro:
            print(f"Erro ao listar Diario: {erro}")
        return resultado

    # Busca todos os diários de um usuário (retorna lista)
    def listar_por_usuario(self, usuario_id):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT livro_id, usuario_id, nota, review, data FROM Diario WHERE usuario_id = %s", 
                        (usuario_id,)
                    )
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_diario(linha))
        except Exception as erro:
            print(f"Erro ao buscar Diario: {erro}")
        return resultado

    # Insere uma nova Diario
    def inserir(self, livro_id, usuario_id, nota, review, data):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO Diario (livro_id, usuario_id, nota, review, data) VALUES (%s, %s, %s, %s, %s)",
                        (livro_id, usuario_id, nota, review, data)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao inserir Diario: {erro}")
        return False

    # Atualiza uma Diario existente (identificado pelo usuario_id)
    def atualizar(self, livro_id, nota, review, data, usuario_id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE Diario SET livro_id = %s, nota = %s, review = %s, data = %s WHERE usuario_id = %s",
                        (livro_id, nota, review, data, usuario_id)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao atualizar Diario: {erro}")
        return False

    # Remove uma Diario (por usuario_id)
    def remover(self, usuario_id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM Diario WHERE usuario_id = %s", 
                        (usuario_id,)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover Diario: {erro}")
        return False