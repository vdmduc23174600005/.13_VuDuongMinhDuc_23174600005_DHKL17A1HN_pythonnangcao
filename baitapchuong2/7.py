import json 
with open(file='./file.json',mode='r',encoding='utf-8') as file:
    object_python = json.load(fp=file)
print(object_python)
print(type(object_python)) 
