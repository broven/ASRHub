# Create Rocketry app
from rocketry import Rocketry
app = Rocketry()

# import BaseCommand
from django.core.management.base import BaseCommand

# Create some tasks

class Command(BaseCommand):
    help = "Setup the periodic tasks runner"

    def handle(self, *args, **options):
        app.run()
        print('ok')