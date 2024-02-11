drop database if exists game_creatures;

create database game_creatures;

use game_creatures;


create table categories (
    id tinyint unsigned primary key auto_increment,
    category varchar(30) not null unique
);

create table species (
    id tinyint unsigned primary key auto_increment,
    species varchar(30) not null unique
);

create table roles (
    id tinyint unsigned primary key auto_increment,
    role varchar(30) not null unique
);

create table locations (
    id smallint unsigned primary key auto_increment,
    location varchar(50) not null unique
);

create table creatures (
    id smallint unsigned primary key auto_increment,
    name varchar(20) not null,
    level tinyint unsigned not null,
    categories_id tinyint unsigned not null,
    species_id tinyint unsigned not null,
    roles_id tinyint unsigned not null,
    locations_id smallint unsigned not null,
    foreign key (categories_id) references categories (id),
    foreign key (species_id) references species (id),
    foreign key (roles_id) references roles (id),
    foreign key (locations_id) references locations (id)
);

create table skills (
    id smallint unsigned primary key auto_increment,
    skill varchar(25) not null unique
);

create table creatures_skills (
    creatures_id smallint unsigned not null,
    skills_id smallint unsigned not null,
    skill_level tinyint unsigned not null,
    primary key (creatures_id, skills_id),
    foreign key (creatures_id) references creatures (id),
    foreign key (skills_id) references skills (id)
);

