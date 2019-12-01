import mysql.connector
class StudentDAO:
  db=""
  def __init__(self):
    self.db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="datarepresentation"
    )
    
  def create(self, values):
    cursor = self.db.cursor()
    sql="INSERT INTO student (name, age) VALUES (%s, %s)"
    cursor.execute(sql, values)
    
    self.db.commit()
    return cursor.lastrowid
  
  def getAll(self):
    cursor = self.db.cursor()
    sql="SELECT * FROM student"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

  def findByID(self, id):
    cursor = self.db.cursor()
    sql="SELECT * FROM student WHERE id = %s"
    values = (id,)

    cursor.execute(sql, values)
    result = cursor.fetchall()
    return result

  def update(self, values):
    cursor = self.db.cursor()
    sql="UPDATE student SET name=%s, age=%s WHERE id = %s"
    cursor.execute(sql, values)
    self.db.commit()
  
  def delete(self, id):
    cursor = self.db.cursor()
    sql="DELETE FROM student WHERE id = %s"
    values = (id,)
    cursor.execute(sql, values)
    self.db.commit()

    print("Delete done")

studentDAO = StudentDAO()


