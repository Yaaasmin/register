#set the database and the chart
#直接复制到Mysql中运行……
create database strong default character set utf8mb4 collate utf8mb4_unicode_ci;

create table strong.users(
    `id` int not null auto_increment,
    `name` varchar(100) not null,
    `sex`  enum('男','女'),
    `campus` varchar(100) not null,
    `grade` enum('大一','大二'),
    `academy` varchar(100) not null,
    `dormitory` varchar(100) not null,
    `phone` varchar(100) not null,
    `first_choice` varchar(100) not null,
    `second_choice` varchar(100) not null,
    `faceTime` varchar(100) not null,
    `selfintroduction` varchar(255) not null,
    primary key(`id`), UNIQUE `unique_phone` (`phone`))
    engine=InnoDB default charset=utf8mb4 collate=utf8mb4_unicode_ci;

create user 'root'@'%' identified by '123456';
grant all privileges on `strong`.*to `root`@'%';