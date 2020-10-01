class Mylist:
def __init__ ( self ,List):
self .mylist=List
def __add__ ( self ,other):
for i in other.mylist:
self .mylist.append(i)
def display( self ):
print ( "Mylist: " , self .mylist)
l= list ( map ( int , input ( "Enter list with space as delimiter" ).split()))
obj=Mylist(l)
print ( "Before adding" )
obj.display()
l2= list ( map ( int , input ( "Enter additional elements" ).split()))
obj+Mylist(l2)
print ( "After adding" )
obj.display()
