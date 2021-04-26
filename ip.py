import requests
webhook = "WEBHOOK_URL_HERE"

def getipa():
    x = requests.get('https://api.ipify.org')
    ipa = x.text
    print(ipa)
    
def sendipa(ipa):
    data = {"username": 'New IP', "content": ipa}
    requests.post(webhook, json=data)

getipa()
