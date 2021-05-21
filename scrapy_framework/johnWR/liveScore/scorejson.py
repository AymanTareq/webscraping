import json

with open('response.json') as f:
    data = json.load(f)

# league = data['events'][0]["tournament"]["name"]
# hometeam = data['events'][0]["homeTeam"]["name"]
# awayteam = data['events'][0]["awayTeam"]["name"]

# homescore = data['events'][0]["homeScore"]["current"]
# awayscore = data['events'][0]["awayScore"]["current"]

print(len(data['events']))

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