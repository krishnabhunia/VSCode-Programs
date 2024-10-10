import datetime as dt
import pandas as pd

# Get the current datetime
t = dt.datetime.now()
print(t)

# Create a Timestamp object using pandas with timezone
ts = pd.Timestamp(dt.datetime.now(), tz='UTC')

# Format the Timestamp as a string
formatted_timestamp = ts.strftime('%Y-%m-%d %H:%M:%S.%f%z')

print(formatted_timestamp)
print(ts)