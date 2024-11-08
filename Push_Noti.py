# Simple Notification Trigger to Mobile
from pushbullet import Pushbullet
import time


API_KEY = "o.QVhTjKwCECLRDhVEUPR8PJNhrIAgxipO"
pb = Pushbullet(API_KEY)

for i in range(200):
    stri ="No is" + str(i)
    time.sleep(1)
    print(stri)

    if stri.__contains__('is7'):
        push = pb.push_note('Alert', 'its 7')
    else:
        continue


# push = pb.push_note('Alert', 'My name iS AJyesh')

