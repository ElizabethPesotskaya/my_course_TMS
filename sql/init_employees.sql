CREATE TABLE employees ( 
id SERIAL PRIMARY KEY,
Name VARCHAR (100),
Department VARCHAR (50), 
Salary NUMERIC (10, 2)
);

INSERT INTO employees (Name, Department, Salary)
VALUES
  ('Tatur Alena', 'Engineer', 2000.00),
  ('Alexey Semashko', 'Financier', 2300.00),
  ('Daria Golub', 'Marketolog', 2100.00),
  ('Alena Shvets', 'Sales manager', 2100.00),
  ('Maxim Gorbatsky', 'Sales manager', 2600.00);

UPDATE employees
SET Department = 'Leading sales manager'
WHERE id = 5;

ALTER TABLE employees
ADD COLUMN "HireDate" DATE;

UPDATE employees 
SET "HireDate" = '2003-12-02' WHERE id = 1;
UPDATE employees 
SET "HireDate" = '2001-04-12' WHERE id = 2;
UPDATE employees 
SET "HireDate" = '1999-09-18' WHERE id = 3;
UPDATE employees 
SET "HireDate" = '1990-03-15' WHERE id = 4;
UPDATE employees 
SET "HireDate" = '2023-04-02' WHERE id = 5;

SELECT * FROM employees 
WHERE Department = 'Sales manager';

SELECT  Name, Department FROM employees 
WHERE Salary = 5000;

SELECT  avg(Salary) FROM employees;

DROP TABLE employees;



