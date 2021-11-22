from django.apps import AppConfig
from django.conf import settings
import os
import joblib

class ApiConfig(AppConfig):
    name = 'api'
    MODEL_FILE = os.path.join(settings.MODELS, "finalized_model.sav")
    model = joblib.load(MODEL_FILE)