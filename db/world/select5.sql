select name
  from city
 where population >= 1000000;

-- +-------------+
-- | name        |
-- +-------------+
-- | Kabul       |
-- | Alger       |
-- ...............
-- | San Antonio |
-- | Harare      |
-- +-------------+
-- 238 rows in set (0.0050 sec)


  select name
    from country
   where region = 'Eastern Europe'
order by population desc;

-- +--------------------+
-- | name               |
-- +--------------------+
-- | Russian Federation |
-- | Ukraine            |
-- | Poland             |
-- | Romania            |
-- | Czech Republic     |
-- | Belarus            |
-- | Hungary            |
-- | Bulgaria           |
-- | Slovakia           |
-- | Moldova            |
-- +--------------------+
-- 10 rows in set (0.0007 sec)


  select name
    from city
   where countrycode = 'RUS'
order by population
   limit 1;

-- +---------------+
-- | name          |
-- +---------------+
-- | Novyi Urengoi |
-- +---------------+
-- 1 row in set (0.0051 sec)


select name
  from country
 where indepyear is null;

-- +----------------------+
-- | name                 |
-- +----------------------+
-- | Aruba                |
-- | Anguilla             |
-- ........................
-- | Virgin Islands, U.S. |
-- | Wallis and Futuna    |
-- +----------------------+
-- 47 rows in set (0.0009 sec)


select name
  from country
 where indepyear between 0 and 1000;

-- +------------+
-- | name       |
-- +------------+
-- | Denmark    |
-- | France     |
-- | San Marino |
-- | Sweden     |
-- +------------+
-- 4 rows in set (0.0015 sec)


select name
  from city
 where name like 'a%a';

-- +----------------------+
-- | name                 |
-- +----------------------+
-- | Annaba               |
-- | Andorra la Vella     |
-- ........................
-- | Alexandria           |
-- | Arvada               |
-- +----------------------+
-- 83 rows in set (0.0058 sec)


select name
  from country
 where continent in ('Europe', 'Asia');

-- +--------------+
-- | name         |
-- +--------------+
-- | Afghanistan  |
-- | Albania      |
-- ................
-- | Yemen        |
-- | Yugoslavia   |
-- +--------------+
-- 97 rows in set (0.0010 sec)


select name
  from country
 where continent = 'Europe' 
    or continent = 'Asia';

-- +--------------+
-- | name         |
-- +--------------+
-- | Afghanistan  |
-- | Albania      |
-- ................
-- | Yemen        |
-- | Yugoslavia   |
-- +--------------+
-- 97 rows in set (0.0009 sec)


select name
  from country
 where char_length(name) <= 4;

-- +------+
-- | name |
-- +------+
-- | Cuba |
-- | Guam |
-- | Iran |
-- | Iraq |
-- | Laos |
-- | Mali |
-- | Niue |
-- | Oman |
-- | Peru |
-- | Chad |
-- | Togo |
-- +------+
-- 11 rows in set (0.0009 sec)
