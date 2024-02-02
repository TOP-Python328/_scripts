  select name, surfacearea, population
    from country
order by surfacearea;

-- +-------------------------------+-------------+------------+
-- | name                          | surfacearea | population |
-- +-------------------------------+-------------+------------+
-- | Holy See (Vatican City State) |        0.40 |       1000 |
-- | Monaco                        |        1.50 |      34000 |
-- ............................................................
-- | Antarctica                    | 13120000.00 |          0 |
-- | Russian Federation            | 17075400.00 |  146934000 |
-- +-------------------------------+-------------+------------+
-- 239 rows in set (0.0015 sec)


  select name, surfacearea, population
    from country
order by surfacearea desc;

-- +-------------------------------+-------------+------------+
-- | name                          | surfacearea | population |
-- +-------------------------------+-------------+------------+
-- | Russian Federation            | 17075400.00 |  146934000 |
-- | Antarctica                    | 13120000.00 |          0 |
-- ............................................................
-- | Monaco                        |        1.50 |      34000 |
-- | Holy See (Vatican City State) |        0.40 |       1000 |
-- +-------------------------------+-------------+------------+
-- 239 rows in set (0.0015 sec)


  select name, 
         population
    from country
order by surfacearea desc;

-- +-------------------------------+------------+
-- | name                          | population |
-- +-------------------------------+------------+
-- | Russian Federation            |  146934000 |
-- | Antarctica                    |          0 |
-- ..............................................
-- | Monaco                        |      34000 |
-- | Holy See (Vatican City State) |       1000 |
-- +-------------------------------+------------+
-- 239 rows in set (0.0008 sec)


  select name,
         population / surfacearea as 'density'
    from country
order by `density`;

-- +-----------------------------+------------+
-- | name                        | density    |
-- +-----------------------------+------------+
-- | Antarctica                  |     0.0000 |
-- | French Southern territories |     0.0000 |
-- ............................................
-- | Monaco                      | 22666.6667 |
-- | Macao                       | 26277.7778 |
-- +-----------------------------+------------+
-- 239 rows in set (0.0015 sec)


select name from country order by population / surfacearea;

-- +-----------------------------+
-- | name                        |
-- +-----------------------------+
-- | Antarctica                  |
-- | French Southern territories |
-- ...............................
-- | Monaco                      |
-- | Macao                       |
-- +-----------------------------+
-- 239 rows in set (0.0017 sec)


select 
  countrycode,
  name,
  population
from city
order by 
  countrycode asc, 
  population desc;

-- +-------------+----------------+------------+
-- | countrycode | name           | population |
-- +-------------+----------------+------------+
-- | ABW         | Oranjestad     |      29034 |
-- | AFG         | Kabul          |    1780000 |
-- | AFG         | Qandahar       |     237500 |
-- | AFG         | Herat          |     186800 |
-- | AFG         | Mazar-e-Sharif |     127800 |
-- | AGO         | Luanda         |    2022000 |
-- | AGO         | Huambo         |     163100 |
-- | AGO         | Lobito         |     130000 |
-- | AGO         | Benguela       |     128300 |
-- | AGO         | Namibe         |     118200 |
-- .............................................
-- | ZMB         | Kabwe          |     154300 |
-- | ZMB         | Chingola       |     142400 |
-- | ZMB         | Mufulira       |     123900 |
-- | ZMB         | Luanshya       |     118100 |
-- | ZWE         | Harare         |    1410000 |
-- | ZWE         | Bulawayo       |     621742 |
-- | ZWE         | Chitungwiza    |     274912 |
-- | ZWE         | Mount Darwin   |     164362 |
-- | ZWE         | Mutare         |     131367 |
-- | ZWE         | Gweru          |     128037 |
-- +-------------+----------------+------------+
-- 4079 rows in set (0.0088 sec)
