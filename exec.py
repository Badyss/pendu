import requests

url = "https://jsonplaceholder.typicode.com/posts/1/comments"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for comment in data:
        print("Email:", comment["email"])
else:
    print("Erreur lors de la récupération des données")
