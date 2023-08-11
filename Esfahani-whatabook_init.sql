#these are the scripts I used to create database and its tables:*/
CREATE DATABASE whatabook;
CREATE TABLE store (
    store_id    INT             NOT NULL    AUTO_INCREMENT,
    locale      VARCHAR(500)    NOT NULL,
    PRIMARY KEY(store_id)
);

CREATE TABLE book (
    book_id     INT             NOT NULL    AUTO_INCREMENT,
    book_name   VARCHAR(200)    NOT NULL,
    author      VARCHAR(200)    NOT NULL,
    details     VARCHAR(500),
    PRIMARY KEY(book_id)
);

CREATE TABLE user (
    user_id         INT         NOT NULL    AUTO_INCREMENT,
    first_name      VARCHAR(75) NOT NULL,
    last_name       VARCHAR(75) NOT NULL,
    PRIMARY KEY(user_id) 
);

CREATE TABLE wishlist (
    wishlist_id     INT         NOT NULL    AUTO_INCREMENT,
    user_id         INT         NOT NULL,
    book_id         INT         NOT NULL,
    PRIMARY KEY (wishlist_id),
    CONSTRAINT fk_book
    FOREIGN KEY (book_id)
        REFERENCES book(book_id),
    CONSTRAINT fk_user
    FOREIGN KEY (user_id)
        REFERENCES user(user_Id)
);
#all the info is just like how the sample was providing.occasionally I was checking the work by SHOW TABLES from whatabook;,
#or SELECT * FROM (table name);


#the following will be ued in a python file to create a program for what a book


#view a users wishlist items

SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author
FROM wishlist
    INNER JOIN user ON wishlist.user_id = user.user_id
    INNER JOIN book ON wishlist.book_id = book.book_id
WHERE user.user_id = 2;

    view the store's location 
SELECT store_id, locale from store;

    view a listing of the books WhatABook offers
SELECT book_id, book_name, author, details from book;

    view a listing of books not already in your a users wishlsit.
SELECT book_id, book_name, author, details
FROM book
WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = 2);

    to add a new book to a users wishlist. 
INSERT INTO wishlist(user_id, book_id)
    VALUES(3, 4)

    Remove a book from the user's wishlist.
DELETE FROM wishlist WHERE user_id = 3 AND book_id = 4;