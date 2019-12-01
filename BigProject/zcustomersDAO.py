import mysql.connector
class CustomersDAO:
  db=""
  def __init__(self):
    self.db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="BigProject"
    )
    
  def create(self, values):
    cursor = self.db.cursor()
    sql="INSERT INTO customers (name, technology, price) VALUES (%s, %s, %s)"
    cursor.execute(sql, values)
    
    self.db.commit()
    return cursor.lastrowid
  
  def getAll(self):
    cursor = self.db.cursor()
    sql="SELECT * FROM customers"
    cursor.execute(sql)
    result = cursor.fetchall()
    return result

  def findByID(self, id):
    cursor = self.db.cursor()
    sql="SELECT * FROM customers WHERE id = %s"
    values = (id,)

    cursor.execute(sql, values)
    result = cursor.fetchall()
    return result

  def update(self, values):
    cursor = self.db.cursor()
    sql="UPDATE customers SET name=%s, price=%s WHERE id = %s"
    cursor.execute(sql, values)
    self.db.commit()
  
  def delete(self, id):
    cursor = self.db.cursor()
    sql="DELETE FROM customers WHERE id = %s"
    values = (id,)
    cursor.execute(sql, values)
    self.db.commit()

    print("Delete done")

customersDAO = CustomersDAO()


