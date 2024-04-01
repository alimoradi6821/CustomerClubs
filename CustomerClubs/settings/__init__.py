from dotenv import load_dotenv
from split_settings.tools import include
import os

load_dotenv()


include('base.py')

if 'development' in os.environ.get('SETTINGS_MODE'):
    include('development.py')
elif 'production' in os.environ.get('SETTINGS_MODE'):
    include('production.py')