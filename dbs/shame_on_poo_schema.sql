-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema shame_on_poo_schema
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema shame_on_poo_schema
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `shame_on_poo_schema` DEFAULT CHARACTER SET utf8 ;
USE `shame_on_poo_schema` ;

-- -----------------------------------------------------
-- Table `shame_on_poo_schema`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shame_on_poo_schema`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `password` VARCHAR(255) NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`));


-- -----------------------------------------------------
-- Table `shame_on_poo_schema`.`reports`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `shame_on_poo_schema`.`reports` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `location` VARCHAR(255) NULL,
  `date` DATE NULL,
  `description` VARCHAR(255) NULL,
  `offense` VARCHAR(45) NULL,
  `is_cleaned` TINYINT NULL DEFAULT 0,
  `img_file` VARCHAR(255) NULL,
  `user_id` INT NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  INDEX `fk_reports_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_reports_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `shame_on_poo_schema`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE NO ACTION);


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
