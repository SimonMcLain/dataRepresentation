import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datarepresentation"
)


cursor = db.cursor()
sql="insert into student (name, age) values (%s,%s)"
values = ("Wendy", 21)

cursor.execute(sql, values)

db.commit()
print("One record inserted, ID: ", cursor.lastrowid)