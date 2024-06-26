import json
from django.core.management.base import BaseCommand
from api.models import BlackCoffer
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Load energy data from JSON file into the database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as file:
            data = json.load(file)

        for item in data:
            # Check for required fields that should not be blank
            required_fields = ['intensity', 'sector', 'topic', 'insight', 'url', 'region', 'country', 'relevance', 'pestle', 'source', 'title', 'likelihood']
            if any(item[field] == "" for field in required_fields):
                self.stdout.write(self.style.WARNING(f"Skipping record with missing required fields: {item}"))
                continue

            # Parse date fields and handle blank dates
            added = parse_datetime(item['added']) if item['added'] else None
            published = parse_datetime(item['published']) if item['published'] else None

            BlackCoffer.objects.create(
                end_year=item.get('end_year', None),
                intensity=item['intensity'],
                sector=item['sector'],
                topic=item['topic'],
                insight=item['insight'],
                url=item['url'],
                region=item['region'],
                start_year=item.get('start_year', None),
                impact=item.get('impact', None),
                added=added,
                published=published,
                country=item['country'],
                relevance=item['relevance'],
                pestle=item['pestle'],
                source=item['source'],
                title=item['title'],
                likelihood=item['likelihood']
            )
        self.stdout.write(self.style.SUCCESS('Data successfully loaded'))
