import json

def averageRatings(content):
    players = content["players"]
    n_players = len(players)

    average = {}
    for key in players[0]["ratings"][0].keys():
        print(key)
        average[key] = 0
    for player in players:
        for key, value in player["ratings"][0].items():
            average[key] += value/n_players

    return average

def averageHeight(content):
    players = content["players"]
    n_players = len(players)

    average = 0
    for player in players:
        average += player["hgt"]/n_players

    return average

def averageWeight(content):
    players = content["players"]
    n_players = len(players)

    average = 0
    for player in players:
        average += player["weight"]/n_players
    return average

def averageAge(content):
    players = content["players"]
    n_players = len(players)

    average = 0
    for player in players:
        average += (content["startingSeason"]-player["born"]["year"])/n_players
    return average

if __name__ == "__main__":

    with open('files/playerNBA.json', "rb") as f:
        file_content = json.load(f)
    print("Ratings: " + str(averageRatings(file_content)))
    print("Height: " + str(averageHeight(file_content)))
    print("Weight: " + str(averageWeight(file_content)))
    print("Age: " + str(averageAge(file_content)))
