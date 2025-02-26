SELECT * FROM twitter.users;
Insert into twitter.users (first_name, last_name)
values ('chaima', 'louhichi');

delete from twitter.users
where id = 7;

UPDATE twitter.users 
set first_name = 'Alla', laste_name = 'Bettayeb'
where id = 1;

