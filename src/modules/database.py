from pprint import pprint
from hashlib import sha256


def protect_password(password: str) -> str:
    """
    Hash the password using SHA-256.

    Args:
        password (str): The password to hash.

    Returns:
        str: The hashed password.
    """
    hash = sha256()
    hash.update(password.encode())
    return hash.hexdigest()


def show_fields() -> None:
    """
    Show the fields of the user in the database.
    """
    fields = [
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
    metade = len(fields) // 2
    for indice in range(metade):
        coluna1 = f"{indice} -> {fields[indice].title()}"
        coluna2 = f"{indice + metade} -> {fields[indice + metade].title()}"
        while len(coluna1) < 25:
            coluna1 += " "
        print(f"{coluna1} {coluna2}")


def validate_if_all_admin(database: list[tuple]) -> bool:
    """
    Check if all users in the database are admins.

    Args:
        database (list[tuple]): The database of users.

    Returns:
        bool: True if all users are admins, False otherwise.
    """
    cont = 0
    for user in database:
        if user[9] == "admin":
            cont += 1
    if cont == len(database):
        return True
    else:
        return False


def delete_user(database: list[tuple], user: str, logged_user: str) -> bool:
    """
    Delete a user from the database.

    Args:
        database (list[tuple]): The database of users.
        user (str): The user to delete.
        logged_user (str): The user who is logged in.

    Raises:
        Exception: If the user is not found or if the logged user is trying to delete themselves.

    Returns:
        bool: True if the user was deleted, False otherwise.
    """
    try:
        for user in database:
            if user != logged_user:
                permicaoUserAtual = validate_perm(database, logged_user)
                permicaoUserSelecionado = validate_perm(database, user)
                if permicaoUserAtual != permicaoUserSelecionado:
                    if user[0] == user:
                        database.remove(user)
                        return True
                else:
                    raise Exception("Você não pode remover outro admin!")
            else:
                raise Exception("Você não pode deletar o usuario que esta logado!")
        else:
            raise Exception("Usuario não encontrado!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False


def validate_index(database: list[tuple], *indices) -> bool:
    """
    Validate if the indices are in the database.

    Args:
        database (list[tuple]): The database of users.

    Returns:
        bool: True if all indices are in the database, False otherwise.
    """
    contador = 0
    for indice in indices:
        for i in enumerate(database):
            if indice == i:
                contador += 1
    else:
        if contador == len(indices):
            return True
        else:
            return False


def search_user_field(database: list[tuple], user: str, field_expected: str) -> None:
    """
    Search for a user in the database and print the field expected.

    Args:
        database (list[tuple]): The database of users.
        user (str): The user to search for.
        field_expected (str): The field to print.

    Raises:
        Exception: If the user is not found or if the field is not found.
    """
    try:
        if user_in_db(database, user):
            for usuario in database:
                if usuario[0] == user:
                    match field_expected:
                        case "0":
                            print(usuario[0])
                        case "1":
                            print(usuario[1])
                        case "2":
                            print(usuario[2])
                        case "3":
                            print(usuario[3])
                        case "4":
                            print(usuario[4])
                        case "5":
                            print(usuario[5])
                        case "6":
                            print(usuario[6])
                        case "7":
                            print(usuario[7])
                        case "8":
                            print(usuario[8])
                        case "9":
                            print(usuario[9])
                        case _:
                            raise Exception("Campo não encontrado")
        else:
            raise Exception("Usuario não existente!")
    except Exception as e:
        print(e)


def show_users(database: list[tuple]) -> None:
    """
    Show the users in the database.

    Args:
        database (list[tuple]): The database of users.

    Raises:
        Exception: If there are no users in the database.
    """
    if len(database) > 0:
        for i, usuario in enumerate(database):
            print(f"{i+1} - {usuario[0]}")
    else:
        raise Exception("Nenhum usuario cadastrado!")


def user_in_db(database: list[tuple], usuario: str) -> bool:
    """
    Check if the user is in the database.

    Args:
        database (list[tuple]): The database of users.
        usuario (str): The user to check.

    Raises:
        Exception: If the user is not found.

    Returns:
        bool: True if the user is in the database, False otherwise.
    """
    try:
        for user in database:
            if user[0] == usuario:
                return True
        else:
            raise Exception("Usuario não encontrado!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False


def validate_user(database: list[tuple], login: str, password: str) -> bool:
    """
    Validate if the user is in the database and if the password is correct.

    Args:
        database (list[tuple]): The database of users.
        login (str): The user to check.
        password (str): The password to check.

    Returns:
        bool: True if the user is in the database and the password is correct, False otherwise.
    """
    for user in database:
        login_cadastrado = user[0]
        senha_cadastrada = user[7]
        if login == login_cadastrado and password == protect_password(senha_cadastrada):
            return True
    return False


def validate_perm(database: list[tuple], usuario: str) -> bool:
    """
    Validate if the user is an admin.

    Args:
        database (list[tuple]): The database of users.
        usuario (str): The user to check.

    Returns:
        bool: True if the user is an admin, False otherwise.
    """
    for user in database:

        if user[0] == usuario:
            if user[9] == "admin":
                return True
    else:
        return False


def register_user(
    database: list[tuple],
    login: str,
    login_type: str,
    email: str,
    name: str,
    rg: str,
    cpf: str,
    birth_date: str,
    password: str,
    address: str,
    role: str,
) -> bool:
    """
    Register a user in the database.

    Args:
        database (list[tuple]): The database of users.
        login (str): User login.
        login_type (str): User login type (email, login, rg or cpf).
        email (str): User email.
        name (str): User name.
        rg (str): User RG.
        cpf (str): User CPF.
        birth_date (str): User birth date.
        password (str): User password.
        address (str): User address.
        role (str): User role (admin or user).

    Returns:
        bool: _description_
    """
    try:
        database.append(
            (
                login,
                login_type,
                email,
                name,
                rg,
                cpf,
                birth_date,
                protect_password(password),
                address,
                role,
            )
        )
        return True
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False


def get_user_index(database: list[tuple], user: str) -> int:
    """
    Get the index of the user in the database.

    Args:
        database (list[tuple]): The database of users.
        user (str): The user to search for.

    Raises:
        Exception: If the user is not found.

    Returns:
        int: The index of the user in the database.
    """
    try:
        for e, user in enumerate(database):
            if user[0].lower() == user.lower():
                return e
        raise Exception("Usuario não esta no banco de dados!")
    except ValueError:
        print("Valor invalido")
    except Exception as e:
        print(e)
