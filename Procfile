web: gunicorn --pythonpath {{ project_name }} {{ project_name }}.wsgi
worker: python {{ project_name }}/manage.py celery worker
