import os
from time import sleep
from utils.validations import *
from modules.database import *


class App:
    def __init__(self) -> None:
        self.logado = False
        self.database: list[tuple] = [
            (
                "felipe",
                "usuario",
                "fglpc2@gmail.com",
                "Felipe",
                None,
                "013025086123",
                "13/02/2006",
                "123",
                "Rua luis porrio, 415",
                "admin",
            ),
            (
                "pedro",
                "usuario",
                "fglpc2@gmail.com",
                "Felipe",
                None,
                "013025086123",
                "13/02/2006",
                "123",
                "Rua luis porrio, 415",
                "user",
            ),
            (
                "lucas",
                "usuario",
                "fglpc2@gmail.com",
                "Felipe",
                None,
                "013025086123",
                "13/02/2006",
                "123",
                "Rua luis porrio, 415",
                "admin",
            ),
            (
                "aram",
                "usuario",
                "fglpc2@gmail.com",
                "Felipe",
                None,
                "013025086123",
                "13/02/2006",
                "123",
                "Rua luis porrio, 415",
                "admin",
            ),
            (
                "aaa",
                "usuario",
                "fglpc2@gmail.com",
                "Felipe",
                None,
                "013025086123",
                "13/02/2006",
                "123",
                "Rua luis porrio, 415",
                "admin",
            ),
            (
                "filho",
                "usuario",
                "fglpc2@gmail.com",
                "Felipe",
                None,
                "013025086123",
                "13/02/2006",
                "123",
                "Rua luis porrio, 415",
                "admin",
            ),
            # Posições
            # login                     ->  0
            # tipo-login                ->  1
            # email                     ->  2
            # nome                      ->  3
            # cpf                       ->  5
            # rg                        ->  4
            # data-nascimento           ->  6
            # senha                     ->  7
            # endereco                  ->  8
            # role(admin or user)       ->  9
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

    def bannerAtualizando(self, nome="usuario") -> None:
        self.clear()
        user = f"---- Atualizando {nome.title()} -----"
        linha = "-" * 31

        tamanhValido = False
        while not tamanhValido:
            if len(linha) != len(user):
                if len(user) < 31:
                    user += "-"
                    user = user[::-1]
                    user += "-"
                    user = user[::-1]
                else:
                    for c in range(len(user)):
                        if len(linha) == len(user):
                            break
                        else:
                            linha += "-"
            else:
                tamanhValido = True
        print(linha)
        print(user)
        print(linha)

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
            usuario = str(input("login: ")).lower()
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

    def _atualizarUsuario(self, usuario: str, indice_campos: list[str]) -> None:
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
                                self.bannerAtualizando(usuario)
                                print(
                                    "Se você selecionou campo de usuário ou o tipo do usuario, \nvocê terá que alterar ambos."
                                )
                                input("APERTE ENTER PARA CONTINUAR")
                                loginEscolhido = False
                                while not loginEscolhido:
                                    self.loginMenu()
                                    choice = str(
                                        input("Qual o novo login do usuario? ")
                                    ).strip()
                                    match choice:
                                        case "1":
                                            loginValido = False
                                            while not loginValido:
                                                self.bannerAtualizando(usuario)
                                                login = str(
                                                    input("Informe o email: ")
                                                ).strip()
                                                loginValido = validarLogin(
                                                    login, choice
                                                )
                                                tipoLogin = "email"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True

                                        case "2":
                                            loginValido = False
                                            while not loginValido:
                                                self.bannerAtualizando(usuario)
                                                login = str(
                                                    input("Informe o usuario: ")
                                                ).strip()
                                                loginValido = validarLogin(
                                                    login, choice
                                                )
                                                tipoLogin = "usuario"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True

                                        case "3":
                                            loginValido = False
                                            while not loginValido:
                                                self.bannerAtualizando(usuario)
                                                login = str(
                                                    input("Informe o cpf: ")
                                                ).strip()
                                                loginValido = validarLogin(
                                                    login, choice
                                                )
                                                tipoLogin = "cpf"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True

                                        case "4":
                                            self.bannerAtualizando(usuario)
                                            loginValido = False
                                            while not loginValido:
                                                self.bannerAtualizando(usuario)
                                                login = str(
                                                    input("Informe o rg: ")
                                                ).strip()
                                                loginValido = validarLogin(
                                                    login, choice
                                                )
                                                tipoLogin = "rg"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True

                                        case _:
                                            print("Opção Invalida")
                                            input("APERTE ENTER PARA CONTINUAR")
                                self.bannerAtualizando(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando(usuario)
                                print("Login atualizado com sucesso!")
                                self.database[indiceUser] = (
                                    login,
                                    tipoLogin,
                                    user[2],
                                    user[3],
                                    user[4],
                                    user[5],
                                    user[6],
                                    user[7],
                                    user[8],
                                    user[9],
                                )

                            case "2":
                                emailValido = False
                                while not emailValido:
                                    self.bannerAtualizando(usuario)
                                    email = input("Informe o novo email:").strip()
                                    emailValido = validarEmail(email)
                                    if not emailValido:
                                        input("APERTE ENTER PARA CONTINUAR")
                                self.database[indiceUser] = (
                                    user[0],
                                    user[1],
                                    email,
                                    user[3],
                                    user[4],
                                    user[5],
                                    user[6],
                                    user[7],
                                    user[8],
                                    user[9],
                                )
                                self.bannerAtualizando(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando(usuario)
                                print("Email atualizado com sucesso!")
                                input("APERTE ENTER PARA CONTINUAR")

                            case "3":
                                nomeValido = False
                                while not nomeValido:
                                    self.bannerAtualizando(usuario)
                                    nome = str(input("Informe o novo nome:")).strip()
                                    nomeValido = validarNome(nome)
                                    if not nomeValido:
                                        input("APERTE ENTER PARA CONTINUAR")
                                self.database[indiceUser] = (
                                    user[0],
                                    user[1],
                                    user[2],
                                    nome,
                                    user[4],
                                    user[5],
                                    user[6],
                                    user[7],
                                    user[8],
                                    user[9],
                                )
                                self.bannerAtualizando(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando(usuario)
                                print("Nome atualizado com sucesso!")

                            case "4" | "5":
                                documentoValido = False
                                while not documentoValido:
                                    self.bannerAtualizando(usuario)
                                    match indice:
                                        case "4":
                                            cpfValido = False
                                            while not cpfValido:
                                                cpf = str(
                                                    input(
                                                        "Informe o novo CPF do usuario: "
                                                    )
                                                ).strip()
                                                cpfValido = validarCpf(cpf)
                                                if not cpfValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            documentoValido = True
                                        case "5":
                                            rgValido = False
                                            while not rgValido:
                                                self.bannerAtualizando(usuario)
                                                rg = str(
                                                    input(
                                                        "Informe o novo RG do usuario: "
                                                    )
                                                ).strip()
                                                rgValido = validarRg(rg)
                                                if not rgValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            documentoValido = True
                                if indice == "4":
                                    self.database[indiceUser] = (
                                        user[0],
                                        user[1],
                                        user[2],
                                        user[3],
                                        cpf,
                                        None,
                                        user[6],
                                        user[7],
                                        user[8],
                                        user[9],
                                    )
                                    self.bannerAtualizando(usuario)
                                    print("Atualizando...")
                                    sleep(1)
                                    self.bannerAtualizando(usuario)
                                    print("CPF atualizado com sucesso")
                                else:
                                    self.database[indiceUser] = (
                                        user[0],
                                        user[1],
                                        user[2],
                                        user[3],
                                        None,
                                        rg,
                                        user[6],
                                        user[7],
                                        user[8],
                                        user[9],
                                    )
                                    self.bannerAtualizando(usuario)
                                    print("Atualizando...")
                                    sleep(1)
                                    self.bannerAtualizando(usuario)
                                    print("RG atualizado com sucesso!")

                            case "6":
                                dataValida = False
                                while not dataValida:
                                    self.bannerAtualizando(usuario)
                                    data = str(
                                        input(
                                            "Informe a data de nascimento do usuario: "
                                        )
                                    ).strip()
                                    dataValida = validarData(data)
                                    if not dataValida:
                                        input("APERTE ENTER PARA CONTINUAR")
                                self.database[indiceUser] = (
                                    user[0],
                                    user[1],
                                    user[2],
                                    user[3],
                                    user[4],
                                    user[5],
                                    data,
                                    user[7],
                                    user[8],
                                    user[9],
                                )
                                self.bannerAtualizando(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando(usuario)
                                print("Data atualizada com sucesso!")

                            case "7":
                                if usuario != self.usuarioLogado:
                                    permitido = verificarPermissao(
                                        self.database, self.usuarioLogado
                                    )
                                else:
                                    permitido = True

                                if not permitido:
                                    self.bannerAtualizando(usuario)
                                    print("Seu usuario não tem permissões para isso.")
                                if permitido:
                                    senhaValida = False
                                    while not senhaValida:
                                        self.bannerAtualizando(usuario)
                                        senha = str(
                                            input("Informe a nova senha:")
                                        ).strip()
                                        senhaValida = validarSenha(senha)
                                        if not senhaValida:
                                            input("APERTE ENTER PARA CONTINUAR")
                                    senha = protegerSenha(senha)
                                    self.database[indiceUser] = (
                                        user[0],
                                        user[1],
                                        user[2],
                                        user[3],
                                        user[4],
                                        user[5],
                                        user[6],
                                        senha,
                                        user[8],
                                        user[9],
                                    )
                                    self.bannerAtualizando(usuario)
                                    print("Atualizando...")
                                    sleep(1)
                                    self.bannerAtualizando(usuario)
                                    print("Senha atualizada com sucesso!")

                            case "8":
                                enderecoValido = False
                                while not enderecoValido:
                                    self.bannerAtualizando(usuario)
                                    endereco = str(
                                        input("Informe o novo endereço: ")
                                    ).strip()
                                    enderecoValido = validarEndereco(endereco)
                                    if not enderecoValido:
                                        input("APERTE ENTER PARA CONTINUAR")
                                self.database[indiceUser] = (
                                    user[0],
                                    user[1],
                                    user[2],
                                    user[3],
                                    user[4],
                                    user[5],
                                    user[6],
                                    senha,
                                    endereco,
                                    user[9],
                                )
                                self.bannerAtualizando(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando(usuario)
                                print("Endereco atualizado com sucesso")

                            case "9":
                                permitido = False
                                while not permitido:
                                    for user in self.database:
                                        if usuario != self.usuarioLogado:
                                            permitidoUserLogado = verificarPermissao(
                                                self.database, self.usuarioLogado
                                            )
                                            permitidoUserEditado = verificarPermissao(
                                                self.database, usuario
                                            )
                                            if (
                                                not permitidoUserLogado
                                                and permitidoUserEditado
                                            ):
                                                permitido = True
                                            else:
                                                raise Exception(
                                                    "Usuario não tem permição para alterar a role do usuario desejado"
                                                )
                                        else:
                                            raise Exception(
                                                "Você não pode mudar suas proprias permissões"
                                            )
                                roleValida = False
                                while not roleValida:
                                    self.bannerAtualizando(usuario)
                                    role = input("Digite a nova role do usuario")
                                    roleValida = validarRole(role)
                                    if not roleValida:
                                        input("APERTE ENTER PARA CONTINUAR")
                                self.database[indiceUser] = (
                                    user[0],
                                    user[1],
                                    user[2],
                                    user[3],
                                    user[4],
                                    user[5],
                                    user[6],
                                    user[7],
                                    user[8],
                                    role,
                                )
                                self.bannerAtualizando(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.bannerAtualizando(usuario)
                                print("Role atualizada com sucesso!")
                            case _:
                                raise Exception("Campo não encontrado!")
        except ValueError:
            print("Valor invalido!")
        except Exception as e:
            print(e)

    def atualizarUsuario(self) -> None:
        if len(self.database) >= 1:
            usuarioValido = False
            while not usuarioValido:
                indiceValido = False
                while not indiceValido:
                    self.bannerAtualizando()
                    mostrarUsuarios(self.database)
                    indice = (
                        str(input("Informe o indice do usuario que deseja atualizar: "))
                        .strip()
                        .lower()
                    )
                    indiceValido = validarIndice(self.database, indice)
                    if not indiceValido:
                        input("APERTE ENTER PARA CONTINUAR")
                usuario = self.database[int(indice) - 1]
                usuarioValido = usuarioInBd(self.database, usuario[0])
                if not usuarioValido:
                    input("APERTE ENTER PARA CONTINUAR")
            indices = []
            verificarSaida = False
            while not verificarSaida:
                if len(indices) == 10:
                    self.bannerAtualizando(nome=usuario[0])
                    print("Todos os campos foram adicionados")
                    input("APERTE ENTER PARA CONTINUAR")
                    verificarSaida = True
                    break
                campoValido = False
                while not campoValido:
                    self.bannerAtualizando(nome=usuario[0])
                    mostrarCampos()
                    campo = str(
                        input("Informe o indice do campo que deseja cadastrar: ")
                    )
                    campoValido = verificarCampo(campo, indices)
                    if not campoValido:
                        input("APERTE ENTER PARA CONTINUAR")
                indices.append(campo)
                continuar = False
                while not continuar:
                    self.bannerAtualizando(nome=usuario[0])
                    resposta = (
                        input("Deseja selecionar outro campo? [Sim/Não]\n")
                        .title()
                        .strip()
                    )
                    continuar = confirmarSaida(resposta)
                    if not verificarSaida:
                        input("APERTE ENTER PARA CONTINUAR")
                if resposta != "Sim":
                    verificarSaida = True
            self.bannerAtualizando(nome=usuario[0])
            print("Iniciando atualização de campos...")
            sleep(1)
            self.bannerAtualizando(nome=usuario[0])
            self._atualizarUsuario(usuario[0], indices)
        else:
            print("Sem usuarios para atualizar!")

    def cadastrarUsuario(self) -> None:  # Cadastrar usuario
        permitido = False
        while not permitido:
            permitido = verificarPermissao(self.database, self.usuarioLogado)
            if not permitido:
                self.bannerCadastro()
                print("Usuario sem permissão de cadastro")
                break
        if permitido:
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
                                login = str(input("Informe o email: ")).strip().lower()
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
                                login = (
                                    str(input("Informe o usuario: ")).strip().lower()
                                )
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
                                login = str(input("Informe o cpf: ")).strip().lower()
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
                                login = str(input("Informe o rg: ")).strip().lower()
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
                        usuarioCadastrado = cadastrarUsuario(
                            self.database,
                            login,
                            tipoLogin,
                            email,
                            nome,
                            rg,
                            cpf,
                            data,
                            senha,
                            endereco,
                            role,
                        )
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
                permitido = False
                while not permitido:
                    permitido = verificarPermissao(self.database, self.usuarioLogado)
                    if not permitido:
                        self.bannerDeletarUsuarios()
                        print("O seu usuario não tem permissões para isso.")
                        break
                if permitido:
                    if not verificarSeTodosAdmin(self.database):
                        usuarioDeletado = False
                        while not usuarioDeletado:
                            indiceValido = False
                            while not indiceValido:
                                self.bannerDeletarUsuarios()
                                mostrarUsuarios(self.database)
                                indice = str(
                                    input(
                                        "Informe o indice do usuario que deseja deletar: "
                                    )
                                )
                                indiceValido = validarIndice(self.database, indice)
                                if not indiceValido:
                                    input("APERTE ENTER PARA CONTINUAR")
                            usuario = self.database[int(indice) - 1]
                            self.bannerDeletarUsuarios()
                            print("Deletando...")
                            sleep(1)
                            usuarioDeletado = deletarUsuario(
                                self.database, usuario[0], self.usuarioLogado
                            )
                            if not usuarioDeletado:
                                input("APERTE ENTER PARA CONTINUAR")
                        print(f'o usuario "{usuario[0]}" foi deletado com sucesso')
                    else:
                        self.bannerDeletarUsuarios()
                        print(
                            "Todos os usuarios encontrados são admin, não é possivel remover!"
                        )
        else:
            print("Você esta sem usuarios adicionados")
            input("APERTE ENTER PARA CONTINUAR")

    def pesquisarUsuario(self) -> None:
        userValido = False
        while not userValido:
            indiceValido = False
            while not indiceValido:
                self.bannerBusca()
                mostrarUsuarios(self.database)
                indiceUsuario = str(input("Informe o indice do usuario: "))
                indiceValido = validarIndice(self.database, indiceUsuario)
                if not indiceValido:
                    input("APERTE ENTER PARA CONTINUAR")
            indice = int(indiceUsuario) - 1
            usuario = self.database[indice]
            if usuarioInBd(self.database, usuario[0]):
                print("Ola")
                self.bannerAtualizando()
                self.bannerBusca()
                print("Procurando...")
                sleep(1)
                userValido = True
            else:
                input("APERTE ENTER PARA CONTINUAR")
        self.bannerBusca()
        print(f"Usuario {usuario[0]} encontrado!")
        input("APERTE ENTER PARA CONTINUAR!")
        indicesCampos = []
        verificarSaida = False
        while not verificarSaida:
            if len(indicesCampos) == 10:
                self.bannerBusca()
                print("Todos os campos foram selecionados!")
                input("APERTE ENTER PARA CONTINUAR")
                verificarSaida == True
                break
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
                resposta = (
                    input("Deseja selecionar outro campo? [Sim/Não]\n").title().strip()
                )
                selecionarOutroCampo = confirmarSaida(resposta)
                if not selecionarOutroCampo:
                    input("APERTE ENTER PARA CONTINUAR")
            if resposta != "Sim":
                verificarSaida = True
        campos = [
            "login",
            "tipo de Login",
            "email",
            "nome",
            "cpf",
            "rg",
            "data de nascimento",
            "senha",
            "endereco",
            "role",
        ]
        cont = 1
        for indice in indicesCampos:
            self.bannerBusca()
            indice_int = int(indice)
            campo = campos[indice_int]
            user = usuario[indice_int]
            if indice_int == 7:
                permitido = False
                while not permitido:
                    permitido = verificarPermissao(self.database, self.usuarioLogado)
                    if not permitido:
                        print("Usuario sem permissão para ver a senha!")
                        input("Aperte enter para continuar")
                        continue
                    else:
                        print(f"{campo}   ->   {user}")
            else:
                print(f"{campo}   ->   {user}")
            if cont != len(indicesCampos):
                input("APERTE ENTER PARA VER O PROXIMO CAMPO!")
                cont += 1

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

    def run(self) -> None:
        self.fazerLogin()
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
