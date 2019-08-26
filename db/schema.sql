CREATE DATABASE IF NOT EXISTS feedback;

USE feedback;

CREATE TABLE IF NOT EXISTS `review` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) DEFAULT NULL,
  `emailid` varchar(50) DEFAULT NULL,
  `message` text,
  PRIMARY KEY (`id`)
)
