import datetime
import timezones
import timestamp
t = datetime.datetime.now()
print(t)


from pandas import Timestamp

# Create a Timestamp object
timestamp = Timestamp(datetime.datetime.now(), tz='UTC')

# Format the Timestamp as a string
formatted_timestamp = timestamp.strftime('%Y-%m-%d %H:%M:%S.%f%z')

print(formatted_timestamp)
print(timestamp)
