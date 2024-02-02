select
  continent,
  count(*) as 'countries'
from country
group by continent;

-- +---------------+-----------+
-- | continent     | countries |
-- +---------------+-----------+
-- | North America |        37 |
-- | Asia          |        51 |
-- | Africa        |        58 |
-- | Europe        |        46 |
-- | South America |        14 |
-- | Oceania       |        28 |
-- | Antarctica    |         5 |
-- +---------------+-----------+
-- 7 rows in set (0.0011 sec)


select
  continent,
  region,
  count(*) as 'countries'
from country
group by continent;

-- ERROR: 1055 (42000): Expression #2 of SELECT list is not in GROUP BY clause and contains nonaggregated column 'world.country.Region' which is not functionally dependent on columns in GROUP BY clause; this is incompatible with sql_mode=only_full_group_by


select
  continent,
  group_concat(distinct region separator ', ') as 'regions',
  count(*) as 'countries'
from country
group by continent;

-- +---------------+------------------------------------------------------------------------------------------------------+-----------+
-- | continent     | regions                                                                                              | countries |
-- +---------------+------------------------------------------------------------------------------------------------------+-----------+
-- | Asia          | Eastern Asia, Middle East, Southeast Asia, Southern and Central Asia                                 |        51 |
-- | Europe        | Baltic Countries, British Islands, Eastern Europe, Nordic Countries, Southern Europe, Western Europe |        46 |
-- | North America | Caribbean, Central America, North America                                                            |        37 |
-- | Africa        | Central Africa, Eastern Africa, Northern Africa, Southern Africa, Western Africa                     |        58 |
-- | Oceania       | Australia and New Zealand, Melanesia, Micronesia, Micronesia/Caribbean, Polynesia                    |        28 |
-- | Antarctica    | Antarctica                                                                                           |         5 |
-- | South America | South America                                                                                        |        14 |
-- +---------------+------------------------------------------------------------------------------------------------------+-----------+
-- 7 rows in set (0.0009 sec)


select
  continent,
  region,
  name 
from country 
order by continent, region;

-- +---------------+---------------+-------------+
-- | continent     | region        | name        |
-- +---------------+---------------+-------------+
-- | Asia          | Eastern Asia  | China       |
-- | Asia          | Eastern Asia  | Japan       |
-- | Asia          | Eastern Asia  | North Korea |
-- | Asia          | Eastern Asia  | Taiwan      |
-- | Asia          | Eastern Asia  | Mongolia    |
-- | Asia          | Eastern Asia  | Macao       |
-- | Asia          | Eastern Asia  | South Korea |
-- | Asia          | Eastern Asia  | Hong Kong   |
-- | Asia          | Middle East   | Armenia     |
-- | Asia          | Middle East   | Kuwait      |
-- ...............................................
-- | South America | South America | Paraguay    |
-- +---------------+---------------+-------------+
-- 239 rows in set (0.0011 sec)


select
  continent,
  region,
  count(*) as 'countries'
from country
group by continent, region
order by continent, region;

-- +---------------+---------------------------+-----------+
-- | continent     | region                    | countries |
-- +---------------+---------------------------+-----------+
-- | Asia          | Eastern Asia              |         8 |
-- | Asia          | Middle East               |        18 |
-- | Asia          | Southeast Asia            |        11 |
-- | Asia          | Southern and Central Asia |        14 |
-- | Europe        | Baltic Countries          |         3 |
-- | Europe        | British Islands           |         2 |
-- | Europe        | Eastern Europe            |        10 |
-- | Europe        | Nordic Countries          |         7 |
-- | Europe        | Southern Europe           |        15 |
-- | Europe        | Western Europe            |         9 |
-- | North America | Caribbean                 |        24 |
-- | North America | Central America           |         8 |
-- | North America | North America             |         5 |
-- | Africa        | Central Africa            |         9 |
-- | Africa        | Eastern Africa            |        20 |
-- | Africa        | Northern Africa           |         7 |
-- | Africa        | Southern Africa           |         5 |
-- | Africa        | Western Africa            |        17 |
-- | Oceania       | Australia and New Zealand |         5 |
-- | Oceania       | Melanesia                 |         5 |
-- | Oceania       | Micronesia                |         7 |
-- | Oceania       | Micronesia/Caribbean      |         1 |
-- | Oceania       | Polynesia                 |        10 |
-- | Antarctica    | Antarctica                |         5 |
-- | South America | South America             |        14 |
-- +---------------+---------------------------+-----------+
-- 25 rows in set (0.0011 sec)


select
  continent,
  region,
  count(*) as 'countries'
from country
group by continent, region with rollup
order by continent, region;

-- +---------------+---------------------------+-----------+
-- | continent     | region                    | countries |
-- +---------------+---------------------------+-----------+
-- | NULL          | NULL                      |       239 |
-- | Africa        | NULL                      |        58 |
-- | Africa        | Central Africa            |         9 |
-- | Africa        | Eastern Africa            |        20 |
-- | Africa        | Northern Africa           |         7 |
-- | Africa        | Southern Africa           |         5 |
-- | Africa        | Western Africa            |        17 |
-- | Antarctica    | NULL                      |         5 |
-- | Antarctica    | Antarctica                |         5 |
-- | Asia          | NULL                      |        51 |
-- | Asia          | Eastern Asia              |         8 |
-- | Asia          | Middle East               |        18 |
-- | Asia          | Southeast Asia            |        11 |
-- | Asia          | Southern and Central Asia |        14 |
-- | Europe        | NULL                      |        46 |
-- | Europe        | Baltic Countries          |         3 |
-- | Europe        | British Islands           |         2 |
-- | Europe        | Eastern Europe            |        10 |
-- | Europe        | Nordic Countries          |         7 |
-- | Europe        | Southern Europe           |        15 |
-- | Europe        | Western Europe            |         9 |
-- | North America | NULL                      |        37 |
-- | North America | Caribbean                 |        24 |
-- | North America | Central America           |         8 |
-- | North America | North America             |         5 |
-- | Oceania       | NULL                      |        28 |
-- | Oceania       | Australia and New Zealand |         5 |
-- | Oceania       | Melanesia                 |         5 |
-- | Oceania       | Micronesia                |         7 |
-- | Oceania       | Micronesia/Caribbean      |         1 |
-- | Oceania       | Polynesia                 |        10 |
-- | South America | NULL                      |        14 |
-- | South America | South America             |        14 |
-- +---------------+---------------------------+-----------+
-- 33 rows in set (0.0012 sec)
