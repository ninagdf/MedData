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
-- Table structure for table `findings`
--

DROP TABLE IF EXISTS `findings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `findings` (
  `PatientReference` char(11) NOT NULL,
  `IllnessCode` int NOT NULL,
  `Illness` varchar(60) DEFAULT NULL,
  PRIMARY KEY (`PatientReference`,`IllnessCode`),
  KEY `idx_IllnessCode` (`IllnessCode`),
  CONSTRAINT `PatientReference` FOREIGN KEY (`PatientReference`) REFERENCES `patient` (`PatientID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `findings`
--

LOCK TABLES `findings` WRITE;
/*!40000 ALTER TABLE `findings` DISABLE KEYS */;
INSERT INTO `findings` VALUES ('10001',1001,'Asthma'),('10002',1002,'Breast Cancer'),('10003',1003,'Acute Myocardial Infarction (Heart Attack)'),('10004',1004,'Hypertension'),('10005',1005,'Diabetes Mellitus Type 2'),('10006',1006,'Anxiety Disorder'),('10007',1007,'Osteoarthritis'),('10008',1008,'Major Depressive Disorder'),('10009',1009,'Chronic Kidney Disease (Stage 3)'),('10011',1011,'Attention Deficit Hyperactivity Disorder (ADHD)'),('10012',1012,'Rheumatoid Arthritis'),('10014',1014,'Depression'),('10015',1014,'Depression'),('10016',1014,'Depressio'),('10018',1014,'Rabies');
/*!40000 ALTER TABLE `findings` ENABLE KEYS */;
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
