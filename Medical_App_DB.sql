CREATE DATABASE IF NOT EXISTS HealthcareApp;
USE HealthcareApp;

CREATE TABLE IF NOT EXISTS users (
  id int,
  full_name varchar(255),
  date_of_Birth varchar(255),
  address varchar(255),
  primary_care_provider varchar(255),
  insurance varchar(255),
  created_at TIMESTAMP,
  CONSTRAINT pk_id PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS billing_info (
  id int,
  name varchar(255),
  card_type varchar(255),
  card_number int,
  expiration_date varchar(255),
  security_code int,
  CONSTRAINT fk_id FOREIGN KEY (id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS medical_history (
  id int,
  height varchar(255),
  weight varchar(255),
  gender char,
  medications varchar(255) COMMENT 'Table holds list of medications taken',
  CONSTRAINT fk_id FOREIGN KEY (id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS collected_data (
  id int,
  temperature int,
  blood_pressure int,
  pulse int,
  oximeter int,
  glucometer int,
  CONSTRAINT fk_id FOREIGN KEY (id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS device_info (
  device_id int,
  device_name varchar(255),
  device_mac_addr varchar(255),
  device_user_id int,
  device_assigner_id int,
  firmware_version varchar(255) DEFAULT 1,
  sofware_version varchar(255),
  date_of_purchase datetime,
  CONSTRAINT pk_device_id PRIMARY KEY (device_id),
  CONSTRAINT fk_id FOREIGN KEY (device_user_id) REFERENCES users(id),
  CONSTRAINT fk_id FOREIGN KEY (device_assigner_id) REFERENCES users(id)
);

CREATE TABLE IF NOT EXISTS device_data (
  device_id int,
  data varchar(255),
  collected_at datetime DEFAULT (now()),
  CONSTRAINT fk_device_id FOREIGN KEY (device_id) REFERENCES device_info(device_id)
);

CREATE TABLE IF NOT EXISTS assign_roles (
  id int PRIMARY KEY,
  name varchar(255),
  role varchar(255),
  permissions varchar(255),
  created_at TIMESTAMP,
  CONSTRAINT fk_id FOREIGN KEY (id) REFERENCES users(id)
);

