import webbrowser
import time
import random

while True:
    sites = random.choice(['google.com','facebook.com','youtube.com','programiz.com'])
    visit = 'http://{}'.format(sites)
    webbrowser.open(visit)
    seconds = random.randrange(2,20)
    time.sleep(5)


    
