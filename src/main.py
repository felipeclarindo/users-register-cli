import os
from utils.validations import *
from modules.database import *

class Main:
    def __init__(self) -> None:
        self.users = []

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear"())
    
    def viewMenu(self):
        self.clear()
        print("------------------------------")
        print("------ Menu de Cadastro ------")
        print("------------------------------")
        print("1 - Cadastrar usuario")
        print("2 - Atualizar usuario")
        print("3 - Mostrar usuarios")
        print("4 - Pesquisar usuario")
        print("5 - Deletar usuario") 
        print("6 - Sair")

    def loginMenu(self):
        self.clear()
        print("------------------------------")
        print("------ Opções de login -------")
        print("------------------------------")
        print("1 - Email")
        print("2 - Usuario")
        print("3 - Cpf")
        print("4 - Rg")

    def executar(self):
        sair = False
        while not sair:
            try:
                self.viewMenu()
                opcao = str(input("Informe a opção desejada:")).strip()
                match opcao:
                    case "1":
                        logado = False
                        while not logado:
                            self.loginMenu()
                            choice = str(input("Como deseja fazer o login? ")).strip()
                            match choice:
                                case "1":
                                    loginValido = False
                                    while not loginValido:
                                        login = str(input("Informe o email: ")).strip()
                                        loginValido = validarLogin(login, choice)
                                    senhaValida = False
                                    while not senhaValida: 
                                        senha = str(input("Informe a senha: ")).strip()
                                        senhaValida = validarSenha(senha)
                                        print("Usuario cadastrado!")
                                
                                case "2":
                                    loginValido = False
                                    while not loginValido:
                                        login = str(input("Informe o usuario: ")).strip()
                                        loginValido = validarLogin(login, choice)
                                    senhaValida = False
                                    while not senhaValida: 
                                        senha = str(input("Informe a senha: ")).strip()
                                        senhaValida = validarSenha(senha)
                                    print("Usuario cadastrado!")
                                
                                case "3":
                                    loginValido = False
                                    while not loginValido:
                                        login = str(input("Informe o cpf: ")).strip()
                                        loginValido = validarLogin(login, choice)
                                    senhaValida = False
                                    while not senhaValida: 
                                        senha = str(input("Informe a senha: ")).strip()
                                        senhaValida = validarSenha(senha)
                                    print("Usuario cadastrado!")
                                
                                case "4":
                                    loginValido = False
                                    while not loginValido:
                                        login = str(input("Informe o rg: ")).strip()
                                        loginValido = validarLogin(login, choice)
                                    senhaValida = False
                                    while not senhaValida: 
                                        senha = str(input("Informe a senha: ")).strip()
                                        senhaValida = validarSenha(senha)
                                    print("Usuario cadastrado!")
                                
                    case "2":
                        pass
                    case "3":
                        pass
                    case "4":
                        pass
                    case "5":
                        pass
                    case "6":
                        confirmar = str(input("Deseja mesmo sair? Sim/Nao"))
                        sair = True
                    case _:
                        print("Opção invalida!")
            except Exception as e:
                print(e)
    
if __name__ == "__main__":
    main = Main()
    main.executar()
