use leodb;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  role VARCHAR(50),
  name VARCHAR(50),
  last_name VARCHAR(50),
  name_last_name VARCHAR(100) GENERATED ALWAYS AS (CONCAT(name, ' ', last_name)) STORED,
  gender VARCHAR(10),
  birthdate DATE,
  email VARCHAR(100),
  password VARCHAR(255),
  workplace VARCHAR(100),
  phone_number VARCHAR(15),
  marital_status VARCHAR(20),
  has_children BOOLEAN,
  has_elders BOOLEAN
);

CREATE TABLE logs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  event VARCHAR(100),
  description TEXT,
  fk_id_user INT,
  FOREIGN KEY (fk_id_user) REFERENCES users(id)
);

CREATE TABLE categories (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(50),
  color VARCHAR(7)
);

CREATE TABLE services (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  data_start DATE,
  data_end DATE,
  description TEXT,
  img_url VARCHAR(255),
  pdf_url VARCHAR(255),
  fk_id_category INT,
  FOREIGN KEY (fk_id_category) REFERENCES categories(id)
);

CREATE TABLE interests (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100)
);

CREATE TABLE subservices (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  data_start DATE,
  data_end DATE,
  description TEXT,
  img_url VARCHAR(255),
  pdf_url VARCHAR(255),
  fk_id_service INT,
  FOREIGN KEY (fk_id_service) REFERENCES services(id)
);

CREATE TABLE user_interests (
  id INT AUTO_INCREMENT PRIMARY KEY,
  fk_id_user INT,
  fk_id_interest INT,
  FOREIGN KEY (fk_id_user) REFERENCES users(id),
  FOREIGN KEY (fk_id_interest) REFERENCES interests(id)
);

CREATE TABLE interest_services (
  id INT AUTO_INCREMENT PRIMARY KEY,
  fk_id_interest INT,
  fk_id_service INT,
  FOREIGN KEY (fk_id_interest) REFERENCES interests(id),
  FOREIGN KEY (fk_id_service) REFERENCES services(id)
);

CREATE TABLE user_services (
  id INT AUTO_INCREMENT PRIMARY KEY,
  priority INT,
  fk_id_user INT,
  fk_id_service INT,
  FOREIGN KEY (fk_id_user) REFERENCES users(id),
  FOREIGN KEY (fk_id_service) REFERENCES services(id)
);


INSERT INTO users (role, name, last_name, gender, birthdate, email, password, workplace, phone_number, marital_status, has_children, has_elders)
VALUES
  ('admin', 'John', 'Doe', 'Male', '1980-01-15', 'john.doe@example.com', '$2b$12$LVs3T46VJjuGylZTbI.hXeUu7aOVhssGddB3a5dFpLQIcWTnwUreW', '123 Elm Street', '555-1234', 'Single', FALSE, FALSE),
  ('user', 'Jane', 'Smith', 'Female', '1990-06-25', 'jane.smith@example.com', '$2b$12$/NuqWslTCPdrUbQx/CNmRuJrSJ9vQh.cXSF3TXK2IvkYDjpszaieq', '456 Oak Avenue', '555-5678', 'Married', TRUE, FALSE);

INSERT INTO categories (name, color)
VALUES
  ('Health', '#FF0000'),
  ('Finance', '#00FF00'),
  ('Legal', '#0000FF');

INSERT INTO services (name, fk_id_category, data_start, data_end, description, img_url, pdf_url)
VALUES
  ('Medical Checkup', 1, '2021-01-01', '2021-12-31', 'Annual medical checkup', 'https://via.placeholder.com/150', 'https://via.placeholder.com/150'),
  ('Retirement Planning', 2, '2021-01-01', '2021-12-31', 'Plan for retirement', 'https://via.placeholder.com/150', 'https://via.placeholder.com/150'),
  ('Will Preparation', 3, '2021-01-01', '2021-12-31', 'Prepare a will', 'https://via.placeholder.com/150', 'https://via.placeholder.com/150');

INSERT INTO interests (name)
VALUES
  ('Health'),
  ('Finance'),
  ('Legal');
