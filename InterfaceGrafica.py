from DiarioDAO import DiarioDAO
from GeneroDAO import GeneroDAO
from LivroDAO import LivroDAO
from LivroGeneroDAO import LivroGeneroDAO
from UsuarioDAO import UsuarioDAO

# Classe que implementa a interface gráfica da aplicação
class InterfaceGrafica:

    def __init__(self):
        self.diario_dao = DiarioDAO()
        self.genero_dao = GeneroDAO()
        self.livro_dao = LivroDAO()
        self.livroGenero_dao = LivroGeneroDAO()
        self.usuario_dao = UsuarioDAO()

    # Menu Principal
    def menu_principal(self):
        while True:
            print("==============================")
            print("Diário de leitura")
            print("==============================")
            print("1 - Cadastro de Usuários")
            print("2 - Cadastro de Livros") 
            print("3 - Cadastro de Gêneros Literarios")
            print("4 - Conectar Livros a gêneros")
            print("5 - Gerir Diarios")
            print("0 - Sair")
            print("==============================")
            opcao = input("Digite uma opção: ")
            if opcao == "1":
                self.menu_cadastro_usuario()
            if opcao == "2":
                self.menu_cadastro_livro()
            if opcao == "3":
                self.menu_cadastro_genero()
            if opcao == "4":
                #self.()
                print("nada")
            if opcao == "5":
                self.menu_cadastro_diario()
            elif opcao == "0":
                print("Aplicação encerrada")
                break
            else:
                print("Opção inválida")

    # Menu Cadastro Usuario
    def menu_cadastro_usuario(self):
        while True:
            print("==============================")
            print("Cadastro de Usuario")
            print("==============================")
            print("1 - Listar Todos")
            print("2 - Buscar por Id")
            print("3 - Inserir")
            print("4 - Atualizar")
            print("5 - Remover")
            print("6 - Adicionar entrada no diário")
            print("7 - Atualizar entrada no diário")
            print("8 - Remover entrada no diário")
            print("0 - Voltar")
            print("==============================")
            opcao = input("Digite uma opção: ")
            if opcao == "1":
                self.listar_todos_usuario()
            elif opcao == "2":
                self.buscar_usuario()
                self.buscar_diario() # TEM QUE CORRIGIR PARA CHAMAR AUTOMATICO DENTRO
            elif opcao == "3":
                self.inserir_usuario()
            elif opcao == "4":
                self.atualizar_usuario()
            elif opcao == "5":
                self.remover_usuario()
            elif opcao == "6":
                self.inserir_diario()
            elif opcao == "7":
                self.atualizar_diario()
            elif opcao == "8":
                self.remover_diario()
            elif opcao == "0":
                break
            else:
                print("Opção inválida")
    
    # Menu Cadastro de Livros
    def menu_cadastro_livro(self):
        while True:
            print("==============================")
            print("Cadastro de livros")
            print("==============================")
            print("1 - Listar Todos")
            print("2 - Buscar por Id")
            print("3 - Inserir")
            print("4 - Atualizar")
            print("5 - Remover")
            print("6 - Listar todas as relações de livro e gênero")
            print("7 - Adicionar relação de livro e gênero")
            print("8 - Remover relação de livro e gênero")
            print("0 - Voltar")
            print("==============================")
            opcao = input("Digite uma opção: ")
            if opcao == "1":
                self.listar_todos_livro()
            elif opcao == "2":
                self.buscar_livro()
                self.buscar_livro_genero() # TEM QUE CORRIGIR PARA CHAMAR AUTOMATICO DENTRO
            elif opcao == "3":
                self.inserir_livro()
            elif opcao == "4":
                self.atualizar_livro()
            elif opcao == "5":
                self.remover_livro()
            elif opcao == "6":
                self.listar_todas_livro_genero()
            elif opcao == "7":
                self.inserir_livro_genero()
            elif opcao == "8":
                self.remover_livro_genero()
            elif opcao == "0":
                break
            else:
                print("Opção inválida")

    # Menu Cadastro de Gêneros
    def menu_cadastro_genero(self):
        while True:
            print("==============================")
            print("Cadastro de Gêneros")
            print("==============================")
            print("1 - Listar Todos")
            print("2 - Buscar por Id")
            print("3 - Inserir")
            print("4 - Atualizar")
            print("5 - Remover")
            print("0 - Voltar")
            print("==============================")
            opcao = input("Digite uma opção: ")
            if opcao == "1":
                self.listar_todas_livro_genero()
            elif opcao == "2":
                self.buscar_genero()
            elif opcao == "3":
                self.inserir_genero()
            elif opcao == "4":
                self.atualizar_genero()
            elif opcao == "5":
                self.remover_genero()
            elif opcao == "0":
                break
            else:
                print("Opção inválida")

    # Listar todos os usuarios
    def listar_todos_usuario(self):
        usuarios = self.usuario_dao.listar_todas()
        if not usuarios:
            print("Nenhum registro encontrado")
            return
        for u in usuarios:
            print(
                f"Id = {u.id} | Nome = {u.nome} | Data de nascimento = {u.dataNascimento} | Descrição = {u.descricao}"
            )

    # Buscar usuario
    def buscar_usuario(self):
        try:
            id = int(input("Digite o id: "))
            u = self.usuario_dao.listar(id)
            if u:
                print(
                    f"Id = {u.id} | Nome = {u.nome} | Data de nascimento = {u.dataNascimento} | Descrição = {u.descricao}"
                )
            else:
                print("Usuário não encontrada.")
        except ValueError:
            print("Id inválido")

    # Inserir usuario
    def inserir_usuario(self):
        nome = input("Nome: ").strip()
        descricao = input("Descrição do usuario: ").strip()
        dataNascimento = input("Data de nascimento do usuario: ").strip()
        sucesso = self.usuario_dao.inserir(nome, descricao, dataNascimento)
        print(
            "Registro inserido com sucesso"
            if sucesso
            else "Falha ao inserir_usuario registro"
        )

    # Atualizar usuario
    def atualizar_usuario(self):
        try:
            id = int(input("Id: "))
            nome = input("Nome: ").strip()
            descricao = input("Descrição do usuario: ").strip()
            dataNascimento = input("Data de nascimento do usuario: ").strip()
            sucesso = self.usuario_dao.inserir(nome, descricao, dataNascimento, id)
            print(
                "Registro atualizado com sucesso"
                if sucesso
                else "Falha ao atualizar_usuario registro"
            )
        except ValueError:
            print("Id inválido")

    # Remover usuario
    def remover_usuario(self):
        try:
            id = int(input("Id: "))
            sucesso = self.usuario_dao.remover(id)
            print(
                "Registro removido com sucesso"
                if sucesso
                else "Falha ao remover_usuario registro"
            )
        except ValueError:
            print("Id inválido")

    # Listar todos livros
    def listar_todos_livro(self):
        livros = self.livro_dao.listar_todas()
        if not livros:
            print("Nenhum registro encontrado")
            return
        for l in livros:
            print(
                f"Id = {l.id} | Nome = {l.nome} | Data de publicação = {l.dataPublicacao} | Descricao = {l.descricao}"
            )

    # Buscar livro
    def buscar_livro(self):
        try:
            id = int(input("Digite o id: "))
            l = self.livro_dao.listar(id)
            if l:
                print(
                    f"Id = {l.id} | Nome = {l.nome} | Data de publicação = {l.dataPublicacao} | Descriçao = {l.descricao}"
                )
            else:
                print("Livro não encontrado.")
        except ValueError:
            print("Id inválido")

    # Inserir livro
    def inserir_livro(self):
        nome = input("Nome: ").strip()
        descricao = input("Descrição: ").strip()
        dataPublicacao = input("Data de publicação: ").strip()
        sucesso = self.livro_dao.inserir(nome, descricao, dataPublicacao)
        print(
            "Registro inserido com sucesso"
            if sucesso
            else "Falha ao inserir registro"
        )

    # Atualizar livro
    def atualizar_livro(self):
        try:
            id = int(input("Id: "))
            nome = input("Nome: ").strip()
            descricao = input("Descrição: ").strip()
            dataPublicacao = input("Data de publicação: ").strip()
            sucesso = self.livro_dao.atualizar(nome, descricao, dataPublicacao, id)
            print(
                "Registro atualizado com sucesso"
                if sucesso
                else "Falha ao atualizar registro"
            )
        except ValueError:
            print("Id inválido")

    # Remover livro
    def remover_livro(self):
        try:
            id = int(input("Id: "))
            sucesso = self.livro_dao.remover(id)
            print(
                "Registro removido com sucesso"
                if sucesso
                else "Falha ao remover registro"
            )
        except ValueError:
            print("Id inválido")

    # Listar todos os generos
    def listar_todos_generos(self):
        genero = self.genero_dao.listar_todas()
        if not genero:
            print("Nenhum registro encontrado")
            return
        for g in genero:
            print(
                f"Id = {g.id} | Nome = {g.nome} | Descrição = {g.descricao}"
            )

    # Buscar genero
    def buscar_genero(self):
        try:
            id = int(input("Digite o id: "))
            g = self.genero_dao.listar(id)
            if g:
                print(
                    f"Id = {g.id} | Nome = {g.nome} | Descrição = {g.descricao}"
                )
            else:
                print("Genero não encontrado.")
        except ValueError:
            print("Id inválido")

    # Inserir genero
    def inserir_genero(self):
        nome = input("Nome: ").strip()
        descricao = input("Descrição: ").strip()
        sucesso = self.genero_dao.inserir(nome, descricao)
        print(
            "Registro inserido com sucesso"
            if sucesso
            else "Falha ao inserir registro"
        )

    # Atualizar genero
    def atualizar_genero(self):
        try:
            id = int(input("Id: "))
            nome = input("Nome: ").strip()
            descricao = input("Descrição: ").strip()
            sucesso = self.genero_dao.atualizar(nome, descricao, id)
            print(
                "Registro atualizado com sucesso"
                if sucesso
                else "Falha ao atualizar registro"
            )
        except ValueError:
            print("Id inválido")

    # Remover genero
    def remover_genero(self):
        try:
            id = int(input("Id: "))
            sucesso = self.genero_dao.remover(id)
            print(
                "Registro removido com sucesso"
                if sucesso
                else "Falha ao remover registro"
            )
        except ValueError:
            print("Id inválido")

    # Listar todas as relações livro genero
    def listar_todas_livro_genero(self):
        livro_genero = self.livroGenero_dao.listar_todas()
        if not livro_genero:
            print("Nenhum registro encontrado")
            return
        for lg in livro_genero:
            print(
                f"Id do livro = {lg.livroId} | Id do gênero = {lg.generoId}"
            )

    # Buscar livro genero
    def buscar_livro_genero(self):
        try:
            idL = int(input("Digite o id: "))
            lg = self.livroGenero_dao.listar(idL)
            if lg: # ISSO DEVE ESTAR RETORNANDO SO O PRIMEIRO GENERO
                print(
                    f"Id do livro = {lg.livroId} | Id do gênero = {lg.generoId}"
                )
            else:
                print("Livro não encontrado.")
        except ValueError:
            print("Id inválido")

    # Inserir livro genero
    def inserir_livro_genero(self):
        livroId = input("Id do livro: ").strip()
        generoId = input("Id do genero: ").strip()
        sucesso = self.livroGenero_dao.inserir(livroId, generoId)
        print(
            "Registro inserido com sucesso"
            if sucesso
            else "Falha ao inserir registro"
        )

    # Remover livro genero
    def remover_livro_genero(self):
        try:
            id = int(input("Id: ")) # ISSO NÃO FUNCIONA
            sucesso = self.livroGenero_dao.remover(id)
            print(
                "Registro removido com sucesso"
                if sucesso
                else "Falha ao remover registro"
            )
        except ValueError:
            print("Id inválido")



# Inicializa a aplicação
if __name__ == "__main__":
    gui = InterfaceGrafica()
    gui.menu_principal()