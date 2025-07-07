CREATE TABLE IF NOT EXISTS products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    description VARCHAR(255),
    supplier_id INT
);
INSERT INTO products (name, quantity, description, supplier_id)
VALUES 
  ('Gear', 200, 'Spur Gear', 1),
  ('Shaft', 100, 'Raduis XX', 2);
  