from src.utils.validations import *

def tests_email():
    assert validarLogin("aaa@gmail.com", "1") == True
    assert validarLogin("aaaaa@gmail.com.br", "1") == True
    assert validarLogin("a@a.com.br", "1") == False
    assert validarLogin("aaaa@a.b", "1") == False
    assert validarLogin("a@aaaa.c.br", "1") == False

def tests_usuario():
    assert validarLogin("", "2")
    assert validarLogin("", "2")
    assert validarLogin("", "2")
    assert validarLogin("", "2")
    assert validarLogin("", "2")
    assert validarLogin("", "2")

def tests_rg():
    assert validarLogin("", "3")
    assert validarLogin("", "3")
    assert validarLogin("", "3")
    assert validarLogin("", "3")
    assert validarLogin("", "3")
    assert validarLogin("", "3")

def tests_cpf():
    assert validarLogin("", "4")
    assert validarLogin("", "4")
    assert validarLogin("", "4")
    assert validarLogin("", "4")
    assert validarLogin("", "4")
    assert validarLogin("", "4")


def tests_senha():
    assert validarSenha("!!11aaBBcc") == False
    assert validarSenha("11111111111111111") == False
    assert validarSenha("aaaaaaaAAAAAABBBBBB!!!!") == False
    assert validarSenha("11111AAAAaaaaaaaa") == False
    assert validarSenha("1111@@aaaaBBBBccc000") == True
    assert validarSenha("!!!!!!!!!!!!!!!!!!!aaaaaBBB") == False

