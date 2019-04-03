/*
Navicat MySQL Data Transfer

Source Server         : localhost_3306
Source Server Version : 80012
Source Host           : localhost:3306
Source Database       : db_lano

Target Server Type    : MYSQL
Target Server Version : 80012
File Encoding         : 65001

Date: 2019-04-03 14:39:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for lano_end_group
-- ----------------------------
DROP TABLE IF EXISTS `lano_end_group`;
CREATE TABLE `lano_end_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(45) DEFAULT NULL,
  `user_uuid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`name`,`user_uuid`) USING BTREE,
  KEY `uuid_idx` (`user_uuid`),
  CONSTRAINT `uuid` FOREIGN KEY (`user_uuid`) REFERENCES `lano_end_user` (`uuid`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=89 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of lano_end_group
-- ----------------------------
INSERT INTO `lano_end_group` VALUES ('64', '1', '0172ad16-5129-11e9-85d2-309c23fa4de9');
INSERT INTO `lano_end_group` VALUES ('86', '1', '0172c1c9-5129-11e9-85d2-309c23fa4de9');
INSERT INTO `lano_end_group` VALUES ('87', '212', '0172c1c9-5129-11e9-85d2-309c23fa4de9');
INSERT INTO `lano_end_group` VALUES ('66', '四川大学', '0172ad16-5129-11e9-85d2-309c23fa4de9');
INSERT INTO `lano_end_group` VALUES ('1', '太原市迎泽区教育舆情监测方案', '0172c1c9-5129-11e9-85d2-309c23fa4de9');
INSERT INTO `lano_end_group` VALUES ('2', '山西高校校园贷监测方案', '0172c1c9-5129-11e9-85d2-309c23fa4de9');

-- ----------------------------
-- Table structure for lano_end_plan
-- ----------------------------
DROP TABLE IF EXISTS `lano_end_plan`;
CREATE TABLE `lano_end_plan` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `fast_name` varchar(54) DEFAULT NULL,
  `fast_area` varchar(54) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fast_character` varchar(54) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fast_event` varchar(54) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `fast_exclude` varchar(54) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `ad_name` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `ad_match` varchar(54) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `ad_exclude` varchar(54) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `user_uuid` varchar(45) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name_UNIQUE` (`ad_name`,`user_uuid`) USING BTREE,
  KEY `group_id` (`group_id`),
  CONSTRAINT `lano_end_plan_ibfk_1` FOREIGN KEY (`group_id`) REFERENCES `lano_end_group` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=74 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of lano_end_plan
-- ----------------------------
INSERT INTO `lano_end_plan` VALUES ('73', null, null, null, null, null, 'test', '太原市+迎泽区+教育', '游戏+食堂', '1', '0172c1c9-5129-11e9-85d2-309c23fa4de9');
