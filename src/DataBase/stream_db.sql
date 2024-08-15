CREATE DATABASE StreamETL_DB;

use StreamETL_DB;

CREATE TABLE streaming (
	idStream bigint NOT NULL,
	category varchar(50) NOT NULL,
	title varchar(120) NOT NULL,
	release_year bigint NOT NULL,
  duration bigint NOT NULL,
  type_duration varchar(20) NOT NULL,
  platform  varchar(20) NOT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

CREATE TABLE gender (
  idStream bigint NOT NULL,
  genre varchar(80) NOT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;
 
CREATE TABLE actors (
  idStream bigint,
  cast varchar(120) NOT NULL
 ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_spanish_ci;

