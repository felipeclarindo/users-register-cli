import datetime


def validate_index(database: list[tuple], index: str) -> bool:
    """
    Function to validate the index of a list of tuples.

    Args:
        database (list[tuple]): The list of tuples representing the database.
        index (str): The index to be validated.

    Raises:
        Exception: If the index is not a digit or is out of range.

    Returns:
        bool: True if the index is valid, False otherwise.
    """
    try:
        index = index.strip()
        userQuantity = len(database)
        if index.isdigit():
            index = int(index) - 1
            if index >= 0 and index < userQuantity:
                return True
            else:
                raise Exception(
                    "Informe o indice de acordo com os indices apresentados!"
                )
        else:
            raise Exception("Indice invalido, é aceito apenas numeros!")
    except ValueError:
        print("Valor invalido")
    except Exception as e:
        print(e)
    return False


def validate_password(password: str) -> bool:
    """
    Function to validate the password.

    Args:
        password (str): The password to be validated.

    Raises:
        Exception: If the password does not meet the requirements.

    Returns:
        bool: True if the password is valid, False otherwise.
    """
    try:
        password = password.strip()
        if len(password) == 0:
            raise ValueError("A senha não pode ser vazia!")
        elif len(password) >= 15:
            numericos = 0
            maiusculo = 0
            minusculo = 0
            especiais = 0
            for caracter in password:
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
                raise Exception("A password não atende aos requisitos do sistema!")
        else:
            raise Exception("password invalida!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False


def validate_email(email: str) -> bool:
    """
    Function to validate the email address.

    Args:
        email (str): The email address to be validated.

    Raises:
        Exception: If the email address does not meet the requirements.

    Returns:
        bool: True if the email address is valid, False otherwise.
    """
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
                                    raise Exception("Email invalido!")
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


def validate_user(user: str) -> bool:
    """
    Function to validate the user.

    Args:
        user (str): The user to be validated.

    Raises:
        ValueError: Error in the value.
        Exception: If the user does not meet the requirements.

    Returns:
        bool: _description_
    """
    try:
        user = user.strip()
        if len(user) >= 3:
            user = user.replace("_", "")
            if user.isalnum():
                return True
            else:
                raise ValueError("Usuario pode conter apenas numeros letras e _")
        else:
            raise ValueError("O valor do usuario não pode ser menor que 3")
    except Exception as e:
        print(e)
    return False


def validate_cpf(cpf: str) -> bool:
    """
    Function to validate the CPF (Cadastro de Pessoas Físicas) number.

    Args:
        cpf (str): The CPF number to be validated.

    Raises:
        ValueError: Error in the value.

    Returns:
        bool: True if the CPF number is valid, False otherwise.
    """
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


def validate_rg(rg: str) -> bool:
    """
    Function to validate the RG (Registro Geral) number.

    Args:
        rg (str): The RG number to be validated.

    Raises:
        ValueError: Error in the value.
        Exception: If the RG number does not meet the requirements.

    Returns:
        bool: True if the RG number is valid, False otherwise.
    """
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


def validate_login(login: str, option: str) -> bool:
    """
    Function to validate the login information.

    Args:
        login (str): login to be validated.
        option (str): option to validate the login.

    Returns:
        bool: True if the login is valid, False otherwise.
    """
    try:
        match option:
            case "1":  # email
                return validate_email(login)
            case "2":  # Usuario
                return validate_user(login)
            case "3":  # Cpf
                return validate_cpf(login)
            case "4":  # Rg
                return validate_rg(login)
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False


def validate_name(name: str) -> bool:
    """
    Function to validate the name.

    Args:
        name (str): The name to be validated.

    Raises:
        Exception: If the name does not meet the requirements.

    Returns:
        bool: _description_
    """
    try:
        name = name.strip()
        if len(name) > 0:
            if name.isalpha():
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


def _validate_data(
    day: int,
    month: int,
    year: int,
) -> True:
    """
    Function to validate the date.

    Args:
        day (int): The day to be validated.
        month (int): The month to be validated.
        year (int): The year to be validated.

    Raises:
        Exception: If the date does not meet the requirements.

    Returns:
        True: If the date is valid, False otherwise.
    """
    try:
        dataAtual = datetime.datetime.now().date()
        verificarDia = day > 0 and day <= 31
        verificarMes = month > 0 and month <= 12
        verificarAno = year > 1600 and year <= dataAtual.year

        if verificarAno and year == dataAtual.year:
            if (
                verificarDia
                and day <= dataAtual.day
                or verificarMes
                and month <= dataAtual.month
            ):
                return True
            else:
                raise Exception("O mês/dia não pode ser maior que o mes/dia atual!")
        elif verificarAno:
            if verificarMes:
                if verificarDia:
                    return True
                else:
                    raise Exception("O Dia deve ser maior que 0 e menor ou igual a 31")
            else:
                raise Exception("O Mês deve ser maior que 0 e menor ou igual a 12")
        else:
            raise Exception("Ano invalido")
    except ValueError:
        print("Valor invalido")
    except Exception as e:
        print(e)
    return False


def validate_date(data: str) -> bool:
    """
    Function to validate the date.

    Args:
        data (str): The date to be validated.

    Raises:
        Exception: If the date does not meet the requirements.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        data = data.strip()
        dataAtual = datetime.datetime.now().date()
        if "/" in data:
            if data.count("/") == 2:
                data_split = data.split("/")
                year = data_split[2]
                month = data_split[1]
                day = data_split[0]
                if (
                    len(day) == 2
                    and len(month) == 2
                    and day.isdigit()
                    and month.isdigit()
                ):
                    if (
                        len(year) == 4
                        and year.isdigit()
                        and int(year) <= dataAtual.year
                    ):
                        return _validate_data(int(day), int(month), int(year))
                    else:
                        raise Exception("Ano invalido!")
                else:
                    raise Exception("Dia ou mes invalido!")
            else:
                raise Exception(
                    "Formato de data invalido, O formato deve ser XX/XX/XXXX"
                )

        else:
            raise Exception("Formato de data invalido, O formato deve ser XX/XX/XXXX")

    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False


def validate_address(address: str) -> bool:
    """
    Function to validate the address.

    Args:
        address (str): The address to be validated.

    Raises:
        Exception: If the address does not meet the requirements.

    Returns:
        bool: True if the address is valid, False otherwise.
    """
    try:
        address = address.strip()
        if len(address) > 0:
            address = address.replace(",", "").replace("-", "").replace(" ", "")
            if address.isalnum():
                return True
            else:
                raise Exception(
                    "Só é permitido conter numeros, letras e ',-' no endereço!"
                )
        else:
            raise Exception("O endereço não pode estar vazio!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False


def confirm_exit(response: str) -> bool:
    """
    Function to confirm exit.

    Args:
        response (str): The response to be validated.

    Raises:
        Exception: If the response does not meet the requirements.

    Returns:
        bool: True if the response is valid, False otherwise.
    """
    try:
        if len(response) > 0:
            if response.title().strip() in ["Sim", "Não", "Nao"]:
                return True
            else:
                raise Exception("Digite conforme o informado!")
        else:
            raise Exception("O valor não pode esta vazio!")
    except Exception as e:
        print(e)
    return False


def validate_field(field: str, field_list: list[str]) -> bool:
    """
    Function to validate the field.

    Args:
        field (str): The field to be validated.
        field_list (list[str]): The list of fields to be validated.

    Raises:
        Exception: If the field does not meet the requirements.

    Returns:
        bool: True if the field is valid, False otherwise.
    """
    try:
        if field.isdigit():
            if len(field) > 0:
                if int(field) in range(10):
                    if field not in field_list:
                        return True
                    else:
                        raise Exception("Campo ja adicionado!")
                else:
                    raise Exception("Campo invalido!")
            else:
                raise Exception("Valor do campo não pode ser vazio!")
        else:
            raise Exception("O campo precisar ser um dos indexs informados!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False


def validate_role(role: str) -> bool:
    """
    Function to validate the role.

    Args:
        role (str): The role to be validated.

    Raises:
        Exception: If the role does not meet the requirements.

    Returns:
        bool: True if the role is valid, False otherwise.
    """
    try:
        if role.strip().lower() in ["admin", "user"]:
            return role.strip().isalpha()
        else:
            raise Exception("Role pode ser apenas admin ou user")
    except Exception as e:
        print(e)
    return False
