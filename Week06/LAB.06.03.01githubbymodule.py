from github import Github
import requests

g = Github("7f81f2d61cc64b32ae247f880d55507babf4f978")

#for repo in g.get_user().get_repos():
   #print(repo.name)

repo = g.get_user().get_repo("LAB06")
print(repo.clone_url)

fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
print (urlOfFile)


response = requests.get(urlOfFile)
contentOfFile = response.text
print (contentOfFile)

newContents = contentOfFile + "\nI have written a program to push commits to github\n"
print (newContents)

gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)