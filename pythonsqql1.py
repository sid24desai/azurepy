import pyodbc
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};''SERVER=tcp:siliconserver09.database.windows.net,1433;''DATABASE=silicondb; UID=siliconserver;PWD=Watermelon@123;')
#conn.commit()
cursor = conn.cursor()
cursor.execute('Select * FROM StudentReviews')
#conn.commit()
for  i  in  cursor:
 print(i)
cursor.close()
conn.close()