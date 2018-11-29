
//Queries

/* search book by title or author */
select id from book where title = {searched title} or author = {searched author};

/* add book to cart */
update book set status = 'unavailable', cart_id = {current user ID} where sku = {sku of book trying to rent}

/* remove book from cart*/
update book set status = 'available', cart_id = null where sku = {sku of book trying to return}

/* check out books from cart */
update book set owner = {current user ID}, cart_id = null where sku = {sku of book trying to check-out}

/* return book after use */
update book set status = 'available', owner = null, cart_id = null where sku = {sku of book trying to return}

/* add books to db*/
insert into book(id, sku, title, author) values
  ('new book id', 'new book sku', 'new book title', 'new book author');

/* delete books from db */
delete from book where id = {id of book trying to remove}

/* check privilege of user(more for check if user is admin) */
select id from user where privilege = 'admin'

/*
