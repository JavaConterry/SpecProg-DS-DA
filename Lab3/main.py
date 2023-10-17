from spyre import server
import lab2 as NOAA_access

data = NOAA_access.request_data
print(data[1])