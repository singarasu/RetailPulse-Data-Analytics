CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    salary INT
);

INSERT INTO employees (employee_id, name, department, salary)
VALUES
    (101, 'Arun', 'IT', 25000),
    (102, 'Priya', 'HR', 30000),
    (103, 'Kumar', 'Sales', 28000),
    (104, 'Divya', 'IT', 35000),
    (105, 'Ravi', 'Finance', 32000);

-- 1. Display all columns
SELECT *
FROM employees;

-- 2. Display only employee names
SELECT name
FROM employees;

-- 3. Display employee names and salaries
SELECT name, salary
FROM employees;

-- 4. Display employee IDs and departments
SELECT employee_id, department
FROM employees;

-- 5. Display names, departments and salaries
SELECT name, department, salary
FROM employees;
