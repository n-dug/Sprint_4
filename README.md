# qa_python
Список реализованных тестов:
- Два вида проверки добавления новой книги:
 * Предусловия / требования: Её жанр есть в списке жанров класса BooksCollector и длина наименования - не более
40 символов. 
  + Наименование и параметры метода: test_add_new_book_add_book_true(self, collector, name, genre).
 * Предусловия / требования: Её жанр не содержится в списке жанров класса BooksCollector или длина наименования - не более
40 символов.
  + Наименование и параметры метода: test_add_new_book_add_book_false(self, collector, name, genre).

- Проверка присвоения книге жанра и получения текущего списка жанров книг. 
 * Предусловия / требования: Книга внесена в список книг с жанрами books_genre и её жанр входит в текущий список жанров
genre. 
  + Наименование и параметры метода: test_set_book_genre_true(self, collector, name, genre).
  + Наименование и параметры метода: test_get_books_genre_true(self, collector, name, genre).

- Проверка получения списка книг с конкретным жанром.
 * Предусловия / требования: Жанр книги передан методу get_books_with_specific_genre(self, genre).
  + Наименование и параметры метода: test_get_books_with_specific_genre_true(self, collector, name, genre).

- Проверка отсутствия книг с возрастным рейтингом в списке детских книг.
 * Предусловия / требования: get_books_for_children возвращает книги, которые подходят детям. У жанра книги не должно быть возрастного рейтинга.
  + Наименование и параметры метода: test_get_books_for_children_true(self, collector, name, genre).

-  Проверка добавления книги в избранное, получения списка избранных книг и удаления книги из списка.
 * Предусловия / требования: Книга должна находиться в словаре books_genre. Повторно добавить книгу в избранное нельзя.
  + Наименование и параметры метода: test_add_book_in_favorites_add_book_once_true(self, collector, name, genre).
  + Наименование и параметры метода: test_get_list_of_favorites_books_true(self, collector, name, genre).
  + Наименование и параметры метода: test_delete_book_from_favorites_true(self, collector, name, genre).




         