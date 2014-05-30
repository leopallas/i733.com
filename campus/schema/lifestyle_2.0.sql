/*
SQLyog Community v10.42
MySQL - 5.1.66-community : Database - lifestyle_2.0
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`lifestyle_2.0` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `lifestyle_2.0`;

/*Table structure for table `account` */

DROP TABLE IF EXISTS `account`;

CREATE TABLE `account` (
  `ACT_ID` varchar(24) NOT NULL COMMENT '主键ID',
  `ACT_NAME` varchar(24) NOT NULL COMMENT '登录账号',
  `ACT_PWD` varchar(100) NOT NULL COMMENT '账号密码',
  `ACT_TYPE` int(1) NOT NULL COMMENT '账号权限（1==系统2==代理商...）',
  `ACT_VALID_IND` int(1) NOT NULL COMMENT '冻结状态（1==启用2==禁用）',
  `ACT_REFERENCE_ID` varchar(24) DEFAULT NULL COMMENT '账号所属关联ID',
  `CREATE_USER` varchar(24) NOT NULL COMMENT '创建人',
  `CREATE_DT` datetime NOT NULL COMMENT '创建时间',
  `UPDATE_USER` varchar(24) NOT NULL COMMENT '更新人',
  `UPDATE_DT` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`ACT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `area` */

DROP TABLE IF EXISTS `area`;

CREATE TABLE `area` (
  `ARE_ID` varchar(24) NOT NULL COMMENT '区域ID',
  `ARE_NAME` varchar(30) NOT NULL COMMENT '区域名',
  `ARE_TYPE` int(1) NOT NULL COMMENT '区域类型(1=省,2=市,3=区县)',
  `ARE_PARENT_ID` varchar(24) DEFAULT NULL COMMENT '区域父节点ID',
  `ARE_SORT_NO` int(10) NOT NULL DEFAULT '0' COMMENT '排序',
  `ARE_STATUS` int(1) NOT NULL DEFAULT '1' COMMENT '状态（1-未开通，2-开通）',
  `ARE_WEATHER_CD` varchar(50) NOT NULL COMMENT '天气预报对应的城市编码',
  PRIMARY KEY (`ARE_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `attachment` */

DROP TABLE IF EXISTS `attachment`;

CREATE TABLE `attachment` (
  `ATT_ID` varchar(24) NOT NULL COMMENT '附件ID',
  `ATT_NAME` varchar(100) NOT NULL COMMENT '附件名称',
  `ATT_TYPE` int(1) NOT NULL COMMENT '附件类型（1==图片2==音频...）',
  `ATT_EXTENSION_NAME` varchar(24) NOT NULL COMMENT '附件后缀（.jpg,.png...）',
  `ATT_REF_ID` varchar(24) DEFAULT NULL COMMENT '附件来源ID',
  `ATT_REF_TYPE` int(1) NOT NULL COMMENT '附件来源（1==社区商城2==拼车...）',
  `CREATE_USER` varchar(24) NOT NULL COMMENT '创建人',
  `CREATED_DT` datetime NOT NULL COMMENT '创建时间',
  PRIMARY KEY (`ATT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `auth_key` */

DROP TABLE IF EXISTS `auth_key`;

CREATE TABLE `auth_key` (
  `SECRET_TOKEN` varchar(50) NOT NULL COMMENT '令牌',
  `SIGNATURE_KEY` varchar(50) NOT NULL COMMENT '签名Key',
  `USR_ID` varchar(24) NOT NULL COMMENT '用户ID',
  PRIMARY KEY (`SECRET_TOKEN`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `community` */

DROP TABLE IF EXISTS `community`;

CREATE TABLE `community` (
  `COM_ID` varchar(24) NOT NULL COMMENT '社区编码',
  `AGT_ID` varchar(24) DEFAULT NULL COMMENT '代理商ID',
  `ARE_ID` varchar(24) DEFAULT NULL COMMENT '关联区域ID',
  `ARE_NAME` varchar(50) DEFAULT NULL COMMENT '关联区域名称',
  `COM_NAME` varchar(50) NOT NULL COMMENT '社区名字',
  `COM_DESC` varchar(200) DEFAULT NULL COMMENT '社区描述',
  `COM_ADDR` varchar(200) DEFAULT NULL COMMENT '社区地址',
  `COM_LNG` double DEFAULT NULL COMMENT '社区经度',
  `COM_LAT` double DEFAULT NULL COMMENT '社区纬度',
  `COM_STATUS` int(1) NOT NULL DEFAULT '1' COMMENT '状态（1==未开通，2==开通）',
  PRIMARY KEY (`COM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='社区表';

/*Table structure for table `lf_barter` */

DROP TABLE IF EXISTS `lf_barter`;

CREATE TABLE `lf_barter` (
  `BAT_ID` varchar(24) NOT NULL COMMENT '易物ID',
  `COM_ID` varchar(24) NOT NULL COMMENT '关联社区ID',
  `BAC_ID` varchar(24) NOT NULL COMMENT '关联易物类型ID',
  `BAT_NAME` varchar(100) NOT NULL COMMENT '易物名',
  `BAT_CONTACT_PHONE` varchar(20) NOT NULL COMMENT '联系电话',
  `BAT_PRICE` decimal(10,2) NOT NULL COMMENT '价格',
  `BAT_IND` int(1) DEFAULT NULL COMMENT '是否置换（1=置换，2=不置换）',
  `BAT_DESCRIPTION` text COMMENT '易物描述',
  `BAT_EXPECT_KEYWORDS` varchar(100) DEFAULT NULL COMMENT '希望交易物品关键字',
  `BAT_EXPECT_DESC` text COMMENT '希望交易物品描述',
  `BAT_COVER_IMAGE_URI` varchar(100) DEFAULT NULL COMMENT '易物图片URI',
  `BAT_STATUS` int(1) NOT NULL COMMENT '易物状态(1=有效，2=关闭)',
  `BAT_REFRESH_DT` datetime NOT NULL COMMENT '易物刷新时间',
  `CREATED_BY` varchar(24) NOT NULL COMMENT '创建用户ID',
  `CREATED_DT` datetime NOT NULL COMMENT '创建时间',
  `UPDATED_BY` varchar(24) NOT NULL COMMENT '更新用户ID',
  `UPDATED_DT` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`BAT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `lf_barter_analyze` */

DROP TABLE IF EXISTS `lf_barter_analyze`;

CREATE TABLE `lf_barter_analyze` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '易物分析ID',
  `BAT_ID` varchar(24) NOT NULL COMMENT '关联易物ID',
  `COM_ID` varchar(24) NOT NULL COMMENT '关联社区ID',
  `BAT_KEYWORD` varchar(50) NOT NULL COMMENT '易物关键字',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=1156 DEFAULT CHARSET=utf8;

/*Table structure for table `lf_barter_category` */

DROP TABLE IF EXISTS `lf_barter_category`;

CREATE TABLE `lf_barter_category` (
  `BAC_ID` varchar(24) NOT NULL COMMENT '易物类型ID',
  `BAC_CATEGORY_NAME` varchar(100) NOT NULL COMMENT '易物类型名',
  `BAC_CATEGORY_DESC` varchar(200) DEFAULT NULL COMMENT '易物类型描述',
  PRIMARY KEY (`BAC_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `lf_car_parker` */

DROP TABLE IF EXISTS `lf_car_parker`;

CREATE TABLE `lf_car_parker` (
  `CAP_ID` varchar(24) NOT NULL COMMENT '抢车位ID',
  `CAP_PARKER_NO` varchar(100) NOT NULL COMMENT '停车车位号',
  `COM_ID` varchar(24) NOT NULL COMMENT '关联社区ID',
  `CAP_CONTACT_NO` varchar(20) NOT NULL COMMENT '车主联系电话号码',
  `CAP_FREE_START_TIME` datetime NOT NULL COMMENT '空闲开始时间',
  `CAP_FREE_END_TIME` datetime NOT NULL COMMENT '空闲截止时间',
  `CAP_DURATION` int(1) NOT NULL COMMENT '闲置周期(1-无周期，2-每天，3-工作日，4-周末)',
  `CAP_PRICE` decimal(10,2) NOT NULL COMMENT '占用车位单价（30分钟计）',
  `CAP_STATUS` int(1) NOT NULL COMMENT '状态（1=有效，2=无效）',
  `CAP_REMARKS` varchar(1000) DEFAULT NULL COMMENT '备注',
  `CREATED_BY` varchar(24) NOT NULL COMMENT '创建用户ID',
  `CREATED_DT` datetime NOT NULL COMMENT '创建时间',
  `UPDATED_BY` varchar(24) NOT NULL COMMENT '更新用户ID',
  `UPDATED_DT` datetime NOT NULL COMMENT '更新时间',
  `LAST_TXN_DT` datetime DEFAULT NULL COMMENT '最后一条TXN的时间',
  PRIMARY KEY (`CAP_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `lf_car_parker_black_list` */

DROP TABLE IF EXISTS `lf_car_parker_black_list`;

CREATE TABLE `lf_car_parker_black_list` (
  `ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '举报ID',
  `CAP_ID` varchar(24) NOT NULL COMMENT '举报抢车位ID',
  `USR_ID` varchar(20) NOT NULL COMMENT '举报用户ID',
  `CPB_REASON` varchar(200) NOT NULL COMMENT '举报原因',
  `CREATE_DT` datetime NOT NULL COMMENT '举报时间',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `lf_car_parker_refund` */

DROP TABLE IF EXISTS `lf_car_parker_refund`;

CREATE TABLE `lf_car_parker_refund` (
  `CPR_ID` varchar(24) NOT NULL COMMENT '退款ID',
  `CPT_ID` varchar(24) NOT NULL COMMENT '关联交易ID',
  `CAP_ID` varchar(24) NOT NULL COMMENT '关联抢车位ID',
  `CPR_REFUND_AMT` decimal(10,2) NOT NULL COMMENT '退款金额',
  `CPR_STATUS` int(1) NOT NULL COMMENT '退款状态（1=申请退款，2-已退款）',
  `CPR_USR_ID` varchar(24) NOT NULL COMMENT '退款用户ID',
  `CPR_DT` datetime NOT NULL COMMENT '退款时间',
  PRIMARY KEY (`CPR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `lf_car_parker_txn` */

DROP TABLE IF EXISTS `lf_car_parker_txn`;

CREATE TABLE `lf_car_parker_txn` (
  `CPT_ID` varchar(24) NOT NULL COMMENT '交易ID',
  `CAP_ID` varchar(24) NOT NULL COMMENT '关联抢车位ID',
  `CPT_TXN_START_TIME` datetime DEFAULT NULL COMMENT '交易开始时间',
  `CPT_TXN_END_TIME` datetime DEFAULT NULL COMMENT '交易截止时间',
  `CPT_TXN_DEPOSIT` decimal(10,2) DEFAULT NULL COMMENT '预交金',
  `CPT_TXN_AMT` decimal(10,2) DEFAULT NULL COMMENT '交易产生的金额',
  `CPT_TXN_PRICE` decimal(10,2) NOT NULL COMMENT '交易单价',
  `CPT_TXN_UST_ID` varchar(24) DEFAULT NULL COMMENT '交易用户ID',
  `CPT_TXN_TYPE` int(1) NOT NULL COMMENT '交易类型(1-空闲, 2=预交款，3-离开，4-关闭)',
  `CPT_TXN_DT` datetime NOT NULL COMMENT '创建交易记录时间',
  PRIMARY KEY (`CPT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `lf_car_together` */

DROP TABLE IF EXISTS `lf_car_together`;

CREATE TABLE `lf_car_together` (
  `CAT_ID` varchar(24) NOT NULL COMMENT '拼车信息ID',
  `COM_ID` varchar(24) NOT NULL COMMENT '社区ID',
  `CAT_DESTINATION` varchar(100) NOT NULL COMMENT '目的地',
  `CAT_SOURCE` varchar(100) NOT NULL COMMENT '出发地',
  `CAT_DESTINATION_LNG` double DEFAULT NULL COMMENT '目的地经度',
  `CAT_DESTINATION_LAT` double DEFAULT NULL COMMENT '目的地纬度',
  `CAT_SOURCE_LNG` double DEFAULT NULL COMMENT '出发地经度',
  `CAT_SOURCE_LAT` double DEFAULT NULL COMMENT '出发地纬度',
  `CAT_APPOINT_TIME` datetime DEFAULT NULL COMMENT '预约时间（null为即时出发）',
  `CAT_CONTACT_NO` varchar(24) NOT NULL COMMENT '联系电话',
  `CAT_TYPE` int(1) NOT NULL COMMENT '拼车类型（1=车主发的信息，2=乘客发的信息）',
  `CAT_EMPTY_POSITION` int(11) DEFAULT NULL COMMENT '空位数量',
  `CAT_IMAGE_URI` varchar(24) DEFAULT NULL COMMENT '拼车图片ID',
  `CAT_DISTANCE` float DEFAULT NULL COMMENT '路线距离',
  `CAT_DURATION` int(1) NOT NULL COMMENT '周期（1-无周期，2-每天，3-工作日，4-周末）',
  `CAT_SCORE` double NOT NULL COMMENT '评分',
  `CAT_COMMENT_COUNT` int(11) NOT NULL COMMENT '评论数量',
  `CAT_DESCRIPTION` text COMMENT '拼车描述',
  `CAT_STATUS` int(1) NOT NULL COMMENT '拼车状态（1==有效2==关闭）',
  `CREATED_DT` datetime NOT NULL COMMENT '创建时间',
  `UPDATED_BY` varchar(24) NOT NULL COMMENT '更形用户ID',
  `UPDATED_DT` datetime NOT NULL COMMENT '更形时间',
  `CREATED_BY` varchar(24) NOT NULL COMMENT '创建用户ID',
  PRIMARY KEY (`CAT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `lf_comment` */

DROP TABLE IF EXISTS `lf_comment`;

CREATE TABLE `lf_comment` (
  `CMM_ID` varchar(24) NOT NULL COMMENT '评论ID',
  `REF_ID` varchar(24) NOT NULL COMMENT '关联发布信息ID',
  `CMM_COMMENT` varchar(1000) NOT NULL COMMENT '评论内容',
  `CMM_SCORE` double DEFAULT NULL COMMENT '评分数',
  `CMM_USR_ID` varchar(24) NOT NULL COMMENT '评论用户ID',
  `CMM_DT` datetime NOT NULL COMMENT '评论时间',
  PRIMARY KEY (`CMM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `lf_reply` */

DROP TABLE IF EXISTS `lf_reply`;

CREATE TABLE `lf_reply` (
  `RPL_ID` int(11) unsigned NOT NULL AUTO_INCREMENT COMMENT '回复ID',
  `CMM_ID` varchar(24) NOT NULL COMMENT '关联评论信息ID',
  `RPL_COMMENT` varchar(1000) NOT NULL COMMENT '回复内容',
  `RPL_USR_ID` varchar(24) NOT NULL COMMENT '回复用户ID',
  `RPL_DT` datetime NOT NULL COMMENT '回复时间',
  PRIMARY KEY (`RPL_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8;

/*Table structure for table `ma_agent` */

DROP TABLE IF EXISTS `ma_agent`;

CREATE TABLE `ma_agent` (
  `AGT_ID` varchar(24) NOT NULL COMMENT '代理商ID',
  `AGT_NAME` varchar(100) NOT NULL COMMENT '代理商名称',
  `AGT_ADDRESS` varchar(100) NOT NULL COMMENT '代理商地址',
  `AGT_STATUS` int(1) NOT NULL COMMENT '代理商状态(1==有效2==无效)',
  `AGT_PHONE` varchar(24) NOT NULL COMMENT '代理商电话',
  `AGT_DESCRIPTION` varchar(100) NOT NULL COMMENT '代理商描述',
  `CREATE_USER` varchar(24) NOT NULL COMMENT '创建人',
  `CREATE_DT` datetime NOT NULL COMMENT '创建时间',
  `UPDATE_USER` varchar(24) NOT NULL COMMENT '更新人',
  `UPDATE_DT` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`AGT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `ma_item` */

DROP TABLE IF EXISTS `ma_item`;

CREATE TABLE `ma_item` (
  `ITM_ID` varchar(24) NOT NULL COMMENT '商品Id',
  `SOP_ID` varchar(24) NOT NULL COMMENT '关联商家ID',
  `ITM_NAME` varchar(100) NOT NULL COMMENT '商品名称',
  `ITM_PRICE` decimal(10,2) NOT NULL COMMENT '商品价格',
  `ITM_STATUS` int(1) NOT NULL COMMENT '商品状态1==上架2==下架默认下架',
  `ITM_DESCRIPTION` varchar(100) DEFAULT NULL COMMENT '商品描述',
  `ITC_ID` varchar(24) NOT NULL COMMENT '商品类别Id',
  `ITM_FILE_URI` varchar(200) DEFAULT NULL COMMENT '商品附件URI',
  `ITM_DISCOUNT_IND` int(1) NOT NULL COMMENT '是否支持打折1==支持2==不支持',
  `CREATE_USER` varchar(24) NOT NULL COMMENT '创建人',
  `CREATE_DT` datetime NOT NULL COMMENT '创建时间',
  `UPDATE_USER` varchar(24) NOT NULL COMMENT '更新人',
  `UPDATE_DT` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`ITM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `ma_item_category` */

DROP TABLE IF EXISTS `ma_item_category`;

CREATE TABLE `ma_item_category` (
  `ITC_ID` varchar(24) NOT NULL COMMENT '商品类型ID',
  `SOP_ID` varchar(24) NOT NULL COMMENT '关联商家ID',
  `ITC_NAME` varchar(24) NOT NULL COMMENT '商品类型名称',
  `ITC_VALID_IND` int(1) NOT NULL COMMENT '状态1==启用2==禁用',
  `ITC_SORT_NO` int(2) NOT NULL DEFAULT '1' COMMENT '商品类型分类',
  `CREATE_USER` varchar(24) NOT NULL COMMENT '创建人',
  `CREATE_DT` datetime NOT NULL COMMENT '创建时间',
  `UPDATE_USER` varchar(24) NOT NULL COMMENT '更新人',
  `UPDATE_DT` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`ITC_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `ma_item_discount` */

DROP TABLE IF EXISTS `ma_item_discount`;

CREATE TABLE `ma_item_discount` (
  `ITD_ID` varchar(24) NOT NULL COMMENT '打折Id',
  `ITM_ID` varchar(24) NOT NULL COMMENT '关联商品Id',
  `ITC_ID` varchar(24) NOT NULL COMMENT '关联商品分类ID',
  `ITD_DISCOUNT_PERCENTAGE` int(3) NOT NULL COMMENT '打折百分比',
  `ITD_DISCOUNTED_PRICE` decimal(10,2) NOT NULL COMMENT '打折后的价格',
  `ITD_START_DT` datetime NOT NULL COMMENT '开始时间',
  `ITD_END_DT` datetime NOT NULL COMMENT '结束时间',
  `ITD_TYPE` int(1) NOT NULL COMMENT '打折类型1==全场2==分类3==单个',
  `CREATE_USER` varchar(24) NOT NULL COMMENT '创建人',
  `CREATE_DT` datetime NOT NULL COMMENT '创建时间',
  `UPDATE_USER` varchar(24) NOT NULL COMMENT '更新人',
  `UPDATE_DT` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`ITD_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `ma_order` */

DROP TABLE IF EXISTS `ma_order`;

CREATE TABLE `ma_order` (
  `ODR_ID` varchar(24) NOT NULL COMMENT '订单ID',
  `COM_ID` varchar(24) NOT NULL COMMENT '关联社区ID',
  `SOP_ID` varchar(24) NOT NULL COMMENT '关联店铺ID',
  `ODR_NO` varchar(24) NOT NULL COMMENT '订单号',
  `ODR_ADDRESS` varchar(100) DEFAULT NULL COMMENT '送餐地址',
  `ODR_STATUS` int(1) NOT NULL COMMENT '状态1==未受理2==商家受理3==商家拒绝4==用户取消5==商家已完成6==用户已完成',
  `ODR_START_DT` datetime DEFAULT NULL COMMENT '预约开始时间',
  `ODR_END_DT` datetime DEFAULT NULL COMMENT '预约结束时间',
  `ODR_REMARK` varchar(100) DEFAULT NULL COMMENT '订餐备注信息',
  `ODR_SOP_PHONE` varchar(24) DEFAULT NULL COMMENT '商家电话',
  `ODR_SOP_REJECT` varchar(100) DEFAULT NULL COMMENT '商家取消描述',
  `ODR_USR_REJECT` varchar(100) DEFAULT NULL COMMENT '用户拒绝描述',
  `ODR_USR_PHONE` varchar(24) DEFAULT NULL COMMENT '用户电话',
  `ODR_USR_NAME` varchar(24) DEFAULT NULL COMMENT '用户名称',
  `ODR_DELIVERY_TYPE` int(1) NOT NULL COMMENT '1==送货上门2==自取',
  `ODR_DELIVERY_FEE` decimal(10,2) NOT NULL COMMENT '送餐费',
  `ODR_TOTAL_PRICE` decimal(10,2) NOT NULL COMMENT '总价',
  `ODR_REVIEW_IND` int(1) NOT NULL DEFAULT '1' COMMENT '用户是否评论(1=未评论,2=已评论)',
  `ODR_PAY_TYPE` int(1) NOT NULL COMMENT '支付方式(1=货到付款,2=在线支付)',
  `CREATE_USER` varchar(24) NOT NULL COMMENT '创建人',
  `CREATE_DT` datetime NOT NULL COMMENT '创建时间',
  `UPDATE_USER` varchar(24) NOT NULL COMMENT '更新人',
  `UPDATE_DT` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`ODR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `ma_order_item` */

DROP TABLE IF EXISTS `ma_order_item`;

CREATE TABLE `ma_order_item` (
  `OIT_ID` varchar(24) NOT NULL COMMENT '订单条目ID',
  `ODR_ID` varchar(24) NOT NULL COMMENT '关联订单ID',
  `ITM_ID` varchar(24) NOT NULL COMMENT '关联商品ID',
  `OIT_ORG_PRICE` decimal(10,2) NOT NULL COMMENT '订单商品原价',
  `OIT_NEW_PRICE` decimal(10,2) NOT NULL COMMENT '订单商品现价',
  `OIT_COUNT` int(11) NOT NULL COMMENT '数量',
  PRIMARY KEY (`OIT_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `ma_shop` */

DROP TABLE IF EXISTS `ma_shop`;

CREATE TABLE `ma_shop` (
  `SOP_ID` varchar(24) NOT NULL COMMENT '店铺ID',
  `SOC_ID` varchar(24) NOT NULL COMMENT '关联店铺类型ID',
  `SOP_NAME` varchar(24) NOT NULL COMMENT '店铺名称',
  `SOP_PHONE` varchar(24) NOT NULL COMMENT '店铺电话号码',
  `SOP_MESSAGE_PHONE` varchar(24) DEFAULT NULL COMMENT '店铺接受短信电话号码',
  `SOP_ADDRESS` varchar(100) NOT NULL COMMENT '店铺地址',
  `SOP_STATUS` int(1) NOT NULL COMMENT '商家状态1==正常2==审批中3==审批不通过4==禁用',
  `SOP_DESCRIPTION` varchar(100) DEFAULT NULL COMMENT '店铺介绍',
  `SOP_NOTICE` varchar(100) DEFAULT NULL COMMENT '店铺公告',
  `SOP_LNG` double DEFAULT NULL COMMENT '店铺经度',
  `SOP_LAT` double DEFAULT NULL COMMENT '店铺纬度',
  `SOP_LOGO_URI` varchar(200) NOT NULL COMMENT 'LOGO图片地址附件ID',
  `SOP_USR_NAME` varchar(24) NOT NULL COMMENT '店主姓名',
  `SOP_USR_IC` varchar(24) NOT NULL COMMENT '身份证号',
  `SOP_DELIVERY_FEE` decimal(10,2) NOT NULL COMMENT '送餐费',
  `SOP_DELIVERY_IND` int(1) NOT NULL COMMENT '是否支持上门服务(1==支持2==不支持)',
  `SOP_START_PRICE` decimal(10,2) NOT NULL COMMENT '起步价',
  `SOP_SORT_NO` int(11) NOT NULL DEFAULT '1' COMMENT '店铺排序',
  `SOP_ODR_IND` int(1) NOT NULL COMMENT '是否支持下单(1==支持2==不支持)',
  `SOP_OPEN_IND` int(1) NOT NULL COMMENT '是否营业(1==营业2==不营业)',
  `SOP_OPEN_START_TIME` varchar(5) DEFAULT NULL COMMENT '营业开始时间(格式HH:mm)',
  `SOP_OPEN_END_TIME` varchar(5) DEFAULT NULL COMMENT '营业结束时间(格式HH:mm)',
  `SOP_LEVEL` int(1) DEFAULT NULL COMMENT '店铺级别(1==普通 2==VIP 3==直营)',
  `SOP_TOTAL_COUNT` int(11) NOT NULL COMMENT '总商品数目',
  `SOP_SCORE` double DEFAULT '5' COMMENT '店铺评分',
  `CREATE_USER` varchar(24) NOT NULL COMMENT '创建人',
  `CREATE_DT` datetime NOT NULL COMMENT '创建时间',
  `UPDATE_USER` varchar(24) NOT NULL COMMENT '更新人',
  `UPDATE_DT` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`SOP_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `ma_shop_category` */

DROP TABLE IF EXISTS `ma_shop_category`;

CREATE TABLE `ma_shop_category` (
  `SOC_ID` varchar(24) NOT NULL COMMENT '店铺类型ID',
  `SOC_NAME` varchar(24) NOT NULL COMMENT '店铺类型名称',
  `SOC_VALID_IND` int(1) NOT NULL COMMENT '是否有效(1==有效2==无效)',
  `SOC_SORT_NO` int(2) NOT NULL DEFAULT '1' COMMENT '店铺类型排序',
  PRIMARY KEY (`SOC_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `ma_shop_comment` */

DROP TABLE IF EXISTS `ma_shop_comment`;

CREATE TABLE `ma_shop_comment` (
  `CMM_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT 'ID',
  `REF_ID` varchar(24) NOT NULL COMMENT '关联ID',
  `CMM_SCORE` double NOT NULL COMMENT '评论分数',
  `CMM_COMMENT` varchar(100) DEFAULT NULL COMMENT '评论描述',
  `CMM_USR_ID` varchar(24) NOT NULL COMMENT '留言人',
  `CMM_DT` datetime NOT NULL COMMENT '留言时间',
  `CMM_REPLY_COMMENT` varchar(100) DEFAULT NULL COMMENT '商家回复内容',
  `CMM_REPLY_USR_ID` varchar(24) DEFAULT NULL COMMENT '回复人ID',
  `CMM_REPLY_DT` datetime DEFAULT NULL COMMENT '回复时间',
  PRIMARY KEY (`CMM_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8;

/*Table structure for table `ma_shop_community` */

DROP TABLE IF EXISTS `ma_shop_community`;

CREATE TABLE `ma_shop_community` (
  `SOP_ID` varchar(24) NOT NULL COMMENT '店铺ID',
  `COM_ID` varchar(24) NOT NULL COMMENT '社区ID',
  PRIMARY KEY (`SOP_ID`,`COM_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `ma_shop_complaint` */

DROP TABLE IF EXISTS `ma_shop_complaint`;

CREATE TABLE `ma_shop_complaint` (
  `SCP_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '店铺投诉ID',
  `SOP_ID` varchar(24) NOT NULL COMMENT '投诉店铺',
  `SCP_COMMENT` varchar(100) NOT NULL COMMENT '投诉内容',
  `SCP_USR_ID` varchar(24) NOT NULL COMMENT '投诉人ID',
  `SCP_DT` datetime NOT NULL COMMENT '投诉时间',
  PRIMARY KEY (`SCP_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2343 DEFAULT CHARSET=utf8;

/*Table structure for table `ma_shop_order_time` */

DROP TABLE IF EXISTS `ma_shop_order_time`;

CREATE TABLE `ma_shop_order_time` (
  `SOT_ID` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键ID',
  `SOP_ID` varchar(24) NOT NULL COMMENT '关联店铺ID',
  `SOT_START_TIME` varchar(5) NOT NULL COMMENT '可以下单开始时间（格式HH:mm）',
  `SOT_END_TIME` varchar(5) NOT NULL COMMENT '可以下单结束时间（格式HH:mm）',
  PRIMARY KEY (`SOT_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8;

/*Table structure for table `register` */

DROP TABLE IF EXISTS `register`;

CREATE TABLE `register` (
  `REG_HP` varchar(20) NOT NULL COMMENT '注册手机号',
  `REG_AUTH_CODE` varchar(16) NOT NULL COMMENT '注册验证码',
  `REG_DT` datetime NOT NULL COMMENT '注册时间',
  `REG_IND` int(1) NOT NULL COMMENT '注册状态(1=注册,2=未注册)',
  PRIMARY KEY (`REG_HP`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `server` */

DROP TABLE IF EXISTS `server`;

CREATE TABLE `server` (
  `ID` int(2) NOT NULL COMMENT 'ID',
  `HTTPS` int(1) DEFAULT NULL COMMENT '是否为HTTPS(1==是,2==不是)',
  `ADDRESS` varchar(50) DEFAULT NULL COMMENT 'IP地址',
  `PORT` int(8) DEFAULT NULL COMMENT 'IP端口号',
  `TYPE` varchar(20) DEFAULT NULL COMMENT '服务器类型',
  `WEB_CONTEXT` varchar(40) DEFAULT NULL COMMENT 'WEB上下文地址',
  `COMMENT` varchar(100) DEFAULT NULL COMMENT '备注',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `USR_ID` varchar(24) NOT NULL COMMENT '用户ID',
  `COM_ID` varchar(24) DEFAULT NULL COMMENT '社区ID',
  `USR_NAME` varchar(50) NOT NULL COMMENT '用户名',
  `USR_PWD` varchar(50) NOT NULL COMMENT '用户密码',
  `USR_REAL_NAME` varchar(50) DEFAULT NULL COMMENT '用户真实姓名',
  `USR_IC_TYPE` int(11) DEFAULT NULL COMMENT '用户证件类型(1=身份证, 2=护照, 3=其它证件)',
  `USR_IC` varchar(50) DEFAULT NULL COMMENT '用户证件号',
  `USR_TYPE` int(11) NOT NULL COMMENT '用户类型(1=普通帐户，2=子帐户，3=主帐户)',
  `USR_EMAIL` varchar(50) DEFAULT NULL COMMENT '用户电子邮箱',
  `USR_PHONE` varchar(50) DEFAULT NULL COMMENT '用户手机',
  `CREATE_DT` datetime NOT NULL COMMENT '创建时间',
  `UPDATE_DT` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`USR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COMMENT='用户表';

/*Table structure for table `user_extend` */

DROP TABLE IF EXISTS `user_extend`;

CREATE TABLE `user_extend` (
  `USR_ID` varchar(24) NOT NULL COMMENT '用户ID',
  `COM_ID` varchar(24) DEFAULT NULL COMMENT '社区ID',
  `USR_NICKNAME` varchar(50) NOT NULL COMMENT '用户昵称',
  `USR_AVATAR` varchar(24) DEFAULT NULL COMMENT '用户头像(关联到Attachment表)',
  `USR_PHONE` varchar(50) DEFAULT NULL COMMENT '用户手机',
  `USR_ODR_NAME` varchar(24) DEFAULT NULL COMMENT '记录用户订单名称',
  `USR_ODR_PHONE` varchar(24) DEFAULT NULL COMMENT '记录用户订单电话',
  `USR_ODR_ADDRESS` varchar(100) DEFAULT NULL COMMENT '记录用户订单地址',
  `USR_SCORE` int(11) DEFAULT NULL COMMENT '用户积分',
  `LAST_BUY_DT` datetime DEFAULT NULL COMMENT '上一次购买时间',
  `USR_DEVICE_TYPE` int(2) DEFAULT NULL COMMENT '用户登录设备类型',
  `USR_DEVICE_SER_NO` varchar(64) DEFAULT NULL COMMENT '用户登录设备序列号',
  `OPEN_SHOP_IND` int(1) DEFAULT '1' COMMENT '是否申请开店(1=未申请,2=已申请开店)',
  `SOP_ID` varchar(24) DEFAULT NULL COMMENT '店铺ID',
  PRIMARY KEY (`USR_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;



/*************************修改店铺默认营业时间******************************************************/
ALTER TABLE `lifestyle_2.0`.`ma_shop` CHANGE `SOP_OPEN_START_TIME` `SOP_OPEN_START_TIME` VARCHAR(5) CHARSET utf8 COLLATE utf8_general_ci DEFAULT '00:00' NULL COMMENT '营业开始时间(格式HH:mm)', CHANGE `SOP_OPEN_END_TIME` `SOP_OPEN_END_TIME` VARCHAR(5) CHARSET utf8 COLLATE utf8_general_ci DEFAULT '23:59' NULL COMMENT '营业结束时间(格式HH:mm)';
