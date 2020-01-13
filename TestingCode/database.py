""" other way to connect to azure sql database without sqlalchemy"""

# import pyodbc
# server = 'facerec.database.windows.net'
# database = 'FaceRec'
# username = 'projectIV'
# password = 'Project4'
# driver= '{ODBC Driver 13 for SQL Server}'
# cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()
# cursor.execute("SELECT * FROM test")
# row = cursor.fetchone()
# while row:
#     print (str(row[0]) + " " + str(row[1]))
#     row = cursor.fetchone()


# print ('Inserting a new row into table')
# #Insert Query
# tsql = "INSERT INTO Employees (Name, Location) VALUES (?,?);"
# with cursor.execute(tsql,'Jake','United States'):
#     print ('Successfully Inserted!')

# #Update Query
# print ('Updating Location for Nikita')
# tsql = "UPDATE Employees SET Location = ? WHERE Name = ?"
# with cursor.execute(tsql,'Sweden','Nikita'):
#     print ('Successfully Updated!')


# #Delete Query
# print ('Deleting user Jared')
# tsql = "DELETE FROM Employees WHERE Name = ?"
# with cursor.execute(tsql,'Jared'):
#     print ('Successfully Deleted!')


#Select Query
# print ('Reading data from table')
# tsql = "SELECT * FROM test;"
# with cursor.execute(tsql):
#     row = cursor.fetchone()
#     while row:
#         print (str(row[0]) + " " + str(row[1]))
#         row = cursor.fetchone()