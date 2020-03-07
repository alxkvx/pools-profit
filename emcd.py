import urllib
import json
import time

apikey = '8fbdd6e0-969d-47a6-808d-66635e50e81d'
url = "https://api.emcd.io/v1/btc/income/%s" % apikey
response = urllib.urlopen(url)
data = json.loads(response.read())

reward = data['income'][0]['income']
hrate  = data['income'][0]['total_hashrate']
timest = data['income'][0]['timestamp']

diff = time.time() - timest
if diff > 24*3600:
    print "Last data is more than 24H old: %d H" % (int(diff)/3600)
else:
    profit = reward/(float(hrate)/10**12)
    print ("Profit per 1 Th/Day: %.8f" % profit)
