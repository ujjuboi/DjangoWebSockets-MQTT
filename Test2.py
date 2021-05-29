import time
import _thread
import json
import websocket

def on_message(ws, message):
    message = json.loads(message)
    print (message)

def on_error(ws, error):
    print ("eroror:", error)

def on_close(ws):
    print ("### closed ###")
    # Attemp to reconnect with 2 seconds interval

def on_open(ws):
    print ("### Initiating new websocket connectipython my-websocket.pyon ###")
    # def run(*args):
    #     for i in range(30000):
    #         # Sending message with 1 second intervall
    #         time.sleep(1)

    #         ws.send(json.dumps({
    #             'message': "Hello %d" % i
    #         }))
    #     time.sleep(1)
    #     ws.close()
    #     print ("thread terminating...")
    # _thread.start_new_thread(run, ())

def initiate():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:8000/ws/data/V2Tcp3Xt/gAAAAABgslDcd4ViJgItT8ff2FOtr42H89_fQf1pCCNyj6ZAWfrv1uFoOHg98BxD5FnKaRLrxItFWIxPmiAQru9vTN6OpntYzTP3ITj70sywesgQoheTuHgoQ1MGbmPt6wWahCodiIuUMH-ixRjIEFJPnabKLXDiiw==/",
        on_message = on_message,
        on_error = on_error,
        on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

if __name__ == "__main__":
    initiate()