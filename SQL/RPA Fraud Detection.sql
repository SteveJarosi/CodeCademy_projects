-- 1
-- What are the column names?
SELECT *
FROM transaction_data
LIMIT 10;

-- 2
-- Find the full_names and emails
-- of the transactions listing 20252 as the zip code.
SELECT full_name, email
FROM transaction_data
where zip = 20252;

-- 3
-- Use a query to find the names 
-- and emails associated with these transactions.
SELECT *
FROM transaction_data
where full_name = 'Art Vandelay'
or full_name like '% der %';

-- 4
-- Find the ip_addresses and emails listed with these transactions.
SELECT ip_address, email
FROM transaction_data
where ip_address like '10.%';

-- 5
-- Find the emails in transaction_data with
-- ‘temp_email.com’ as a domain.
SELECT *
FROM transaction_data
where email like '%temp_email.com';

-- 6
-- The finance department is looking for a specific transaction. 
-- They know that the transaction occurred from an ip address starting 
-- with ‘120.’ and their full name starts with ‘John’.

-- Can you find the transaction?
SELECT *
FROM transaction_data
where ip_address like '120.%'
and full_name like 'John%';

-- 7
-- Challenge
-- Return only those customers residing in GA. Use the list of ZIP CODE prefixes
-- (https://en.wikipedia.org/wiki/List_of_ZIP_Code_prefixes)
-- to determine the best query for zip codes belonging to Georgia(GA).
SELECT *
FROM transaction_data
where zip like '30%'
or zip like '31%'
order by zip;

SELECT *
FROM transaction_data
where zip between 30000 and 31999
order by zip;