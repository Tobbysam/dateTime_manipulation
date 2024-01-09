from datetime import datetime
from datetime import timedelta
import time

# pull current system time
dateTime_now = datetime.now()
print (dateTime_now)


# dateTime minus one hour
dateTime_now_less_1hour = dateTime_now - timedelta(hours=1)
print (dateTime_now_less_1hour)

# removes decimals from timeStamp
formatted_dateTime = dateTime_now_less_1hour.strftime("%d/%m/%Y %H:%M:%S")
print (formatted_dateTime)

#dateTime to epoch
epoch = dateTime_now.timestamp()
print (epoch)

#modify epoch to custom DT fortmat
timestamp_epoch = time.strftime("%Y-%M-%D %H:%M:%S", time.localtime(epoch))
print (timestamp_epoch)