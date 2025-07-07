CREATE TABLE IF NOT EXISTS suppliers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    contact_info VARCHAR(255)
);

INSERT INTO suppliers (name, contact_info)
VALUES
  ('ABC Manufacturing', 'abc@abcman.com'),
  ('XYZ Supplies', 'xyz@supplies.com');
  SELECT * FROM suppliers