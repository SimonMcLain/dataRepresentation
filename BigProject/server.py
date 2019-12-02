#!flask/bin/python
from flask import Flask, jsonify, request, abort
from xcustomersDAO import customersDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#curl "http://127.0.0.1:5000/customers"
@app.route('/customers')
def getAll():
  results = customersDAO.getAll()
  return jsonify(results)

#curl "http://127.0.0.1:5000/customers/2"
@app.route('/customers/<int:id>')
def findById(id):
  foundCustomer = customersDAO.findById(id)
  
  return jsonify(foundCustomer)

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Name\":\"Google\",\"Technology\":\"Teleportation\",\"Price\":430}" "http://127.0.0.1:5000/customers"
@app.route('/customers', methods=['POST'])
def create():
  if not request.json:
    abort(400)
  customer = {
    "Name": request.json['Name'],
    "Technology": request.json['Technology'],
    "Price": request.json['Price']
  }
  values =(customer['Name'],customer['Technology'],customer['Price'])
  newId = customersDAO.create(values)
  customer['id'] = newId
  return jsonify(customer)

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Name\":\"Google\",\"Technology\":\"Teleportation\",\"Price\":430}" "http://127.0.0.1:5000/customers/1"
@app.route('/customers/<int:id>', methods=['PUT'])
def update(id):
  foundCustomers = customersDAO.findById(id)
  if not foundCustomers:
    abort(404)
  if not request.json:
    abort(400)
  reqJson = request.json
  if 'Price' in reqJson and type(reqJson['Price']) is not int:
    abort(400)
  if 'Name' in reqJson:
    foundCustomers['Name'] = reqJson['Name']
  if 'Technology' in reqJson:
    foundCustomers['Technology'] = reqJson['Technology']
  if 'Price' in reqJson:
    foundCustomers['Price'] = reqJson['Price']

  values =(foundCustomers['Name'], foundCustomers['Technology'], foundCustomers['Price'], foundCustomers['id'])
  customersDAO.update(values)
  return jsonify(foundCustomers)

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
