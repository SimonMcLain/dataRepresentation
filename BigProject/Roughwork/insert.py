import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="CommerceGuildStore"
)


cursor = db.cursor()
sql="insert into guild_store (Name, Technology, Price) values (%s,%s,%s)"
values = ("Hutts", "Imperial Barge", 5000)

cursor.execute(sql, values)

db.commit()
print("One record inserted, ID: ", cursor.lastrowid)