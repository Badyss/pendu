import requests

url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Titre:", data["title"])
    print("Contenu:", data["body"])
else:
    print("Erreur lors de la récupération des données")
