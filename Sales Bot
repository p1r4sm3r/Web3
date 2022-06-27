import requests
import json
import time
import datetime

# Only problem is during initial start/launch of program NFTs are not displayed in chronological order.

# input webhook of choice
webhook = ""

# setting up lists to store, messy
soldNFT = []
loggedNFTs = []
sentNFTs = []

# template from discohook
data = {
        # "content": null,
        "embeds": [
            {
                "title": "Copetown",
                "color": 11707857,
                "fields": [
                    {
                        "name": "Price",
                        "value": "Invalid"
                    },
                    {
                        "name": "Date",
                        "value": "12/26/2021, 12:11:58 PM"
                    }
                ],
                "image": {
                    "url": "https://arweave.net/kcf61NRRO0gyN9EUagEXujbhRE5JG2RaK3uD3mwOIM4"
                },
                "thumbnail": {
                    "url": "https://img-cdn.magiceden.dev/rs:fill:170:170:0:0/plain/https://bafybeiayexoagwpuz77qolunjhuzeleb2difcvfxwrvu2eukahx3vetxti.ipfs.dweb.link/"
                }
            }
        ],
    }

while True: # loops
    activityURL = requests.get("https://api-mainnet.magiceden.dev/v2/collections/copetown/activities?offset=0&limit=100") # refreshes for new activity, shows last "limit=" amount
    activityData = json.loads(activityURL.text) # opens new activity
    for token in activityData:  # for number of tokens in all activity
        if not token["tokenMint"] in loggedNFTs:  # if current token is not logged
            if (token["type"]) == "buyNow":  # if sold, not listed, bid etc
                soldNFT.append(token) # adds to list that is output
            loggedNFTs.append(token["tokenMint"]) # adds to list of checked NFTs

    for validTOKEN in soldNFT:  # for number of tokens in list of NFTs valid, all sold, not bid, listed etc
        if not validTOKEN["tokenMint"] in sentNFTs: # if current token has not already been sent
            tokenINFO_URL = requests.get("https://api-mainnet.magiceden.dev/v2/tokens/" + validTOKEN["tokenMint"])  # retrieve info of each token
            tokenINFO = json.loads(tokenINFO_URL.text) # loads to scannable format
            data["embeds"][0]["fields"][0]["value"], data["embeds"][0]["title"], data["embeds"][0]["image"]["url"], data["embeds"][0]["fields"][1]["value"] = str(validTOKEN["price"]), tokenINFO["name"], tokenINFO["image"], "<t:"+str(validTOKEN["blockTime"])+">"  # changes the template, price is an integer so has to be converted to str, using epoch time therefore accurate to each person's timezone.
            # print(validTOKEN["price"], tokenINFO["name"], tokenINFO["image"], (str(datetime.datetime.fromtimestamp(validTOKEN["blockTime"])))) for testing, can be used without webhook working
            r = requests.post(webhook, json=data) # sends the webhook, as a json file
            sentNFTs.append(validTOKEN["tokenMint"]) # appends to list of already sent NFTs, avoids resending
    print("Checking...") # checks if program is still running
    time.sleep(5) # repeats every 5 seconds
