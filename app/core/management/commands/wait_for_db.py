import time

from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Comand Django"""

    def handle(self, *args,  **options):
        self.stdout.write('Esperando la Base de Datos')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Datos indisponible,espere 1 segundo..')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Base de Datos Disponible!!.'))
