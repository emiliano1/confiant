import requests
import json

from ..redis_helper import get_redis


while True:
    item = json.loads(get_redis().blpop('weather_requests', timeout=None)[1])

    # WU Rest endpoint
    r = requests.get(
        'http://api.wunderground.com/api/d8fc77c2b9c3a4e7/geolookup/conditions/q/NY/New_York.json')

    if r.ok:
        data = r.json()

        if 'location' in data:
            airport_stations = data['location']['nearby_weather_stations']['airport']['station']
            pws_stations = data['location']['nearby_weather_stations']['pws']['station']
            nearby_weather_stations = airport_stations + pws_stations

            response = {
                "temp_f": data['current_observation']['temp_f'],
                "forecast_url": data['current_observation']['forecast_url'],
                "lat_lon": [[s['lat'], s['lon']] for s in nearby_weather_stations]
            }

            # Save result in appropriate key with a TTL of 600 seconds
            get_redis().set('weather_response_' + item['id_'], json.dumps(response), ex=600)
    else:
        # Add back to queue in case of failed request
        get_redis().rpush('weather_requests', json.dumps(item))
