import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0a5cd948fbef0ae6b8deab1e9df201f2'
HEADER =  {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '12991'

'''def test_status_code():
    response = requests.get(url= f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID}, )
    assert response.status_code == 200



def test_part_of_response():
    response_get= requests.get(url = f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID}, )
    assert response_get.json()['data'][0]["name"] == 'Бульбазавр'''


'''@pytest.mark.parametrize('key, value', [('name', 'Бульбазавр'), ('trainer_id', TRAINER_ID), ('id', '186060')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID}, )
    assert response_parametrize.json()["data"][0][key] == value
'''


def test_status_code_trainers():
    response = requests.get(url= f'{URL}/trainers', params={'trainer_id' : TRAINER_ID}, )
    assert response.status_code == 200



def test_status_code_trainers_qwer():
    response = requests.get(url= f'{URL}/trainers?trainer_id=12991')
    assert response.json()['data'][0]['id'] == TRAINER_ID