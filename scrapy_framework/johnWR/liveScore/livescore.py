import requests
import json

url = "https://api.sofascore.com/api/v1/sport/football/scheduled-events/2021-05-09"

headers = {
    "cookie": "__cfduid=d3e2a2152642472201d9f324fc98725891620562767",
    "Content-Type": "application/json"
}

response = requests.request("GET", url, headers=headers)

data = json.loads(response.text)

c = 1
for item in data['events']:
    league = item["tournament"]["name"]
    hometeam = item["homeTeam"]["name"]
    awayteam = item["awayTeam"]["name"]
    try:
        homescore = item["homeScore"]["current"]
        awayscore = item["awayScore"]["current"]
    except:
        # homescore = None
        # awayscore = None
        continue

    # if homescore is None:
    #     continue

    print("<{}>".format(c),league, "|", hometeam, homescore, "-", awayteam, awayscore)
    c += 1