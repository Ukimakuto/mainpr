from django.apps import AppConfig
# apps.py
# help the user include any application configuration for the app.
class LecturesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lectures'
