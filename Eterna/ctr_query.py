# consider buffer memory

import json
from collections import defaultdict

f_click = open(r"190515-click-22.json", 'rb')
dict_click = defaultdict(int)

while(True):
    click = f_click.readline()
    if not click :
        break
    try:
        nowquery = json.loads(click.decode())["location_param_query"]
        dict_click[nowquery] = dict_click[nowquery] + 1
    except:
        pass

f_pv =  open(r"190515-pv-22.json", 'rb')
dict_pv = defaultdict(int)

while(True):

    pv = f_pv.readline()
    if not pv:
        break
    try:
        nowquery = json.loads(pv.decode())["location_param_query"]
        dict_pv[nowquery] = dict_pv[nowquery] + 1
    except:
        pass

dict_ctr = defaultdict(int)
for key in dict_pv.keys():
    if(key in dict_click) : # click 개수 있는 경우
        dict_ctr[key] = dict_click[key] / dict_pv[key]
    else:
        dict_ctr[key] = 0

f_click.close()
f_pv.close()
with open('ctr_query.json', 'w') as fp:
    json.dump(dict_ctr, fp, ensure_ascii = False)
