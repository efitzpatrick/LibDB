use library;

create table user(
  id varchar(20) not null,
  email varchar(255) not null,
  address varchar(255) not null,
  name varchar(255) not null,
  username varchar(20) not null,
  password varchar(20) not null,
  privileges varchar(20) not null,
  balance numeric(4,2) not null DEFAULT 0);


INSERT INTO user(id, email, address, name, username, password, privileges, balance) VALUES
    ('10000', 'libadmin@case.edu', '1343 Euclid Ave Cleveland, OH', 'admin1', 'libadmin', 'libraryrox', 'admin', 0),
    ('10001', 'libadmin2@case.edu', '1343 Euclid Ave Cleveland, OH', 'admin2', 'libadmin2', 'libraryrox', 'admin', 0),
    ('12345', 'jxk807@case.edu', '1728 E 116th st, Cleveland, OH', 'Jae Yong Kim', 'jxk807', 'mypwd123', 'student', 10.50),
    ('12346', 'eef33@case.edu', '1234 Juniper rd, Cleveland, OH', 'Ellie Fitzpatrick', 'eef33', 'password123', 'student', 0),
    ('12347', 'hxk443@case.edu', '1234 Murray Hill rd, Cleveland, OH', 'Haroon Khazi', 'hxk443', 'password125', 'student', 30),
    ('12348', 'jmn101@case.edu', '11474 Euclid Ave Cleveland, OH', 'Jimmy Nagy', 'jmn101', 'password124', 'student', 20.12);



create table cart(
   id int not null,
   book_id varchar(20) not null,
   book_title varchar(255) not null);


create table book(
   id varchar(20) not null,
   title varchar(255) not null);


create table author(
   id varchar(20),
   name varchar(255) not null);


create table info(
   id varchar(10),
   publisher varchar(30) not null);
