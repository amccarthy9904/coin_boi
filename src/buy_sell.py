import requests
import json
import os
import data_grab

WALLET = os.environ["WALLET"]


def exchange(amount, pair):
    request = dict()
    request['amount'] = amount
    request['withdrawl'] = WALLET
    request['pair'] = pair
    request['returnAddress'] = WALLET
    return float(json.loads(requests.post("https://shapeshift.io/sendamount", json.dumps(request)))[u'success'][u'withdrawalAmount'])


def fake_exchange(amount, pair):
    return do_fees(amount, pair)


def do_fees(amount, pair):
    info = data_grab.gather_data()[pair]
    return float(info[u'rate']) * amount - float(info[u'minerFee'])

