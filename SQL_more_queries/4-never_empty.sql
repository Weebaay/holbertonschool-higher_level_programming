-- create table id_not_null on MySQL server
CREATE TABLE IF NOT EXISTS id_not_null (
	id INT DEFAULT 1 NOT NULL,
	name VARCHAR(256)
);