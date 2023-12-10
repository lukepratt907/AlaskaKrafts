import csv
from books.models import Store, Book


STORES_FILENAME = "books/seeddata/stores.csv"
def run():
    print(f'Opening file: {STORES_FILENAME}')
    with open(STORES_FILENAME) as incsvfile:
        reader = csv.DictReader(incsvfile)
        for row in reader:
            print(f'Processing row: {row}')
            name = row['name']
            address = row['address']
            link = row['link']
            # if not Airport.objects.filter(code=code, city=city).exists():
            #     a=Airport(code=code, city=city)
            #     a.save()
            Store.objects.get_or_create(name=name, address=address, link=link)



'''
class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **options):
        # Open and read the CSV file
        with open('seeddata/seeddata.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Create Store instance if it doesn't exist
                store, created = Store.objects.get_or_create(
                    name=row['name'],
                    address=row['address']
                    # Add other fields as needed
                )

                # Create Book instance if it doesn't exist
                book, created = Book.objects.get_or_create(
                    title=row['book_title']
                    # Add other fields as needed
                )

                # Add the store to the book's stores
                book.stores.add(store)
'''