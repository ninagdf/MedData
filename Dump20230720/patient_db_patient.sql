-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: patient_db
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `patient`
--

DROP TABLE IF EXISTS `patient`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `patient` (
  `PatientID` char(11) NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `ContactNumber` char(13) DEFAULT NULL,
  `Age` int DEFAULT NULL,
  `Sex` char(1) DEFAULT NULL,
  `CurrentPhysician` varchar(45) DEFAULT NULL,
  `DateofLastUpdate` date DEFAULT NULL,
  PRIMARY KEY (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `patient`
--

LOCK TABLES `patient` WRITE;
/*!40000 ALTER TABLE `patient` DISABLE KEYS */;
INSERT INTO `patient` VALUES ('10001','Juan Dela Cruz','9123456789',30,'M','Dr. Maria Santos','2023-07-19'),('10002','Maria Garcia','09201234567',45,'F','Dr. Juanito Martinez','2023-07-19'),('10003','Pedro Mendoza','09452223333',60,'M','Dr. Isabel Cruz','2023-07-19'),('10004','Sofia Lopez','09191234567',55,'F','Dr. Ricardo Gomez','2023-07-19'),('10005','Gabriel Torres','09201112222',42,'M','Dr. Sofia Hernandez','2023-07-19'),('10006','Angelica Tan','09092223333',28,'F','Dr. Michael Santos','2023-07-19'),('10007','Ricardo Garcia','09333334444',68,'M','Dr. Patricia Reyes','2023-07-19'),('10008','Sofia Reyes','09093334444',35,'F','Dr. Martin Hernandez','2023-07-19'),('10009','Gabriel Santos','09226663333',50,'M','Dr. Angela Gomez','2023-07-19'),('10011','Miguel Reyes','09001112222',18,'M','Dr. Patricia Gomez','2023-07-19'),('10012','Isabella Garcia','09334445555',60,'F','Dr. Martin Lopez','2023-07-19'),('10014','Sofia Velasc','9220002222',39,'F','Dr. Juanito Visico','2023-07-19'),('10015','Sofia Velasc','9220002222',39,'F','Dr. Juanito Visico','2023-07-19'),('10016','Sofia Velasc','9220002222',39,'F','Dr. Juanito Visico','2023-07-19'),('10018','Sofia Velasco','9220002222',39,'F','Dr. Juanito Visico','2023-07-19');
/*!40000 ALTER TABLE `patient` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-20  2:52:48
