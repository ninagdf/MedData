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
INSERT INTO `diagnosisandmeds` VALUES ('10001',1001,1,'Salbutamol','2 puffs','Every 4 hours','2023-07-10','2023-07-25','Relieve asthma symptoms','Patient responds well to medication. Avoid triggers.','2023-07-05','2023-07-15'),('10002',1002,2,'Tamoxifen','20mg','Once daily','2023-07-10','2023-12-31','Adjuvant therapy for breast cancer treatment','Patient experiences mild side effects. Regular check-ups required.','2023-06-15','2023-07-05'),('10003',1003,3,'Aspirin','80mg','Once daily','2023-07-10','2023-08-09','Prevent blood clotting post-heart attack','Patient recovering well. Lifestyle changes recommended.','2023-07-05','2023-07-10'),('10004',1004,4,'Amlodipine','5mg','Once daily','2023-07-10','2023-08-01','Control high blood pressure','Patient\'s blood pressure well managed. Regular ','2023-07-05','2023-07-10'),('10005',1005,5,'Metformin','500mg','Twice daily after meals','2023-07-10','2023-12-31','Manage blood sugar levels','Patient\'s blood sugar levels stable. Diet and exercise advised. ','2023-07-05','2023-07-25'),('10006',1006,6,'Sertraline','50mg','Once daily in the morning','2023-07-10','2023-12-31','Manage anxiety symptoms','Patient feels improvement in anxiety symptoms.Regular follow-ups required. ','2023-07-02','2023-07-20'),('10007',1007,7,'Celecoxib','200mg','Once daily','2023-07-10','2023-08-31','Relieve joint pain and inflammation','Patient experiences improvement in mobility. Gentle exercises recommended.','2023-06-25','2023-07-10'),('10008',1008,8,'10mg','200mg','Once daily in the morning','2023-07-10','2023-09-30','Manage depressive symptoms','Patient shows gradual improvement in mood.','2023-07-01','2023-07-20'),('10009',1009,9,'Losartan','50mg','Once daily','2023-07-10','2024-01-31','Manage blood pressure and protect kidneys','Patient needs regular kidney function monitoring. Follow renal diet.','2023-06-30','2023-07-15'),('10011',1011,11,'Methylphenidate','10mg','Twice daily before meals','2023-07-10','2023-10-15','Improve focus and reduce impulsivity','Patient shows improvement in attention and concentration.','2023-07-05','2023-07-25'),('10012',1012,12,'Methotrexate','10mg','Once weekly','2023-07-10','2024-03-31','Control joint inflammation and pain','Patient experiences relief in joint stiffness. Monitor liver function.','2023-07-07','2023-07-30'),('10014',1014,14,'Fluoxetin','20mg','Once daily in the morning','2023-07-11','2023-10-30','Manage depressive symptoms','Patient shows gradual improvement in moo','2023-07-14','2023-07-26'),('10015',1014,14,'Fluoxetin','20mg','Once daily in the morning','2023-07-11','2023-10-30','Manage depressive symptoms','Patient shows gradual improvement in moo','2023-07-14','2023-07-26'),('10016',1014,14,'Fluoxetin','20mg','Once daily in the morning','2023-07-11','2023-10-30','Manage depressive symptoms','Patient shows gradual improvement in moo','2023-07-14','2023-07-26'),('10018',1014,14,'Fluoxetin','20mg','Once daily in the morning','2023-07-11','2023-10-30','Manage depressive symptoms','Patient shows gradual improvement in moo','2023-07-14','2023-07-26');
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

-- Dump completed on 2023-07-20  2:52:47
