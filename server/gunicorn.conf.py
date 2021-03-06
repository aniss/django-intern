import multiprocessing

bind            = "127.0.0.1:8000"
workers         = multiprocessing.cpu_count() * 2 + 1
#django_settings = "project_settings.local"
pythonpath      = "/home/aniss/vpm/djangointern"
accesslog       = "server/logs/gunicorn/access.log"
errorlog        = "server/logs/gunicorn/error.log"
user            = "aniss"
group           = "aniss"
loglevel        = "debug"
