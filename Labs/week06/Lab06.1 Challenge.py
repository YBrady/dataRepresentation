# Do your imports
import requests, json
from xlwt import *

#url = "https://api.github.com/users?sie=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"
response = requests.get(url)
data = response.json()
print(data)

#Get the file name for the new file to write
filename = 'githubusers.json'
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)


# Write to Excel file
w = Workbook()
ws = w.add_sheet('ghusers')
row = 0
ws.write(row, 0, "login")
ws.write(row, 1, "id")
ws.write(row, 2, "node_id")
ws.write(row, 3, "gravatar_id")
ws.write(row, 4, "url")
ws.write(row, 5, "html_url")
ws.write(row, 6, "url")
ws.write(row, 7, "followers_url")
ws.write(row, 8, "following_url")
ws.write(row, 9, "gists_url")
ws.write(row, 10, "starred_url")
ws.write(row, 11, "subscriptions_url")
ws.write(row, 12, "organizations_url")
ws.write(row, 13, "repos_url")
ws.write(row, 14, "events_url")
ws.write(row, 15, "received_events_url")
ws.write(row, 16, "type")
ws.write(row, 17, "site_admin")
row += 1
for ghuser in data:
    ws.write(row, 0, ghuser["login"])
    ws.write(row, 1, ghuser["id"])
    ws.write(row, 2, ghuser["node_id"])
    ws.write(row, 3, ghuser["avatar_url"])
    ws.write(row, 4, ghuser["gravatar_id"])
    ws.write(row, 5, ghuser["url"])
    ws.write(row, 6, ghuser["html_url"])
    ws.write(row, 7, ghuser["followers_url"])
    ws.write(row, 8, ghuser["following_url"])
    ws.write(row, 9, ghuser["gists_url"])
    ws.write(row, 10, ghuser["starred_url"])
    ws.write(row, 11, ghuser["subscriptions_url"])
    ws.write(row, 12, ghuser["organizations_url"])
    ws.write(row, 13, ghuser["repos_url"])
    ws.write(row, 14, ghuser["events_url"])
    ws.write(row, 15, ghuser["received_events_url"])
    ws.write(row, 16, ghuser["type"])
    ws.write(row, 17, ghuser["site_admin"])
    row += 1

w.save("ghusers.xls")