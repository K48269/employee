CREATE DATABASE hello;
USE hello;
CREATE TABLE Employee_info (id varchar(150) primary key,name varchar(150),Mobile_number varchar(150) unique key,Email_id varchar(150) unique key);
CREATE TABLE login_passwords(id varchar(150),e_key varchar(150), p_key varchar(150), foreign key (id) references Employee_info(id))