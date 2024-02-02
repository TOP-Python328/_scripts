select
  count(*) as 'vacations'
from vacations
group by doctors_id
order by `vacations` desc;

-- +-----------+
-- | vacations |
-- +-----------+
-- |        26 |
-- |        25 |
-- |        23 |
-- .............
-- |         8 |
-- |         8 |
-- |         8 |
-- +-----------+
-- 70 rows in set (0.0024 sec)


select
  doctors_id, 
  count(*) as 'vacations'
from vacations
group by doctors_id
having `vacations` < 10
order by `vacations` desc;

-- +------------+-----------+
-- | doctors_id | vacations |
-- +------------+-----------+
-- |          4 |         9 |
-- |         27 |         9 |
-- |         28 |         9 |
-- |         32 |         9 |
-- |         37 |         9 |
-- |         50 |         8 |
-- |         57 |         8 |
-- |         70 |         8 |
-- +------------+-----------+
-- 8 rows in set (0.0010 sec)

