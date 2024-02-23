begin;
--
-- create model author
--
create table "authors" (
  "id" integer not null primary key autoincrement, 
  "last_name" varchar(30) not null, 
  "first_name" varchar(30) not null
);
--
-- create model book
--
create table "books" (
  "id" integer not null primary key autoincrement, 
  "title" varchar(100) not null, 
  "author_id" integer not null 
    references "authors" ("id") deferrable initially deferred
);
--
-- create model publisher
--
create table "publishers" (
  "id" integer not null primary key autoincrement, 
  "name" varchar(150) not null unique
);

create table "publishers_authors" (
  "id" integer not null primary key autoincrement, 
  "publisher_id" smallint not null 
    references "publishers" ("id") deferrable initially deferred, 
  "author_id" integer not null 
    references "authors" ("id") deferrable initially deferred
);

create table "publishers_books" (
  "id" integer not null primary key autoincrement, 
  "publisher_id" smallint not null 
    references "publishers" ("id") deferrable initially deferred, 
  "book_id" integer not null 
    references "books" ("id") deferrable initially deferred
);

create index "books_author_id_c90d3b48" on "books" ("author_id");

create unique index "publishers_authors_publisher_id_author_id_6c42d3ca_uniq" on "publishers_authors" ("publisher_id", "author_id");

create index "publishers_authors_publisher_id_13c72537" on "publishers_authors" ("publisher_id");

create index "publishers_authors_author_id_5c59c3c2" on "publishers_authors" ("author_id");

create unique index "publishers_books_publisher_id_book_id_d2f7d931_uniq" on "publishers_books" ("publisher_id", "book_id");

create index "publishers_books_publisher_id_9319f5d0" on "publishers_books" ("publisher_id");

create index "publishers_books_book_id_c37e42a2" on "publishers_books" ("book_id");

commit;
