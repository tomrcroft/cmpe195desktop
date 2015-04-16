import pypyodbc 

def sql_info():
	server = "cmt.cs87d7osvy2t.us-west-2.rds.amazonaws.com,1433"
	db = "CMT"
	username = "admin"
	password = "SJSUcmpe195"

	connection_string ="""DRIVER={{SQL Server}};SERVER={0};DATABASE={1};UID={2};PWD={3};Trusted_Connection=No;""".format(server, db, username, password)
	connection = pypyodbc.connect(connection_string)
	cur = connection.cursor()
	
	return (cur, connection)