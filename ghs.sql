- --------------------------------------------------------------------------------
-- Table des services
-- --------------------------------------------------------------------------------
CREATE TABLE `services` (
  `serviceID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `serviceCode` VARCHAR(10) NOT NULL UNIQUE,
  `serviceName` VARCHAR(100) NOT NULL,
  `parentServiceID` INT UNSIGNED,
  `description` TEXT,
  `manager` VARCHAR(100),
  `createdAt` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------------------------------
-- Table des employés
-- --------------------------------------------------------------------------------
CREATE TABLE `employees` (
  `employeeID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `employeeNumber` VARCHAR(20) NOT NULL UNIQUE,
  `lastName` VARCHAR(20) NOT NULL,
  `firstName` VARCHAR(30) NOT NULL,
  `serviceID` INT UNSIGNED NOT NULL,
  `contractType` ENUM('CDI', 'CDD', 'Interim', 'Stage', 'Alternance', 'MOO') DEFAULT 'CDI',
  `contact` VARCHAR(20),
  `birthdate` DATE,
  `createdAt` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (`serviceID`) REFERENCES `services`(`serviceID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------------------------------
-- Table des comptes
-- --------------------------------------------------------------------------------
CREATE TABLE `accounts` (
  `accountID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `employeeID` INT UNSIGNED NOT NULL UNIQUE,
  `username` VARCHAR(50) NOT NULL UNIQUE,
  `password` VARCHAR(255) NOT NULL,
  `profile` ENUM('Validator', 'Supervisor', 'Administrator', 'Coordinator') DEFAULT 'Validator',
  `isActive` TINYINT(1) DEFAULT 1,
  `lastLogin` TIMESTAMP NULL,
  `resetToken` VARCHAR(100),
  `resetTokenExpiry` TIMESTAMP NULL,
  `createdAt` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (`employeeID`) REFERENCES `employees`(`employeeID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------------------------------
-- Table des demandes d'heures supplémentaires
-- --------------------------------------------------------------------------------
CREATE TABLE `requests` (
  `requestID` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `employeeID` INT UNSIGNED NOT NULL,
  `requestDate` DATE NOT NULL,
  `previousStart` TIME NULL,
  `previousEnd` TIME NULL,
  `startAt` TIME NOT NULL,
  `endAt` TIME NOT NULL,
  `status` ENUM('pending', 'submitted', 'firstLevelApproved', 'inProgress', 'secondLevelApproved', 'accepted', 'rejected') DEFAULT 'pending',
  `comment` TEXT,
  `createdBy` INT UNSIGNED,
  `validatedN1At` TIMESTAMP NULL,
  `validatedN2At` TIMESTAMP NULL,
  `createdAt` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updatedAt` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  CONSTRAINT `check_hours` CHECK (`endAt` > `startAt`),
  CONSTRAINT `check_previous_hours` CHECK (`previousEnd` > `previousStart`),
  FOREIGN KEY (`employeeID`) REFERENCES `employees`(`employeeID`) ON DELETE CASCADE ON UPDATE CASCADE,
  FOREIGN KEY (`createdBy`) REFERENCES `employees`(`employeeID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------------------------------
-- Table des délégations
-- --------------------------------------------------------------------------------
CREATE TABLE `delegations`(
    `delegationID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `delegatedBy` BIGINT UNSIGNED NOT NULL,
    `delegatedTo` BIGINT UNSIGNED NOT NULL,
    `startAt` DATE NOT NULL,
    `endAt` DATE NOT NULL,
    FOREIGN KEY (`delegatedBy`) REFERENCES `employees`(`employeeID`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`delegatedTo`) REFERENCES `employees`(`employeeID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------------------------------
-- Table des workflows
-- --------------------------------------------------------------------------------
CREATE TABLE `workflows`(
    `workflowID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `requestID` BIGINT UNSIGNED NOT NULL,
    `validator` BIGINT UNSIGNED NOT NULL,
    `delegate` BIGINT UNSIGNED NULL,
    `assignDate` DATETIME NOT NULL,
    `validationDate` DATETIME NULL,
    `status` BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (`requestID`) REFERENCES `requests`(`requestID`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`validator`) REFERENCES `employees`(`employeeID`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`delegate`) REFERENCES `employees`(`employeeID`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------------------------------
-- Table de liaison RequestEmployee
-- --------------------------------------------------------------------------------
CREATE TABLE `requestEmployee`(
    `ID` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `employeeID` BIGINT UNSIGNED NOT NULL,
    `requestID` BIGINT UNSIGNED NOT NULL,
    `totalHours` FLOAT NOT NULL,
    FOREIGN KEY (`employeeID`) REFERENCES `employees`(`employeeID`) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (`requestID`) REFERENCES `requests`(`requestID`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
