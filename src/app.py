import os
from time import sleep
from .utils.validations import (
    validate_login,
    validate_email,
    validate_name,
    validate_cpf,
    validate_rg,
    validate_date,
    validate_password,
    validate_address,
    validate_role,
    validate_index,
    validate_field,
    confirm_exit,
)
from .modules.database import (
    protect_password,
    validate_user,
    get_user_index,
    validate_perm,
    show_users,
    user_in_db,
    show_fields,
    register_user,
    validate_if_all_admin,
    delete_user,
)


class App:
    """
    Class to manage the application.
    """

    def __init__(self) -> None:
        """
        Initialize the application.
        """
        self.logado = False
        self.database: list[tuple] = [
            (
                "admin",  # Login
                "usuario",  # Tipo de login
                "email@gmail.com",  # Email
                "Felipe",  # Nome
                "123456789",  # RG
                "013025086123",  # CPF
                "13/02/2006",  # Data de nascimento
                "admin",  # Senha
                "enrereco",  # Endereco
                "admin",  # Role
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
        """
        Clear the console.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def view_menu(self) -> None:
        """
        Show the main menu of the application.
        """
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

    def login_menu(self) -> None:
        """
        Show the login menu of the application.
        """
        self.clear()
        print("------------------------------")
        print("------ Opções de login -------")
        print("------------------------------")
        print("1 - Email")
        print("2 - Usuario")
        print("3 - Cpf")
        print("4 - Rg")

    def banner_register(self) -> None:
        """
        Show the banner for the registration menu.
        """
        self.clear()
        print("-------------------------------")
        print("---------- Cadastro -----------")
        print("-------------------------------")

    def banner_get_details(self) -> None:
        """
        Show the banner for the search menu.
        """
        self.clear()
        print("-------------------------------")
        print("---- Informações de busca -----")
        print("-------------------------------")

    def banner_users(self) -> None:
        """
        Show the banner for the users menu.
        """
        self.clear()
        print("------------------------------")
        print("--------- Usuarios -----------")
        print("------------------------------")

    def banner_delete_users(self) -> None:
        """
        Show the banner for the delete users menu.
        """
        self.clear()
        print("------------------------------")
        print("------ Deletar Usuarios ------")
        print("------------------------------")

    def banner_update(self, nome="usuario") -> None:
        """
        Show the banner for the update menu.

        Args:
            nome (str, optional): The name of the user to update. Defaults to "usuario".
        """
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

    def banner_login(self) -> None:
        """
        Show the banner for the login menu.
        """
        self.clear()
        print("--------------------------------")
        print("------------ Login -------------")
        print("--------------------------------")

    def banner_search(self) -> None:
        """
        Show the banner for the search menu.
        """
        self.clear()
        print("--------------------------------")
        print("-------- Buscar Usuario --------")
        print("--------------------------------")

    def banner_exit(self) -> None:
        """
        Show the banner for the exit menu.
        """
        self.clear()
        print("----------------------------------")
        print("-------- Verificar Saida ---------")
        print("----------------------------------")

    def auth(self) -> None:
        """
        Authenticate the user.
        """
        while not self.logado:
            self.banner_login()
            usuario = str(input("login: ")).lower()
            senha = str(input("senha: "))
            senha = protect_password(senha)
            self.banner_login()
            print("Verificando...")
            sleep(1)
            self.banner_login()
            self.logado = validate_user(self.database, usuario, senha)
            if not self.logado:
                print("login ou senha invalidos!")
                input("APERTE ENTER PARA CONTINUAR")
        self.usuarioLogado = usuario
        self.banner_login()
        print("Logando...")
        sleep(1)
        self.banner_login()
        print("Usuario logado com sucesso!")
        input("APERTE ENTER PARA CONTINUAR")

    def _update_user(self, usuario: str, indice_campos: list[str]) -> None:
        """
        Update the user in the database.

        Args:
            usuario (str): The user to update.
            indice_campos (list[str]): The fields to update.

        Raises:
            Exception: If the user is not found.
        """
        try:
            indiceUser = get_user_index(self.database, usuario)
            for user in self.database:
                if user[0] == usuario:
                    for indice in indice_campos:
                        match indice:
                            case "0" | "1":
                                if indice == "0":
                                    indice_campos.remove("1")
                                else:
                                    indice_campos.remove("0")
                                self.banner_update(usuario)
                                print(
                                    "Se você selecionou campo de usuário ou o tipo do usuario, \nvocê terá que alterar ambos."
                                )
                                input("APERTE ENTER PARA CONTINUAR")
                                loginEscolhido = False
                                while not loginEscolhido:
                                    self.login_menu()
                                    choice = str(
                                        input("Qual o novo login do usuario? ")
                                    ).strip()
                                    match choice:
                                        case "1":
                                            loginValido = False
                                            while not loginValido:
                                                self.banner_update(usuario)
                                                login = str(
                                                    input("Informe o email: ")
                                                ).strip()
                                                loginValido = validate_login(
                                                    login, choice
                                                )
                                                tipoLogin = "email"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True

                                        case "2":
                                            loginValido = False
                                            while not loginValido:
                                                self.banner_update(usuario)
                                                login = str(
                                                    input("Informe o usuario: ")
                                                ).strip()
                                                loginValido = validate_login(
                                                    login, choice
                                                )
                                                tipoLogin = "usuario"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True

                                        case "3":
                                            loginValido = False
                                            while not loginValido:
                                                self.banner_update(usuario)
                                                login = str(
                                                    input("Informe o cpf: ")
                                                ).strip()
                                                loginValido = validate_login(
                                                    login, choice
                                                )
                                                tipoLogin = "cpf"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True

                                        case "4":
                                            self.banner_update(usuario)
                                            loginValido = False
                                            while not loginValido:
                                                self.banner_update(usuario)
                                                login = str(
                                                    input("Informe o rg: ")
                                                ).strip()
                                                loginValido = validate_login(
                                                    login, choice
                                                )
                                                tipoLogin = "rg"
                                                if not loginValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            loginEscolhido = True

                                        case _:
                                            print("Opção Invalida")
                                            input("APERTE ENTER PARA CONTINUAR")
                                self.banner_update(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.banner_update(usuario)
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
                                    self.banner_update(usuario)
                                    email = input("Informe o novo email:").strip()
                                    emailValido = validate_email(email)
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
                                self.banner_update(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.banner_update(usuario)
                                print("Email atualizado com sucesso!")
                                input("APERTE ENTER PARA CONTINUAR")

                            case "3":
                                nomeValido = False
                                while not nomeValido:
                                    self.banner_update(usuario)
                                    nome = str(input("Informe o novo nome:")).strip()
                                    nomeValido = validate_name(nome)
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
                                self.banner_update(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.banner_update(usuario)
                                print("Nome atualizado com sucesso!")

                            case "4" | "5":
                                documentoValido = False
                                while not documentoValido:
                                    self.banner_update(usuario)
                                    match indice:
                                        case "4":
                                            cpfValido = False
                                            while not cpfValido:
                                                cpf = str(
                                                    input(
                                                        "Informe o novo CPF do usuario: "
                                                    )
                                                ).strip()
                                                cpfValido = validate_cpf(cpf)
                                                if not cpfValido:
                                                    input("APERTE ENTER PARA CONTINUAR")
                                            documentoValido = True
                                        case "5":
                                            rgValido = False
                                            while not rgValido:
                                                self.banner_update(usuario)
                                                rg = str(
                                                    input(
                                                        "Informe o novo RG do usuario: "
                                                    )
                                                ).strip()
                                                rgValido = validate_rg(rg)
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
                                    self.banner_update(usuario)
                                    print("Atualizando...")
                                    sleep(1)
                                    self.banner_update(usuario)
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
                                    self.banner_update(usuario)
                                    print("Atualizando...")
                                    sleep(1)
                                    self.banner_update(usuario)
                                    print("RG atualizado com sucesso!")

                            case "6":
                                dataValida = False
                                while not dataValida:
                                    self.banner_update(usuario)
                                    data = str(
                                        input(
                                            "Informe a data de nascimento do usuario: "
                                        )
                                    ).strip()
                                    dataValida = validate_date(data)
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
                                self.banner_update(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.banner_update(usuario)
                                print("Data atualizada com sucesso!")

                            case "7":
                                if usuario != self.usuarioLogado:
                                    permitido = validate_perm(
                                        self.database, self.usuarioLogado
                                    )
                                else:
                                    permitido = True

                                if not permitido:
                                    self.banner_update(usuario)
                                    print("Seu usuario não tem permissões para isso.")
                                if permitido:
                                    senhaValida = False
                                    while not senhaValida:
                                        self.banner_update(usuario)
                                        senha = str(
                                            input("Informe a nova senha:")
                                        ).strip()
                                        senhaValida = validate_password(senha)
                                        if not senhaValida:
                                            input("APERTE ENTER PARA CONTINUAR")
                                    senha = protect_password(senha)
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
                                    self.banner_update(usuario)
                                    print("Atualizando...")
                                    sleep(1)
                                    self.banner_update(usuario)
                                    print("Senha atualizada com sucesso!")

                            case "8":
                                enderecoValido = False
                                while not enderecoValido:
                                    self.banner_update(usuario)
                                    endereco = str(
                                        input("Informe o novo endereço: ")
                                    ).strip()
                                    enderecoValido = validate_address(endereco)
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
                                self.banner_update(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.banner_update(usuario)
                                print("Endereco atualizado com sucesso")

                            case "9":
                                permitido = False
                                while not permitido:
                                    for user in self.database:
                                        if usuario != self.usuarioLogado:
                                            permitidoUserLogado = validate_perm(
                                                self.database, self.usuarioLogado
                                            )
                                            permitidoUserEditado = validate_perm(
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
                                    self.banner_update(usuario)
                                    role = input("Digite a nova role do usuario")
                                    roleValida = validate_role(role)
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
                                self.banner_update(usuario)
                                print("Atualizando...")
                                sleep(1)
                                self.banner_update(usuario)
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
                    self.banner_update()
                    show_users(self.database)
                    indice = (
                        str(input("Informe o indice do usuario que deseja atualizar: "))
                        .strip()
                        .lower()
                    )
                    indiceValido = validate_index(self.database, indice)
                    if not indiceValido:
                        input("APERTE ENTER PARA CONTINUAR")
                usuario = self.database[int(indice) - 1]
                usuarioValido = user_in_db(self.database, usuario[0])
                if not usuarioValido:
                    input("APERTE ENTER PARA CONTINUAR")
            indices = []
            verificarSaida = False
            while not verificarSaida:
                if len(indices) == 10:
                    self.banner_update(nome=usuario[0])
                    print("Todos os campos foram adicionados")
                    input("APERTE ENTER PARA CONTINUAR")
                    verificarSaida = True
                    break
                campoValido = False
                while not campoValido:
                    self.banner_update(nome=usuario[0])
                    show_fields()
                    campo = str(
                        input("Informe o indice do campo que deseja cadastrar: ")
                    )
                    campoValido = validate_field(campo, indices)
                    if not campoValido:
                        input("APERTE ENTER PARA CONTINUAR")
                indices.append(campo)
                continuar = False
                while not continuar:
                    self.banner_update(nome=usuario[0])
                    resposta = (
                        input("Deseja selecionar outro campo? [Sim/Não]\n")
                        .title()
                        .strip()
                    )
                    continuar = confirm_exit(resposta)
                    if not verificarSaida:
                        input("APERTE ENTER PARA CONTINUAR")
                if resposta != "Sim":
                    verificarSaida = True
            self.banner_update(nome=usuario[0])
            print("Iniciando atualização de campos...")
            sleep(1)
            self.banner_update(nome=usuario[0])
            self._update_user(usuario[0], indices)
        else:
            print("Sem usuarios para atualizar!")

    def cadastrarUsuario(self) -> None:  # Cadastrar usuario
        permitido = False
        while not permitido:
            permitido = validate_perm(self.database, self.usuarioLogado)
            if not permitido:
                self.banner_register()
                print("Usuario sem permissão de cadastro")
                break
        if permitido:
            cadastrado = False
            while not cadastrado:
                loginEscolhido = False
                while not loginEscolhido:
                    self.login_menu()
                    choice = str(input("Qual o login do usuario? ")).strip()
                    match choice:
                        case "1":
                            loginValido = False
                            while not loginValido:
                                self.banner_register()
                                login = str(input("Informe o email: ")).strip().lower()
                                loginValido = validate_login(login, choice)
                                tipoLogin = "email"
                                if not loginValido:
                                    input("APERTE ENTER PARA CONTINUAR")
                            senhaValida = False
                            while not senhaValida:
                                self.banner_register()
                                senha = str(input("Informe a senha: ")).strip()
                                senhaValida = validate_password(senha)
                                if not senhaValida:
                                    input("APERTE ENTER PARA CONTINUAR")
                            senha = protect_password(senha)
                            loginEscolhido = True

                        case "2":
                            loginValido = False
                            while not loginValido:
                                self.banner_register()
                                login = (
                                    str(input("Informe o usuario: ")).strip().lower()
                                )
                                loginValido = validate_login(login, choice)
                                tipoLogin = "usuario"
                                if not loginValido:
                                    input("APERTE ENTER PARA CONTINUAR:")
                            senhaValida = False
                            while not senhaValida:
                                self.banner_register()
                                senha = str(input("Informe a senha: ")).strip()
                                senhaValida = validate_password(senha)
                                if not senhaValida:
                                    input("APERTE ENTER PARA CONTINUAR")
                            senha = protect_password(senha)
                            loginEscolhido = True

                        case "3":
                            loginValido = False
                            while not loginValido:
                                self.banner_register()
                                login = str(input("Informe o cpf: ")).strip().lower()
                                loginValido = validate_login(login, choice)
                                tipoLogin = "cpf"
                                if not loginValido:
                                    input("APERTE ENTER PARA CONTINUAR")
                            senhaValida = False
                            while not senhaValida:
                                self.banner_register()
                                senha = str(input("Informe a senha: ")).strip()
                                senhaValida = validate_password(senha)
                                if not senhaValida:
                                    input("APERTE ENTER PARA CONTINUAR")
                            senha = protect_password(senha)
                            loginEscolhido = True

                        case "4":
                            loginValido = False
                            while not loginValido:
                                self.banner_register()
                                login = str(input("Informe o rg: ")).strip().lower()
                                loginValido = validate_login(login, choice)
                                tipoLogin = "rg"
                                if not loginValido:
                                    input("APERTE ENTER PARA CONTINUAR")
                            senhaValida = False
                            while not senhaValida:
                                self.banner_register()
                                senha = str(input("Informe a senha: ")).strip()
                                senhaValida = validate_password(senha)
                                if not senhaValida:
                                    input("APERTE ENTER PARA CONTINUAR")
                            senha = protect_password(senha)
                            loginEscolhido = True
                        case _:
                            print("Opção Invalida")
                            input("APERTE ENTER PARA CONTINUAR")
                emailValido = False
                while not emailValido:
                    self.banner_register()
                    email = str(input("Qual o email do usuario? ")).strip()
                    emailValido = validate_email(email)
                    if not emailValido:
                        input("APERTE ENTER PARA CONTINUAR")
                nomeValido = False
                while not nomeValido:
                    self.banner_register()
                    nome = str(input("Qual o nome do usuario? ")).strip()
                    nomeValido = validate_name(nome)
                    if not nomeValido:
                        input("APERTE ENTER PARA CONTINUAR")
                documentoValido = False
                while not documentoValido:
                    self.banner_register()
                    print("Documentos")
                    print("1 - CPF")
                    print("2 - RG")
                    option = str(input("Informe o documento desejado: "))
                    match option:
                        case "1":
                            cpfValido = False
                            while not cpfValido:
                                self.banner_register()
                                cpf = str(input("Informe o CPF do usuario: "))
                                cpfValido = validate_cpf(cpf)
                                if not cpfValido:
                                    input("APERTE ENTER PARA CONTINUAR")
                            rg = None
                            documentoValido = True
                        case "2":
                            rgValido = False
                            while not rgValido:
                                self.banner_register()
                                rg = str(input("Informe o RG do usuario: "))
                                rgValido = validate_rg(rg)
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
                    self.banner_register()
                    data = str(input("Informe a data de nascimento do usuario: "))
                    dataValida = validate_date(data)
                    if not dataValida:
                        input("APERTE ENTER PARA CONTINUAR")
                endereco_valido = False
                while not endereco_valido:
                    self.banner_register()
                    endereco = str(input("Informe o endereço: ")).strip()
                    endereco_valido = validate_address(endereco)
                    if not endereco_valido:
                        input("APERTE ENTER PARA CONTINUAR")
                roleValida = False
                while not roleValida:
                    self.banner_register()
                    print("Permissões")
                    print("1 - Admin")
                    print("2 - User")
                    choice = str(input("Informe a opção desejada: "))
                    match choice:
                        case "1":
                            self.banner_register()
                            print("Permissões do usuario definida como admin!")
                            input("APERTE ENTER PARA CONTINUAR")
                            role = "admin"
                            roleValida = True
                        case "2":
                            self.banner_register()
                            print("Permissões do usuario definida como user!")
                            input("APERTE ENTER PARA CONTINUAR")
                            role = "user"
                            roleValida = True
                        case _:
                            print("Opção invalida!")
                            input("APERTE ENTER PARA CONTINUAR")
                usuarioCadastrado = False
                while not usuarioCadastrado:
                    self.banner_register()
                    print("Cadastrando...")
                    sleep(1)
                    self.banner_register()
                    if not user_in_db(self.database, login):
                        usuarioCadastrado = register_user(
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
                        self.banner_register()
                        usuarioCadastrado = True
                        raise Exception("Usuario ja cadastrado!")
            if cadastrado:
                self.banner_register()
                print(f"usuario {login} cadastrado com sucesso!")

    def delete_user(self) -> None:
        """
        Delete a user from the database.
        """
        if len(self.database) >= 1:
            if len(self.database) == 1:
                self.banner_delete_users()
                show_users(self.database)
                print("\nExiste apenas 1 usuario adicionado\nnão é possivel remove-lo!")
            else:
                permitido = False
                while not permitido:
                    permitido = validate_perm(self.database, self.usuarioLogado)
                    if not permitido:
                        self.banner_delete_users()
                        print("O seu usuario não tem permissões para isso.")
                        break
                if permitido:
                    if not validate_if_all_admin(self.database):
                        usuarioDeletado = False
                        while not usuarioDeletado:
                            indiceValido = False
                            while not indiceValido:
                                self.banner_delete_users()
                                show_users(self.database)
                                indice = str(
                                    input(
                                        "Informe o indice do usuario que deseja deletar: "
                                    )
                                )
                                indiceValido = validate_index(self.database, indice)
                                if not indiceValido:
                                    input("APERTE ENTER PARA CONTINUAR")
                            usuario = self.database[int(indice) - 1]
                            self.banner_delete_users()
                            print("Deletando...")
                            sleep(1)
                            usuarioDeletado = delete_user(
                                self.database, usuario[0], self.usuarioLogado
                            )
                            if not usuarioDeletado:
                                input("APERTE ENTER PARA CONTINUAR")
                        print(f'o usuario "{usuario[0]}" foi deletado com sucesso')
                    else:
                        self.banner_delete_users()
                        print(
                            "Todos os usuarios encontrados são admin, não é possivel remover!"
                        )
        else:
            print("Você esta sem usuarios adicionados")
            input("APERTE ENTER PARA CONTINUAR")

    def search_user(self) -> None:
        """
        Search for a user in the database and display their information.
        """
        userValido = False
        while not userValido:
            indiceValido = False
            while not indiceValido:
                self.banner_search()
                show_users(self.database)
                indiceUsuario = str(input("Informe o indice do usuario: "))
                indiceValido = validate_index(self.database, indiceUsuario)
                if not indiceValido:
                    input("APERTE ENTER PARA CONTINUAR")
            indice = int(indiceUsuario) - 1
            usuario = self.database[indice]
            if user_in_db(self.database, usuario[0]):
                print("Ola")
                self.banner_update()
                self.banner_search()
                print("Procurando...")
                sleep(1)
                userValido = True
            else:
                input("APERTE ENTER PARA CONTINUAR")
        self.banner_search()
        print(f"Usuario {usuario[0]} encontrado!")
        input("APERTE ENTER PARA CONTINUAR!")
        indicesCampos = []
        verificarSaida = False
        while not verificarSaida:
            if len(indicesCampos) == 10:
                self.banner_search()
                print("Todos os campos foram selecionados!")
                input("APERTE ENTER PARA CONTINUAR")
                verificarSaida == True
                break
            campoValido = False
            while not campoValido:
                self.banner_search()
                show_fields()
                campo = input("Informe o indice do campo desejado: ").strip()
                campoValido = validate_field(campo, indicesCampos)
                if not campoValido:
                    input("APERTE ENTER PARA CONTINUAR")
            indicesCampos.append(campo)
            selecionarOutroCampo = False
            while not selecionarOutroCampo:
                self.banner_search()
                resposta = (
                    input("Deseja selecionar outro campo? [Sim/Não]\n").title().strip()
                )
                selecionarOutroCampo = confirm_exit(resposta)
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
            self.banner_search()
            indice_int = int(indice)
            campo = campos[indice_int]
            user = usuario[indice_int]
            if indice_int == 7:
                permitido = False
                while not permitido:
                    permitido = validate_perm(self.database, self.usuarioLogado)
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

    def exit(self) -> None:
        """
        Exit the program after confirming with the user.
        """
        verificarSaida = False
        while not verificarSaida:
            self.banner_exit()
            resposta = input("Deseja mesmo sair? [Sim/Nao]\n").title().strip()
            verificarSaida = confirm_exit(resposta)
            if not verificarSaida:
                input("APERTE ENTER PARA CONTINUAR")
        if resposta == "Sim":
            self.sair = True
            self.banner_exit()
            print("Finalizando...")
            sleep(1)
            self.banner_exit()
            print("Programa finalizado!")
        else:
            print("Certo")

    def show_users(self):
        """
        Show the users in the database.
        """
        self.banner_users()
        print("Buscando usuarios...")
        sleep(1)
        self.banner_users()
        show_users(self.database)

    def run(self) -> None:
        """
        Run the main loop of the application.
        """
        self.auth()
        if self.logado:
            self.sair = False
            while not self.sair:
                try:
                    self.view_menu()
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
                            self.search_user()
                        case "5":
                            # Deletar usuario
                            self.delete_user()
                        case "6":
                            # Sair
                            self.exit()
                        case _:
                            # Caso não for nenhum dos mencionados acima
                            print("Opção invalida!")
                except Exception as e:
                    print(e)
                finally:
                    input("APERTE ENTER PARA CONTINUAR")
                    self.clear()
