🌍 [Read in English](README.md)

# Users Register CLI

Este programa é uma aplicação de linha de comando para gerenciar usuários. Ele permite cadastrar, atualizar, mostrar, pesquisar e deletar usuários. O sistema também possui um menu de login para autenticação dos usuários.

## Estrutura de Dados

O sistema usa uma lista de tuplas para armazenar os dados dos usuários com os seguintes campos: 1. login 2. tipo-login 3. email 4. nome 5. cpf 6. rg 7. data-nascimento 8. senha 9. endereco 10. role (admin ou user)

## Passos para execução

1. Clone o repositório do Projeto para sua máquina:

```bash
git clone https://github.com/felipeclarindo/users-register-cli.git
```

2. Navegue até a pasta do projeto:

```bash
cd user-register
```

3. Execute o programa:

```bash
python src/main.py
```

## Como usar

### 1. Autenticação

As credenciais para autenticação são:

- login: admin
- passwrd: admin

### 2. Ao iniciar o programa, você verá um menu principal. Escolha uma das opções digitando o número correspondente e pressionando Enter:

- 1 - Cadastrar usuário: Cadastra um novo usuário.
- 2 - Atualizar usuário: Atualiza as informações de um usuário existente.
- 3 - Mostrar usuários: Exibe a lista de usuários cadastrados.
- 4 - Pesquisar usuário: Pesquisa um usuário com base em critérios especificados.
- 5 - Deletar usuário: Remove um usuário do sistema.
- 6 - Sair: Encerra o programa.

### 3. No menu de login, você pode escolher o método de autenticação:

- 1 - Email
- 2 - Usuário
- 3 - CPF
- 4 - RG

## Contribuições

Contribuições são bem-vindas! Se você encontrar algum problema ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autor

Desenvolvido por **Felipe Clarindo**.

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo/)
- [Instagram](https://www.instagram.com/lipethegoat)
- [GitHub](https://github.com/felipeclarindo)

## Licença

Este projeto está licenciado sob a [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
