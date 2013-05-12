from base import *

########## TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = SITE_ROOT
TEST_DISCOVER_ROOT = SITE_ROOT
TEST_DISCOVER_PATTERN = "test_*.py"
########## DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}_test',
        'USER': '{{ project_name }}_test',
        'PASSWORD': '{{ project_name }}_test',
        'PORT': '5432',
        'HOST': 'localhost',
        'OPTIONS': {
            'autocommit': True,
        }
    }
}


########## CELERY CONFIGURATION
# See: http://docs.celeryproject.org/en/latest/getting-started/brokers/redis.html#broker-redis
BROKER_URL = 'redis://localhost:6379/0'
########## END CELERY CONFIGURATION
