'''
This code creates MySQL Database "contact".
'''
# Import the required module
import mysql.connector

# Establish a connection to MySQL
myDB = mysql.connector.connect(
    host="localhost",  # Host name
    user="root",  # User name
    password=""  # Password
)

# Create a cursor object to interact with the database
myCursor = myDB.cursor()

# Create the database
myCursor.execute("CREATE DATABASE contact")

