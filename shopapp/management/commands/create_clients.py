from django.core.management.base import BaseCommand
from ....shopapp.models import Client

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("count", type=int, help="client count")

    def handle(self, *args, **kwargs):
        count = kwargs["count"]
        for i in range(count):
            client = Client(name=f"client_{i}", email=f"email_{i}@mail.ru", phone=f"99999999{i}", address=f"address_{i}")
            client.save()

