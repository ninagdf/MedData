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
-- Table structure for table `diagnosisandmeds`
--

DROP TABLE IF EXISTS `diagnosisandmeds`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diagnosisandmeds` (
  `PatientNumber` char(11) NOT NULL,
  `IllnessCode` int NOT NULL,
  `MedicineReferenceNumber` int NOT NULL,
  `Medicationname` varchar(45) DEFAULT NULL,
  `Dosage` varchar(45) DEFAULT NULL,
  `Freq` varchar(45) DEFAULT NULL,
  `MedStartDate` date DEFAULT NULL,
  `MedEndDate` date DEFAULT NULL,
  `Purpose` varchar(50) DEFAULT NULL,
  `TreatmentNotes` varchar(100) DEFAULT NULL,
  `IllnessStartDate` date DEFAULT NULL,
  `IllnessEndDate` date DEFAULT NULL,
  PRIMARY KEY (`PatientNumber`,`IllnessCode`,`MedicineReferenceNumber`),
  KEY `IllnessCode_idx` (`IllnessCode`),
  CONSTRAINT `PatientNumber` FOREIGN KEY (`PatientNumber`) REFERENCES `patient` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diagnosisandmeds`
--

LOCK TABLES `diagnosisandmeds` WRITE;
/*!40000 ALTER TABLE `diagnosisandmeds` DISABLE KEYS */;
INSERT INTO `diagnosisandmeds` VALUES ('00',5,653,'gfg','dfgd','fgdfg','2023-11-05','2023-11-10','dgdgdf','gfdgdfg','2023-11-05','2023-11-09'),('0000-0004',1,5684,'Paracetamol','500mg','3 x a day','2022-10-10','2022-10-10','to mend','it worked','2022-10-10','2022-10-10'),('0000-0009',2,9658,'Paracetamol','500mg','3 x a day','2022-10-10','2022-10-10','to mend','it worked','2022-10-10','2022-10-10'),('0000-0010',2,7777,'Paracetamol','500mg','3 x a day','2022-10-10','2022-10-10','to mend','it worked','2022-10-10','2022-10-10'),('6565464',45646,34534,'sdfdfsdfsd','fsdfdsfsdfsf','sdfdsfsdfs','2023-05-05','2023-05-05','dfgdfg','gfdgdfg','2023-05-05','2023-05-05');
/*!40000 ALTER TABLE `diagnosisandmeds` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-16 22:36:42
