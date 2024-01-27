drop database if exists library;
create database library;
use library;

create table authors (
  id smallint unsigned primary key auto_increment,
  last_name varchar(50) not null, 
  first_name varchar(50) not null,
  patr_name varchar(50)
);

create table books (
  id smallint unsigned primary key auto_increment,
  title varchar(200) not null,
  author_id smallint unsigned not null 
    references authors (id)
    on delete restrict
);

create table publishers (
  id tinyint unsigned primary key auto_increment,
  name varchar(150) not null
);

create table publishers_authors (
  publisher_id tinyint unsigned not null
    references publishers (id),
  author_id smallint unsigned not null
    references authors (id),
  primary key (publisher_id, author_id)
);

create table publishers_books (
  publisher_id tinyint unsigned not null
    references publishers (id),
  book_id smallint unsigned not null
    references books (id)
);
