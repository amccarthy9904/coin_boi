import requests
import json
import os

WALLET = os.environ["WALLET"]


def exchange(amount, pair):
    request = dict()
    request['amount'] = amount
    request['withdrawl'] = WALLET
    request['pair'] = pair
    request['returnAddress'] = WALLET
    return requests.post("https://shapeshift.io/sendamount", json.dumps(request))
