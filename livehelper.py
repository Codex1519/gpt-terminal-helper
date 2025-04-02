import requests
import time
import urllib.parse

def search_stackoverflow(query):
    encoded_query = urllib.parse.quote(query)
    url = f"https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q={encoded_query}&site=stackoverflow"
    
    print(f"\n Suche nach: '{query}' ...\n")
    response = requests.get(url)
    data  = response.json()
    
    if "items" not in data  or not data["items"]:
        print("Keine Ergebnisse gefunden.")
        return
    
    for i, item in enumerate(data["items"] [:5], start = 1):
        title  = item["title"]
        link = item["link"]
        print(f"{i}.{title}\n {link}\n")
        
def main():
    print("Live-Coding-Hilfe (Stackoverflow Terminal Tool)")
    print("Zum Beenden: einfach Leer lassen und [Enter] drücken.\n")
    
    while True:
        query = input("Problem oder Stichwort eingeben: ").strip()
        if not query:
            print("Ciao ! Viel Erfolg beim Coden.")
            break
        search_stackoverflow(query)
        print("-------------------------------------------------")
        time.sleep(1)

if __name__ == "__main__":
    main()