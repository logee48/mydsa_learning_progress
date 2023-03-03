-- sql order by

select * from table_name order by city;
select * from table_name order by city desc;
select * from table_name order by city asc;
select * from table_name order by city desc, name asc;


--insert 
insert into table_name values(1001, 'sdfs', 'dsfgs');
insert into table_name(col1, col2) values(1002, 'sdgs');


--update
update table_name set name='sam' where id=1001;
update table_name set name='sam', city='chennai' where id=1002;
update table_name set name='sam'; --if you omit the where part all data will be changed


--delete
delete from table_name where id=1001;
delete from table_name; --it will delete all data without deleting the table itself


--select limited no of data
--for oracle
select * from table_name fetch first 5 rows only; --first 5 rows
select * from table_name fetch first 50 percent rows only;

--for mysql
select * from table_name where limit 5; -- first 5 rows


