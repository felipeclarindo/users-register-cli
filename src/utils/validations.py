import datetime

def validarSenha(senha:str) -> bool:
    try:
        if len(senha) == 0:
            raise ValueError("A Senha ão pode ser vazia!")
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
            raise ValueError("Senha invalida!")
        return False
    except Exception as e:
        print(e)

def validarLogin(login:str, opcao:str) -> bool:
    try:
        match opcao:
            case "1": #email
                if len(login) > 0:
                    login_separado = login.split("@")
                    dominio_separado = login_separado[1].split(".")
                    if len(login_separado) == 2 or len(dominio_separado) in [2,3]:
                        for dominio, login in dominio_separado, login_separado:
                            if len(dominio) == 2 or len(login) == 2 :
                                return True
                            else:
                                raise ValueError("Email invalido!")
                    else:
                        raise ValueError("Email invalido!")
                else:
                    raise ValueError("O email não pode ser vazio!")
                return False
            
            case "2": #Usuario
                if len(login) > 0:
                    for caracter in login:
                        if "_" in caracter:
                            caracter = caracter.replace("_", "")
                        if caracter.isalnum():
                            return True
                        else:
                            raise ValueError("Usuario pode conter apenas numeros letras e _")
                else:
                    raise ValueError("O valor do usuario não pode ser vazio")
                return False
            
            case "3": #Cpf
                if len(login) > 0:
                    if ".-" in login:
                        login = login.replace(".", "")
                        login = login.replace("-", "")

                    if login.isdigit() and len(login) == 11:
                        return True
                    else:
                        raise ValueError("O CPF deve conter apenas numeros e 11 algorismos")
                else:
                    raise ValueError("O Cpf não pode ser vazio!")
                return False
            
            case "4": #Rg
                if len(login) > 0:
                    if ".-" in login:
                        login = login.replace(".", "")
                        login = login.replace("-", "")
                    if login.isdigit() and len(login) == 9:
                        return True
                    else:
                        raise ValueError("O RG deve conter apenas numeros e 9 algorismos")
                else:
                    raise ValueError("O Rg não pode ser vazio!")
                return False
    except Exception as e:
        print(e)

def validarData(data:str) -> bool:
    dataAtual = datetime.datetime.now().date()
    ano = dataAtual.year
    mes = dataAtual.month
    dia = dataAtual.day

    data_separada = data.split("/")
    contador = 0
    for data in data_separada:
        if len(data) != 2:
            return False
        contador += 1
    if contador != 3:
        return False
    else:
        if data_separada[0] > dia and data_separada[1] and data_separada[2] > ano:
            return False
    return True