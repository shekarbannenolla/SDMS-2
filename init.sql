CREATE TABLE students (

id INT AUTO_INCREMENT PRIMARY KEY,

name VARCHAR(100),

roll_number VARCHAR(30),

class VARCHAR(30),

school VARCHAR(100),

email VARCHAR(100),

Phone VARCHAR(15)

);

INSERT INTO students
(name, roll_number, class, school, email, Phone)

VALUES

('Rahul','101','10th','ABC School','rahul@example.com','1234567890'),
('Priya','102','9th','XYZ School','priya@example.com','0987654321');