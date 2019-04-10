import time
import random
import webbrowser

while True:
    sites=random.choice(['facebook','twitter','google','instagram','python'])
    visit='http://{}'.format(sites)
    webbrowser.open(visit)
    seconds=random.randrange(5)
    time.sleep(3)
