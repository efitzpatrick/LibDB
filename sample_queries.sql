//Queries

/* search book by title or author */
select id from book where title = {searched title} or author = {searched author};

/* add book to cart */
insert into book(status, owner, cart_id) VALUES
  ('')
