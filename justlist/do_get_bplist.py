# just get list of BP via API
import json
import requests

# url = "https://api.main.alohaeos.com/v1/chain/get_producers"
url = "https://api.eosnewyork.io:443/v1/chain/get_producers"

payload = "{\"limit\":\"500\",\"json\":\"true\"}"
response = requests.request("POST", url, data=payload)

data = json.loads(response.text)

i=0
rank=1
tpvw = data["total_producer_vote_weight"]

while True:
    try:
        bpowner = data["rows"][i]["owner"]
        bpurl = data["rows"][i]["url"]
        bptotv = data["rows"][i]["total_votes"]
        bplct = data["rows"][i]["last_claim_time"]
        bploc = data["rows"][i]["location"]
        bppk = data["rows"][i]["producer_key"]
        bpub = data["rows"][i]["unpaid_blocks"]
        bpia = data["rows"][i]["is_active"]
    except IndexError:
        break

    vote_percent = (float(bptotv) / float(tpvw)) * 100
    print("%s, %d, %.2f, %s" % (bpowner, rank, vote_percent, bpurl))
    i += 1
    rank += 1

#print(response.text)