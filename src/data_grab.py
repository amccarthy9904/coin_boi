import requests
import json


def gather_data():
    """
    Grabs all of the coins and organizes their exchange rates

    :return: A map from coins to exchange rate
    """
    rate_map = {}
    r = requests.get("https://shapeshift.io/marketinfo")
    result = json.loads(r.text)
    for cur_map in result:
        rate_map[cur_map[u'pair']] = cur_map
    return rate_map


if __name__ == "__main__":
    print(gather_data())
