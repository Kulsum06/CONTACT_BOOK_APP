import mysql.connector
import time
# Establish connection to the MySQL database
db = mysql.connector.connect(
  host="localhost", # Host name
  user="root", # User name
  password="", # password
  database="contact" #Database name
)
if db==None:
  print("not connected")
else:
  print("connected")
from collections import Counter #built in
from tabulate import tabulate #pip install tabulate
import time #built in
cursor = db.cursor()
cursor.execute(""" CREATE TABLE IF NOT EXISTS book (
  name char(30) primary key,
  address char(100),
  mobile char(15),
  email char(30)
);
""")
