import requests

# WU Rest endpoint
r = requests.get(
    'http://api.wunderground.com/api/d8fc77c2b9c3a4e7/geolookup/conditions/q/NY/New_York.json')

# Pop items from `weather_requests`. The payload will have the following format:

# {
#     'id_': 'some_id'
# }

# Create a response with the following format:

# {
# "temp_f": 75.3,
# "forecast_url": "http://www.wunderground.com/...",
# "lat_lon": [
#     [
#     "40.77000046",
#     "-73.98000336"
#     ],
#     [
#     "40.70000076",
#     "-74.01000214"
#     ]
# ]
# }

# Save result in appropriate key with a TTL of 600 seconds
