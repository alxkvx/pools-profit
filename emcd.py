import urllib
import json

url = "https://api.emcd.io/v1/btc/income/8fbdd6e0-969d-47a6-808d-66635e50e81d"
response = urllib.urlopen(url)
data = json.loads(response.read())

reward = data['income'][0]['income']
hrate = data['income'][0]['total_hashrate']

profit = reward/(float(hrate)/10**12)

print ("Profit per 1 Th/Day: %.8f" % profit)

