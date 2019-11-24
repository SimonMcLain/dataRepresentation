#!flask/bin/python
from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')
# PUT THIS INTO A DATABASE INSTEAD OF A FILE

customers=[
          {"id": 5001, "name":"Amazon", "totalApprovals": 4},
          {"id": 5002, "name":"FaceBook", "totalApprovals": 2},
          {"id": 5003,"name":"Google", "totalApprovals": 1}
          ]

nextId=5004

#curl "http://127.0.0.1:5000/customers"
@app.route('/customers')
def getAll():
  return jsonify(customers)

#curl http://127.0.0.1:5000/customers/5001
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
    "totalApprovals": 0
  }
  nextId += 1
  customers.append(customer)
  return jsonify(customer)

#curl -X DELETE "http://127.0.0.1:5000/customers/1"
@app.route('/customers/<int:id>', methods=['DELETE'])
def delete(id):
  foundCustomers = list(filter(lambda t: t['id'] ==id, customers))
  if (len(foundCustomers)==0):
    abort(404)
  customers.remove(foundCustomers[0])
  return jsonify({"done":True})

#curl -i -H "Content-Type:application/json" -X POST -d "{\"approve\":10}" "http://127.0.0.1:5000/approve/5001"
@app.route('/approve/<int:id>', methods={'POST'})
def addApproval(id):
  foundCustomers=list(filter(lambda t: t['id'] == id, customers))
  if len(foundCustomers) == 0:
    abort(404)
  if not request.json:
    abort(400)
  if not 'approve' in request.json and type(request.json['approve']) is not int:
    abort(401)     
  
  newApprovals = request.json['approve']

  foundCustomers[0]['totalApprovals'] += newApprovals

  return jsonify(foundCustomers[0])

# curl "http://127.0.0.1:5000/approve/List"
@app.route('/approve/List')
def getList():
  customers.sort(key=lambda x: x['totalApprovals'], reverse=True)
  return jsonify(customers)


if __name__ == '__main__' :
 app.run(debug= True)