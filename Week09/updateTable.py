import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="BigProject"
)


cursor = db.cursor()
sql="update student set name=%s, age=%s WHERE id = %s"
values = ("Joe", 33, 1)

cursor.execute(sql, values)

db.commit()
print("update done")