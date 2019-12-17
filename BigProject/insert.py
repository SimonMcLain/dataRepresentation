import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="BigProject"
)


cursor = db.cursor()
sql="insert into stores (Name, Technology, Price) values (%s,%s,%s)"
values = ("Amazon", "Universal Translator", 5000)

cursor.execute(sql, values)

db.commit()
print("One record inserted, ID: ", cursor.lastrowid)