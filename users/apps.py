from django.apps import AppConfig

class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    def ready(self):
        # We leave this empty for the first migration to prevent crashes
        try:
            import users.signals
        except ImportError:
            pass