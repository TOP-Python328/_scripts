update vacations
set end_date = adddate(start_date, floor(5 + rand()*39))
where datediff(end_date, start_date) > 40;
