BEGIN TRANSACTION;
CREATE TABLE "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(80) NOT NULL UNIQUE);
CREATE TABLE "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("group_id", "permission_id"));
CREATE TABLE "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(50) NOT NULL, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id"), "codename" varchar(100) NOT NULL, UNIQUE ("content_type_id", "codename"));
INSERT INTO "auth_permission" VALUES(1,'Can add log entry',1,'add_logentry');
INSERT INTO "auth_permission" VALUES(2,'Can change log entry',1,'change_logentry');
INSERT INTO "auth_permission" VALUES(3,'Can delete log entry',1,'delete_logentry');
INSERT INTO "auth_permission" VALUES(4,'Can add permission',2,'add_permission');
INSERT INTO "auth_permission" VALUES(5,'Can change permission',2,'change_permission');
INSERT INTO "auth_permission" VALUES(6,'Can delete permission',2,'delete_permission');
INSERT INTO "auth_permission" VALUES(7,'Can add group',3,'add_group');
INSERT INTO "auth_permission" VALUES(8,'Can change group',3,'change_group');
INSERT INTO "auth_permission" VALUES(9,'Can delete group',3,'delete_group');
INSERT INTO "auth_permission" VALUES(10,'Can add user',4,'add_user');
INSERT INTO "auth_permission" VALUES(11,'Can change user',4,'change_user');
INSERT INTO "auth_permission" VALUES(12,'Can delete user',4,'delete_user');
INSERT INTO "auth_permission" VALUES(13,'Can add content type',5,'add_contenttype');
INSERT INTO "auth_permission" VALUES(14,'Can change content type',5,'change_contenttype');
INSERT INTO "auth_permission" VALUES(15,'Can delete content type',5,'delete_contenttype');
INSERT INTO "auth_permission" VALUES(16,'Can add session',6,'add_session');
INSERT INTO "auth_permission" VALUES(17,'Can change session',6,'change_session');
INSERT INTO "auth_permission" VALUES(18,'Can delete session',6,'delete_session');
INSERT INTO "auth_permission" VALUES(19,'Can add image list',7,'add_imagelist');
INSERT INTO "auth_permission" VALUES(20,'Can change image list',7,'change_imagelist');
INSERT INTO "auth_permission" VALUES(21,'Can delete image list',7,'delete_imagelist');
INSERT INTO "auth_permission" VALUES(22,'Can add csv import',8,'add_csvimport');
INSERT INTO "auth_permission" VALUES(23,'Can change csv import',8,'change_csvimport');
INSERT INTO "auth_permission" VALUES(24,'Can delete csv import',8,'delete_csvimport');
INSERT INTO "auth_permission" VALUES(25,'Can add import model',9,'add_importmodel');
INSERT INTO "auth_permission" VALUES(26,'Can change import model',9,'change_importmodel');
INSERT INTO "auth_permission" VALUES(27,'Can delete import model',9,'delete_importmodel');
CREATE TABLE "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NOT NULL, "is_superuser" bool NOT NULL, "username" varchar(30) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "email" varchar(75) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL);
INSERT INTO "auth_user" VALUES(1,'pbkdf2_sha256$15000$D6RAKWwA8xeR$idHxBrIUtomp2H3MfOcKcaP1WKWG0gbpsCzDKm2wSjM=','2015-02-03 03:08:25.748543',1,'anne','','','',1,1,'2015-02-03 03:06:51.418930');
CREATE TABLE "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "group_id" integer NOT NULL REFERENCES "auth_group" ("id"), UNIQUE ("user_id", "group_id"));
CREATE TABLE "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id"), "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id"), UNIQUE ("user_id", "permission_id"));
CREATE TABLE "csvimport_csvimport" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "model_name" varchar(255) NOT NULL,
    "field_list" varchar(255) NOT NULL,
    "upload_file" varchar(100) NOT NULL,
    "file_name" varchar(255) NOT NULL,
    "encoding" varchar(32) NOT NULL,
    "upload_method" varchar(50) NOT NULL,
    "error_log" text NOT NULL,
    "import_date" date NOT NULL,
    "import_user" varchar(255) NOT NULL
);
CREATE TABLE "csvimport_importmodel" (
    "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "csvimport_id" integer NOT NULL REFERENCES "csvimport_csvimport" ("id"),
    "numeric_id" integer unsigned NOT NULL,
    "natural_key" varchar(100) NOT NULL
);
CREATE TABLE "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "action_flag" smallint unsigned NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id"), "user_id" integer NOT NULL REFERENCES "auth_user" ("id"));
CREATE TABLE "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL, UNIQUE ("app_label", "model"));
INSERT INTO "django_content_type" VALUES(1,'log entry','admin','logentry');
INSERT INTO "django_content_type" VALUES(2,'permission','auth','permission');
INSERT INTO "django_content_type" VALUES(3,'group','auth','group');
INSERT INTO "django_content_type" VALUES(4,'user','auth','user');
INSERT INTO "django_content_type" VALUES(5,'content type','contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES(6,'session','sessions','session');
INSERT INTO "django_content_type" VALUES(7,'image list','get_img','imagelist');
INSERT INTO "django_content_type" VALUES(8,'csv import','csvimport','csvimport');
INSERT INTO "django_content_type" VALUES(9,'import model','csvimport','importmodel');
CREATE TABLE "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO "django_migrations" VALUES(1,'contenttypes','0001_initial','2015-02-03 03:05:54.260987');
INSERT INTO "django_migrations" VALUES(2,'auth','0001_initial','2015-02-03 03:05:54.592207');
INSERT INTO "django_migrations" VALUES(3,'admin','0001_initial','2015-02-03 03:05:54.860385');
INSERT INTO "django_migrations" VALUES(4,'sessions','0001_initial','2015-02-03 03:05:55.070525');
INSERT INTO "django_migrations" VALUES(5,'get_img','0001_initial','2015-02-03 04:28:03.791672');
INSERT INTO "django_migrations" VALUES(6,'get_img','0002_imagelist_imageorder','2015-02-04 10:06:11.350095');
INSERT INTO "django_migrations" VALUES(7,'get_img','0003_imagelist_imagekeyword','2015-02-04 15:26:14.531023');
INSERT INTO "django_migrations" VALUES(8,'get_img','0004_auto_20150204_1046','2015-02-04 15:46:50.770744');
CREATE TABLE "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
INSERT INTO "django_session" VALUES('jrz5xs7awjo22pqxwtfbzupkz8di9rgt','NDdhOWI2NDRjNGRmYzg2MDgzNmJkNDk3ZjBiY2QzYjU5ZTVlNWNkYTp7Il9hdXRoX3VzZXJfaGFzaCI6IjEyMWY0NmMyNDEzMzRlN2I3YjMxYmMxZWU2NGM0ZGM2NjBmNWY1ZGQiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOjF9','2015-02-17 03:08:25.895640');
INSERT INTO "django_session" VALUES('gcuipfwz6aethz0lxrz2li9bwpuvlxw6','NjJlYWMyOTRiNDNhZjIzMTVkOWZiYTQ1NmM5MWJmN2IzN2M5YTJjMjp7fQ==','2015-02-17 03:08:26.130797');
CREATE TABLE "get_img_imagelist" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "ImageOrder" integer NOT NULL, "ImageURL" varchar(300) NOT NULL, "ImageREF" varchar(300) NOT NULL, "ImageTitle" varchar(200) NOT NULL, "ImageKeyword" varchar(100) NOT NULL);
INSERT INTO "get_img_imagelist" VALUES(1,9999,'sdf dfs','sdf sf','sdfsf  df','google image');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('django_content_type',9);
INSERT INTO "sqlite_sequence" VALUES('django_migrations',8);
INSERT INTO "sqlite_sequence" VALUES('auth_permission',27);
INSERT INTO "sqlite_sequence" VALUES('auth_user',1);
INSERT INTO "sqlite_sequence" VALUES('get_img_imagelist',1);
CREATE INDEX "auth_permission_417f1b1c" ON "auth_permission" ("content_type_id");
CREATE INDEX "auth_group_permissions_0e939a4f" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_8373b171" ON "auth_group_permissions" ("permission_id");
CREATE INDEX "auth_user_groups_e8701ad4" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_0e939a4f" ON "auth_user_groups" ("group_id");
CREATE INDEX "auth_user_user_permissions_e8701ad4" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_8373b171" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_417f1b1c" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_e8701ad4" ON "django_admin_log" ("user_id");
CREATE INDEX "django_session_de54fa62" ON "django_session" ("expire_date");
CREATE INDEX "csvimport_importmodel_367c7ba0" ON "csvimport_importmodel" ("csvimport_id");
COMMIT;
