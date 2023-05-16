import wiringpi
import time
import json
import requests

url = "http://iotessentialsr0929431.hub.ubeac.io/iotessEwoud"
uid = "iotessEwoudForster"

def upload(status, count):
    global url
    if status == "Off":
        new_status=0
    elif status == "armed":
        new_status = 1
    elif status == "triggered":
        new_status = 2
    data = {
        "id": uid,
        "sensors": [
            {'id': 'Status',
             'data': new_status
             },
            {'id': 'Counter',
             'data': count
             }
        ]
    }
     
    r = requests.post(url, verify=False, json=data)
