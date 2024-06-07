-- calculate the total number of books, average year published, and total number of characters in titles
SELECT COUNT(*) AS total_books,
       AVG(year_published) AS average_year_published,
       SUM(LENGTH(title)) AS total_characters_in_titles

--calculate the average age of book
SELECT AVG(year_published) AS average_publish_year
FROM books;
