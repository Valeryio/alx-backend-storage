-- create table user

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) UNIQUE,
	name VARCHAR(255) UNIQUE,
	country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL,
	);
