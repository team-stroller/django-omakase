web: newrelic-admin gunicorn -b 0.0.0.0:$PORT --max-requests 50 -t 30
worker: newrelic-admin celeryd -E -B --loglevel=WARNING
redis: redis-server