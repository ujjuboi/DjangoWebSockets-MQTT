# DjangoWebSockets-MQTT

## Brief Idea:
Project can be sub divided as follows:-  
* We need to register sensors 
* We need to register client
* We need to provide client with the sensor data he clicks on
* Use of WebSocket or MQTT to send data from the server to the client's application

## Installation:
Please see the appropriate guide for your environment of choice:
* <a href = "https://www.python.org/downloads/">Python 3.9</a>
* <a href = "https://redis.io/download">Redis 6.2</a>

## Technologies:
Project is created with:
* <a href="https://www.djangoproject.com/">Django 3.1.7</a>
* <a href="https://channels.readthedocs.io/en/stable/">Django Channels 3.0.3</a>
* <a href="https://pypi.org/project/websockets/">Python WebSockets 8.1</a>
* <a href="https://www.chartjs.org/">Chart.js</a>

## Setup:
To run the project locally, open terminal & enter the following commands:
```
$ cd path/to/your/dev/folder
$ mkdir DjangoMQTT
$ cd DjangoMQTT
$ git clone https://github.com/ujjuboi/DjangoWebSockets-MQTT.git .
$ git remote remove origin
$ virtualenv -p python .
$ source bin/activate
(DjangoMQTT) $ pip install -r requirements.txt
```

Reminder:exclamation: Delete settings.py (specifically secret key when deploying the app - generate new one)
