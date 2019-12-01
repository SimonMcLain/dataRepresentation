import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datarepresentation"
)

cursor = db.cursor()
sql="DELETE FROM student WHERE id = %s"
values = (1,)

cursor.execute(sql, values)

db.commit()

print("delete done")