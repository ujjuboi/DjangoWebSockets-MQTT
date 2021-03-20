import json
import time, random
import websocket
import redis
import requests

ws = websocket.WebSocket() #initialised websocket object
#for homepage
ws.connect('ws://localhost:8000/ws/home/')
ws.send(json.dumps({}))
ws.close()

#for dashboard
ws.connect('ws://localhost:8000/ws/graph/')
#send 10 random values with a time interval of 1s
for i in range (1,100):
    time.sleep(1)
    ws.send(json.dumps({'value': random.randint(1,100)}))
ws.close()