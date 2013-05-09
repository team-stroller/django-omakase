from base import *

########## TEST SETTINGS
TEST_RUNNER = 'discover_runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = SITE_ROOT
TEST_DISCOVER_ROOT = SITE_ROOT
TEST_DISCOVER_PATTERN = "test_*.py"
########## IN-MEMORY TEST DATABASE
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
