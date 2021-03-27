# Ledger

Ledger is a python and mysql based command-line application.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies.

```bash
pip install mysql-connector-python
```

## Usage

First, you have to set the database credentials. Go into 'Database' -> 'database.py', change 'user' and 'password' as your local mysql username and password.

For the first time, as there will be no database or tables for the application, it will create one. Every time after that, it will try to access the created database. The initial balance is defined 0 (zero).

Tasks:

    * A product can be added by giving the name, buy price, sell price, quantity in the inventory as input.
    * A product can be deleted if that is in the inventory by giving the name.
    * A product can be bought if that is in the inventory by giving name and quantity as input till his balanace is sufficient.
    * A product can be sold if that is in the inventory by giving name and quantity as input till he runs out the product.
    * All the products can be shown in a tabular form that are available in the inventory.
    * Current balance can be showed.
