import pytest
from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:


   # пример теста:
   # обязательно указывать префикс test_
   # дальше идет название метода, который тестируем add_new_book_
   # затем, что тестируем add_two_books - добавление двух книг
   def test_add_new_book_add_two_books(self):
       # создаем экземпляр (объект) класса BooksCollector
       collector = BooksCollector()


       # добавляем две книги
       collector.add_new_book('Гордость и предубеждение и зомби')
       collector.add_new_book('Что делать, если ваш кот хочет вас убить')


       # проверяем, что добавилось именно две
       # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
       assert len(collector.books_genre) == 2


   # напиши свои тесты ниже
   # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
   def test_set_book_genre(self):
       # создаем экземпляр (объект) класса BooksCollector
       collector = BooksCollector()
       # добавляем две книги
       collector.add_new_book('Гордость и предубеждение и зомби')
       collector.add_new_book('Что делать, если ваш кот хочет вас убить')
       # добавляем две книги  с жанрами
       collector.set_book_genre('Гордость и предубеждение и зомби','Фантастика')
       collector.set_book_genre('Что делать, если ваш кот хочет вас убить','Ужасы')
       # проверяем жанры книг по названию
       assert 'Гордость и предубеждение и зомби' in collector.books_genre.keys()
       assert 'Что делать, если ваш кот хочет вас убить' in collector.books_genre.keys()
       assert 'Фантастика' in collector.books_genre.values()
       assert 'Ужасы' in collector.books_genre.values()


   @pytest.mark.parametrize("name, genre", [['Гордость и предубеждение и зомби', 'Фантастика'],['Что делать, если ваш кот хочет вас убить', 'Ужасы']])
   def test_get_book_genre(self, name, genre):
       # создаем экземпляр (объект) класса BooksCollector
       collector = BooksCollector()
       # добавляем две книги
       collector.add_new_book(name)
       # добавляем две книги  с жанрами
       collector.set_book_genre(name, genre)
       # проверяем жанры книг по названию
       assert collector.books_genre[name] == genre


   def test_get_books_with_specific_genre(self):
       # создаем экземпляр (объект) класса BooksCollector
       collector = BooksCollector()
       # добавляем 3 книги
       collector.add_new_book('Гордость и предубеждение и зомби')
       collector.add_new_book('Что делать, если ваш кот хочет вас убить')
       collector.add_new_book('Москва - Кассиопея')
       # добавляем 3 книги  с жанрами, 2 из них в жанре Фантастика
       collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
       collector.set_book_genre('Что делать, если ваш кот хочет вас убить', 'Ужасы')
       collector.set_book_genre('Москва - Кассиопея', 'Фантастика')
       # убеждаемся, что только 2 книги в списке в жанре Фантастика
       assert len(collector.get_books_with_specific_genre("Фантастика")) == 2


   def test_get_books_genre(self):
       # создаем экземпляр (объект) класса BooksCollector
       collector = BooksCollector()
       # добавляем две книги
       collector.add_new_book('Гордость и предубеждение и зомби')
       collector.add_new_book('Самая длинная книга для проверки длины текста свыше сорока одного символа')
       # добавляем две книги  с жанрами
       collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
       collector.set_book_genre('Самая длинная книга для проверки длины текста свыше сорока одного символа', 'Детективы')
       # проверяем жанры книг по названию
       assert 'Гордость и предубеждение и зомби' in collector.books_genre.keys()
       assert 'Самая длинная книга для проверки длины текста свыше сорока одного символа' not in collector.books_genre.keys()
       assert 'Фантастика' in collector.books_genre.values()
       assert 'Детективы' not in collector.books_genre.values()


   def test_get_books_for_children(self):
       # создаем экземпляр (объект) класса BooksCollector
       collector = BooksCollector()
       # добавляем 3 книги
       collector.add_new_book('Гордость и предубеждение и зомби')
       collector.add_new_book('Не детская книжка')
       collector.add_new_book('Ну, погоди')
       # добавляем 3 книги  с жанрами
       collector.set_book_genre('Гордость и предубеждение и зомби', 'Фантастика')
       collector.set_book_genre('Не детская книжка','Детективы')
       collector.set_book_genre('Ну, погоди', 'Мультфильмы')
       # Проверяем, что только 2 книги добавилось в список для детей
       assert len(collector.get_books_for_children()) == 2
       # Проверяем, что такого названия нет в списке
       assert 'Не детская книжка' not in collector.get_books_for_children()


   def test_add_book_in_favorites(self):
       # создаем экземпляр (объект) класса BooksCollector
       collector = BooksCollector()
       # добавляем 2 книги
       collector.add_new_book('Гордость и предубеждение и зомби')
       collector.add_new_book('Не детская книжка')
       # добавляем 2 книги в избранное
       collector.add_book_in_favorites('Гордость и предубеждение и зомби')
       collector.add_book_in_favorites('Не детская книжка')
       # Проверяем, что 2 книги добавились в избранное
       assert len(collector.favorites) == 2


   def test_delete_book_from_favorites(self):
       # создаем экземпляр (объект) класса BooksCollector
       collector = BooksCollector()
       # добавляем две книги
       collector.add_new_book('Гордость и предубеждение и зомби')
       collector.add_new_book('Не детская книжка')
       # добавляем 2 книги в избранное
       collector.add_book_in_favorites('Гордость и предубеждение и зомби')
       collector.add_book_in_favorites('Не детская книжка')
       # удаляем одну из книг
       collector.delete_book_from_favorites('Не детская книжка')
       # проверяем, что книга удалена
       assert 'Не детская книжка' not in collector.favorites


   def test_get_list_of_favorites_books(self):
       # создаем экземпляр (объект) класса BooksCollector
       collector = BooksCollector()
       # добавляем две книги
       collector.add_new_book('Гордость и предубеждение и зомби')
       collector.add_new_book('Не детская книжка')
       # добавляем 2 книги в избранное
       collector.add_book_in_favorites('Гордость и предубеждение и зомби')
       collector.add_book_in_favorites('Не детская книжка')
       # удаляем одну из книг
       collector.delete_book_from_favorites('Не детская книжка')
       assert 'Гордость и предубеждение и зомби' in collector.favorites
