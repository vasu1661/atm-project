import json

import pandas as pd

room_1 = '{"TL1":0,"TL2":0,"OL":0,"F1":0,"F2":0,"TV":0}'
# room_2 = '{"r1":'
#         {"tl":["tl1":0,"tl2":0],
#         "ol":0,"f":0,"tv":0}}'
v1 = json.loads(room_1)
v1.keys()
type(v1)
option = int(input('enter 0 to off all and 1 to on all : '))
if option == 1:
    for i in v1.values():
        i = 1
        print(i)


elif option == 0:
    for i in v1.values():
        i = 0
        print(i)
else:
    print('wrong number')







  # with open('room_1.json', 'a') as json_file:
  #       f =pd.read_json('room_1.json',end='\n')
  #       json.dump(room_1, json_file)
  #       print()












