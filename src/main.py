import os
from time import sleep
from utils.validations import *
from modules.database import *

class Main:
    def __init__(self) -> None:
        self.logado = False
        self.database:list[tuple] = [
            ("felipe", "usuario", "fglpc2@gmail.com", "Felipe", None, "013025086123", "13/02/2006", "123", "Rua luis porrio, 415", "admin")
            # Posições
            #login                     ->  0
            #tipo-login                ->  1
            #email                     ->  2
            #nome                      ->  3
            #cpf                       ->  5
            #rg                        ->  4
            #data-nascimento           ->  6
            #senha                     ->  7
            #endereco                  ->  8
            #role(admin or user)       ->  9
        ]

    def clear(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
    
    def viewMenu(self) -> None:
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

    def loginMenu(self) -> None:
        self.clear()
        print("------------------------------")
        print("------ Opções de login -------")
        print("------------------------------")
        print("1 - Email")
        print("2 - Usuario")
        print("3 - Cpf")
        print("4 - Rg")

    def bannerCadastro(self) -> None:
        self.clear()
        print("-------------------------------")
        print("---------- Cadastro -----------")
        print("-------------------------------")

    def bannerInformacoesBusca(self) -> None:
        self.clear()
        print("-------------------------------")
        print("---- Informações de busca -----")
        print("-------------------------------")

    def bannerUsuarios(self) -> None:
        self.clear()
        print("------------------------------")
        print("--------- Usuarios -----------")
        print("------------------------------")

    def bannerDeletarUsuarios(self) -> None:
        self.clear()
        print("------------------------------")
        print("------ Deletar Usuarios ------")
        print("------------------------------")

    def bannerAtualizando(self) -> None:
        self.clear()
        print("-------------------------------")
        print("---- Atualizando Usuario -----")
        print("-------------------------------")

    def bannerLogin(self) -> None:
        self.clear()
        print("--------------------------------")
        print("------------ Login -------------")
        print("--------------------------------")

    def bannerBusca(self) -> None:
        self.clear()
        print("--------------------------------")
        print("-------- Buscar Usuario --------")
        print("--------------------------------")

    def bannerSaida(self) -> None:
        self.clear()
        print("----------------------------------")
        print("-------- Verificar Saida ---------")
        print("----------------------------------")
        
    def fazerLogin(self) -> None:
        while not self.logado:
            self.bannerLogin()
            usuario = str(input("login: "))
            senha = str(input("senha: "))
            senha = protegerSenha(senha)
            self.bannerLogin()
            print("Verificando...")
            sleep(1)
            self.bannerLogin()
            self.logado = validateUser(self.database, usuario, senha)
            if not self.logado:
                print("login ou senha invalidos!")
                input("APERTE ENTER PARA CONTINUAR")
        self.usuarioLogado = usuario
        self.bannerLogin()
        print("Logando...")
        sleep(1)
        self.bannerLogin()
        print("Usuario logado com sucesso!")
        input("APERTE ENTER PARA CONTINUAR")

    def _atualizarUsuario(self, usuario, indice_campos:list[str]) -> None:
        try:
            indiceUser = pegarIndiceDoUsuario(self.database, usuario)
            for user in self.database:
                if user[0] == usuario:
                    for indice in indice_campos:
                        match indice:
                            case "0" | "1":
                                if indice == "0":
                                    indice_campos.remove("1")
                                else:
                                    indice_campos.remove("0")
                                self.bannerAtualizando()
                                print("Se você selecionou campo de usuário ou o tipo do usuario, \nvocê terá que alterar ambos.")
                                input("APERTE ENTER PARA CONTINUAR")
                                loginEscolhido = False
                                while not loginEscolhido:
                                    self.loginMenu()
                                    choice = str(input("Qual o novo login do usuario? ")).strip()
                                    match choice:
                                        case "1":
                                            loginValido = False
                                            while not loginValido:
                                                self.bannerAtualizando()
                                                login = str(input("Informe o email: ")).strip()
                                                loginValido = validarLogin(login, choice)
                                                tipoLogin = "email"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True

                                        case "2":
                                            loginValido = False
                                            while not loginValido:
                                                self.bannerAtualizando()
                                                login = str(input("Informe o usuario: ")).strip()
                                                loginValido = validarLogin(login, choice)
                                                tipoLogin = "usuario"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True
                                        
                                        case "3":
                                            loginValido = False
                                            while not loginValido:
                                                self.bannerAtualizando()
                                                login = str(input("Informe o cpf: ")).strip()
                                                loginValido = validarLogin(login, choice)
                                                tipoLogin = "cpf"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True
                                        
                                        case "4":
                                            self.bannerAtualizando()
                                            loginValido = False
                                            while not loginValido:
                                                self.bannerAtualizando()
                                                login = str(input("Informe o rg: ")).strip()
                                                loginValido = validarLogin(login, choice)
                                                tipoLogin = "rg"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True

                                        case _:
                                            print("Opção Invalida")
                                            input("APERTE ENTER PARA CONTINUAR")
                                self.bannerAtualizando()
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando()
                                print("Login atualizado com sucesso!")
                                self.database[indiceUser] = (login, tipoLogin, user[2], user[3], user[4], user[5], user[6], user[7], user[8], user[9])

                            case "2":
                                emailValido = False
                                while not emailValido:
                                    self.bannerAtualizando()
                                    email = input("Informe o novo email:").strip()
                                    emailValido = validarEmail(email)
                                    if not emailValido:
                                        input("APERTE ENTER PARA CONTINUAR")
                                self.database[indiceUser] = (user[0], user[1], email, user[3], user[4], user[5], user[6], user[7], user[8], user[9])
                                self.bannerAtualizando()
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando()
                                print("Email atualizado com sucesso!")
                                input("APERTE ENTER PARA CONTINUAR")

                            case "3":
                                nomeValido = False
                                while not nomeValido:
                                    self.bannerAtualizando()
                                    nome = str(input("Informe o novo nome:")).strip()
                                    nomeValido = validarNome(nome)
                                    if not nomeValido:
                                        input("APERTE ENTER PARA CONTINUAR")
                                self.database[indiceUser] = (user[0], user[1], user[2], nome, user[4], user[5], user[6], user[7], user[8], user[9])
                                self.bannerAtualizando()
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando()
                                print("Nome atualizado com sucesso!")
                                input("APERTE ENTER PARA CONTINUAR")

                            case "4" | "5":
                                documentoValido = False
                                while not documentoValido:
                                    self.bannerAtualizando()
                                    match indice:
                                        case "4":
                                            cpfValido = False
                                            while not cpfValido:
                                                cpf = str(input("Informe o novo CPF do usuario: ")).strip()
                                                cpfValido = validarCpf(cpf)
                                                if not cpfValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            documentoValido = True
                                        case "5":
                                            rgValido = False
                                            while not rgValido:
                                                self.bannerAtualizando()
                                                rg = str(input("Informe o novo RG do usuario: ")).strip()
                                                rgValido = validarRg(rg)
                                                if not rgValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            documentoValido = True
                                if indice == "4":
                                    self.database[indiceUser] = (user[0], user[1], user[2], user[3], cpf, None, user[6], user[7], user[8], user[9])
                                    self.bannerAtualizando()
                                    print("Atualizando...")
                                    sleep(1)
                                    self.bannerAtualizando()
                                    print("CPF atualizado com sucesso")
                                    input("APERTE ENTER PARA CONTINUAR")
                                else: 
                                    self.database[indiceUser] = (user[0], user[1], user[2], user[3], None, rg, user[6], user[7], user[8], user[9])
                                    self.bannerAtualizando()
                                    print("Atualizando...")
                                    sleep(1)
                                    self.bannerAtualizando()
                                    print("RG atualizado com sucesso!")
                                    input("APERTE ENTER PARA CONTINUAR")                            

                            case "6":
                                dataValida = False
                                while not dataValida:
                                    self.bannerAtualizando()
                                    data = str(input("Informe a data de nascimento do usuario: ")).strip()
                                    dataValida = validarData(data)
                                    if not dataValida:
                                        input("APERTE ENTER PARA CONTINUAR")
                                self.database[indiceUser] = (user[0], user[1], user[2], user[3], user[4], user[5], data, user[7], user[8], user[9])
                                self.bannerAtualizando()
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando()
                                print("Data atualizada com sucesso!")
                                input("APERTE ENTER PARA CONTINUAR")
                            
                            case "7":
                                for user in self.database:
                                    permitido = False
                                    while not permitido:
                                        if usuario != self.usuarioLogado:
                                            permitido = verificarPermissão(self.database, self.usuarioLogado)
                                            if not permitido:
                                                raise Exception("Você so tem permição de alterar a senha do seu usuario!")
                                        elif user[0] == usuario:
                                            permitido = True
                                        else:
                                            raise Exception("Usuario não encontrado!")
                                    senhaValida = False
                                    while not senhaValida:
                                        senha = str(input("Informe a nova senha:")).strip()
                                        senhaValida = validarSenha(senha)
                                        if not senhaValida:
                                            input("APERTE ENTER PARA CONTINUAR")
                                    self.database[indiceUser] = (user[0], user[1], user[2], user[3], user[4], user[5], user[6], senha, user[8], user[9])
                                    senha = protegerSenha(senha)
                                    self.bannerAtualizando()
                                    print("Atualizando...")
                                    sleep(1)
                                    self.bannerAtualizando()
                                    print("Senha atualizada com sucesso!")
                                    input("APERTE ENTER PARA CONTINUAR")
                            case "8":
                                enderecoValido = False
                                while not enderecoValido:
                                    endereco = str(input("Informe o novo endereço: ")).strip()
                                    enderecoValido = validarEndereco(endereco)
                                    if not enderecoValido:
                                        input("APERTE ENTER PARA CONTINUAR")
                                self.database[indiceUser] = (user[0], user[1], user[2], user[3], user[4], user[5], user[6], senha, endereco, user[9])
                                self.bannerAtualizando()
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando
                                print("Endereco atualizado com sucesso")
                                input("APERTE ENTER PARA CONTINUAR")

                            case "9":
                                permitido = False
                                while not permitido:
                                    for user in self.database:
                                        if usuario != self.usuarioLogado:
                                            permitidoUserLogado = verificarPermissão(self.usuarioLogado)
                                            permitidoUserEditado = verificarPermissão(usuario)
                                            if not permitidoUserLogado and permitidoUserEditado:
                                                permitido = True
                                            else:
                                                raise Exception("Usuario não tem permição para alterar a role do usuario desejado")
                                        else:
                                            raise Exception("Você não pode mudar suas proprias permições")
                                roleValida = False
                                while not roleValida:
                                    role = input("Digite a nova role do usuario")
                                    roleValida = validarRole(role)
                                    if not roleValida:
                                        input("APERTE ENTER PARA CONTINUAR")
                                self.database[indiceUser] = (user[0], user[1], user[2], user[3], user[4], user[5], user[6], user[7], user[8], role)
                                self.bannerAtualizando()
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando()
                                print("Role atualizada com sucesso!")
                                input("APERTE ENTER PARA CONTINUAR")
                            case _:
                                raise Exception("Campo não encontrado!")
                else:
                    raise Exception("Usuario não encontrado!")
        except ValueError:
            print("Valor invalido!")     
        except Exception as e:
            print(e)

    def atualizarUsuario(self) -> None:
        usuarioValido = False
        while not usuarioValido:                            
            self.bannerAtualizando()
            mostrarUsuarios(self.database)
            usuario = str(input("Informe o nome do usuario que deseja atualizar: ")).strip()
            usuarioValido = usuarioInBd(self.database, usuario)
            if not usuarioValido:
                input("APERTE ENTER PARA CONTINUAR")
        indices = []
        verificarSaida = False
        while not verificarSaida:
            campoValido = False
            while not campoValido:
                self.bannerAtualizando()
                mostrarCampos()
                campo = str(input("Informe o indice do campo que deseja cadastrar: "))
                campoValido = verificarCampo(campo, indices)
                if not campoValido:
                    input("APERTE ENTER PARA CONTINUAR")
            indices.append(campo)
            self.bannerAtualizando()
            continuar = False
            while not continuar:
                self.bannerAtualizando()
                resposta = input("Deseja selecionar outro campo? [Sim/Não]\n").title().strip()
                continuar = confirmarSaida(resposta)
                if not verificarSaida:
                    input("APERTE ENTER PARA CONTINUAR")   
            if resposta != "Sim":
                verificarSaida = True
        self.bannerAtualizando()
        print("Iniciando atualização de campos...")
        sleep(1)
        self.bannerAtualizando()
        self._atualizarUsuario(usuario, indices)

    def cadastrarUsuario(self) -> None:                            # Cadastrar usuario
        permitido = False
        while not permitido:
            permitido = verificarPermissão(self.database, self.usuarioLogado)
            if not permitido:
                print("Usuario sem permissão de cadastro")
                break
        cadastrado = False
        while not cadastrado:
            loginEscolhido = False
            while not loginEscolhido:
                self.loginMenu()
                choice = str(input("Qual o login do usuario? ")).strip()
                match choice:
                    case "1":
                        loginValido = False
                        while not loginValido:
                            self.bannerCadastro()
                            login = str(input("Informe o email: ")).strip()
                            loginValido = validarLogin(login, choice)
                            tipoLogin = "email"
                            if not loginValido:
                                input("APERTE ENTER PARA CONTINUAR")
                        senhaValida = False
                        while not senhaValida: 
                            self.bannerCadastro()
                            senha = str(input("Informe a senha: ")).strip()
                            senhaValida = validarSenha(senha)
                            if not senhaValida:
                                input("APERTE ENTER PARA CONTINUAR")
                        senha = protegerSenha(senha)
                        loginEscolhido = True
                    
                    case "2":
                        loginValido = False
                        while not loginValido:
                            self.bannerCadastro()
                            login = str(input("Informe o usuario: ")).strip()
                            loginValido = validarLogin(login, choice)
                            tipoLogin = "usuario"
                            if not loginValido:
                                input("APERTE ENTER PARA CONTINUAR:")
                        senhaValida = False
                        while not senhaValida: 
                            self.bannerCadastro()
                            senha = str(input("Informe a senha: ")).strip()
                            senhaValida = validarSenha(senha)
                            if not senhaValida:
                                input("APERTE ENTER PARA CONTINUAR")
                        senha = protegerSenha(senha)
                        loginEscolhido = True
                    
                    case "3":
                        loginValido = False
                        while not loginValido:
                            self.bannerCadastro()
                            login = str(input("Informe o cpf: ")).strip()
                            loginValido = validarLogin(login, choice)
                            tipoLogin = "cpf"
                            if not loginValido:
                                input("APERTE ENTER PARA CONTINUAR")
                        senhaValida = False
                        while not senhaValida: 
                            self.bannerCadastro()
                            senha = str(input("Informe a senha: ")).strip()
                            senhaValida = validarSenha(senha)
                            if not senhaValida:
                                input("APERTE ENTER PARA CONTINUAR")
                        senha = protegerSenha(senha)
                        loginEscolhido = True
                    
                    case "4":
                        loginValido = False
                        while not loginValido:
                            self.bannerCadastro()
                            login = str(input("Informe o rg: ")).strip()
                            loginValido = validarLogin(login, choice)
                            tipoLogin = "rg"
                            if not loginValido:
                                input("APERTE ENTER PARA CONTINUAR")
                        senhaValida = False
                        while not senhaValida: 
                            self.bannerCadastro()
                            senha = str(input("Informe a senha: ")).strip()
                            senhaValida = validarSenha(senha)
                            if not senhaValida:
                                input("APERTE ENTER PARA CONTINUAR")
                        senha = protegerSenha(senha)
                        loginEscolhido = True
                    case _:
                        print("Opção Invalida")
                        input("APERTE ENTER PARA CONTINUAR")
            emailValido = False
            while not emailValido:
                self.bannerCadastro()
                email = str(input("Qual o email do usuario? ")).strip()
                emailValido = validarEmail(email)
                if not emailValido:
                    input("APERTE ENTER PARA CONTINUAR")
            nomeValido = False
            while not nomeValido:
                self.bannerCadastro()
                nome = str(input("Qual o nome do usuario? ")).strip()
                nomeValido = validarNome(nome)
                if not nomeValido:
                    input("APERTE ENTER PARA CONTINUAR")
            documentoValido = False
            while not documentoValido:
                self.bannerCadastro()
                print("Documentos")
                print("1 - CPF")
                print("2 - RG")
                option = str(input("Informe o documento desejado: "))
                match option:
                    case "1":
                        cpfValido = False
                        while not cpfValido:
                            self.bannerCadastro()
                            cpf = str(input("Informe o CPF do usuario: "))
                            cpfValido = validarCpf(cpf)
                            if not cpfValido:
                                input("APERTE ENTER PARA CONTINUAR")
                        rg = None
                        documentoValido = True
                    case "2":
                        rgValido = False
                        while not rgValido:
                            self.bannerCadastro()
                            rg = str(input("Informe o RG do usuario: "))
                            rgValido = validarRg(rg)
                            if not rgValido:
                                input("APERTE ENTER PARA CONTINUAR")
                        cpf = None
                        documentoValido = True
                    case _:
                        print("Opção invalida!")
                if not documentoValido:
                    input("APERTE ENTER PARA CONTINUAR")
            dataValida = False
            while not dataValida:
                self.bannerCadastro()
                data = str(input("Informe a data de nascimento do usuario: "))
                dataValida = validarData(data)
                if not dataValida:
                    input("APERTE ENTER PARA CONTINUAR")
            endereco_valido = False
            while not endereco_valido:
                self.bannerCadastro()
                endereco = str(input("Informe o endereço: ")).strip()
                endereco_valido = validarEndereco(endereco)
                if not endereco_valido:
                    input("APERTE ENTER PARA CONTINUAR")
            roleValida = False
            while not roleValida:
                self.bannerCadastro()
                print("Permissões")
                print("1 - Admin")
                print("2 - User")
                choice = str(input("Informe a opção desejada: "))
                match choice:
                    case "1":
                        self.bannerCadastro()
                        print("Permissões do usuario definida como admin!")
                        input("APERTE ENTER PARA CONTINUAR")
                        role = "admin"
                        roleValida = True
                    case "2":
                        self.bannerCadastro()
                        print("Permissões do usuario definida como user!")
                        input("APERTE ENTER PARA CONTINUAR")
                        role = "user"
                        roleValida = True
                    case _:
                        print("Opção invalida!")
                        input("APERTE ENTER PARA CONTINUAR")
            usuarioCadastrado = False
            while not usuarioCadastrado:
                self.bannerCadastro()
                print("Cadastrando...")
                sleep(1)
                self.bannerCadastro()
                if not usuarioInBd(self.database, login):
                    usuarioCadastrado = cadastrarUsuario(self.database, login, tipoLogin, email, nome, rg, cpf, data, senha, endereco, role)
                    cadastrado = True
                else:
                    self.bannerCadastro()
                    usuarioCadastrado = True
                    raise Exception("Usuario ja cadastrado!")
        if cadastrado:
            self.bannerCadastro()
            print(f"usuario {login} cadastrado com sucesso!")

    def deletarUsuario(self) -> None:
        if len(self.database) >= 1:
            if len(self.database) == 1:
                self.bannerDeletarUsuarios()
                mostrarUsuarios(self.database)
                print("\nExiste apenas 1 usuario adicionado\nnão é possivel remove-lo!")
            else:
                usuarioDeletado = False
                while not usuarioDeletado:
                    self.bannerDeletarUsuarios()
                    mostrarUsuarios(self.database)
                    usuario = str(input("Informe o nome usuario que deseja deletar: "))
                    self.bannerDeletarUsuarios()
                    print("Deletando...")
                    sleep(1)
                    usuarioDeletado = deletarUsuario(self.database, usuario, self.usuarioLogado)
                    if not usuarioDeletado:
                        input("APERTE ENTER PARA CONTINUAR")
                print(f'o usuario "{usuario}" foi deletado com sucesso')
        else:
            print("Você esta sem usuarios adicionados")
            input("APERTE ENTER PARA CONTINUAR")

    def pesquisarUsuario(self) -> None:
        userValido = False
        while not userValido:
            self.bannerBusca()
            mostrarUsuarios(self.database)
            indiceValido = False
            while not indiceValido:
                indiceUsuario = int(input("Informe o indice do usuario: "))
                indiceValido = validarIndice(indiceUsuario)
                if not indiceValido:
                    input("APERTE ENTER PARA CONTINUAR")
            usuario = self.database[indice]
            if usuarioInBd(self.database, usuario[0]):
                self.bannerAtualizando
                self.bannerBusca()
                print("Procurando...")
                sleep(1)
                userValido = True
            else:
                input("APERTE ENTER PARA CONTINUAR")
        self.bannerBusca()
        print(f"Usuario {self.database[indiceUsuario][0]} encontrado!")
        input("APERTE ENTER PARA CONTINUAR!")
        indicesCampos = []
        verificarSaida = False
        while not verificarSaida:
            campoValido = False
            while not campoValido:
                self.bannerBusca()
                mostrarCampos()
                campo = input("Informe o indice do campo desejado: ").strip()
                campoValido = verificarCampo(campo, indicesCampos)
                if not campoValido:
                    input("APERTE ENTER PARA CONTINUAR")
            indicesCampos.append(campo)
            selecionarOutroCampo = False
            while not selecionarOutroCampo:
                self.bannerBusca()
                resposta = input("Deseja selecionar outro campo? [Sim/Não]\n").title().strip()
                selecionarOutroCampo = confirmarSaida(resposta)
                if not selecionarOutroCampo:
                    input("APERTE ENTER PARA CONTINUAR")
            if resposta != "Sim" :
                verificarSaida = True
        
        campos = ["login", "tipo de Login","email", "nome", "cpf", "rg", "data de nascimento", "senha", "endereco", "role"]
        for indice in indicesCampos:
            indice_int = int(indice)
            campo = campos[indice_int]
            user = usuario[indice_int]
            print(f"{campo}   ->   {user}")
    def saida(self) -> None:
        verificarSaida = False
        while not verificarSaida:
            self.bannerSaida()
            resposta = input("Deseja mesmo sair? [Sim/Nao]\n").title().strip()
            verificarSaida = confirmarSaida(resposta)
            if not verificarSaida:
                input("APERTE ENTER PARA CONTINUAR")
        if resposta == "Sim":
            self.sair = True
            self.bannerSaida()
            print("Finalizando...")
            sleep(1)
            self.bannerSaida()
            print("Programa finalizado!")
        else:
            print("Certo")

    def mostrarUsuarios(self):
        self.bannerUsuarios()  
        print("Buscando usuarios...")
        sleep(1)
        self.bannerUsuarios()
        mostrarUsuarios(self.database)

    def executar(self) -> None:
        # self.fazerLogin()
        self.logado = True
        self.usuarioLogado = "felipe"
        if self.logado:
            self.sair = False
            while not self.sair:
                try:
                    self.viewMenu()
                    opcao = str(input("Informe a opção desejada: ")).strip()
                    match opcao:
                        case "1":
                            # Cadastrar Usuario
                            self.cadastrarUsuario()
                        case "2":
                            # Atualizar usuario
                            self.atualizarUsuario()
                        case "3":
                            # Mostrar usuarios
                            self.mostrarUsuarios()
                        case "4":
                            # Pesquisar usuario
                            self.pesquisarUsuario()
                        case "5":
                            # Deletar usuario
                            self.deletarUsuario()
                        case "6":
                            # Sair
                            self.saida()
                        case _:
                            # Caso não for nenhum dos mencionados acima
                            print("Opção invalida!")
                except Exception as e:
                    print(e)
                finally:
                    input("APERTE ENTER PARA CONTINUAR")
                    self.clear()

if __name__ == "__main__":
    main = Main()
    main.executar()