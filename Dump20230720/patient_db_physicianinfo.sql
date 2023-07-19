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
-- Table structure for table `physicianinfo`
--

DROP TABLE IF EXISTS `physicianinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `physicianinfo` (
  `PhysicianLicenseNumber` char(11) NOT NULL,
  `Physician` varchar(45) DEFAULT NULL,
  `ContactNumber` char(13) DEFAULT NULL,
  PRIMARY KEY (`PhysicianLicenseNumber`),
  KEY `idx_PhysicianLicenseNumber` (`PhysicianLicenseNumber`),
  CONSTRAINT `PhysicianLicenseNumber` FOREIGN KEY (`PhysicianLicenseNumber`) REFERENCES `physician` (`PhysicianLicenseNumber`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `physicianinfo`
--

LOCK TABLES `physicianinfo` WRITE;
/*!40000 ALTER TABLE `physicianinfo` DISABLE KEYS */;
INSERT INTO `physicianinfo` VALUES ('12321','Dr. Andres Cruz','09444443333'),('12345','Dr. Jose Reyes','9187654321'),('23456','Dr. Sofia Cruz','09123449999'),('34567','Dr. Angela Reyes','09223334444'),('45678','Dr. Ricardo Lopez','09171115555'),('54321','Dr. Angela Reyes','09229998888'),('5567','Dr. Patrici','922444555'),('55675','Dr. Patrici','922444555'),('55676','Dr. Patrici','922444555'),('55677','Dr. Patricia','922444555'),('67890','Dr. Sofia Ramirez','09201234567'),('67891','Dr. Sofia Hernandez','09111223344'),('76543','Dr. Sofia Ramirez','09124441111'),('87654','Dr. Karen Lee','09555551111'),('98765','Dr. Jose Cruz','09201234567');
/*!40000 ALTER TABLE `physicianinfo` ENABLE KEYS */;
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
