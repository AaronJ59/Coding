import sys

if len(sys.argv) == 2 and float(sys.argv[1]):
    float(sys.argv[1])
elif len(sys.argv) == 1:
    sys.exit("Missing command-line argument")
else:
    sys.exit("Command-line argument is not a number")

import requests


try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    o = response.json()
    rate_float = o["bpi"]["USD"]["rate_float"]
    rate_float = rate_float * float(sys.argv[1])
    print(f"${rate_float:,.4f}")
except requests.RequestException:
    print("RequestException")