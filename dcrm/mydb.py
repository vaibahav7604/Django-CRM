import mysql.connector
# pip install mysql-connector-python
# pip install mysql-connector
# pip install mysql,pip insatall django ,django-admin startproject dcrm,
''' git commands:-# Configuration commands
git config --global user.name "Meghani Vaibhav"
git config --global user.email "vaibhavmeghani79@gmail.com"
git config --global push.default matching
git config --global alias.co checkout

# Initialize a new repository
git init

# Staging and committing changes
git add .
git commit -am 'initial commit'

# Adding a remote repository
git remote add origin https://github.com/vaibahav7604/Django-CRM

# Rename the branch to main
git branch -M main

# Pushing changes to the remote repository
git push -u origin main'''

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