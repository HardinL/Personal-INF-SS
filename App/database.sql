create database if not exists list;
use list;

drop table person;
CREATE TABLE `person` (
  `name` varchar(255) NOT NULL,
  `gender` char(1) NOT NULL,
  `dob` date NOT NULL,
  `height` int(3) NOT NULL,
  `weight` int(3) NOT NULL,
  `married` char(30) NOT NULL,
  `education` char(50) NOT NULL,
  `salary` int(20) NOT NULL,
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

INSERT INTO `person` (`name`, `gender`, `dob`, `height`, `weight`, `married`, `education`, `salary`) VALUES ('Hardin Liu', 'm', '2002-02-05', 170, 130, 'no', 'college', 500000);