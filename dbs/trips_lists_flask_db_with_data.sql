CREATE DATABASE  IF NOT EXISTS `trip_lists_flask_db` /*!40100 DEFAULT CHARACTER SET utf8mb3 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `trip_lists_flask_db`;
-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: trip_lists_flask_db
-- ------------------------------------------------------
-- Server version	8.0.36

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
-- Table structure for table `items`
--

DROP TABLE IF EXISTS `items`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `items` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `unit` varchar(255) DEFAULT NULL,
  `quantity` float DEFAULT NULL,
  `list_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `is_packed` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_items_lists1_idx` (`list_id`),
  CONSTRAINT `fk_items_lists1` FOREIGN KEY (`list_id`) REFERENCES `lists` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `items`
--

LOCK TABLES `items` WRITE;
/*!40000 ALTER TABLE `items` DISABLE KEYS */;
INSERT INTO `items` VALUES (1,'Ham Sandwhich','sets',4,5,'2024-06-29 14:38:44','2024-07-02 18:51:19',1),(3,'Skillet','ea',2,4,'2024-06-29 14:45:13','2024-07-02 18:51:12',1),(4,'Cutting Board','eaw',1,4,'2024-06-29 14:45:41','2024-07-02 11:34:32',1),(6,'Lighter','ea',2,3,'2024-06-29 14:48:28','2024-07-07 14:56:05',0),(8,'Sleeping Pad','ea',2,3,'2024-06-29 14:51:06','2024-07-02 18:27:02',1),(11,'Tuxedo','BLACK',1,10,'2024-06-29 16:39:19','2024-07-02 12:08:06',0),(12,'Dress','Very Black',1,10,'2024-06-29 16:39:39','2024-07-02 01:41:20',0),(13,'Salt & Pepper','Shakers',2,4,'2024-06-29 16:57:36','2024-07-02 11:34:34',1),(14,'Squash','ea',2,3,'2024-06-29 22:06:54','2024-07-07 14:56:06',0),(19,'Groom Gift','Cigar',23,12,'2024-06-29 22:57:00','2024-07-02 18:54:03',0),(24,'Tarp','Big',3,3,'2024-07-01 23:15:28','2024-07-07 14:56:06',0),(25,'Matress Pump','Hand',1,3,'2024-07-01 23:16:44','2024-07-02 18:52:24',1),(26,'Beer','12oz can',24,17,'2024-07-01 23:18:31','2024-07-02 18:51:16',1),(27,'Ass Cream','Tube',1,18,'2024-07-02 01:28:24','2024-07-07 14:56:09',0),(28,'Chupa','Get the dark blue one!',15,18,'2024-07-02 01:28:51','2024-07-07 14:56:07',0),(29,'Bottles','Big, not small',3,18,'2024-07-02 01:29:18','2024-07-02 01:33:46',1),(35,'Bug Spray','Cans',2,22,'2024-07-02 12:25:41','2024-07-02 12:25:41',NULL),(36,'Paracord','ft',100,3,'2024-07-02 18:24:45','2024-07-07 14:56:02',1),(38,'Beer','12 oz can',2,21,'2024-07-02 19:09:43','2024-07-02 19:13:39',0),(39,'pony ','pile',3,24,'2024-07-07 14:54:13','2024-07-07 14:55:00',0);
/*!40000 ALTER TABLE `items` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lists`
--

DROP TABLE IF EXISTS `lists`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lists` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `trip_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_lists_trips_idx` (`trip_id`),
  CONSTRAINT `fk_lists_trips` FOREIGN KEY (`trip_id`) REFERENCES `trips` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lists`
--

LOCK TABLES `lists` WRITE;
/*!40000 ALTER TABLE `lists` DISABLE KEYS */;
INSERT INTO `lists` VALUES (3,'Yellow Bin',2,'2024-06-28 22:04:21','2024-06-28 22:04:21'),(4,'Kitchen Bin',2,'2024-06-28 22:05:39','2024-06-28 22:05:39'),(5,'Supplies Bag',2,'2024-06-28 22:05:50','2024-06-28 22:05:50'),(10,'Formal Wear',4,'2024-06-28 23:18:22','2024-06-28 23:18:22'),(12,'Gifts',4,'2024-06-29 22:37:15','2024-06-29 22:37:15'),(16,'Tessssss',4,'2024-07-01 23:07:03','2024-07-01 23:07:03'),(17,'Beer Cooler',2,'2024-07-01 23:17:40','2024-07-01 23:17:40'),(18,'Diaper Bag',2,'2024-07-02 01:27:53','2024-07-02 01:27:53'),(21,'Lunch Box',9,'2024-07-02 12:23:45','2024-07-02 12:23:45'),(22,'Satchel',6,'2024-07-02 12:25:30','2024-07-02 12:25:30'),(24,'ertterterte',11,'2024-07-07 14:54:03','2024-07-07 14:54:03');
/*!40000 ALTER TABLE `lists` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `trips`
--

DROP TABLE IF EXISTS `trips`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `trips` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `days` int DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `user_id` int NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `fk_trips_users1_idx` (`user_id`),
  CONSTRAINT `fk_trips_users1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `trips`
--

LOCK TABLES `trips` WRITE;
/*!40000 ALTER TABLE `trips` DISABLE KEYS */;
INSERT INTO `trips` VALUES (2,'Family Visit','1999-11-11',7,'Montrose',1,'2024-06-28 17:06:15','2024-06-28 22:57:56'),(4,'Honeymoon','1999-11-11',180,'Mars',1,'2024-06-28 20:33:19','2024-06-28 20:33:19'),(6,'Camping with the boys','2024-07-08',7,'Deckers',1,'2024-07-01 14:12:14','2024-07-01 14:12:14'),(9,'To McDonalds','2000-02-22',1,'Round the Corner',3,'2024-07-02 12:22:09','2024-07-02 12:22:09'),(11,'asdfasdf','2024-07-29',4,'asdf',4,'2024-07-07 14:53:57','2024-07-07 14:53:57');
/*!40000 ALTER TABLE `trips` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'admin','admin','admin@admin.com','$2b$12$d9a1AB59dCvX5WwkMp.wXOzjryXUbB0l5P4F7rlbmfDDXcGN1HfEi','2024-06-28 17:05:39','2024-07-02 11:57:36'),(2,'Test 88218','User 88218','88218@user.com','$2b$12$CBJ2UV25N/3lYLA.x.g.YepkpTg7jGvLBLig1C6OqW6RiViWoeJMq','2024-06-28 20:33:48','2024-06-28 20:33:48'),(3,'Test 51436','User 51436','51436@user.com','$2b$12$vIzZPZGnlcTjXQOiLY.6GOTYZcv1RRVWbqK/L75MxPiQzRjJ.QOCu','2024-07-02 11:50:44','2024-07-02 11:50:44'),(4,'Test 10691','User 10691','10691@user.com','$2b$12$.WuFi0bj.8xO1JXdk9BYPO79/wNAwKMBeutpoUovsFosBGhMYGjdu','2024-07-07 14:53:40','2024-07-07 14:53:40');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-07 18:10:10
