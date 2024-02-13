# yourapp/management/commands/import_books.py
import csv
from django.core.management.base import BaseCommand
from Book.models import Book

class Command(BaseCommand):
    help = 'Import books from CSV file to the database'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='Path to the CSV file, e.g., C:/Users/ASUS/Bookshelf/Bookshelf/books.csv')

    def handle(self, *args, **options):
        csv_file_path = options['csv_file']

        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Handle empty or non-numeric values for num_pages
                num_pages = int(row['num_pages']) if row['num_pages'].strip() else None

                # Handle empty or non-numeric values for average_rating
                average_rating = float(row['average_rating']) if row['average_rating'].strip() else None

                # Handle empty or non-numeric values for ratings_count
                ratings_count = int(row['ratings_count']) if row['ratings_count'].strip() else None

                # Handle empty or non-numeric values for published_year
                published_year = int(row['published_year']) if row['published_year'].strip() else None

                Book.objects.create(
                    isbn10=row['isbn10'],
                    title=row['title'],
                    authors=row['authors'],
                    categories=row['categories'],
                    thumbnail=row['thumbnail'],
                    description=row['description'],
                    published_year=published_year,
                    average_rating=average_rating,
                    num_pages=num_pages,
                    ratings_count=ratings_count,
                    price=row['price']
                )

        self.stdout.write(self.style.SUCCESS('Books imported successfully'))
