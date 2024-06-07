-- update records in the authors data set to X where last name is Collins
update authors
SET last_name = 'Award Winning'
where last_name = 'Collins';

-- update records in the books to silly name
UPDATE books
SET title = 'Books I Fell Asleep Reading'
WHERE LENGTH(title) >= 1;
