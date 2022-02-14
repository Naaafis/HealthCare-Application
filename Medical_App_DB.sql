CREATE DATABASE IF NOT EXISTS MedicalUsers;
USE MedicalUsers;

CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `full_name` varchar(255),
  `date_of_Birth` datetime,
  `address` varchar(255),
  `primary_care_provider` varchar(255),
  `insurance` Table,
  `created_at` timestamp
);

CREATE TABLE `billing_info` (
  `id` int UNIQUE PRIMARY KEY NOT NULL,
  `name` varchar(255),
  `card_type` varchar(255),
  `card_number` int,
  `expiration_date` varchar(255),
  `security_code` int
);

CREATE TABLE `medical_history` (
  `id` int PRIMARY KEY,
  `height` varchar(255),
  `weight` varchar(255),
  `gender` char,
  `medications` Table COMMENT 'Table holds list of medications taken'
);

CREATE TABLE `collected_data` (
  `id` int PRIMARY KEY,
  `temperature` int,
  `blood_pressure` int,
  `pulse` int,
  `oximeter` int,
  `glucometer` int
);

CREATE TABLE `device_info` (
  `device_id` int,
  `device_name` varchar(255),
  `device_mac_addr` varchar(255),
  `device_user_id` int,
  `device_assigner_id` int,
  `firmware_version` varchar(255) DEFAULT 1,
  `sofware_version` varchar(255),
  `date_of_purchase` datetime,
  PRIMARY KEY (`device_user_id`, `device_assigner_id`)
);

CREATE TABLE `device_data` (
  `device_id` int,
  `data` varchar(255),
  `collected_at` datetime DEFAULT (now())
);

CREATE TABLE `assign_roles` (
  `id` int PRIMARY KEY,
  `name` varchar(255),
  `role` Roles,
  `permissions` Table,
  `created_at` datetime DEFAULT (now())
);

ALTER TABLE `collected_data` ADD FOREIGN KEY (`id`) REFERENCES `users` (`id`);

ALTER TABLE `device_info` ADD FOREIGN KEY (`device_user_id`) REFERENCES `users` (`id`);

ALTER TABLE `device_info` ADD FOREIGN KEY (`device_assigner_id`) REFERENCES `users` (`id`);

ALTER TABLE `device_data` ADD FOREIGN KEY (`device_id`) REFERENCES `device_info` (`device_id`);

ALTER TABLE `users` ADD FOREIGN KEY (`id`) REFERENCES `billing_info` (`id`);

ALTER TABLE `users` ADD FOREIGN KEY (`id`) REFERENCES `medical_history` (`id`);

ALTER TABLE `assign_roles` ADD FOREIGN KEY (`id`) REFERENCES `users` (`id`);

CREATE INDEX `Roles` ON `assign_roles` (`id`, `role`);

CREATE UNIQUE INDEX `assign_roles_index_1` ON `assign_roles` (`id`);
