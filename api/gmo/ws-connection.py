import json
import websocket

websocket.enableTrace(True)
ws = websocket.WebSocketApp('wss://forex-api.coin.z.com/ws/public/v1')
class Streamer(object):
    def on_open(self, ws):
        message = {
            "command": "subscribe",
            "channel": "ticker",
            "symbol": "USD_JPY"
        }
        ws.send(json.dumps(message))

    # def on_message(self, message, ws):
        # print(message)


    def run(self, ws):
        ws.on_open = self.on_open
        # ws.on_message = self.on_message
        ws.run_forever()

if __name__ == "__main__":
    s = Streamer()
    s.run(ws)
