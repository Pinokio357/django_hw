from django.core.management.base import BaseCommand
from ....shopapp.models import Client

class Command(BaseCommand):


    def handle(self, *args, **options):
        clients = Client.objects.all()
        self.stdout.write(f"{clients}")
