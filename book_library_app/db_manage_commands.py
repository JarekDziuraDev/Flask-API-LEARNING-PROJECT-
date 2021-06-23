import json
from pathlib import Path
from datetime import datetime
from book_library_app import app, db
from book_library_app.model import Author



@app.cli.group()
def db_manage():
    """Opis komendy"""
    pass

@db_manage.command()
def add_data():
    """Opsi"""
    try:
        authors_path = Path(__file__).parent / 'samples' / 'authors.json'
        with open(authors_path) as file:
            data_jason = json.load(file)

        for item in data_jason:
            item['birth_date'] = datetime.strptime(item['birth_date'], '%d-%m-%Y').date()
            author = Author(**item)
            db.session.add(author)
        db.session.commit()
        print('Data has been succesfully added to databases')
    except Exception as ex:
        print("Unexpected error: {}".format(ex))


@db_manage.command()
def remove_data():
    """Opis"""
    try:
        db.session.execute('TRUNCATE TABLE authors')
        db.session.commit()
        print('Data has been succesfully remove from databases')
    except Exception as ex:
        print("Unexpected error: {}".format(ex))