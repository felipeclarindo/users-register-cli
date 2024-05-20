import os
import sys

# Adicionar o diretório pai ao sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.validations import *

# Testes da validação de email
def tests_email_passeds():
    assert validarEmail("aaa@gmail.com") == True
    assert validarEmail("aaaaa@gmail.com.br") == True
    assert validarEmail("fiap.com.br@gmail.com") == True

def tests_email_fails():
    assert validarEmail("") == False
    assert validarEmail("222.gmail.com") == False
    assert validarEmail("a@a.com.br") == False
    assert validarEmail("aaaa@a.b") == False
    assert validarEmail("a@aaaa.c.br") == False
    assert validarEmail("aaa@kdoakd") == False
    assert validarEmail("fiap.com.br@joaopedro") == False

# Testes de validação de usuario
def tests_usuario_passeds():
    assert validarUsuario("FELIpe__") == True
    assert validarUsuario("felipe") == True
    assert validarUsuario("_felipe") == True

def tests_usuario_fails():
    assert validarUsuario("") == False
    assert validarUsuario("aa") == False
    assert validarUsuario("22!!") == False

# Testes de validação de rg
def tests_rg_passeds():
    assert validarRg("123456789") == True
    assert validarRg("         123456789       ") == True

def tests_rg_fails():
    assert validarRg("") == False
    assert validarRg("14425") == False
    assert validarRg("aaa") == False
    assert validarRg("242aaa") == False
    assert validarRg("aaaaaaaaa") == False
    assert validarRg("aaa234567") == False
    assert validarRg("1 2 3 451") == False
    assert validarRg("1 2 3 45 6 7 8 9") == False

# Testes de validação de cpf
def tests_cpf_passeds():
    assert validarCpf("12345678910") == True
    assert validarCpf("     12345678910    ") == True
    
def tests_cpf_fails():
    assert validarCpf("124") == False
    assert validarCpf("aaa") == False
    assert validarCpf("123456789161") == False
    assert validarCpf("1234567aaa6") == False
    assert validarCpf("1324aaa") == False
    assert validarCpf("") == False
    assert validarCpf("") == False

# Testes de validação de senha
def tests_senha_fails():
    assert validarSenha("!!11aaBBcc") == False
    assert validarSenha("11111111111111111") == False
    assert validarSenha("aaaaaaaAAAAAABBBBBB!!!!") == False
    assert validarSenha("11111AAAAaaaaaaaa") == False
    assert validarSenha("!!!!!!!!!!!!!!!!!!!aaaaaBBB") == False
    assert validarSenha("    !!!!!!!!!!!!!!!!!!!aaaaaBBB        ") == False

def tests_senha_passeds():
    assert validarSenha("1111@@aaaaBBBBccc000") == True
    assert validarSenha("       1111@@aaaaBBBBccc000          ") == True  

# Testes de validação de nome
def tests_nome_fails():
    assert validarNome(" ") == False
    assert validarNome("124") == False
    assert validarNome("      13aaa2") == False

def tests_nome_passeds():
    assert validarNome("Joao") == True
    assert validarNome("   Joao          ") == True

# Testes de validação de data
def tests_data_passeds():
    assert validarData("14/02/2022") == True
    assert validarData("31/12/2022") == True
    assert validarData("  15/02/2005   ") == True
    assert validarData("16/05/2024") == True

def tests_data_fails():
    assert validarData("") == False
    assert validarData("32/-2") == False
    assert validarData("1302206") == False
    assert validarData("52/32/20282") == False
    assert validarData("13/02/7034") == False
    assert validarData("32/12/2022") == False
    assert validarData("31/13/2022") == False
    assert validarData("32/13/2022") == False
    assert validarData("31/13/2024") == False
    assert validarData("31/13/2025") == False

def tests_confirmar_saida_passeds():
    assert confimarSaida("Sim") == True
    assert confimarSaida("Nao") == True
    assert confimarSaida("nao") == True
    assert confimarSaida("nAo") == True
    assert confimarSaida("Não") == True
    assert confimarSaida("nÃo") == True
    assert confimarSaida("     Não         ") == True
    
def tests_confirmar_saida_fails():
    assert confimarSaida("") == False
    assert confimarSaida("ola") == False
    assert confimarSaida("n") == False
    assert confimarSaida("ajda") == False
    assert confimarSaida("     oi   ") == False

def tests_validar_role_passeds():
    assert validarRole("admin") == True
    assert validarRole("aDMin") == True
    assert validarRole("user") == True
    assert validarRole("uSeR") == True
    assert validarRole("   user") == True
    assert validarRole("   uSer    ") == True

def tests_validar_roles_fails():
    assert validarRole("") == False
    assert validarRole("oal") == False
    assert validarRole("-10") == False
    assert validarRole("24@") == False
    

def tests_verificar_campos_passeds():
    assert verificarCampo("1",[]) == True
    assert verificarCampo("2", ["5", "6",]) == True
    assert verificarCampo("0", ["1","4","6"]) == True

def tests_verificar_campos_fails():
    assert verificarCampo("1",["1"]) == False
    assert verificarCampo("2", ["2","3"]) == False
    assert verificarCampo("32",["3","2"]) == False
    assert verificarCampo("-1", [""]) == False
    assert verificarCampo("-1", ["-1"]) == False
