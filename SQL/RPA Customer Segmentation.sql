-- 1
-- What are the column names?
SELECT *
FROM users
LIMIT 20;
 
-- 2
-- Find the email addresses and birthdays of users whose 
-- birthday is between 1980-01-01 and 1989-12-31.
select email, birthday
from users
where birthday between 1980-01-01 and 1990-01-01;
   
-- 3
-- Find the emails and creation date of users 
-- whose created_at date matches this condition.
select *
from users
where created_at < '2017-05-01';

-- 4
-- Find the emails of the users who received the ‘bears’ test.
select *
from users
where test = 'bears';

-- 5
-- Find all the emails of all users who 
-- received a campaign on website BBB.
select email, campaign
from users
where campaign like 'BBB%';

-- 6
-- Find all the emails of all users who received ad copy 2 in 
-- their campaign.
select email, campaign
from users
where campaign like '%2';

-- 7
-- Find the emails for all users who received both a campaign and a test. 
-- These users will have non-empty entries in the 
-- campaign and test columns.
select email, campaign, test
from users
where campaign is not null
and test is not null;

-- 8
-- Challenge
-- One of the members of the marketing team had an idea of calculating
-- how old users were when they signed up.
alter table users
add age integer;
update users
set age = created_at - birthday;
select *
from users
limit 20;


