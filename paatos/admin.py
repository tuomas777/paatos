from django.apps import apps
from django.contrib import admin

for model in apps.get_app_config("paatos").get_models():
    admin.register(model)
