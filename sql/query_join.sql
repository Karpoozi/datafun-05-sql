-- retrieve titles and authors' last names using INNER JOIN
SELECT b.title, a.last_name
FROM books b
INNER JOIN authors a ON b.author_id = a.author_id;

