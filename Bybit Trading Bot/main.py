from pybit import spot
import os
import sys
import time
from dotenv import load_dotenv

load_dotenv()

tradeHistory = []

session_auth = spot.HTTP(
    endpoint="https://api.bybit.com",
    api_key=os.getenv('API_KEY'),
    api_secret=os.getenv('API_SECRET')
)

# print(session_auth.get_wallet_balance())

# print(session_auth.place_active_order(
#     symbol="SOLUSDT",
#     side="Buy",
#     type="LIMIT",
#     price="TEST",
#     qty="FILL",
#     timeInForce="FOK"
# ))

allBids = []

shortBids, longBids = [], []

allBids.append(shortBids)
allBids.append(longBids)

def priceDrop ():
    allBids[0].append(session_auth.best_bid_ask_price(
    symbol="SOL3SUSDT")["result"]["bidPrice"]
    )
    allBids[1].append(session_auth.best_bid_ask_price(
    symbol="SOL3LUSDT")["result"]["bidPrice"]
    )
    # return symbol, price, qty
    pass

def placeOrder ():
    if len(allBids)>1:
        for i in allBids:
            #if drop of more than 0.5%, buy
            #print(float(i[len(i)-2]),(float(i[len(i)-1])  ))
            if float(i[len(i)-2])>(float(i[len(i)-1])*1.005):
                print('W')
                tradeHistory.append(str(i[len(i)-2] + '|' + i[len(i)-1]))
                print(tradeHistory)
    #if price[-1]>(price[-2]*1.01):

def sellOrder ():
    if len(tradeHistory)>0:
        pass

print('Go')
while True:
    priceDrop()
    placeOrder()
    time.sleep(1)

# while True:
#     priceDrop()
#     if shortBids[-1]>(price[-2]*1.01):
#     print('Short: ', shortBids, '\n' + 'Long: ', longBids)
#     time.sleep(30)
