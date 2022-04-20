import requests
import threading
url = input("URL> ")
threads = int(input("Threads> "))

def yes():
    while True:
        try:
            response = requests.get(url)
            print("CODE: " + str(response.status_code))
        except:
            pass

for i in range(threads): 
    threading.Thread(target=yes).start()
