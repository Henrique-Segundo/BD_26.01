import psycopg2
from Usuario import Usuario

# Classe DAO da entidade usuario
class UsuarioDAO:

    # Conectar-se ao banco de dados
    def conectar(self):
        return psycopg2.connect(user="postgres", password="ufc123", host="localhost", port="5432", database="livros")

    # Criar um objeto usuario a partir da linha de dados
    def criar_usuario(self, linha):
        u = Usuario()
        u.id = linha[0]
        u.nome = linha[1]
        u.descricao = linha[2]
        u.dataNascimento = linha[3]
        return u

    # Lista todas as pessoas
    def listar_todas(self):
        resultado = []
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute("SELECT id, nome, descricao, data_de_nascimento FROM usuario")
                    for linha in cursor.fetchall():
                        resultado.append(self.criar_usuario(linha))
        except Exception as erro:
            print(f"Erro ao listar usuários: {erro}")
        return resultado

    # Busca um usuario pelo id
    def listar(self, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "SELECT id, nome, data_de_nascimento, descricao FROM usuario WHERE id = %s", 
                        (id,)
                    )
                    linha = cursor.fetchone()
                    if linha:
                        return self.criar_usuario(linha)
        except Exception as erro:
            print(f"Erro ao buscar usuário: {erro}")
        return None

    # Insere um novo usuario
    def inserir(self, nome, descricao, data_de_nascimento):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO usuario (nome, descricao, data_de_nascimento) VALUES (%s, %s, %s)",
                        (nome, descricao, data_de_nascimento)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao inserir usuario: {erro}")
        return False

    # Atualiza uma usuario existente
    def atualizar(self, nome, descricao, data_de_nascimento, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "UPDATE usuario SET nome = %s, descricao = %s, data_de_nascimento = %s WHERE id = %s",
                        (nome, descricao, data_de_nascimento, id)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao atualizar usuario: {erro}")
        return False

    # Remove uma usuario
    def remover(self, id):
        try:
            with self.conectar() as connection:
                with connection.cursor() as cursor:
                    cursor.execute(
                        "DELETE FROM usuario WHERE id = %s", 
                        (id,)
                    )
                    return cursor.rowcount == 1
        except Exception as erro:
            print(f"Erro ao remover usuario: {erro}")
        return False