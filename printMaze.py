import json

with open('myMaze.json', 'r') as f:
    maze = json.load(f)

for i in maze:
    print(''.join(i))
