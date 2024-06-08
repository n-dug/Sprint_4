import pytest

from main import BooksCollector


@pytest.fixture()
def collector(name, genre):
    collector = BooksCollector()
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    return collector


