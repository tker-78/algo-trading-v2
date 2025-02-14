import json
import websocket
from datetime import datetime
from apiclient import Ticker

from models import generate_candle

class Streamer(object):
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp('wss://forex-api.coin.z.com/ws/public/v1')

    def on_open(self, ws):
        message = {
            "command": "subscribe",
            "channel": "ticker",
            "symbol": "USD_JPY"
        }
        ws.send(json.dumps(message))

    def on_message(self, message, ws):
        data = json.loads(ws)
        timestamp = datetime.strptime(data["timestamp"], "%Y-%m-%dT%H:%M:%S.%fZ")
        bid = float(data["bid"])
        ask = float(data["ask"])
        ticker = Ticker(timestamp, bid, ask)

        # tickerの情報をデータベースに書き込む
        # **todo**
        generate_candle(ticker, "USD_JPY", "1h")


    def run(self):
        self.ws.on_open = self.on_open
        self.ws.on_message = self.on_message
        self.ws.run_forever()

if __name__ == "__main__":
    s = Streamer()
    s.run()
