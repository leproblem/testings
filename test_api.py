import json
import requests

keykekw = 'fce0a52ccdc9d77b4bd77b3b54dfd551d255cc8d355ad4359955ee08'

def get_api_key(email: str, passwd: str):
    headers = {'email': email, 'password': passwd, }
    res = requests.get('https://petfriends1.herokuapp.com/api/key', headers=headers)
    status = res.status_code
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result
#print(get_api_key('nikita.krgs@gmail.com','ebbvk-y61jwq'))

#---------------POST-------------------

def get_pet_list(key: str, filter: str):
    headers = {'auth_key': key}
    params = {'filter' : filter}
    res = requests.get('https://petfriends1.herokuapp.com/api/pets', headers=headers, params=params)
    status = res.status_code
    try:
        result = res.json()
    except json.decoder.JSONDecodeError: 
        result = res.text
    return status, result
print(get_pet_list(keykekw,'my_pets'))

def pet_add(key: str, name: str, animal_type: str, age: int):
    headers = {'auth_key': key}
    data = {'name' : name, 'animal_type': animal_type, 'age': age}
    res = requests.post('https://petfriends1.herokuapp.com/api/create_pet_simple', headers=headers, data=data)
    status = res.status_code
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result

#   

#---------------PUT------------

def pet_add(key: str, pet_id:str, name: str, animal_type: str, age: int):
    headers = {'auth_key': key}
    data = {'name' : name, 'animal_type': animal_type, 'age': age}
    res = requests.put('https://petfriends1.herokuapp.com/api/' + pet_id, headers=headers, data=data)
    status = res.status_code
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result

#--------------------DELETE-------------------------------

def pet_del(key: str, pet_id: str):
    headers = {'auth_key': key}
    res = requests.delete('https://petfriends1.herokuapp.com/api/pets/' + pet_id, headers=headers)
    status = res.status_code
    try:
        result = res.json()
    except json.decoder.JSONDecodeError:
        result = res.text
    return status, result

print(pet_del(keykekw,'49b04274-0d02-4115-9f95-ecd9582f6fe0'))
print(get_pet_list(keykekw,'my_pets'))