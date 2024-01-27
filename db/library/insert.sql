insert authors
  (first_name, patr_name, last_name)
values
  ('Фёдор', 'Михайлович', 'Достоевский'),
  ('Лоис', null, 'Буджолд'),
  ('Михаил', 'Афанасьевич', 'Булгаков'),
  ('Александр', 'Сергеевич', 'Пушкин'),
  ('Марк', null, 'Твен');

insert books
  (title, author_id)
values
  ('Барраяр', 2),
  ('Ученик воина', 2),
  ('Игры форов', 2),
  ('Цетаганда', 2),
  ('Бесы', 1),
  ('Преступление и наказание', 1),
  ('Братья Карамазовы', 1),
  ('Мастер и Маргарита', 3),
  ('Том Сойер', 5),
  ('Сказка о рыбаке и рыбке', 4),
  ('Пиковая дама', 4),
  ('Сказ о попе и работнике его Балде', 4),
  ('Приключения Гекельбери Финна', 5);

insert publishers
  (name)
values
  ('Азбука'),
  ('Эксмо'),
  ('АСТ');

insert publishers_books
values
  (3,  1),
  (3,  2),
  (3,  3),
  (3,  4),
  (1,  5),
  (1,  6),
  (1,  7),
  (1,  8),
  (1,  9),
  (2,  9),
  (1, 10),
  (1, 11),
  (2, 11),
  (1, 12),
  (2, 13);