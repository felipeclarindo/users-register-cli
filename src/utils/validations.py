import datetime

<<<<<<< HEAD
def validarIndice(database:list[tuple], indice:str):
    try:
        indice = indice.strip()
        quantidadeUser = len(database) 
=======

def validarIndice(database: list[tuple], indice: str):
    try:
        indice = indice.strip()
        quantidadeUser = len(database)
>>>>>>> developer/felipe
        if indice.isdigit():
            indice = int(indice) - 1
            if indice >= 0 and indice < quantidadeUser:
                return True
            else:
<<<<<<< HEAD
                 raise Exception("Informe o indice de acordo com os indices apresentados!")
=======
                raise Exception(
                    "Informe o indice de acordo com os indices apresentados!"
                )
>>>>>>> developer/felipe
        else:
            raise Exception("Indice invalido, é aceito apenas numeros!")
    except ValueError:
        print("Valor invalido")
    except Exception as e:
        print(e)
    return False

<<<<<<< HEAD
def validarSenha(senha:str) -> bool:
=======

def validarSenha(senha: str) -> bool:
>>>>>>> developer/felipe
    try:
        senha = senha.strip()
        if len(senha) == 0:
            raise ValueError("A Senha não pode ser vazia!")
        elif len(senha) >= 15:
            numericos = 0
            maiusculo = 0
            minusculo = 0
            especiais = 0
            for caracter in senha:
                if caracter.isdigit():
                    numericos += 1
                    continue
                if caracter.isupper():
                    maiusculo += 1
                    continue
                if caracter.islower():
                    minusculo += 1
                    continue
                if caracter in "!@#$%&*()[]{};,.:/\|":
                    especiais += 1
                    continue
            if numericos >= 2 and maiusculo >= 2 and minusculo >= 2 and especiais >= 2:
                return True
            else:
                raise Exception("A senha não atende aos requisitos do sistema!")
        else:
            raise Exception("Senha invalida!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False


<<<<<<< HEAD
def validarEmail(email:str) -> bool:
=======
def validarEmail(email: str) -> bool:
>>>>>>> developer/felipe
    try:
        email = email.strip()
        if len(email) > 0:
            if "@" in email:
                email_separado = email.split("@")
                if len(email_separado) == 2:
                    dominio = email_separado[1]
                    if "." in dominio:
                        dominio_separado = dominio.split(".")
                        if len(dominio_separado) in [2, 3]:
                            for dominio_parte in dominio_separado:
                                if len(dominio_parte) < 2 or len(email_separado[0]) < 3:
<<<<<<< HEAD
                                    raise Exception ("Email invalido!")
=======
                                    raise Exception("Email invalido!")
>>>>>>> developer/felipe
                                else:
                                    return True
                        else:
                            raise Exception("Email Invalido")
                    else:
                        raise Exception("Email Invalido")
                else:
                    raise Exception("Email invalido!")
            else:
                raise Exception("É necessario ter @ no email!")
        else:
            raise Exception("O email não pode ser vazio!")
    except ValueError:
        print("Valor invalido")
    except Exception as e:
        print(e)
    return False

<<<<<<< HEAD
def validarUsuario(usuario:str) -> bool:
=======

def validarUsuario(usuario: str) -> bool:
>>>>>>> developer/felipe
    try:
        usuario = usuario.strip()
        if len(usuario) >= 3:
            usuario = usuario.replace("_", "")
            if usuario.isalnum():
                return True
            else:
                raise ValueError("Usuario pode conter apenas numeros letras e _")
        else:
            raise ValueError("O valor do usuario não pode ser menor que 3")
    except Exception as e:
        print(e)
    return False

<<<<<<< HEAD
def validarCpf(cpf:str) -> bool:
=======

def validarCpf(cpf: str) -> bool:
>>>>>>> developer/felipe
    try:
        cpf = cpf.strip()
        if len(cpf) > 0:
            cpf = cpf.replace("-", "").replace(".", "")
            if cpf.isdigit() and len(cpf) == 11:
                return True
            else:
                raise ValueError("O CPF deve conter apenas numeros e 11 algorismos")
        else:
            raise ValueError("O Cpf não pode ser vazio!")
    except Exception as e:
        print(e)
    return False
<<<<<<< HEAD
    
def validarRg(rg:str) -> bool:  
=======


def validarRg(rg: str) -> bool:
>>>>>>> developer/felipe
    try:
        rg = rg.strip()
        if len(rg) > 0:
            rg = rg.replace(".", "").replace("-", "")
            if rg.isdigit() and len(rg) == 9:
                return True
            else:
                raise Exception("O RG deve conter apenas numeros e 9 algorismos")
        else:
            raise ValueError("O Rg não pode ser vazio!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False

<<<<<<< HEAD
def validarLogin(login:str, opcao:str) -> bool:
    try:
        match opcao:
            case "1": #email
                return validarEmail(login)
            case "2": #Usuario
                return validarUsuario(login)
            case "3": #Cpf
                return validarCpf(login)
            case "4": #Rg
=======

def validarLogin(login: str, opcao: str) -> bool:
    try:
        match opcao:
            case "1":  # email
                return validarEmail(login)
            case "2":  # Usuario
                return validarUsuario(login)
            case "3":  # Cpf
                return validarCpf(login)
            case "4":  # Rg
>>>>>>> developer/felipe
                return validarRg(login)
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False

<<<<<<< HEAD
def validarNome(nome:str) -> bool:
=======

def validarNome(nome: str) -> bool:
>>>>>>> developer/felipe
    try:
        nome = nome.strip()
        if len(nome) > 0:
            if nome.isalpha():
                return True
            else:
                raise Exception("Deve ter apenas letras no nome!")
        else:
            raise Exception("O Nome não pode estar vazio!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False

<<<<<<< HEAD
def _validarData(dia:int, mes:int, ano:int,):
=======

def _validarData(
    dia: int,
    mes: int,
    ano: int,
):
>>>>>>> developer/felipe
    try:
        dataAtual = datetime.datetime.now().date()
        verificarDia = dia > 0 and dia <= 31
        verificarMes = mes > 0 and mes <= 12
        verificarAno = ano > 1600 and ano <= dataAtual.year

        if verificarAno and ano == dataAtual.year:
<<<<<<< HEAD
            if verificarDia and dia <= dataAtual.day or verificarMes and mes <= dataAtual.month:
=======
            if (
                verificarDia
                and dia <= dataAtual.day
                or verificarMes
                and mes <= dataAtual.month
            ):
>>>>>>> developer/felipe
                return True
            else:
                raise Exception("O mês/dia não pode ser maior que o mes/dia atual!")
        elif verificarAno:
            if verificarMes:
                if verificarDia:
                    return True
<<<<<<< HEAD
                else: 
                   raise Exception("O Dia deve ser maior que 0 e menor ou igual a 31")
=======
                else:
                    raise Exception("O Dia deve ser maior que 0 e menor ou igual a 31")
>>>>>>> developer/felipe
            else:
                raise Exception("O Mês deve ser maior que 0 e menor ou igual a 12")
        else:
            raise Exception("Ano invalido")
    except ValueError:
        print("Valor invalido")
    except Exception as e:
        print(e)
    return False

<<<<<<< HEAD
def validarData(data:str) -> bool:
=======

def validarData(data: str) -> bool:
>>>>>>> developer/felipe
    try:
        data = data.strip()
        dataAtual = datetime.datetime.now().date()
        if "/" in data:
<<<<<<< HEAD
            if data.count("/") == 2: 
=======
            if data.count("/") == 2:
>>>>>>> developer/felipe
                data_separada = data.split("/")
                ano = data_separada[2]
                mes = data_separada[1]
                dia = data_separada[0]
                if len(dia) == 2 and len(mes) == 2 and dia.isdigit() and mes.isdigit():
                    if len(ano) == 4 and ano.isdigit() and int(ano) <= dataAtual.year:
                        return _validarData(int(dia), int(mes), int(ano))
                    else:
                        raise Exception("Ano invalido!")
                else:
                    raise Exception("Dia ou mes invalido!")
            else:
<<<<<<< HEAD
                raise Exception("Formato de data invalido, O formato deve ser XX/XX/XXXX")
        
        else:
            raise Exception("Formato de data invalido, O formato deve ser XX/XX/XXXX")
        
=======
                raise Exception(
                    "Formato de data invalido, O formato deve ser XX/XX/XXXX"
                )

        else:
            raise Exception("Formato de data invalido, O formato deve ser XX/XX/XXXX")

>>>>>>> developer/felipe
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False

<<<<<<< HEAD
def validarEndereco(endereco:str) -> bool:
=======

def validarEndereco(endereco: str) -> bool:
>>>>>>> developer/felipe
    try:
        endereco = endereco.strip()
        if len(endereco) > 0:
            endereco = endereco.replace(",", "").replace("-", "").replace(" ", "")
            if endereco.isalnum():
                return True
<<<<<<< HEAD
            else: 
                raise Exception("Só é permitido conter numeros, letras e ',-' no endereço!")
=======
            else:
                raise Exception(
                    "Só é permitido conter numeros, letras e ',-' no endereço!"
                )
>>>>>>> developer/felipe
        else:
            raise Exception("O endereço não pode estar vazio!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False

<<<<<<< HEAD
def confirmarSaida(resposta:str) -> bool:
=======

def confirmarSaida(resposta: str) -> bool:
>>>>>>> developer/felipe
    try:
        if len(resposta) > 0:
            if resposta.title().strip() in ["Sim", "Não", "Nao"]:
                return True
            else:
                raise Exception("Digite conforme o informado!")
        else:
            raise Exception("O valor não pode esta vazio!")
    except Exception as e:
        print(e)
    return False

<<<<<<< HEAD
def verificarCampo(campo:str, listaCampos:list[str]) -> bool:
=======

def verificarCampo(campo: str, listaCampos: list[str]) -> bool:
>>>>>>> developer/felipe
    try:
        if campo.isdigit():
            if len(campo) > 0:
                if int(campo) in range(10):
                    if campo not in listaCampos:
                        return True
                    else:
                        raise Exception("Campo ja adicionado!")
                else:
                    raise Exception("Campo invalido!")
            else:
                raise Exception("Valor do campo não pode ser vazio!")
        else:
            raise Exception("O campo precisar ser um dos indices informados!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False

<<<<<<< HEAD
def validarRole(role:str) -> bool:
=======

def validarRole(role: str) -> bool:
>>>>>>> developer/felipe
    try:
        if role.strip().lower() in ["admin", "user"]:
            return role.strip().isalpha()
        else:
            raise Exception("Role pode ser apenas admin ou user")
    except Exception as e:
        print(e)
<<<<<<< HEAD
    return False
=======
    return False
>>>>>>> developer/felipe
