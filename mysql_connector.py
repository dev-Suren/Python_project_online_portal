import mysql.connector
from mysql.connector import Error
try:
	myconn= mysql.connector.connect(host='localhost',user='root',password='H@ckmeifyoucan1',database='job_portal')
	mycur= myconn.cursor()
	mycur.execute("create table jobpost(application_id mediumint auto_increment not null PRIMARY KEY,role varchar(50),company_name varchar(100),min_salary int,max_salary int,compan_address varchar(250),email_address varchar(250),work_location varchar(2500),about_us varchar(2500),min_requirement varchar(2500),min_education varchar(2500),key_skills varchar(2500))")
except Error as err:
	print(err)
finally:
	if myconn.is_connected():
		mycur.close()
		myconn.close()
		print("the the table is created")