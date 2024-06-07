-- update records in the authors data set to X where last name is Collins
update authors
SET last_name = 'Award Winning'
where last_name = 'Collins';

-- update records in the books data set to reflect Books Made into Movies in the 2000s
UPDATE books
SET title = 'Books Made into Movies in the 2000s'
WHERE year_published IN ('1925', '1813', '1954', '1997');