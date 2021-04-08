-- 1
-- What are the column names?
SELECT *
FROM orders
LIMIT 10;

-- 2 
-- How recent is this data?
select distinct order_date
from orders
order by order_date desc;


-- 3
-- Instead of selecting all the columns using *, 
-- write a query that selects only the special_instructions column.
select special_instructions 
from orders
-- Limit the result to 20 rows.



-- 4 
-- Can you edit the query so that we are only 
-- returning the special instructions that are not empty?
where special_instructions is not null
and special_instructions like '%sauce%'

-- 5
-- Let’s go even further and sort the instructions 
-- in alphabetical order (A-Z).
order by special_instructions 
limit 20;

-- 6
-- Let’s search for special instructions that have the word ‘sauce’.

-- Are there any funny or interesting ones? 


-- 7
-- Let’s search for special instructions that have the word ‘door’.
-- Any funny or interesting ones?
select special_instructions
from orders
where special_instructions like '%door%';

-- 8
-- Let’s search for special instructions that have the word ‘box’.
-- Any funny or interesting ones?
select id, special_instructions
from orders
where special_instructions like '%box%';

-- 9
-- Instead of just returning the special instructions, also return their order ids.

-- For more readability:
-- Rename id as ‘#’
-- Rename special_instructions as ‘Notes’
select id as '#', special_instructions as 'Notes'
from orders
where special_instructions like '%box%';

-- 10
-- Challenge
-- They have asked you to query the customer who made the phrase. 
-- Return the item_name restaurant_id, and user_id for the person created the phrase.
--- what phrase???

