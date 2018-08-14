import mysql.connector
import os
from mysql.connector import errorcode
filename="config.txt"

def start():
	try:	
		file=open(filename,'r')
		read_config(file)
	except IOError:
		print("No File by the name of %s was found"%(filename))
		create_config_file()

def sql_db_link(line_var):
	try:
		cnx = mysql.connector.connect(user=str(line_var[0]), password=str(line_var[1]),
		host=str(line_var[2]),
		database=str(line_var[3]))
		print("Database connect!!!")
	except mysql.connector.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Something is wrong with your user name or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
		reset_config()		
	else:
		cnx.close()		
def create_config_file():
	file=open(filename,'w+')
	line_var=["Database user","Database password","Database host","Database name","Tool_ID","Tool_Name"]
	for i in range(len(line_var)):
		ans=input("Please enter the "+line_var[i]+":")
		line_var[i] =line_var[i]+":" + str(ans)
		file.write(line_var[i]+'\n')
	file.close()
	assign_var(line_var)
	

def assign_var(line_var):
	config_info=[]
	for i in range(len(line_var)):
		var=line_var[i].split(":")
		config_info.append(var[1])
		print(str(config_info[i]))
	sql_db_link(config_info)		

def read_config(file):
	holding_list=[]
	for i in file:
		i=i.rstrip('\n')
		holding_list.append(i)
	file.close()
	assign_var(holding_list)

def reset_config():
	os.remove(filename)
	create_config_file()

def main():
	start()
	#create_config_file()
	#fileinfo()

if __name__ == "__main__":	
	main()