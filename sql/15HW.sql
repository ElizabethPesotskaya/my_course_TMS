--Задача 1
--Создала таблицу "authors" с полями "first_name", "last_name"
CREATE TABLE authors (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(50)
);

--Создала таблицу «book» с полями "title", "author_id" , "publication_year" 
CREATE TABLE books (
  id SERIAL PRIMARY KEY,
  author_id INTEGER REFERENCES authors(id),
  title VARCHAR(200),
  publication_year INTEGER
);

--Создала таблицу "sales" с полями "book_id", "quantity"
CREATE TABLE sales (
  id SERIAL PRIMARY KEY,
  book_id INTEGER REFERENCES books(id),
  quantity INTEGER
);

--Вставила в таблицу несколько авторов
INSERT INTO authors (first_name, last_name)
VALUES
('Alexander', 'Pushkin'),
('Mikhail', 'Lermontov'),
('Leo', 'Tolstoy');

--Вставила в таблицу  книги авторов 
INSERT INTO books (title, author_id, publication_year)
VALUES
('Eugene Onegin', 1, 1833),
('A Hero of Our Time', 2, 1840),
('War and Peace', 3, 1869);

--Вставила в таблицу продажи этих книг
INSERT INTO sales (book_id, quantity)
VALUES
(1, 1500),
(2, 456),
(3, 1200);



--Задача 2 
--Используйте INNER JOIN для получения списка всех книг и их авторов
SELECT books.title, authors.first_name, authors.last_name
FROM books
INNER JOIN authors ON books.author_id = authors.id;

--Используйте LEFT JOIN для получения списка всех авторов и их книг (включая авторов, у которых нет книг).
SELECT books.title, authors.first_name, authors.last_name
FROM authors
LEFT JOIN books ON books.author_id = authors.id;

--Используйте RIGHT JOIN для получения списка всех книг и их авторов, включая книги, у которых автор не указан
SELECT books.title, authors.first_name, authors.last_name
FROM books
RIGHT JOIN authors ON books.author_id = authors.id;




--Задача 3 
--Используйте INNER JOIN для связывания таблиц authors, books и sales, чтобы получить список всех книг, их авторов ипродаж
SELECT books.title, authors.first_name, authors.last_name, sales.quantity
FROM books
INNER JOIN authors ON books.author_id = authors.id
INNER JOIN sales ON books.id = sales.book_id;

--Используйте LEFT JOIN для связывания таблиц authors, books и sales, чтобы получить список всех авторов, их книг и продаж (включая авторов без книг и книги без продаж)
SELECT books.title, authors.first_name, authors.last_name, sales.quantity
FROM authors
LEFT JOIN books ON books.author_id = authors.id
LEFT JOIN sales ON books.id = sales.book_id;




--Задание 4 
--Используйте INNER JOIN и функции агрегации для определения общего количества проданных книг каждого автора
SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sold
FROM authors
INNER JOIN books ON authors.id = books.author_id
INNER JOIN sales ON books.id = sales.book_id
GROUP BY authors.id, authors.first_name, authors.last_name;

--Используйте LEFT JOIN и функции агрегации для определения общего количества проданных книг каждого автора, включая авторов без продаж
SELECT authors.first_name, authors.last_name, COALESCE(SUM(sales.quantity), 0) AS total_sold
FROM authors
LEFT JOIN books ON authors.id = books.author_id
LEFT JOIN sales ON books.id = sales.book_id
GROUP BY authors.id, authors.first_name, authors.last_name;




--Задание 5 
--Найдите автора с наибольшим количеством проданных книг, используя подзапросы и JOIN
SELECT authors.first_name, authors.last_name, SUM(sales.quantity) AS total_sold
FROM authors
JOIN books ON authors.id = books.author_id
JOIN sales ON books.id = sales.book_id
GROUP BY authors.id, authors.first_name, authors.last_name
HAVING SUM(sales.quantity) = (
  SELECT MAX(total)
  FROM (
    SELECT SUM(s.quantity) AS total
    FROM authors a
    JOIN books b ON a.id = b.author_id
    JOIN sales s ON b.id = s.book_id
    GROUP BY a.id
  ) AS subquery
);

--Найдите книги, которые были проданы в количестве, превышающем среднее количество продаж всех книг, используя подзапросы и JOIN
SELECT books.title, SUM(sales.quantity) AS total_sold
FROM books
JOIN sales ON books.id = sales.book_id
GROUP BY books.id, books.title
HAVING SUM(sales.quantity) > (
  SELECT AVG(total)
  FROM (
    SELECT SUM(quantity) AS total
    FROM sales
    GROUP BY book_id
  ) AS subquery
);
