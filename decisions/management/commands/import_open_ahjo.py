from django.core.management.base import BaseCommand, CommandError
from decisions.importer.open_ahjo import OpenAhjoImporter


class Command(BaseCommand):
    help = 'Imports Open Ahjo data'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        importer = OpenAhjoImporter(options)
        importer.import_data(options['filename'])
