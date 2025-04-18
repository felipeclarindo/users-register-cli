🌍 [Leia em Português](README.pt-BR.md)

# Users Register CLI

This program is a command line application for managing users. It allows you to register, update, show, search and delete users. The system also has a login menu for user authentication.

## Data Structure

The system uses a list of tuples to store users' data with the following fields: 1. login 2. login type 3. email 4. name 5. cpf 6. rg 7. date of birth 8. password 9. address 10. role (admin or user)

## Steps to perform

1. Clone the repository:

```bash
git clone git clone https://github.com/felipeclarindo/users-register-cli.git
```

2. Navigate to the project folder:

````bash
cd user-register
```bash
cd user-register
````

3. Run the program:

```bash
python ./src/main.py
```

## How to use

### 1. Authentication

The credentials to authenticate is:

- login: admin
- passwrd: admin

### 2. When starting the program, you will see a main menu. Choose one of the options by typing the corresponding number and pressing Enter:

- 1 - Register user: Register a new user.
- 2 - Update user: Updates the information of an existing user.
- 3 - Show users: Displays the list of registered users.
- 4 - Search user: Search a user based on specified criteria.
- 5 - Delete user: Removes a user from the system.
- 6 - Exit: Closes the program.

### 3. In the login menu, you can choose the authentication method:

- 1 - Email
- 2 - User
- 3 - CPF
- 4 - RG

## Contribution

Contributions are welcome! If you have suggestions for improvements, feel free to open an issue or submit a pull request.

## Author

**Felipe Clarindo**

- [LinkedIn](https://www.linkedin.com/in/felipeclarindo)
- [Instagram](https://www.instagram.com/lipethecoder)
- [GitHub](https://github.com/felipeclarindo)

## License

This project is licensed under the [GNU Affero License](https://www.gnu.org/licenses/agpl-3.0.html).
