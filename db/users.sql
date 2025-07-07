
CREATE DATABASE inventory_management;
USE inventory_management;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(80) NOT NULL
);
INSERT INTO users (username, password)
VALUES
    ('admin', 'pk@123456'),
    ('user1', 'pk@12345'),
    ('user2', 'pk@1234'),
    ('user3', 'pk@123'),
    ('user4', 'pk@me');
    
