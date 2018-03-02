from datetime import datetime
import time

while 1==1:
    time.sleep(1)
    now = datetime.now()
    print("%s:%s:%s" % (now.hour, now.minute, now.second))
