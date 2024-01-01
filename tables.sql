CREATE TABLE `Account_Holders` (
  `id` int NOT NULL AUTO_INCREMENT,
  `Account_Number` varchar(45) NOT NULL,
  `Holder's Name` varchar(45) NOT NULL,
  `Holder's Email` varchar(45) NOT NULL,
  `Holder's Address` varchar(100) NOT NULL,
  `Account_Type` varchar(10) NOT NULL DEFAULT 'SAVINGS',
  `Account's PIN` varchar(45) NOT NULL,
  `balance` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `Account_Number_UNIQUE` (`Account_Number`)
);
