import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e49bc329c1754d7e8c9493f97b03138c'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "tmarina@rambler.ru",
    "password": "Iloveqa1706"
}
response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)
body_create = { "name": "Бульбазавр",
    "photo_id": "53"}
response_create =  requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)


body_change = {
    "pokemon_id": "66744",
    "name": "IRRA",
    "photo_id": "53"
}

response_change =  requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

body_pokeboll = {
    "pokemon_id": "66744"
}

response_pokeboll =  requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
print(response_pokeboll.text)