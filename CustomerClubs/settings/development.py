import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

import mongoengine
mongoengine.connect(db=os.environ.get("MONGO_DATABASE_NAME"), host=os.environ.get("MONGO_HOST"), username=os.environ.get("MONGO_USERNAME"), password=os.environ.get("MONGO_PASSWORD"))
