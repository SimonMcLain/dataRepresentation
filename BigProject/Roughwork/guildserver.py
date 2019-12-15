#!flask/bin/python
from flask import Flask, jsonify, request, abort
from guildStoreDAO import guildStoreDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#curl "http://127.0.0.1:5000/sellers"
@app.route('/sellers')
def getAll():
  results = guildStoreDAO.getAll()
  return jsonify(results)

#curl "http://127.0.0.1:5000/sellers/2"
@app.route('/sellers/<int:id>')
def findById(id):
  foundSeller = guildStoreDAO.findById(id)
  
  return jsonify(foundSeller)

#curl -i -H "Content-Type:application/json" -X POST -d "{\"Name\":\"Hutt\",\"Technology\":\"Blaster\",\"Price\":430}" "http://127.0.0.1:5000/sellers"
@app.route('/sellers', methods=['POST'])
def create():
  if not request.json:
    abort(400)
  seller = {
    "Name": request.json['Name'],
    "Technology": request.json['Technology'],
    "Price": request.json['Price'],
  }
  values =(seller['Name'],seller['Technology'],seller['Price'])
  newId = guildStoreDAO.create(values)
  seller['id'] = newId
  return jsonify(seller)

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"Name\":\"Google\",\"Technology\":\"Teleportation\",\"Price\":430}" "http://127.0.0.1:5000/sellers/1"
@app.route('/sellers/<int:id>', methods=['PUT'])
def update(id):
  foundSeller = guildStoreDAO.findById(id)
  if not foundSeller:
    abort(404)
  if not request.json:
    abort(400)
  reqJson = request.json
  if 'Price' in reqJson and type(reqJson['Price']) is not int:
    abort(400)
  if 'Name' in reqJson:
    foundSeller['Name'] = reqJson['Name']
  if 'Technology' in reqJson:
    foundSeller['Technology'] = reqJson['Technology']
  if 'Price' in reqJson:
    foundSeller['Price'] = reqJson['Price']
  values = (foundSeller['Name'], foundSeller['Technology'], foundSeller['Price'], foundSeller['id'])
  guildStoreDAO.update(values)
  #return "in update for id" + str(id)
  return jsonify(foundSeller)
  

#curl -X DELETE "http://127.0.0.1:5000/sellers/1"
@app.route('/sellers/<int:id>', methods=['DELETE'])
def delete(id):
    guildStoreDAO.delete(id)
    return jsonify({"done":True})
  

if __name__ == '__main__' :
 app.run(debug= True)
