CREATE DATABASE  IF NOT EXISTS `db_lano` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */;
USE `db_lano`;
-- MySQL dump 10.13  Distrib 8.0.15, for Win64 (x86_64)
--
-- Host: localhost    Database: db_lano
-- ------------------------------------------------------
-- Server version	8.0.15

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
 SET NAMES utf8 ;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `lano_end_exclude_web`
--

DROP TABLE IF EXISTS `lano_end_exclude_web`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lano_end_exclude_web` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `url` varchar(45) DEFAULT NULL,
  `state` tinyint(4) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lano_end_exclude_web`
--

LOCK TABLES `lano_end_exclude_web` WRITE;
/*!40000 ALTER TABLE `lano_end_exclude_web` DISABLE KEYS */;
/*!40000 ALTER TABLE `lano_end_exclude_web` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lano_end_exclude_weibo`
--

DROP TABLE IF EXISTS `lano_end_exclude_weibo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lano_end_exclude_weibo` (
  `id` int(11) NOT NULL,
  `nick_name` varchar(45) DEFAULT NULL,
  `weibo_id` varchar(45) DEFAULT NULL,
  `state` tinyint(4) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lano_end_exclude_weibo`
--

LOCK TABLES `lano_end_exclude_weibo` WRITE;
/*!40000 ALTER TABLE `lano_end_exclude_weibo` DISABLE KEYS */;
/*!40000 ALTER TABLE `lano_end_exclude_weibo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lano_end_exclude_weichat`
--

DROP TABLE IF EXISTS `lano_end_exclude_weichat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lano_end_exclude_weichat` (
  `id` int(11) NOT NULL,
  `weichat_name` varchar(45) DEFAULT NULL,
  `weichat_number` varchar(45) DEFAULT NULL,
  `state` tinyint(4) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lano_end_exclude_weichat`
--

LOCK TABLES `lano_end_exclude_weichat` WRITE;
/*!40000 ALTER TABLE `lano_end_exclude_weichat` DISABLE KEYS */;
/*!40000 ALTER TABLE `lano_end_exclude_weichat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lano_end_monitor_web`
--

DROP TABLE IF EXISTS `lano_end_monitor_web`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lano_end_monitor_web` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  `url` varchar(45) DEFAULT NULL,
  `state` tinyint(4) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lano_end_monitor_web`
--

LOCK TABLES `lano_end_monitor_web` WRITE;
/*!40000 ALTER TABLE `lano_end_monitor_web` DISABLE KEYS */;
/*!40000 ALTER TABLE `lano_end_monitor_web` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lano_end_monitor_weibo`
--

DROP TABLE IF EXISTS `lano_end_monitor_weibo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lano_end_monitor_weibo` (
  `id` int(11) NOT NULL,
  `nick_name` varchar(45) DEFAULT NULL,
  `weibo_id` varchar(45) DEFAULT NULL,
  `state` tinyint(4) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lano_end_monitor_weibo`
--

LOCK TABLES `lano_end_monitor_weibo` WRITE;
/*!40000 ALTER TABLE `lano_end_monitor_weibo` DISABLE KEYS */;
/*!40000 ALTER TABLE `lano_end_monitor_weibo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lano_end_monitor_weichat`
--

DROP TABLE IF EXISTS `lano_end_monitor_weichat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lano_end_monitor_weichat` (
  `id` int(11) NOT NULL,
  `weichat_name` varchar(45) DEFAULT NULL,
  `weichat_number` varchar(45) DEFAULT NULL,
  `state` tinyint(4) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lano_end_monitor_weichat`
--

LOCK TABLES `lano_end_monitor_weichat` WRITE;
/*!40000 ALTER TABLE `lano_end_monitor_weichat` DISABLE KEYS */;
/*!40000 ALTER TABLE `lano_end_monitor_weichat` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-29 17:52:17
