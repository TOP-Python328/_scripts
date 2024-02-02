select 2 + 3 as 'col' from country;

-- +-----+
-- | col |
-- +-----+
-- |   5 |
-- |   5 |
-- .......
-- |   5 |
-- |   5 |
-- +-----+
-- 239 rows in set (0.0008 sec)


select code, code2, name from country;

-- +------+-------+-------------+
-- | code | code2 | name        |
-- +------+-------+-------------+
-- | ABW  | AW    | Aruba       |
-- | AFG  | AF    | Afghanistan |
-- ..............................
-- | ZMB  | ZM    | Zambia      |
-- | ZWE  | ZW    | Zimbabwe    |
-- +------+-------+-------------+
-- 239 rows in set (0.0012 sec)


select 
  name, 
  surfacearea, 
  population 
from country;

-- +-------------+-------------+------------+
-- | name        | surfacearea | population |
-- +-------------+-------------+------------+
-- | Aruba       |      193.00 |     103000 |
-- | Afghanistan |   652090.00 |   22720000 |
-- ..........................................
-- | Zambia      |   752618.00 |    9169000 |
-- | Zimbabwe    |   390757.00 |   11669000 |
-- +-------------+-------------+------------+
-- 239 rows in set (0.0015 sec)


select
  name,
  population / surfacearea as 'density'
from country;

-- +-------------+------------+
-- | name        | density    |
-- +-------------+------------+
-- | Aruba       |   533.6788 |
-- | Afghanistan |    34.8418 |
-- ............................
-- | Zambia      |    12.1828 |
-- | Zimbabwe    |    29.8625 |
-- +-------------+------------+
-- 239 rows in set (0.0023 sec)


select
  name,
  population
from city;

-- +----------+------------+
-- | name     | population |
-- +----------+------------+
-- | Kabul    |    1780000 |
-- | Qandahar |     237500 |
-- .........................
-- | Nablus   |     100231 |
-- | Rafah    |      92020 |
-- +----------+------------+
-- 4079 rows in set (0.0069 sec)
