
//Queries

/* search book by title or author */
select id from book where title = {searched title} or author = {searched author};

/* add book to cart */
update book set cart_id = {current user ID} where sku = {sku of book trying to rent};
update status set availability = 'unavailable' where id = {id of status} and book_sku = {sku of book trying to add};

/* remove book from cart*/
update book set cart_id = null where sku = {sku of book trying to return};
update status set availability = 'available' where id = {id of status} and book_sku = {sku of book trying to remove};

/* check out books from cart */
update book set owner = {current user ID}, cart_id = null where sku = {sku of book trying to check-out};
update status set start_date = {current_date}, return_date = {current_date + 21days}, num_times_rented = num_times_rented+1
  where id = {id of status}, book_sku = {sku of book trying to check-out};

/* return book after use */
update book set owner = null, cart_id = null where sku = {sku of book trying to return}
update statu set availability = 'available', start_date = null, return_date = null where id = {id of status}, book_sku = {sku of book returned};

/* add books to db*/
insert into book(id, sku, title, author) values
  ('new book id', 'new book sku', 'new book title', 'new book author');

/* delete books from db */
delete from book where id = {id of book trying to remove}

/* check privilege of user(more for check if user is admin) */
select id from user where privilege = 'admin'

/* find all books that a user has checked out */
select id from book b inner join status s on b.sku = s.book_sku where b.owner = {current user_id} and availability = 'unavailable';

/* all books in the user's cart */
select id, return_date from book b inner join status s on b.sku = s.sku inner join cart c on b.cart_id = c.id where c.user_id = {current user_id} ;
select sku from book b inner join cart c on b.cart_id = c.id and c.user_id = {user ID};


/* Analytics Queries

/* Check for number of books checked out until now */
select sum(num_times_rented) from status;

/* Check for number of users */
select count(id) from user;

/* Check for average balance */
select avg(balance) from user;