cd /home/pi/Binance-volatility-trading-bot/balance-script
source ../.venv/bin/activate
while true
do
    python3 getusdt.py
    echo "Script died. Press [CTRL+C] to cancel restart."
    sleep 1
done
