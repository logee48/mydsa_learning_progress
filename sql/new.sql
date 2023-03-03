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


--min max count avg sum
select max(col1) from table_name; --largest data in col1
select min(col1) from table_name; --smallest data in col1
select count(col1) from table_name; --no of data in col1
select avg(col1) from table_name; --finds avg of col1
select sum(col1) from table_name; --finds sum of col1
-- use can also use with 'where' conditions


-- LIKE operations
select * from table_name where name like "s%";

WHERE CustomerName LIKE 'a%' 	--Finds any values that start with "a"
WHERE CustomerName LIKE '%a' 	--Finds any values that end with "a"
WHERE CustomerName LIKE '%or%' 	--Finds any values that have "or" in any position
WHERE CustomerName LIKE '_r%' 	--Finds any values that have "r" in the second position
WHERE CustomerName LIKE 'a_%' 	--Finds any values that start with "a" and are at least 2 characters in length
WHERE CustomerName LIKE 'a__%' 	--Finds any values that start with "a" and are at least 3 characters in length
WHERE CustomerName LIKE 'a%o' 	--Finds any values that start with "a" and ends with "o"


--sql IN operation

select * from table_name where city in('chennai','london'); -- display records where city is chennai and london
select * from table_name where city not in('chennai', 'london'); -- opposite
select * from table_name where city in(select city from table_name1); -- using other table to get city vals


--sql BETWEEN operation
select * from table_name where id BETWEEN 1001 and 1005; --display details of user from 1001 to 1005
select * from table_name where id not BETWEEN 1001 and 1005; -- opposite
select * from table_name where name BETWEEN 'abby' and 'sam'; --display details of user from 'a' to 's'
select * from table_name where dataa BETWEEN '01/04/2004' and '24/12/2006';


--sql aliases
--mostly used to rename col names
select max(col1) as max_val from table_name;
select sum(col1) as total from table_name;

