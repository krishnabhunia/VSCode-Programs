from pandas import Timestamp
import datetime

import timestamp
import timezones

t = datetime.datetime.now()
print(t)


# Create a Timestamp object
timestamp = Timestamp(datetime.datetime.now(), tz='UTC')

# Format the Timestamp as a string
formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S.%f%z')

print(formatted_timestamp)
print(timestamp)
