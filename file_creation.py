Write a python program to create a file and write contents into the file. Open the file created
and count the number of words in the file.
f = open ( "l.txt" , 'w' )
con = input ( "enter the text" )
print (con)
f.write(con)
f.close()
f = open ( "l.txt" , 'r' )
data = f.read()
n = data.split()
print ( len (n))
