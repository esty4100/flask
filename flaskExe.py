# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from flask import Flask,request

with open('data.json', 'r') as f:
  data = json.load(f)
app = Flask(__name__)

def sameProfile(capsul,profile):
  for p in profile:
    if capsul[p]!=profile[p]:
      return False
  return True

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/image/<id>")
def byImage(id):
  for d in data:
    if d['image']==id:
      return d
  return 'No such image id!!'

@app.route("/capsules/byName/<name>")
def byName(name):
  for d in data:
    if d['name']==name:
      return d
  return 'No such data!!'

@app.route("/capsules/byId/<id>")
def byId(id):
  for d in data:
    if str(d['id'])==id:
      return d
  return 'No such id!!'

@app.route("/capsules/all")
def allcapsulot():
  return str(data)
# POST
@app.route("/capsules/filterByProfile",methods=['POST'])
def byProfile():
  profile=request.json['profile']
  answer=[]
  for d in data:
    if sameProfile(d['profile'],profile)==True:
      answer.append(d)
  return str(answer)

# PUT
@app.route("/capsules/id",methods=['PUT'])
def put():
  id=request.json
  for d in data:
    if d['id']==id['id']:
      d['price']+=10
      with open('data.json','w') as jsonFile:
        json.dump(data,jsonFile)
  return id

if __name__ == "__main__":
  app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/