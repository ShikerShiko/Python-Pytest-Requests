import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '0a5cd948fbef0ae6b8deab1e9df201f2'
HEADER =  {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '12991'


'''body_registration = {
    "trainer_token": TOKEN,
    "email": "dima-manager@ya.ru",
    "password": "Q1111111"
} 
body_confirmation_email = {
    "trainer_token": TOKEN
}'''
'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print (response.text)'''

'''response_confirmation = requests.post( url = f'{URL}/trainers/confirm_email', headers=HEADER, json= body_confirmation_email )
print (response_confirmation.text)'''
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
response_create = requests.post (url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print (response_create.text)

message = response_create.json()['message']
print(message)

body_rename = {
    "pokemon_id": "186053",
    "name": "Бульбазавр",
    "photo_id": 2
}
response_rename = requests.put (url = f'{URL}/pokemons', headers = HEADER, json = body_rename)
print (response_rename.text)

message = response_rename.json()['message']
print(message)



body_add = {
    "pokemon_id": "186053"
}
response_add = requests.post (url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print (response_add.text)

message = response_add.json()['message']
print(message)
