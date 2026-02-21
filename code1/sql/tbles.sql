/* use this command to run .sql files sqlcmd -S servername -d dbname -i filename.sql */
CREATE TABLE student(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    grade VARCHAR(10)
);
delete from student;
insert into student (id, name, age, grade) values (1, 'Alice', 20, 'A');
insert into student (id, name, age, grade) values (2, 'Bob', 22, 'B');
insert into student (id, name, age, grade) values (3, 'Charlie', 21, 'A');
insert into student (id, name, age, grade) values (4, 'David', 23, 'C');
insert into student (id, name, age, grade) values (5, 'Eve', 20, 'B');
select *from student;