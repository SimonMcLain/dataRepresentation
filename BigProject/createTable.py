import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="BigProject"
)


cursor = db.cursor()

sql="CREATE TABLE stores (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), technology VARCHAR(255), price FLOAT(11))"

cursor.execute(sql)