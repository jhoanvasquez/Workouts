-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Versión del servidor:         10.1.36-MariaDB - mariadb.org binary distribution
-- SO del servidor:              Win32
-- HeidiSQL Versión:             9.3.0.4984
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

-- Volcando estructura de base de datos para workout
CREATE DATABASE IF NOT EXISTS `workout` /*!40100 DEFAULT CHARACTER SET latin1 */;
USE `workout`;


-- Volcando estructura para tabla workout.auth_group
CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.auth_group: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;


-- Volcando estructura para tabla workout.auth_group_permissions
CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.auth_group_permissions: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;


-- Volcando estructura para tabla workout.auth_permission
CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.auth_permission: ~32 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
	(1, 'Can add log entry', 1, 'add_logentry'),
	(2, 'Can change log entry', 1, 'change_logentry'),
	(3, 'Can delete log entry', 1, 'delete_logentry'),
	(4, 'Can view log entry', 1, 'view_logentry'),
	(5, 'Can add permission', 2, 'add_permission'),
	(6, 'Can change permission', 2, 'change_permission'),
	(7, 'Can delete permission', 2, 'delete_permission'),
	(8, 'Can view permission', 2, 'view_permission'),
	(9, 'Can add group', 3, 'add_group'),
	(10, 'Can change group', 3, 'change_group'),
	(11, 'Can delete group', 3, 'delete_group'),
	(12, 'Can view group', 3, 'view_group'),
	(13, 'Can add user', 4, 'add_user'),
	(14, 'Can change user', 4, 'change_user'),
	(15, 'Can delete user', 4, 'delete_user'),
	(16, 'Can view user', 4, 'view_user'),
	(17, 'Can add content type', 5, 'add_contenttype'),
	(18, 'Can change content type', 5, 'change_contenttype'),
	(19, 'Can delete content type', 5, 'delete_contenttype'),
	(20, 'Can view content type', 5, 'view_contenttype'),
	(21, 'Can add session', 6, 'add_session'),
	(22, 'Can change session', 6, 'change_session'),
	(23, 'Can delete session', 6, 'delete_session'),
	(24, 'Can view session', 6, 'view_session'),
	(25, 'Can add user model', 7, 'add_usermodel'),
	(26, 'Can change user model', 7, 'change_usermodel'),
	(27, 'Can delete user model', 7, 'delete_usermodel'),
	(28, 'Can view user model', 7, 'view_usermodel'),
	(29, 'Can add habilidades user', 8, 'add_habilidadesuser'),
	(30, 'Can change habilidades user', 8, 'change_habilidadesuser'),
	(31, 'Can delete habilidades user', 8, 'delete_habilidadesuser'),
	(32, 'Can view habilidades user', 8, 'view_habilidadesuser');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;


-- Volcando estructura para tabla workout.auth_user
CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.auth_user: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
	(1, 'pbkdf2_sha256$216000$O1imED2QjdPI$fQ2sP+I/wDxAtVDkzhGg/wYLe+nldjrMxlhIFB9w8dg=', '2021-03-10 02:16:19.016354', 1, 'admin', '', '', 'jhoan0498@gmail.com', 1, 1, '2021-03-10 02:16:04.951835');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;


-- Volcando estructura para tabla workout.auth_user_groups
CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.auth_user_groups: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;


-- Volcando estructura para tabla workout.auth_user_user_permissions
CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.auth_user_user_permissions: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;


-- Volcando estructura para tabla workout.django_admin_log
CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.django_admin_log: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;


-- Volcando estructura para tabla workout.django_content_type
CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.django_content_type: ~8 rows (aproximadamente)
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
	(1, 'admin', 'logentry'),
	(3, 'auth', 'group'),
	(2, 'auth', 'permission'),
	(4, 'auth', 'user'),
	(5, 'contenttypes', 'contenttype'),
	(6, 'sessions', 'session'),
	(8, 'Users', 'habilidadesuser'),
	(7, 'Users', 'usermodel');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;


-- Volcando estructura para tabla workout.django_migrations
CREATE TABLE IF NOT EXISTS `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.django_migrations: ~19 rows (aproximadamente)
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
	(1, 'Users', '0001_initial', '2021-03-10 01:02:43.337165'),
	(2, 'contenttypes', '0001_initial', '2021-03-10 01:02:45.736302'),
	(3, 'auth', '0001_initial', '2021-03-10 01:02:48.674470'),
	(4, 'admin', '0001_initial', '2021-03-10 01:03:03.059293'),
	(5, 'admin', '0002_logentry_remove_auto_add', '2021-03-10 01:03:05.978460'),
	(6, 'admin', '0003_logentry_add_action_flag_choices', '2021-03-10 01:03:06.095466'),
	(7, 'contenttypes', '0002_remove_content_type_name', '2021-03-10 01:03:07.836566'),
	(8, 'auth', '0002_alter_permission_name_max_length', '2021-03-10 01:03:09.457659'),
	(9, 'auth', '0003_alter_user_email_max_length', '2021-03-10 01:03:10.854739'),
	(10, 'auth', '0004_alter_user_username_opts', '2021-03-10 01:03:10.921742'),
	(11, 'auth', '0005_alter_user_last_login_null', '2021-03-10 01:03:11.794792'),
	(12, 'auth', '0006_require_contenttypes_0002', '2021-03-10 01:03:11.850796'),
	(13, 'auth', '0007_alter_validators_add_error_messages', '2021-03-10 01:03:11.915799'),
	(14, 'auth', '0008_alter_user_username_max_length', '2021-03-10 01:03:13.135869'),
	(15, 'auth', '0009_alter_user_last_name_max_length', '2021-03-10 01:03:14.841967'),
	(16, 'auth', '0010_alter_group_name_max_length', '2021-03-10 01:03:16.652070'),
	(17, 'auth', '0011_update_proxy_permissions', '2021-03-10 01:03:16.784078'),
	(18, 'auth', '0012_alter_user_first_name_max_length', '2021-03-10 01:03:18.026149'),
	(19, 'sessions', '0001_initial', '2021-03-10 01:03:18.634184');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;


-- Volcando estructura para tabla workout.django_session
CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.django_session: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
	('vecbbucrgk04e8mgjdfyhnc86oz7rbic', '.eJxVjEEOwiAQRe_C2pCBFtq6dO8ZyMDMSNVAUtqV8e7apAvd_vfef6mA25rD1ngJM6mzMur0u0VMDy47oDuWW9WplnWZo94VfdCmr5X4eTncv4OMLX_rUToDHSaXDBknZooOMYofLAr0ETyPbMEPHcAEBBMRsfRCvRiiZFm9P-yROKg:1lJoOc:qpF6fHUzY3r870jHOx0-fumZti5eiDeHcPFOGq5uDg0', '2021-03-24 02:16:22.590559'),
	('ze8dbvudibvw8kaahldwux6s3tj39g8u', '.eJxVjEEOwiAQRe_C2pCBFtq6dO8ZyMDMSNVAUtqV8e7apAvd_vfef6mA25rD1ngJM6mzMur0u0VMDy47oDuWW9WplnWZo94VfdCmr5X4eTncv4OMLX_rUToDHSaXDBknZooOMYofLAr0ETyPbMEPHcAEBBMRsfRCvRiiZFm9P-yROKg:1lJoOc:qpF6fHUzY3r870jHOx0-fumZti5eiDeHcPFOGq5uDg0', '2021-03-24 02:16:22.407548');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;


-- Volcando estructura para tabla workout.users_habilidadesuser
CREATE TABLE IF NOT EXISTS `users_habilidadesuser` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `resistencia` int(11) NOT NULL,
  `fuerza` int(11) NOT NULL,
  `velocidad` int(11) NOT NULL,
  `aceleración` int(11) NOT NULL,
  `Agilidad` int(11) NOT NULL,
  `flexibilidad` int(11) NOT NULL,
  `coordinación` int(11) NOT NULL,
  `precisión` int(11) NOT NULL,
  `user_id_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `Users_habilidadesuser_user_id_id_8ed01698_fk_Users_usermodel_id` (`user_id_id`),
  CONSTRAINT `Users_habilidadesuser_user_id_id_8ed01698_fk_Users_usermodel_id` FOREIGN KEY (`user_id_id`) REFERENCES `users_usermodel` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.users_habilidadesuser: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `users_habilidadesuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `users_habilidadesuser` ENABLE KEYS */;


-- Volcando estructura para tabla workout.users_usermodel
CREATE TABLE IF NOT EXISTS `users_usermodel` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nombre` varchar(20) NOT NULL,
  `apellido` varchar(20) NOT NULL,
  `edad` int(11) NOT NULL,
  `genero` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(20) NOT NULL,
  `pais` varchar(20) NOT NULL,
  `region` varchar(20) NOT NULL,
  `ciudad` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

-- Volcando datos para la tabla workout.users_usermodel: ~1 rows (aproximadamente)
/*!40000 ALTER TABLE `users_usermodel` DISABLE KEYS */;
INSERT INTO `users_usermodel` (`id`, `nombre`, `apellido`, `edad`, `genero`, `email`, `password`, `pais`, `region`, `ciudad`) VALUES
	(1, 'prueba', 'prueba', 20, 'masculino', 'jhoan0498@gmail.com', '123jh', 'prueba', 'prueba', 'prueba');
/*!40000 ALTER TABLE `users_usermodel` ENABLE KEYS */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
