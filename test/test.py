import json

with open('data.json') as json_file:
    data = json.load(json_file)
    print(data['Test1'][0]['name'])