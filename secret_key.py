
from app import app
import os

from dotenv import load_dotenv



load_dotenv('.env')



STRIPE_PUBLIC_KEY = os.environ.get('STRIPE_PUBLIC_KEY')
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')



