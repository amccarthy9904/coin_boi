import requests
import json

rate_map = {}
r = requests.get("https://shapeshift.io/marketinfo")
result = json.loads(r.text)
for cur_map in result:
    rate_map[cur_map[u'pair']] = cur_map[u'rate']

print rate_map
