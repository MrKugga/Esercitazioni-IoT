import requests
import json

def getLatest(cur):
    currency = "EUR" if cur == "e" else "USD" if cur == "u" else "GBP" if cur == "p" else None
    if currency is None:
        return("Valuta non valida")

    endpoint = "https://api.exchangeratesapi.io/latest"
    payload = {
        "base": currency
    }
    try:
        response = requests.get(endpoint, params= payload)
        if response.status_code != 200:
            return "Errore nella comunicazione col server"
        else:
            return json.loads(response.content)
    except:
        return "C'è qualcosa che non va ma non ho idea di cosa sia"

def getHistory(dict):
    try:
        payload = {
            "start_at": dict["start_at"],
            "end_at": dict["end_at"]
        }
        endpoint = "https://api.exchangeratesapi.io/history"
        response = requests.get(endpoint, params= payload)
        if response.status_code != 200:
            return "Errore nella comunicazione col server"
        else:
            return json.loads(response.content)

    except KeyError:
            endpoint = f"https://api.exchangeratesapi.io/{dict['year']}-{dict['month']}-{dict['day']}"
            response = requests.get(endpoint)
            if response.status_code != 200:
                return "Errore nella comunicazione col server"
            else:
                return json.loads(response.content)


if __name__ == "__main__":
    print(f"""
Available command:
latest: latest change rate
history: historic exchange rates
quit: exit""")

    while True:
        choise = input("-> ").casefold()

        if choise == "latest":
            cur = input("Which base currency do you want?\nE: Euro\nU: USD\nP: GBP\n-> ").casefold()
            output = getLatest(cur)

        elif choise == "history":
            user_input = input("Type D for a day and I for an interval\n-> ").casefold()
            if user_input == "d":
                dict = {}
                dict["year"] = input("Write the year:\n").zfill(2)
                dict["month"] = input("Write the month:\n").zfill(2)
                dict["day"] = input("Write the day:\n").zfill(2)
                output = getHistory(dict)

            elif user_input == "i":
                # basterebbe aggiungere al dizionario data di partenza e fine
                print("Hai scelto intervallo ma non ho voglia di implementare questa funzione")

            else:
                print("Scelta non valida. Riprova.")

            print(output)

        elif choise == "quit":
            break

        else:
            print("scelta non valida. Riprova.")
