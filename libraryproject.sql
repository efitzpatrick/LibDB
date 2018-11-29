



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
   user_id varchar(20) not null,
   book_sku varchar(255) not null);


create table book(
   id varchar(20) not null,
   title varchar(255) not null,
   author varchar(255) not null,
   quantity int not null,
   status varchar(255) default 'In stock',
   owner varchar(255) default null,
   cart_id varchar(255) default null);

insert into book(id, title, author, quantity) values
  ('10000', 'Harry Potter', 'J.K Rowling', 4);
  ('10001', 'DRM348532', 'The Charlottes Web', 'E.B White', 2);
  ('10002', 'FTS593234', 'Eragon', 'Christopher Paolini', 1);
  ('10003', 'CS343245', 'Database Systems', 'Eamon Johnson', 1);



//Queries

/* search book by title or author */
select id from book where title = {searched title} or author = {searched author};

/* add book to cart */
insert into book(status, owner, cart_id) VALUES
  ('')
