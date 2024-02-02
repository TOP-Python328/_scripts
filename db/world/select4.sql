select id, name from city limit 10;

-- +----+----------------+
-- | id | name           |
-- +----+----------------+
-- |  1 | Kabul          |
-- |  2 | Qandahar       |
-- |  3 | Herat          |
-- |  4 | Mazar-e-Sharif |
-- |  5 | Amsterdam      |
-- |  6 | Rotterdam      |
-- |  7 | Haag           |
-- |  8 | Utrecht        |
-- |  9 | Eindhoven      |
-- | 10 | Tilburg        |
-- +----+----------------+
-- 10 rows in set (0.0005 sec)


select id, name from city limit 5, 10;

-- +----+-----------+
-- | id | name      |
-- +----+-----------+
-- |  6 | Rotterdam |
-- |  7 | Haag      |
-- |  8 | Utrecht   |
-- |  9 | Eindhoven |
-- | 10 | Tilburg   |
-- | 11 | Groningen |
-- | 12 | Breda     |
-- | 13 | Apeldoorn |
-- | 14 | Nijmegen  |
-- | 15 | Enschede  |
-- +----+-----------+
-- 10 rows in set (0.0008 sec)


  select code, name, localname, region
    from country
order by surfacearea desc
   limit 1;

-- +------+--------------------+-----------+----------------+
-- | code | name               | localname | region         |
-- +------+--------------------+-----------+----------------+
-- | RUS  | Russian Federation | Rossija   | Eastern Europe |
-- +------+--------------------+-----------+----------------+
-- 1 row in set (0.0011 sec)


  select code, name, localname, region
    from country
order by population desc
   limit 1;

-- +------+-------+-----------+--------------+
-- | code | name  | localname | region       |
-- +------+-------+-----------+--------------+
-- | CHN  | China | Zhongquo  | Eastern Asia |
-- +------+-------+-----------+--------------+
-- 1 row in set (0.0018 sec)


  select name
    from city
order by population desc
   limit 10;

-- +------------------+
-- | name             |
-- +------------------+
-- | Mumbai (Bombay)  |
-- | Seoul            |
-- | São Paulo        |
-- | Shanghai         |
-- | Jakarta          |
-- | Karachi          |
-- | Istanbul         |
-- | Ciudad de México |
-- | Moscow           |
-- | New York         |
-- +------------------+
-- 10 rows in set (0.0053 sec)

