-- group books by the decade of publication and count the number of books in each decade
SELECT FLOOR(year_published / 10) * 10 AS decade,
       COUNT(*) AS books_in_decade
FROM books
GROUP BY decade;