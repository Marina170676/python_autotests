import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'e49bc329c1754d7e8c9493f97b03138c'
HEADER = {'Content-Type' : 'application/json' , 'trainer_token' : TOKEN}
TRAINER_ID = 5549
def test_status_code():

     response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
     assert response.status_code == 200