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
-- Table structure for table `lano_end_monitor_web`
--

DROP TABLE IF EXISTS `lano_end_monitor_web`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lano_end_monitor_web` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `domain` varchar(255) DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `domain` (`domain`,`plan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lano_end_monitor_web`
--

LOCK TABLES `lano_end_monitor_web` WRITE;
/*!40000 ALTER TABLE `lano_end_monitor_web` DISABLE KEYS */;
INSERT INTO `lano_end_monitor_web` VALUES (1,'qwe','eeeeee',0,50),(22,'四川省教育考试院','http://www.sceea.cn',1,51),(23,'四川教育网','http://www.scedu.net',1,51),(24,'[站内信息]公示公告','	 http://www.scedu.net/p/8/?StId=st_app_news_search_x635684225871384675_x_',1,51),(25,'\r\n	�Ĵ���ѧ�о���Ժ-��ҳ\r\n','http://gs.scu.edu.cn',1,51),(27,'电子科技大学研究生院','http://gr.uestc.edu.cn',1,47),(28,'\r\n	�Ĵ���ѧ�о���Ժ-��ҳ\r\n','http://gs.scu.edu.cn',1,50),(30,'四川大学 Sichuan University','http://www.scu.edu.cn',1,47),(31,'四川省教育考试院','http://www.sceea.cn',1,48);
/*!40000 ALTER TABLE `lano_end_monitor_web` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lano_end_monitor_wechat`
--

DROP TABLE IF EXISTS `lano_end_monitor_wechat`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lano_end_monitor_wechat` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `wxid` varchar(45) DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`plan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lano_end_monitor_wechat`
--

LOCK TABLES `lano_end_monitor_wechat` WRITE;
/*!40000 ALTER TABLE `lano_end_monitor_wechat` DISABLE KEYS */;
INSERT INTO `lano_end_monitor_wechat` VALUES (5,'中青网教育','weixinid',1,51),(6,'四川教育发布','weixinid',1,51),(7,'11111','weixinid',1,50),(8,'四川大学','weixinid',1,47),(10,'中青网教育','weixinid',1,47),(11,'教育','weixinid',1,48);
/*!40000 ALTER TABLE `lano_end_monitor_wechat` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lano_end_monitor_weibo`
--

DROP TABLE IF EXISTS `lano_end_monitor_weibo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
 SET character_set_client = utf8mb4 ;
CREATE TABLE `lano_end_monitor_weibo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `uid` varchar(45) DEFAULT NULL,
  `status` tinyint(4) DEFAULT NULL,
  `plan_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`,`plan_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lano_end_monitor_weibo`
--

LOCK TABLES `lano_end_monitor_weibo` WRITE;
/*!40000 ALTER TABLE `lano_end_monitor_weibo` DISABLE KEYS */;
INSERT INTO `lano_end_monitor_weibo` VALUES (6,'央视新闻','12345',1,51),(7,'四川大学','12345',1,51),(8,'12345','12345',1,50),(9,'四川大学','12345',1,47),(10,'教育','12345',1,48);
/*!40000 ALTER TABLE `lano_end_monitor_weibo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-04-02 17:38:30
