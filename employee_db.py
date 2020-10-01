mport sqlite3
conn=sqlite3.connect("data.db")
conn.execute('''CREATE TABLE EMP (ID INT PRIMARY KEY ,E_NAME TEXT NOT
NULL,SALARY REAL)''')
conn.execute('''INSERT INTO EMP (ID,E_NAME,SALARY) VALUES(1,"RAM",58000)''')
conn.execute('''INSERT INTO EMP (ID,E_NAME,SALARY) VALUES(2,"UJJWAL",50000)''')
conn.execute('''INSERT INTO EMP (ID,E_NAME,SALARY) VALUES(3,"GEETA",55000)''')
conn.execute('''INSERT INTO EMP (ID,E_NAME,SALARY) VALUES(4,"SITA",3000)''')
cur=conn.execute('''SELECT * FROM EMP WHERE SALARY>50000''')
HOD, Dept. of CSE
for row in cur:
print("ID :",row[0]," E_NAME:", row[1]," SALARY:" ,row[2])
