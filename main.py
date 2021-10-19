import json
from fastapi import FastAPI, HTTPException

with open("menu.json", "r") as read_file:
    data = json.load(read_file)
app = FastAPI()

@app.get('/')
def root():
    return{'Menu':'Item'}

@app.get('/menu/{item_id}')
async def read_menu(item_id: int):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            return menu_item
    raise HTTPException(
        status_code=404, detail=f'Item not found'
        )

@app.post('/menu/{item_id}/{item_name}')
async def write_menu(name: str):
    item_id = len(data['menu'])+1
    newdata = {'id': item_id, 'name' : name}
    if(item_id > 1):
        data['menu'].append(newdata)
        with open("menu.json", "w") as write_file:
            json.dump(data, write_file)
        write_file.close()
        return data
        
@app.put('/menu/{item_id}')
async def update_menu(item_id: int, new_name: str):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            menu_item['name'] = new_name
        read_file.close()    
        with open("menu.json", "w") as write_file:
            json.dump(data, write_file,indent=4)
        write_file.close()
    return {'message':'Data changed successfully'}

@app.delete('/menu/{item_id}')
async def delete_menu(item_id: int):
    for menu_item in data['menu']:
        if menu_item['id'] == item_id:
            data['menu'].remove(menu_item)
        read_file.close()    
        with open("menu.json", "w") as write_file:
            json.dump(data, write_file)
        write_file.close()
    return {'message':'Data deleted successfully'}