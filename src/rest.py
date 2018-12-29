import uuid
import json

from flask import request
from flask_restful import Resource, abort

from .redis_helper import get_redis


def authenticate():
    """ Simple API authentication """

    token = request.headers.get('X-Auth-Token') or None

    if token not in ['88d72110d6c27f7d231c4c3197364ef0a17551c5', '137fb4b88f9a75d47d9ea5753e5ad40faf985c70']:
        abort(401, message='401 Unauthorized')


class Generate(Resource):
    def get(self):
        """ Generate a new request """

        authenticate()

        # Generate a new request
        id_ = str(uuid.uuid4()).replace('-', '')

        # Add to queue
        payload = {
            'id_': id_
        }
        get_redis().rpush('weather_requests', json.dumps(payload))
        get_redis().set('weather_pending_' + id_, '1')

        # Default to 200 OK
        return {
            'success': True,
            'id': id_,
        }


class Retrieve(Resource):
    def get(self, id_):
        """ Get a response """

        authenticate()

        # Look for item in queue
        item = get_redis().get('weather_response_' + id_)

        if item:  # Item found
            item = json.loads(item)

            return {
                'success': True,
                'pending': False,
                'id': id_,
                'temp_f': item['temp_f'],
                'forecast_url': item['forecast_url'],
                'stations': [{'lat': station[0], 'lon': station[1]} for station in item['lat_lon']],
            }
        else:  # Not found
            pending = get_redis().get('weather_pending_' + id_)

            if pending:  # Item is pending
                return {
                    'success': True,
                    'pending': True,
                    'id': id_,
                }
            else:  # Item does not exists
                abort(404, message="ID {} doesn't exist".format(id_))
