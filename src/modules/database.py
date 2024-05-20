from pprint import pprint
from hashlib import sha256

def protegerSenha(senha:str) -> str:
    hash = sha256()
    hash.update(senha.encode())
    return hash.hexdigest()

def mostrarCampos() -> None:
    campos = ["login", "tipo de Login","email", "nome", "cpf", "rg", "data de nascimento", "senha", "endereco", "role"]       
    for i, campo in enumerate(campos):
        print(f"{i} - {campo.title()}")

def deletarUsuario(bd:list[tuple], usuario:str, usuarioLogado:str) -> None:
    try:
        for user in bd:
            if usuario != usuarioLogado:
                permicaoUserAtual = verificarPermissão(usuarioLogado)
                permicaoUserSelecionado = verificarPermissão(usuario)
                if permicaoUserAtual and permicaoUserSelecionado:
                    raise Exception("Você não pode remover outro admin!")
                else:
                    if user[0] == usuario:
                        bd.remove(user)
                        return True
            else:
                raise Exception("Você não pode deletar o usuario que esta logado!")
        else:
            raise Exception("Usuario não encontrado!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False

def verificarIndice(bd, *indices):
    contador = 0
    for indice in indices:
        for i in enumerate(bd):
            if indice == i:
                contador += 1
    else:
        if contador == len(indices):
            return True
        else:
            return False

def buscarCampoUsuario(bd:list[tuple], user:str, campoDesejado:str) -> None:
    try:
        if usuarioInBd(bd, user):
            for usuario in bd:
                if usuario[0] == user:
                    match campoDesejado:
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

def mostrarUsuarios(bd:list[tuple]) -> None:
    if len(bd) > 0:
        for i, usuario in enumerate(bd):
            print(f"{i+1} - {usuario[0]}")
    else:
        raise Exception("Nenhum usuario cadastrado!")
        
def usuarioInBd(bd:list[tuple], usuario:str) -> bool:
    try:
        for user in bd:
            if user[0] == usuario:
                    return True
            else:
                raise Exception("Usuario não encontrado!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False

def validateUser(bd:list[tuple], login:str, senha:str) -> bool:
    for usuario in bd:
        login_cadastrado = usuario[0]
        senha_cadastrada  = usuario[7]
        if login == login_cadastrado and senha == protegerSenha(senha_cadastrada):
            return True
    return False

def verificarPermissão(bd:list[tuple], usuario:str) -> bool:
    for user in bd:
        if user[0] == usuario:
            if user[9] == "admin":
                return True
    else:
        return False

def cadastrarUsuario(bd:list[tuple], login:str, tipo:str, email:str, nome:str, rg:str, cpf:str, nascimento:str, senha:str, endereco:str, role:str) -> bool:
    try:
        if not usuarioInBd:
            bd.append((login, tipo, email, nome, rg, cpf, nascimento, senha, endereco, role))
            return True
        else:
            raise Exception("Usuario ja existente!")
    except ValueError:
        print("Valor invalido!")
    except Exception as e:
        print(e)
    return False

def pegarIndiceDoUsuario(database:list[tuple], usuario:str) -> int:
    try:
        for e, user in enumerate(database):
            if user[0] == usuario:
                return e
        else:
            raise Exception("Usuario não esta no banco de dados!")
    except ValueError:
        print("Valor invalido")
    except Exception as e:
        print(e)