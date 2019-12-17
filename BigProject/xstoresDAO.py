import mysql.connector

class StoresDAO:
  db=""
  def __init__(self):
    self.db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bigproject",
    auth_plugin='mysql_native_password'
    )
    
  def create(self, values):
    cursor = self.db.cursor()
    sql="INSERT INTO stores (Name, Technology, Price) VALUES (%s, %s, %s)"
    cursor.execute(sql, values)
    
    self.db.commit()
    return cursor.lastrowid
  
  def getAll(self):
    cursor = self.db.cursor()
    sql="SELECT * FROM stores"
    cursor.execute(sql)
    results = cursor.fetchall()
    returnArray = []
    print(results)
    for result in results:
      print(result)
      returnArray.append(self.convertToDict(result))
    return returnArray

  def findById(self, id):
    cursor = self.db.cursor()
    sql="SELECT * FROM stores WHERE id = %s"
    values = (id,)

    cursor.execute(sql, values)
    result = cursor.fetchone()
    return self.convertToDict(result)

  def update(self, values):
    cursor = self.db.cursor()
    sql="UPDATE stores SET Name=%s, Technology=%s, Price=%s WHERE id = %s"
    cursor.execute(sql, values)
    self.db.commit()
  
  def delete(self, id):
    cursor = self.db.cursor()
    sql="DELETE FROM stores WHERE id = %s"
    values = (id,)
    cursor.execute(sql, values)
    self.db.commit()
    print("Delete done")

  def convertToDict(self, result):
    colNames=['id', 'Name', 'Technology', 'Price']
    item = {}
    
    if result:
      for i, colName in enumerate(colNames):
        value = result[i]
        item[colName] = value
      
    return item

storesDAO = StoresDAO()


