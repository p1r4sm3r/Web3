from pybit import spot
from datetime import datetime
import json
import time
import matplotlib.pyplot as plt

session_unauth = spot.HTTP(
    endpoint="https://api.bybit.com"
)

# json_object = json.dumps(session_unauth.query_kline(symbol="SOL3SUSDT", interval="1m"), indent=4)
# with open("test.json", "w") as outfile:
#     json.dump(session_unauth.query_kline(symbol="SOL3SUSDT", interval="1m"), outfile)

timeList = []
bidList = []
n=0
# print(session_unauth.last_traded_price(symbol="SOL3SUSDT"))
while True:
    # timeList.append(session_unauth.last_traded_price(symbol="SOL3SUSDT")["result"]["price"])
    timeList.append(n)
    bidList.append(session_unauth.best_bid_ask_price(symbol="SOL3SUSDT")["result"]["bidPrice"])
    plt.plot(timeList, bidList, ':')
    plt.pause(5)
    n+=1
