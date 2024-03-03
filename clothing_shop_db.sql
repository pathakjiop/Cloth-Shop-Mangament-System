

CREATE DATABASE clothing_shop_db;

-- Use the database
USE clothing_shop_db;

CREATE TABLE IF NOT EXISTS cloths (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    size VARCHAR(50),
    price DECIMAL(10, 2) NOT NULL,
    quantity INT NOT NULL DEFAULT 0

);