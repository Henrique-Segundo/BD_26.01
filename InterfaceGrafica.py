from DiarioDAO import DiarioDAO
from GeneroDAO import GeneroDAO
from LivrosDAO import LivrosDAO
from LivroGeneroDAO import LivroGeneroDAO
from UsuarioDAO import UsuarioDAO

# Classe que implementa a interface gráfica da aplicação
class InterfaceGrafica:

    def __init__(self):
        self.diario_dao = DiarioDAO()
        self.genero_dao = GeneroDAO()
        self.livro_dao = LivrosDAO()
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
            print("4 - Gerir Diarios")
            print("0 - Sair")
            print("==============================")
            opcao = input("Digite uma opção: ")
            if opcao == "1":
                self.menu_cadastro_usuario()
            elif opcao == "2":
                self.menu_cadastro_livro()
            elif opcao == "3":
                self.menu_cadastro_genero()
            elif opcao == "4":
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
            print("2 - Buscar por Id (e ver gêneros)")
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
                resp = input("Deseja listar os gêneros deste livro? (s/n): ")
                if resp.lower() == 's':
                    try:
                        id = int(input("Digite o id do livro novamente: "))
                        self.listar_generos_do_livro(id)
                    except ValueError:
                        print("Id inválido")
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
                self.listar_todos_generos()
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

    # Menu de Diários
    def menu_cadastro_diario(self):
        while True:
            print("==============================")
            print("Gerenciar Diários")
            print("==============================")
            print("1 - Listar todos os diários")
            print("2 - Buscar diários por usuário")
            print("3 - Inserir novo diário")
            print("4 - Atualizar diário")
            print("5 - Remover diário (por usuário)")
            print("0 - Voltar")
            print("==============================")
            opcao = input("Digite uma opção: ")
            if opcao == "1":
                self.listar_todos_diarios()
            elif opcao == "2":
                self.listar_diarios_por_usuario_interativo()
            elif opcao == "3":
                self.inserir_diario()
            elif opcao == "4":
                self.atualizar_diario()
            elif opcao == "5":
                self.remover_diario()
            elif opcao == "0":
                break
            else:
                print("Opção inválida")

    # -------------------- Métodos para Usuário --------------------
    def listar_todos_usuario(self):
        usuarios = self.usuario_dao.listar_todas()
        if not usuarios:
            print("Nenhum registro encontrado")
            return
        for u in usuarios:
            print(
                f"Id = {u.id} | Nome = {u.nome} | Data de nascimento = {u.dataNascimento} | Descrição = {u.descricao}"
            )

    def buscar_usuario(self):
        try:
            id = int(input("Digite o id: "))
            u = self.usuario_dao.listar(id)
            if u:
                print(
                    f"Id = {u.id} | Nome = {u.nome} | Data de nascimento = {u.dataNascimento} | Descrição = {u.descricao}"
                )
            else:
                print("Usuário não encontrado.")
        except ValueError:
            print("Id inválido")

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

    def atualizar_usuario(self):
        try:
            id = int(input("Id: "))
            nome = input("Nome: ").strip()
            descricao = input("Descrição do usuario: ").strip()
            dataNascimento = input("Data de nascimento do usuario: ").strip()
            sucesso = self.usuario_dao.atualizar(nome, descricao, dataNascimento, id)
            print(
                "Registro atualizado com sucesso"
                if sucesso
                else "Falha ao atualizar_usuario registro"
            )
        except ValueError:
            print("Id inválido")

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

    # -------------------- Métodos para Livro --------------------
    def listar_todos_livro(self):
        livros = self.livro_dao.listar_todas()
        if not livros:
            print("Nenhum registro encontrado")
            return
        for l in livros:
            print(
                f"Id = {l.id} | Nome = {l.nome} | Data de publicação = {l.data_de_publicacao} | Descricao = {l.descricao}"
            )

    def buscar_livro(self):
        try:
            id = int(input("Digite o id: "))
            l = self.livro_dao.listar(id)
            if l:
                print(
                    f"Id = {l.id} | Nome = {l.nome} | Data de publicação = {l.data_de_publicacao} | Descriçao = {l.descricao}"
                )
            else:
                print("Livro não encontrado.")
        except ValueError:
            print("Id inválido")

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

    # -------------------- Métodos para Gênero --------------------
    def listar_todos_generos(self):
        generos = self.genero_dao.listar_todas()
        if not generos:
            print("Nenhum registro encontrado")
            return
        for g in generos:
            print(
                f"Id = {g.id} | Nome = {g.nome} | Descrição = {g.descricao}"
            )

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

    def inserir_genero(self):
        nome = input("Nome: ").strip()
        descricao = input("Descrição: ").strip()
        sucesso = self.genero_dao.inserir(nome, descricao)
        print(
            "Registro inserido com sucesso"
            if sucesso
            else "Falha ao inserir registro"
        )

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

    def listar_todas_livro_genero(self):
        livro_genero = self.livroGenero_dao.listar_todas()
        if not livro_genero:
            print("Nenhum registro encontrado")
            return
        for lg in livro_genero:
            g = self.genero_dao.listar(lg.genero_id)
            l = self.livro_dao.listar(lg.livro_id)
            print(
                f"Nome do livro = {l.nome} | Nome do gênero = {g.nome}"
            )

    def listar_generos_do_livro(self, livro_id):
        """Lista todos os gêneros associados a um livro."""
        relacoes = self.livroGenero_dao.listar_por_livro(livro_id)
        if not relacoes:
            print("Este livro não possui gêneros associados.")
        else:
            print(f"Gêneros do livro {livro_id}:")
            for lg in relacoes:
                g = self.genero_dao.listar(lg.genero_id)
                print(f" Nome do gênero = {g.nome}")

    def inserir_livro_genero(self):
        try:
            livro_id = int(input("Id do livro: ").strip())
            genero_id = int(input("Id do genero: ").strip())
            sucesso = self.livroGenero_dao.inserir(livro_id, genero_id)
            print(
                "Registro inserido com sucesso"
                if sucesso
                else "Falha ao inserir registro"
            )
        except ValueError:
            print("IDs devem ser números inteiros.")

    def remover_livro_genero(self):
        try:
            livro_id = int(input("Id do livro: ").strip())
            genero_id = int(input("Id do genero: ").strip())
            sucesso = self.livroGenero_dao.remover_por_livro_genero(livro_id, genero_id)
            print(
                "Registro removido com sucesso"
                if sucesso
                else "Falha ao remover registro"
            )
        except ValueError:
            print("IDs devem ser números inteiros.")

    def listar_todos_diarios(self):
        diarios = self.diario_dao.listar_todas()
        if not diarios:
            print("Nenhum registro encontrado")
            return
        for d in diarios:
            u = self.usuario_dao.listar(d.usuario_id)
            l = self.livro_dao.listar(d.livro_id)
            print(
                f"ID = {u.id} | Usuário = {u.nome} | Livro = {l.nome} | Nota = {d.nota} | Review = {d.review} | Data = {d.data}"
            )

    def listar_diarios_por_usuario_interativo(self):
        try:
            usuario_id = int(input("Digite o id do usuário: "))
            self.listar_diarios_por_usuario(usuario_id)
        except ValueError:
            print("Id inválido")

    def listar_diarios_por_usuario(self, usuario_id):
        diarios = self.diario_dao.listar_por_usuario(usuario_id)
        if not diarios:
            print("Nenhum diário encontrado para este usuário.")
        else:
            print(f"Diários do usuário {usuario_id}:")
            for d in diarios:
                u = self.usuario_dao.listar(d.usuario_id)
                l = self.livro_dao.listar(d.livro_id)
                print(f"Diário de {u.nome}:\n  Livro {l.nome} | Nota {d.nota} | Review {d.review} | Data {d.data}")

    def inserir_diario(self):
        try:
            livro_id = int(input("Id do livro: ").strip())
            usuario_id = int(input("Id do usuário: ").strip())
            nota = input("Nota (0-10): ").strip()
            review = input("Review: ").strip()
            data = input("Data (YYYY-MM-DD): ").strip()
            sucesso = self.diario_dao.inserir(livro_id, usuario_id, nota, review, data)
            print(
                "Registro inserido com sucesso"
                if sucesso
                else "Falha ao inserir registro"
            )
        except ValueError:
            print("IDs devem ser números inteiros.")

    def atualizar_diario(self):
        try:
            usuario_id = int(input("Id do usuário: ").strip())
            livro_id = int(input("ID do livro: ").strip())
            nota = input("Nova nota: ").strip()
            review = input("Novo review: ").strip()
            data = input("Nova data (YYYY-MM-DD): ").strip()
            sucesso = self.diario_dao.atualizar(livro_id, nota, review, data, usuario_id)
            print(
                "Registro atualizado com sucesso"
                if sucesso
                else "Falha ao atualizar registro"
            )
        except ValueError:
            print("IDs devem ser números inteiros.")

    def remover_diario(self):
        try:
            usuario_id = int(input("Id do usuário (para remover o diário): ").strip())
            sucesso = self.diario_dao.remover(usuario_id)
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