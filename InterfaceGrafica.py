from PessoaDAO import PessoaDAO

# Classe que implementa a interface gráfica da aplicação
class InterfaceGrafica:

    def __init__(self):
        self.pessoa_dao = PessoaDAO()

    # Menu Principal
    def menu_principal(self):
        while True:
            print("==============================")
            print("Cadastro de Pessoas")
            print("==============================")
            print("1 - Cadastro de Pessoas")
            print("0 - Sair")
            print("==============================")
            opcao = input("Digite uma opção: ")
            if opcao == "1":
                self.menu_cadastro_pessoa()
            elif opcao == "0":
                print("Aplicação encerrada")
                break
            else:
                print("Opção inválida")

    # Menu Cadastro Pessoa
    def menu_cadastro_pessoa(self):
        while True:
            print("==============================")
            print("Cadastro de Pessoas")
            print("==============================")
            print("1 - Listar Todas")
            print("2 - Buscar por Código")
            print("3 - Inserir")
            print("4 - Atualizar")
            print("5 - Remover")
            print("0 - Voltar")
            print("==============================")
            opcao = input("Digite uma opção: ")
            if opcao == "1":
                self.listar_todas()
            elif opcao == "2":
                self.buscar()
            elif opcao == "3":
                self.inserir()
            elif opcao == "4":
                self.atualizar()
            elif opcao == "5":
                self.remover()
            elif opcao == "0":
                break
            else:
                print("Opção inválida")

    # Listar todas pessoas
    def listar_todas(self):
        pessoas = self.pessoa_dao.listar_todas()
        if not pessoas:
            print("Nenhum registro encontrado")
            return
        for p in pessoas:
            print(
                f"Código = {p.codigo} | Nome = {p.nome} | Login = {p.login}"
            )

    # Buscar pessoa
    def buscar(self):
        try:
            codigo = int(input("Digite o código: "))
            p = self.pessoa_dao.listar(codigo)
            if p:
                print(
                    f"Código = {p.codigo} | Nome = {p.nome} | Login = {p.login}"
                )
            else:
                print("Pessoa não encontrada.")
        except ValueError:
            print("Código inválido")

    # Inserir pessoa
    def inserir(self):
        nome = input("Nome: ").strip()
        login = input("Login: ").strip()
        senha = input("Senha: ").strip()
        sucesso = self.pessoa_dao.inserir(nome, login, senha)
        print(
            "Registro inserido com sucesso"
            if sucesso
            else "Falha ao inserir registro"
        )

    # Atualizar pessoa
    def atualizar(self):
        try:
            codigo = int(input("Código: "))
            nome = input("Nome: ").strip()
            login = input("Login: ").strip()
            senha = input("Senha: ").strip()
            sucesso = self.pessoa_dao.atualizar(nome, login, senha, codigo)
            print(
                "Registro atualizado com sucesso"
                if sucesso
                else "Falha ao atualizar registro"
            )
        except ValueError:
            print("Código inválido")

    # Remover pessoa
    def remover(self):
        try:
            codigo = int(input("Código: "))
            sucesso = self.pessoa_dao.remover(codigo)
            print(
                "Registro removido com sucesso"
                if sucesso
                else "Falha ao remover registro"
            )
        except ValueError:
            print("Código inválido")

# Inicializa a aplicação
if __name__ == "__main__":
    gui = InterfaceGrafica()
    gui.menu_principal()