import requests
import json
from xlwt import *

response = requests.get('https://api.github.com')
print(response.status_code)
if response:
    print('Success!')
else:
    print('An error has occurred.')
apiKey = '7f81f2d61cc64b32ae247f880d55507babf4f978'

url = 'https://api.github.com/user/repos'

response = requests.get(url, auth=('token',apiKey))

repoJSON = response.json()
print (response.status_code)

newFile = open("SMclRepos.json", "w")
json.dump(repoJSON, newFile, indent=4)

# url = https://github.com/SimonMcLain/datarepresentationstudent-aPrivateOne
# token = 7f81f2d61cc64b32ae247f880d55507babf4f978 