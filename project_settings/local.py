from .base import *

"""
    Change STATIC_ROOT & STATICFILES_DIRS
    to serve all static files from /static dir.
"""

STATIC_ROOT = ''

STATICFILES_DIRS += (
    os.path.join(PROJECT_ROOT, 'static'),
    )
