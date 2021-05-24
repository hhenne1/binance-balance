# use for environment variables
import os
from binance.client import Client
from datetime import datetime, timedelta
import time

# Switch between testnet and mainnet
TESTNET = False

# Get binance key and secret for TEST and MAINNET
api_key_test = "yourkey"
api_secret_test = "yourkey"

api_key_live = "yourkey"
api_secret_live = "yourkey"

# Authenticate with the client
if TESTNET:
    client = Client(api_key_test, api_secret_test)
    client.API_URL = 'https://testnet.binance.vision/api'

else:
    client = Client(api_key_live, api_secret_live)


def write_log(logline):
    timestamp = datetime.now().strftime("%d/%m %H:%M:%S:")
    with open('balance.txt','a+') as f:
        f.write(timestamp + '\n' + str("%.2f" % logline) + '\n')

def get_account_cash():
    return float(client.get_asset_balance("USDT")["free"])


if __name__ == '__main__':
    starttime = time.time()
    while True:
        timestamp = datetime.now().strftime("%d/%m %H:%M:%S:")
        print(timestamp + 'logging USDT balance..')
        write_log(get_account_cash())
        time.sleep(60.0 - ((time.time() - starttime) % 60.0))

# end