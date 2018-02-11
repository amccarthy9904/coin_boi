import requests
import json


def sort_currency(coin):
    """
    Grabs all of the coins and organizes their cost for transactions

    :return: A sorted list of currency exchange rates
    """
    fee_map = []
    r = requests.get("https://shapeshift.io/marketinfo")
    result = json.loads(r.text)
    for cur_map in result:
        fee_map.append((cur_map[u'pair'], cur_map[u'minerFee']))
    fees = filter(lambda x: "{}_".format(coin) in x[0], fee_map)
    fees.sort(key=lambda x: x[1])
    return fees, fees[0]
