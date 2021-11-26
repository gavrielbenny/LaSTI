import json
from fastapi import FastAPI, HTTPException, Depends

from auth.auth_handler import signJWT, get_password_hash, verify_password
from auth.auth_bearer import JWTBearer

with open("presence.json", "r") as read_file:
    data = json.load(read_file)
with open("user.json", "r") as read_file2:
    data2 = json.load(read_file2)

app = FastAPI()

@app.post('/user/register')
async def write_user(username : str, password : str):
    hashing = get_password_hash(password)
    newdata = {'username': username, 'password' : hashing}
    data2.append(newdata)
    with open("user.json", "w") as write_file:
        json.dump(data2, write_file)
    write_file.close()
    return data2

@app.post('/user/login')
async def write_user(username : str, password : str):
    for data_user in data2:
        if data_user['username'] == username:
            if verify_password(password, data_user['password']):
                return signJWT(username)
            else :
                return('login failed')

@app.get('/')
def root():
    return{'Presence':'Item'}

@app.get('/presence/{user_id}', dependencies=[Depends(JWTBearer())])
async def read_presence(user_id: int):
    for presence_user in data['presence']:
        if presence_user['id'] == user_id:
            return presence_user
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

@app.post('/presence/{user_id}', dependencies=[Depends(JWTBearer())])
async def write_presence(name: str, date: str, time: str):
    user_id = len(data['presence'])+1
    newdata = {'id': user_id, 'name' : name, 'date' : date, 'time' : time}
    if(user_id > 1):
        data['presence'].append(newdata)
        with open("presence.json", "w") as write_file:
            json.dump(data, write_file)
        write_file.close()
        return data