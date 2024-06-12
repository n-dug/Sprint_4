from main import BooksCollector
import pytest


# класс TestBooksCollector объединяет набор тестов для приложения BooksCollector
class TestBooksCollector:

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Твин Пикс', 'Детективы']
        ]
    )
    def test_add_new_book_new_book_added(self, name, genre):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # проверка добавления новой книги с жанром в списке жанров и с кол-вом символов <= 40
        assert collector.books_genre[name] == genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Вялые паруса', 'Драма'],
            ['Консервный ряд', 'Жанр для проверки на количество символов > 40']
        ]
    )
    def test_add_new_book_not_added_books(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # проверка того, что новые книги с жанрами не в списке жанров и с кол-вом символов > 40 не добавлены в список
        assert collector.books_genre[name] != genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Твин Пикс', 'Детективы']
        ]
    )
    def test_set_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # проверяем, что книге задан жанр, если она есть в books_genre и её жанр входит в список genre
        assert genre == collector.books_genre[name]

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Твин Пикс', 'Детективы']
        ]
    )
    def test_get_books_with_specific_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # проверяем получение списка книг с определенным жанром
        assert name in collector.get_books_with_specific_genre(genre)

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Сборник Агаты Кристи', 'Детективы']
        ]
    )
    def test_get_books_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # проверяем получение словаря
        assert genre in collector.get_books_genre().values()

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Ну, погоди!', 'Мультфильмы']
        ]
    )
    def test_get_book_genre(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # проверяем получение книги по жанру
        assert genre in collector.get_book_genre(name)

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Ну, погоди!', 'Мультфильмы']
        ]
    )
    def test_get_books_for_children(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # проверяем, что детская книга есть в списке книг для детей
        collector.genre_age_rating.append(name)
        assert name in collector.get_books_for_children()

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Твин Пикс', 'Детективы']
        ]
    )
    def test_add_book_in_favorites_add_book_once(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # добавляем одну и ту же книгу в избранное два раза
        # проверяем, что она добавится всего один раз
        collector.add_book_in_favorites(name)
        collector.add_book_in_favorites(name)
        assert collector.favorites.count(name) == 1

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Оно', 'Ужасы']
        ]
    )
    def test_get_list_of_favorites_books(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # добавляем книгу в избранное
        collector.add_book_in_favorites(name)
        # проверяем наличие первой книги в избранном
        assert name in collector.get_list_of_favorites_books()
        # добавляем ещё одну книгу в избранное
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        collector.add_book_in_favorites('Гарри Поттер')
        # проверяем наличие второй книги в избранном
        assert 'Гарри Поттер' in collector.get_list_of_favorites_books()

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Супер Марио', 'Мультфильмы']
        ]
    )
    def test_delete_book_from_favorites_book_deleted(self, name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        # добавляем книгу в избранное и проверяем её удаление
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites
