import requests
import json
from xlwt import *

#html = '<h1>Hello World</h1>This is an API Lab'
f = open("carviewerv2.html", "r")
html = f.read()
# print(html)

apiKey = '46ceed910c24ff7cce8240e89ec7b71912f6f40f2ec55fd217ce150ad6d4f1c4'

url = 'https://api.html2pdf.app/v1/generate'

data = {'html': html, 'apiKey': apiKey}

response = requests.post(url, json=data)

print(response.status_code)

newFile = open("LAB-06-02-02.htmlaspdf.pdf", "wb")
newFile.write(response.content)

# url = https://github.com/SimonMcLain/datarepresentationstudent-aPrivateOne.git
# token = 7f81f2d61cc64b32ae247f880d55507babf4f978 
