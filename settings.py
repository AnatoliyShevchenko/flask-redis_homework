# Flask
from flask import Flask
from flask_caching import Cache

# Python
from decouple import config


# Flask
app = Flask(__name__)

# Flask-Caching
cache = Cache(app, config={
    'CACHE_TYPE' : 'redis',
    'CACHE_REDIS_URL' : config('REDIS_URL')
})

# API
url = config('URL')
headers = {
    	"X-RapidAPI-Key": config('X_KEY'),
    	"X-RapidAPI-Host": config('X_HOST')
    }