# Banking System Documentation

## Introduction

The Banking System is a command-line-based application that simulates basic banking operations such as user registration, login, account management, and financial transactions. This documentation provides an overview of the system architecture, functionalities, and usage instructions.

## Table of Contents

1. [System Architecture](#system-architecture)
2. [Classes and Modules](#classes-and-modules)
3. [Functionality Overview](#functionality-overview)
4. [Usage Instructions](#usage-instructions)
5. [Future Improvements](#future-improvements)
6. [Contributing](#contributing)
7. [License](#license)

## System Architecture

The system is built using Python and utilizes the MySQL database for data storage. The main components include:

- **Database Management:**
  - `DataBase` class manages the connection to the MySQL database and handles user-related queries.

- **User Management:**
  - `UserAlgo` class provides methods for user registration, login, and basic account operations.

- **User Interface:**
  - `choose`, `OPEN`, and `LOGIN` classes handle the user interface and interaction.

- **Main Menu:**
  - `main` class displays the main menu for logged-in users, offering various banking operations.

## Classes and Modules

- **`DataBase`:**
  - Manages database connections and user-related queries.

- **`UserAlgo`:**
  - Handles user registration, login, and basic account operations.

- **`LoginUser` and `RegisterUser`:**
  - Data classes for organizing user input for login and registration.

- **`main`, `OPEN`, `LOGIN`:**
  - Classes responsible for the main menu, account opening, and login processes.

- **`choose`:**
  - Manages the initial menu for choosing between login, account opening, or quitting.

## Functionality Overview

1. **User Registration:**
   - New users can register by providing account details such as account number, name, email, address, and PIN.

2. **Login:**
   - Existing users can log in by entering their account number and PIN.

3. **Main Menu:**
   - Logged-in users can access the main menu to perform various operations:
     - View account details.
     - Check account balance.
     - Transfer money to other accounts.
     - Withdraw money.
     - Deposit money.
     - Logout.

4. **Database Operations:**
   - Database operations include updating account balances, transferring funds between accounts, and fetching user details.

## Usage Instructions

1. **Installation:**
   - Ensure Python is installed.
   - Install the required MySQL connector: `pip install mysql-connector-python`.

2. **Database Setup:**
   - Create a MySQL database named "Bank" and execute the SQL script provided.

3. **Run the Application:**
   - Execute the Python script: `python banking_system.py`.

4. **Follow On-screen Prompts:**
   - Follow the on-screen prompts to register, login, and perform banking operations.

## Future Improvements

- Enhanced error handling and input validation.
- Improved user interface with a graphical user interface (GUI).
- Additional security measures, such as password hashing.
- Support for multiple user accounts and concurrent sessions.

## Contributing

If you would like to contribute to the project, please follow the contribution guidelines in the repository.

## License

This project is licensed under the [MIT License](LICENSE).
