from django.apps import AppConfig


class SaleConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.sale'

    def ready(self):
        """Import signals when app is ready."""
        import apps.sale.signals 