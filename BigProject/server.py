#!flask/bin/python
from flask import Flask, jsonify, request, abort
from zcustomersDAO import customerDAO

app = Flask(__name__, static_url_path='', static_folder='.')
#app.config["DEBUG"] = True 
# PUT THIS INTO A DATABASE INSTEAD OF A FILE

customers=[
          {"id": 1, "Name": "FaceBook", "Technology": "Time-Travel", "Price": 50000},
          {"id": 2, "Name": "Amazon", "Technology": "Flying Cars", "Price": 500},
          {"id": 3, "Name": "Intel", "Technology": "Quantum Computer", "Price": 500}
          ]

nextId=4

#curl "http://127.0.0.1:5000/customers"
@app.route('/customers')
def getAll():
  return jsonify(customers)

#curl "http://127.0.0.1:5000/customers/2"
@app.route('/customers/<int:id>')
def findById(id):
  foundCustomers = list(filter(lambda c: c['id'] == id, customers))
  if len(foundCustomers) == 0:
    return jsonify({}), 204
  
  return jsonify(foundCustomers[0])

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Name\":\"Google\",\"Technology\":\"Teleportation\",\"Price\":430}" "http://127.0.0.1:5000/customers"
@app.route('/customers', methods=['POST'])
def create():
  global nextId
  if not request.json:
    abort(400)
  customer = {
    "id": nextId,
    "Name": request.json['Name'],
    "Technology": request.json['Technology'],
    "Price": request.json['Price']
  }
  nextId += 1
  customers.append(customer)
  return jsonify(customer)

# curl -i -H "Content-Type:application/json" -X PUT -d "{\"Name\":\"Google\",\"Technology\":\"Teleportation\",\"Price\":430}" "http://127.0.0.1:5000/customers/1"
@app.route('/customers/<int:id>', methods=['PUT'])
def update(id):
  foundCustomers = list(filter(lambda t: t['id'] ==id, customers))
  if (len(foundCustomers)==0):
    abort(404)
  foundCustomer = foundCustomers[0]
  if not request.json:
    abort(400)
  reqJson = request.json
  if 'Price' in reqJson and type(reqJson['Price']) is not int:
    abort(400)
  if 'Name' in reqJson:
    foundCustomer['Name'] = reqJson['Name']
  if 'Technology' in reqJson:
    foundCustomer['Technology'] = reqJson['Technology']
  if 'Price' in reqJson:
    foundCustomer['Price'] = reqJson['Price']

  return jsonify(foundCustomer)

  return "in update"+str(id)

#curl -X DELETE "http://127.0.0.1:5000/customers/1"
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete(id):
  foundCustomers = list(filter(lambda t: t['id'] ==id, customers))
  if (len(foundCustomers)==0):
    abort(404)
  customers.remove(foundCustomers[0])
  return jsonify({"done":True})
  

if __name__ == '__main__' :
 app.run(debug= True)
