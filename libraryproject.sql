use team20;


DROP TABLE IF EXISTS `user`;
create table user(
  id varchar(20) not null,
  email varchar(255) not null,
  address varchar(255) not null,
  name varchar(255) not null,
  username varchar(20) not null,
  password varchar(20) not null,
  privilege varchar(20) not null,
  balance numeric(4,2) not null DEFAULT 0);


INSERT INTO user(id, email, address, name, username, password, privilege, balance) VALUES
    ('10000', 'libadmin@case.edu', '1343 Euclid Ave Cleveland, OH', 'admin1', 'libadmin', 'libraryrox', 'admin', 0),
    ('10001', 'libadmin2@case.edu', '1343 Euclid Ave Cleveland, OH', 'admin2', 'libadmin2', 'libraryrox', 'admin', 0),
    ('12345', 'jxk807@case.edu', '1728 E 116th st, Cleveland, OH', 'Jae Yong Kim', 'jxk807', 'mypwd123', 'student', 10.50),
    ('12346', 'eef33@case.edu', '1234 Juniper rd, Cleveland, OH', 'Ellie Fitzpatrick', 'eef33', 'password123', 'student', 0),
    ('12347', 'hxk443@case.edu', '1234 Murray Hill rd, Cleveland, OH', 'Haroon Khazi', 'hxk443', 'password125', 'student', 30),
    ('12348', 'jmn101@case.edu', '11474 Euclid Ave Cleveland, OH', 'Jimmy Nagy', 'jmn101', 'password124', 'student', 20.12);


DROP TABLE IF EXISTS `cart`;
create table cart(
   id varchar(20) not null,
   user_id varchar(20) not null,
   book_sku varchar(255) not null);

DROP TABLE IF EXISTS `book`;
create table book(
   id varchar(20) not null,
   sku varchar(255) not null,
   title varchar(255) not null,
   author varchar(255) not null,
   owner varchar(255) default null,
   cart_id varchar(255) default null);

insert into book(id, sku, title, author) values
  ('10000', 'FTS123440', 'Harry Potter', 'J.K Rowling'),
  ('10000', 'FTS123441', 'Harry Potter', 'J.K Rowling'),
  ('10001', 'DRM348532', 'The Charlottes Web', 'E.B White'),
  ('10002', 'FTS593234', 'Eragon', 'Christopher Paolini'),
  ('10003', 'CS343245', 'Database Systems', 'Eamon Johnson'),
  ('10004', 'FIC234123', 'Tuesdays with Morrie', 'Mitch Albom'),
  ('10005', 'FIC948719', 'The Kite Runner', 'Khaled Hosseini'),
  ('10006', 'FTS392741', 'Lord of the Rings', 'J. R. R. Tolkien'),
  ('10007', 'FTS304859', 'Murder on the Orient Express', 'Agatha Christie'),
  ('10008', 'FIC394584', '1984', 'George Orwell');

DROP TABLE IF EXISTS 'status';
create table status(
  id varchar(20) not null,
  book_sku varchar(255) not null,
  availability varchar(255) not null default 'available',
  start_date int,
  return_date int,
  rate numeric(2,2) default 2.50,
  num_times_rented int default 0
);

DROP TABLE IF EXISTS 'has_status';
create table has_status(
  book_sku varchar(255) not null,
  status_id varchar(20) not null
);
