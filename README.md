# Flask Virtual Market

Welcome to Flask Virtual Market! This web application is designed to provide users with a virtual market experience, enabling them to register, buy and sell products, and manage their credits. Built with Python and Flask, Flask Virtual Market also utilizes a database to store user information, product details, and owned items by the user. This README provides an overview of the project and how to get started.

<br>

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Features](#features).
5. [Future Enhancements](#future-enhancements)
6. [Conclusion](#conclusion)

## Introduction

Flask Virtual Market is a user-friendly web application that simulates a virtual online market platform. Users can create an account, log in, and interact with the virtual market. They can use their credits to buy products available on the market or list their own products for sale, creating a dynamic and engaging marketplace.

## Installation

To run Flask Virtual Market on your local machine, follow these installation steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/flask-virtual-market.git
```

2. Navigate to the project directory:

```bash
cd flask-virtual-market
```

3. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

4. Activate the virtual environment:

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

   - On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

5. Install the required dependencies:

   - Tools include VS Code (or any Code Editor), DB Browser for SQlite (or other), Latest Version of Python (my version `Python 3.11`), and some VS code plugins.
   - Install packages/modules of Flask : `flask`, `flask_login`, `flask_wtf`, `flask_sqlalchemy` and more....
  
6. Set up the database:

   - Configure your preferred database (e.g., SQLite, MySQL, PostgreSQL) inside `__init__.py` and for creating database go to terminal & import `__init__.py` for `app` & `db`, then import `models.py` for using the models to create tables and feeding the data.

7. Initialize the database

## Usage

1. Start the Flask development server:

```bash
flask run
```

2. Open your web browser and go to `http://localhost:5000`.

3. Register a new account or log in if you already have an account.

4. Upon logging in, you can explore the virtual market and use your credits to purchase products from other sellers.

5. To list your products for sale, use the provided functionality.

## Features

- User registration and authentication system.
- Browse and search for products in the virtual market.
- Purchase products from other sellers using credits.
- Ability for users to list their own products for sale.
- Credit management system to track user credits.
- Integration with a database to store user data, product information, and transaction history.


## Future Enhancements

We have some of exciting plans which might be added for Flask Virtual Market in the future. Some of the planned enhancements include:

- Improved user interface and design.
- Advanced search and filtering options for products.
- User ratings and reviews for sellers and products.
- Real-time notifications for transactions.
- Enhanced user profiles with customization options.


## Conclusion

Thank you for checking out Flask Virtual Market!  Happy shopping and selling! 🛍️
