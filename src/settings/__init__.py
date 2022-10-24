import os

settings_module = os.environ.get('INTEGRADOR_SETTINGS', None)

if not settings_module:
    from .sandbox import *
else:
    exec(f'from {settings_module} import *')
