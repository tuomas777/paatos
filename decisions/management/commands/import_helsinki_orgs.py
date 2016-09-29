from django.core.management.base import BaseCommand, CommandError
from decisions.importer.helsinki import HelsinkiImporter


class Command(BaseCommand):
    help = 'Imports Helsinki organizations'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        importer = HelsinkiImporter(options)
        importer.import_organizations(options['filename'])
        self.stdout.write(self.style.SUCCESS('All done!'))
