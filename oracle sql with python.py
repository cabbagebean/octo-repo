import cx_Oracle

conStr='system/carefree@localhost:1521/xepdb1'
#create a connection object
conn=cx_Oracle.connect(conStr)
#get a cursor object from the connection
cur = conn.cursor()

#delete table rows

#sqlTxt='delete from "CEN434".STUDENT_INFO (MATNO, NAME, PROGRAMME, ROOMNO, AGE)  values (:1, :2, :3, :4, :5)'

#update table rows
#sqlTxt='update "CEN434".STUDENT_INFO set NAME=:1 where NAME=:2'
#cur.execute(sqlTxt,("Bukola Scott","Ajayi Davies"))

#insert table rows
#sqlTxt='insert into "CEN434".STUDENT_INFO (MATNO, NAME, PROGRAMME, ROOMNO, AGE)  values (:1, :2, :3, :4, :5)'

#cur.execute(sqlTxt,('20CL023456','Pete Davidson','MassComm', 'F205', '22'))
#IF MATNO IS NOT UNIQUE CODE WON'T RUN BECAUSE IT WAS SET AS A PRIMARY KEY
conn.commit()

cur.close()
#close the cursor object to avoid memory leaks
conn.close()
#close the connection  object also