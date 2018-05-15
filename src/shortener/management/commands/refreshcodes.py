from django.core.management.base import BaseCommand, CommandError

from shortener.models import MyUrl

class Command(BaseCommand):
    help = 'Refreshes all URL shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        return MyUrl.objects.refresh_shortcode(items=options['items'])
