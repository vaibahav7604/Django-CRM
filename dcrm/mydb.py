import mysql.connector
# pip install mysql-connector-python
# pip install mysql-connector
# pip install mysql,pip insatall django ,django-admin startproject dcrm,
# git commands:-
dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin'
)

cursor = dataBase.cursor()

# Drop the database if it exists
cursor.execute("DROP DATABASE IF EXISTS Tester")

# Create a new database
cursor.execute("CREATE DATABASE Tester")

print("Database created successfully")