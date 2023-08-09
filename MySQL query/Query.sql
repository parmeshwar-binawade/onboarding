CREATE TABLE EmployeeInfo(EmployeeId INT,Department VARCHAR(25),Age INT);

INSERT INTO EmployeeInfo(EmployeeID,Department,Age) VALUES (1002, 'HR' , 46),(1003, 'Finance' , 28),(1004, 'IT' , 39);

INSERT INTO EmployeeInfo values(1005,'MIS',28)

SELECT * FROM EmployeeInfo;

UPDATE employeeinfo SET age=30 WHERE age=28;

SELECT * FROM Employeeinfo;

UPDATE employeeinfo SET age=31;

SELECT * FROM employeeinfo;

DELETE FROM employeeinfo;

SELECT * FROM employeeinfo;

INSERT INTO EmployeeInfo(EmployeeID,Department,Age) VALUES (1002, 'HR' , 46),(1003, 'Finance' , 28),(1004, 'IT' , 39);

INSERT INTO EmployeeInfo values(1005,'MIS',28)

SELECT * FROM employeeinfo;

SELECT age FROM employeeinfo GROUP BY age;

SELECT age,COUNT(age) FROM employeeinfo GROUP BY age;

SELECT age,COUNT(age) FROM employeeinfo GROUP BY age HAVING COUNT(age)>1;

SELECT AVG(Age) FROM EmployeeInfo;

CREATE TABLE company(c_id INT AUTO_INCREMENT PRIMARY KEY, c_name VARCHAR(25), c_address VARCHAR(30));

INSERT INTO company values(1,'epam','pune');

SELECT * FROM company;

INSERT INTO company (c_name,c_address) values('microsoft','USA'),('altimetrik','banglore');

SELECT * FROM company;

INSERT INTO company VALUES(10,'valasys','Pune');

SELECT * FROM company;

INSERT INTO company (c_name) VALUES ('IBM');

SELECT * FROM company;

INSERT INTO company VALUES(8,'EXL','Pune');

SELECT * FROM company;

INSERT INTO company (c_name) VALUES ('hcl')

SELECT * FROM company;

INSERT INTO company VALUES(-3,'hexaware','Pune');

SELECT * FROM company;

INSERT INTO company (c_name) VALUES ('wns');

SELECT * FROM company;

INSERT INTO company VALUES(6,'research reports','Pune');

SELECT * FROM company;

INSERT INTO company (c_name) VALUES ('TCS');

SELECT * FROM company;

DESC company;

ALTER TABLE company MODIFY c_id NOT null;


