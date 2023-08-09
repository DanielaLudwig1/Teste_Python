import requests

#endpoint = input("Qual endpoint gostaria de consultar?: ")
usuario = input('Qual usuario gostaria de consultar?')

#url = f"http://localhost:44300/api/services/app/{endpoint}"
url = f'http://api.github.com/users/{usuario}'

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    print(data)

else:
    print("Não foi possivel realizar a consulta")