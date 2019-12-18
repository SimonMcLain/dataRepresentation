#!flask/bin/python
from flask import Flask, jsonify, request, abort
from xstoresDAO import storesDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#curl "http://127.0.0.1:5000/stores"
@app.route('/stores')
def getAll():
  results = storesDAO.getAll()
  return jsonify(results)

#curl "http://127.0.0.1:5000/stores/2"
@app.route('/stores/<int:id>')
def findById(id):
  foundCustomer = storesDAO.findById(id)
  
  return jsonify(foundCustomer)

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Name\":\"Ray\",\"Technology\":\"Teleportation\",\"Price\":430}" "http://127.0.0.1:5000/stores"
@app.route('/stores', methods=['POST'])
def create():
  if not request.json:
    abort(400)
  customer = {
    "Name": request.json['Name'],
    "Technology": request.json['Technology'],
    "Price": request.json['Price'],
  }
  values =(customer['Name'],customer['Technology'],customer['Price'])
  newId = storesDAO.create(values)
  customer['id'] = newId
  return jsonify(customer)

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Name\":\"Google\",\"Technology\":\"Teleportation\",\"Price\":430}" "http://127.0.0.1:5000/stores/1"
@app.route('/stores/<int:id>', methods=['PUT'])
def update(id):
  foundCustomers = storesDAO.findById(id)
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
  values = (foundCustomers['Name'], foundCustomers['Technology'], foundCustomers['Price'], foundCustomers['id'])
  storesDAO.update(values)
  #return "in update for id" + str(id)
  return jsonify(foundCustomers)
  

#curl -X DELETE "http://127.0.0.1:5000/customers/1"
@app.route('/stores/<int:id>', methods=['DELETE'])
def delete(id):
    storesDAO.delete(id)
    return jsonify({"done":True})
  

if __name__ == '__main__' :
 app.run(debug= True)
