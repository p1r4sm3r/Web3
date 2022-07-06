import requests
import json
import time

webhook = "" # YOUR webhook
url = requests.get("https://api-mainnet.magiceden.dev/v2/collections/copetown/stats") # example collection
data = json.loads(url.text)
floorPrice = data["floorPrice"]
floorPrice = floorPrice/1000000000 #bugged api
#offset because ME lists based on earliest listed, so total listed - 5 = last 5 listed // offset="+str(listedCount-=5)+"
#above comment now invalid, 0 is last listed/most recently listed
url2 = requests.get("https://api-mainnet.magiceden.dev/v2/collections/copetown/listings?offset=0&limit=5") #only recently listed, not at floor price
data2 = json.loads(url2.text)
loggedNFTS = []

while True:
    for token in data2: #for the number of tokens, we've displayed 5
        if not token["tokenMint"] in loggedNFTS: #avoids repeating already shown NFTs
            if token["price"] <= floorPrice: #if current token is under or equal to 37.99, success is printed, there are 3 so it's printed a total of 3 times
                print("success!")
                link = "https://magiceden.io/item-details/"+token["tokenMint"]
                r = requests.post(webhook, data={"content": link}) #webhook
            loggedNFTS.append(token["tokenMint"])
    print("Checking...")
    time.sleep(5) #checks ever 5 seconds
