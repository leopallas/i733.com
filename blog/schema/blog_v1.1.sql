/*
SQLyog Ultimate v11.11 (64 bit)
MySQL - 5.5.37-0ubuntu0.12.04.1 : Database - blog
*********************************************************************
*/


/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`blog` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `blog`;

/*Table structure for table `comment` */

DROP TABLE IF EXISTS `comment`;

CREATE TABLE `comment` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `post_id` bigint(20) unsigned NOT NULL,
  `author` tinytext NOT NULL,
  `author_email` varchar(100) NOT NULL,
  `author_url` varchar(200) NOT NULL,
  `author_ip` varchar(100) NOT NULL,
  `date` datetime NOT NULL,
  `date_gmt` datetime NOT NULL,
  `content` text NOT NULL,
  `karma` int(11) NOT NULL,
  `approved` varchar(20) NOT NULL,
  `agent` varchar(255) NOT NULL,
  `type` varchar(20) NOT NULL,
  `parent` bigint(20) unsigned NOT NULL,
  `user_id` bigint(20) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `date_gmt` (`date_gmt`),
  KEY `post_id` (`post_id`),
  KEY `approved_date_gmt` (`approved`,`date_gmt`),
  KEY `parent` (`parent`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `commentmeta` */

DROP TABLE IF EXISTS `commentmeta`;

CREATE TABLE `commentmeta` (
  `meta_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `comment_id` bigint(20) unsigned NOT NULL,
  `meta_key` varchar(255) DEFAULT NULL,
  `meta_value` longtext,
  PRIMARY KEY (`meta_id`),
  KEY `comment_id` (`comment_id`),
  KEY `meta_key` (`meta_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `link` */

DROP TABLE IF EXISTS `link`;

CREATE TABLE `link` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `url` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `image` varchar(255) NOT NULL,
  `target` varchar(25) NOT NULL,
  `description` varchar(255) NOT NULL,
  `visible` varchar(20) NOT NULL,
  `owner` bigint(20) unsigned NOT NULL,
  `rating` int(11) NOT NULL,
  `updated` datetime NOT NULL,
  `rel` varchar(255) NOT NULL,
  `notes` mediumtext NOT NULL,
  `rss` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `visible` (`visible`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `option` */

DROP TABLE IF EXISTS `option`;

CREATE TABLE `option` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(64) NOT NULL,
  `value` longtext NOT NULL,
  `autoload` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `post` */

DROP TABLE IF EXISTS `post`;

CREATE TABLE `post` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `author` bigint(20) unsigned NOT NULL,
  `date` datetime NOT NULL,
  `date_gmt` datetime NOT NULL,
  `content` longtext NOT NULL,
  `title` text NOT NULL,
  `excerpt` text NOT NULL,
  `status` varchar(20) NOT NULL,
  `comment_status` varchar(20) NOT NULL,
  `ping_status` varchar(20) NOT NULL,
  `password` varchar(20) NOT NULL,
  `name` varchar(200) NOT NULL,
  `to_ping` text NOT NULL,
  `pinged` text NOT NULL,
  `modified` datetime NOT NULL,
  `modified_gmt` datetime NOT NULL,
  `content_filtered` longtext NOT NULL,
  `parent` bigint(20) unsigned NOT NULL,
  `guid` varchar(255) NOT NULL,
  `menu_order` int(11) NOT NULL,
  `type` varchar(20) NOT NULL,
  `mime_type` varchar(100) NOT NULL,
  `comment_count` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `parent` (`parent`),
  KEY `type_status_date` (`type`,`status`,`date`,`id`),
  KEY `name` (`name`),
  KEY `author` (`author`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `postmeta` */

DROP TABLE IF EXISTS `postmeta`;

CREATE TABLE `postmeta` (
  `meta_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `post_id` bigint(20) unsigned NOT NULL,
  `meta_key` varchar(255) DEFAULT NULL,
  `meta_value` longtext,
  PRIMARY KEY (`meta_id`),
  KEY `post_id` (`post_id`),
  KEY `meta_key` (`meta_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `stat_trace` */

DROP TABLE IF EXISTS `stat_trace`;

CREATE TABLE `stat_trace` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `time` time NOT NULL,
  `ip` varchar(39) DEFAULT NULL,
  `request_uri` text,
  `agent` text,
  `referrer` text,
  `os` varchar(128) DEFAULT NULL,
  `browser` varchar(128) DEFAULT NULL,
  `search_engine` varchar(128) DEFAULT NULL,
  `spider` varchar(128) DEFAULT NULL,
  `feed` varchar(128) DEFAULT NULL,
  `nation` varchar(16) DEFAULT NULL,
  `real_post` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `term` */

DROP TABLE IF EXISTS `term`;

CREATE TABLE `term` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `slug` varchar(200) NOT NULL,
  `term_group` bigint(10) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `term_relationship` */

DROP TABLE IF EXISTS `term_relationship`;

CREATE TABLE `term_relationship` (
  `object_id` bigint(20) unsigned NOT NULL,
  `term_taxonomy_id` bigint(20) unsigned NOT NULL,
  `term_order` int(11) NOT NULL,
  PRIMARY KEY (`object_id`,`term_taxonomy_id`),
  KEY `term_taxonomy_id` (`term_taxonomy_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `term_taxonomy` */

DROP TABLE IF EXISTS `term_taxonomy`;

CREATE TABLE `term_taxonomy` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `term_id` bigint(20) unsigned NOT NULL,
  `taxonomy` varchar(32) NOT NULL,
  `description` longtext NOT NULL,
  `parent` bigint(20) unsigned NOT NULL,
  `count` bigint(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `term_id_taxonomy` (`term_id`,`taxonomy`),
  KEY `taxonomy` (`taxonomy`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `login` varchar(60) NOT NULL,
  `password` varchar(64) NOT NULL,
  `nicename` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `url` varchar(100) NOT NULL,
  `registered` datetime NOT NULL,
  `activation_key` varchar(60) NOT NULL,
  `status` int(11) NOT NULL,
  `display_name` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `login_key` (`login`),
  KEY `nicename` (`nicename`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `usermeta` */

DROP TABLE IF EXISTS `usermeta`;

CREATE TABLE `usermeta` (
  `umeta_id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `user_id` bigint(20) unsigned NOT NULL,
  `meta_key` varchar(255) DEFAULT NULL,
  `meta_value` longtext,
  PRIMARY KEY (`umeta_id`),
  KEY `user_id` (`user_id`),
  KEY `meta_key` (`meta_key`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
