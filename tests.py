# класс TestBooksCollector объединяет набор тестов для приложения BooksCollector

import pytest


class TestBooksCollector:

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Твин Пикс', 'Детективы']
        ]
    )
    def test_add_new_book_add_book_true(self, collector, name, genre):
        # проверка добавления новой книги с жанром в списке жанров и с кол-вом символов <= 40
        assert collector.books_genre[name] == genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Вялые паруса', 'Драма'],
            ['Консервный ряд', 'Жанр для проверки на количество символов > 40']
        ]
    )
    def test_add_new_book_add_book_false(self, collector, name, genre):
        # проверка добавления новой книги с жанром не в списке жанров или с кол-вом символов > 40
        assert collector.books_genre[name] != genre

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Твин Пикс', 'Детективы']
        ]
    )
    def test_set_book_genre_true(self, collector, name, genre):
        # проверяем, что книге задан жанр, если она есть в books_genre и её жанр входит в список genre
        assert genre == collector.books_genre[name]

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Твин Пикс', 'Детективы']
        ]
    )
    def test_get_books_with_specific_genre_true(self, collector, name, genre):
        # проверяем получение списка книг с определенным жанром
        assert genre in collector.books_genre[name]

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Сборник Агаты Кристи', 'Детективы']
        ]
    )
    def test_get_books_genre_true(self, collector, name, genre):
        # проверяем получение словаря
        assert collector.get_books_genre() is not None

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Твин Пикс', 'Детективы']
        ]
    )
    def test_get_books_for_children_true(self, collector, name, genre):
        # проверяем, что книги с возрастным рейтингом отсутствуют в списке книг для детей
        collector.genre_age_rating.append(name)
        assert genre not in collector.get_books_for_children()

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Твин Пикс', 'Детективы']
        ]
    )
    def test_add_book_in_favorites_add_book_once_true(self, collector, name, genre):
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
    def test_get_list_of_favorites_books_true(self, collector, name, genre):
        # добавляем книгу в избранное и проверяем вывод списка избранных книг
        collector.add_book_in_favorites(name)
        assert collector.get_list_of_favorites_books() is not None

    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Супер Марио', 'Мультфильмы']
        ]
    )
    def test_delete_book_from_favorites_true(self, collector, name, genre):
        # добавляем книгу в избранное и проверяем её удаление
        collector.add_book_in_favorites(name)
        collector.delete_book_from_favorites(name)
        assert name not in collector.favorites
