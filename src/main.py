import os

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

    def executar(self):
        sair = False
        while not sair:
            try:
                self.viewMenu()
            except Exception as e:
                print(e)
    
if __name__ == "__main__":
    main = Main()
    main.executar()
