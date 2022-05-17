-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema HotGirlParties
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `HotGirlParties` ;

-- -----------------------------------------------------
-- Schema HotGirlParties
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `HotGirlParties` DEFAULT CHARACTER SET utf8 ;
USE `HotGirlParties` ;

-- -----------------------------------------------------
-- Table `HotGirlParties`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HotGirlParties`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NULL,
  `email` VARCHAR(255) NULL,
  `password` VARCHAR(255) NULL,
  `level` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `HotGirlParties`.`parties`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `HotGirlParties`.`parties` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `starttime` DATETIME NULL,
  `endtime` DATETIME NULL,
  `genre` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  `user_id` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_parties_users_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_parties_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `HotGirlParties`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
