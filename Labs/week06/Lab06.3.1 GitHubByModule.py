from github import Github 
import requests 

# remove the minus sign from the key 
g = Github("1-7891d5635a02570115b7432abd1e11a6dab5790") 

# Prints out all the repository names in my account
# for repo in g.get_user().get_repos(): 
#    print(repo.name)

# The specific private repository
repo = g.get_repo("YBrady/DataRepPrivate") 
#print(repo.clone_url)

# Chosing a particular file in the repository
fileInfo = repo.get_contents("text.txt") 
# Get the URL
urlOfFile = fileInfo.download_url 
#print (urlOfFile)

# Make the GET request
response = requests.get(urlOfFile) 
# Get the content of the file
contentOfFile = response.text 
# Print out the file contents
# print (contentOfFile)

# Adding a new line to newContents
newContents = contentOfFile + " more stuff \n" 
# print (newContents)

# Update and commit 
gitHubResponse=repo.update_file(fileInfo.path,"Updated by program", newContents, fileInfo.sha) 
print (gitHubResponse)