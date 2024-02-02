-- обычные функции вызываются для каждой извлечённой строки
select 
  name, 
  round(population / surfacearea, 1) as 'density' 
from country;

-- +-------------+---------+
-- | name        | density |
-- +-------------+---------+
-- | Aruba       |   533.7 |
-- | Afghanistan |    34.8 |
-- .........................
-- | Zambia      |    12.2 |
-- | Zimbabwe    |    29.9 |
-- +-------------+---------+
-- 239 rows in set (0.0332 sec)


select population from country;

-- +------------+
-- | population |
-- +------------+
-- |     103000 |
-- |   22720000 |
-- ..............
-- |    9169000 |
-- |   11669000 |
-- +------------+
-- 239 rows in set (0.0009 sec)


-- агрегирующие функции вызываются для каждой группы, созданной из извлечённых строк
-- в примере ниже создаётся одна группа для всех строк, извлечённых из таблицы country
select sum(population) from country;

-- +-----------------+
-- | sum(population) |
-- +-----------------+
-- |      6078749450 |
-- +-----------------+
-- 1 row in set (0.0028 sec)


select name, indepyear from country;

-- +--------------+-----------+
-- | name         | indepyear |
-- +--------------+-----------+
-- | Aruba        |      NULL |
-- | Afghanistan  |      1919 |
-- | Angola       |      1975 |
-- | Anguilla     |      NULL |
-- | Albania      |      1912 |
-- ............................
-- | Yemen        |      1918 |
-- | Yugoslavia   |      1918 |
-- | South Africa |      1910 |
-- | Zambia       |      1964 |
-- | Zimbabwe     |      1980 |
-- +--------------+-----------+
-- 239 rows in set (0.0007 sec)


select count(name) from country;

-- +-------------+
-- | count(name) |
-- +-------------+
-- |         239 |
-- +-------------+
-- 1 row in set (0.0017 sec)


select count(indepyear) from country;

-- +------------------+
-- | count(indepyear) |
-- +------------------+
-- |              192 |
-- +------------------+
-- 1 row in set (0.0006 sec)


select count(*) from country;

-- +----------+
-- | count(*) |
-- +----------+
-- |      239 |
-- +----------+
-- 1 row in set (0.0017 sec)


select count(*) from countrylanguage;

-- +----------+
-- | count(*) |
-- +----------+
-- |      984 |
-- +----------+
-- 1 row in set (0.0019 sec)


select count(*) from city;

-- +----------+
-- | count(*) |
-- +----------+
-- |     4079 |
-- +----------+
-- 1 row in set (0.0020 sec)


select count(distinct name) from country;

-- +----------------------+
-- | count(distinct name) |
-- +----------------------+
-- |                  239 |
-- +----------------------+
-- 1 row in set (0.0021 sec)


select count(continent) from country;

-- +------------------+
-- | count(continent) |
-- +------------------+
-- |              239 |
-- +------------------+
-- 1 row in set (0.0013 sec)


select count(distinct continent) from country;

-- +---------------------------+
-- | count(distinct continent) |
-- +---------------------------+
-- |                         7 |
-- +---------------------------+
-- 1 row in set (0.0007 sec)


select count(distinct region) from country;

-- +------------------------+
-- | count(distinct region) |
-- +------------------------+
-- |                     25 |
-- +------------------------+
-- 1 row in set (0.0008 sec)


select count(distinct governmentform) from country;

-- +--------------------------------+
-- | count(distinct governmentform) |
-- +--------------------------------+
-- |                             35 |
-- +--------------------------------+
-- 1 row in set (0.0008 sec)


select count(distinct language) from countrylanguage;

-- +--------------------------+
-- | count(distinct language) |
-- +--------------------------+
-- |                      457 |
-- +--------------------------+
-- 1 row in set (0.0018 sec)

