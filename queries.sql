-- Create the database
create database college;

-- create the table
create table students (sr_no int, name varchar[50], dept varchar[50]);

-- insrting values
insert into students values ("1" , "Samay" , "Printing");
insert into students values ("2" , "Balraj" , "Comedy");

-- updating values
update students set dept = "Habitat" where sr_no = "2";

-- search
select * from students where name = "Samay";

-- delete 
delete from students where name = "Balraj";
