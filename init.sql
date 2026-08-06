CREATE TABLE students (

id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100),

roll_number VARCHAR(30),

class VARCHAR(30),

school VARCHAR(100)

);

INSERT INTO students
(name, roll_number, class, school)

VALUES

('Rahul','101','10th','ABC School'),
('Priya','102','9th','XYZ School');