class withdrawError( Exception ):
pass
HOD, Dept. of CSE
class depositError( Exception ):
pass
class Circle:
def __init__ ( self , balance = 500 ):
try :
if balance< 500 :
raise depositError
else :
self .b = balance
print ( "the balance is " , self .b)
except depositError:
print ( "the balance cannot be less than 500" )
def deposit( self , a):
self .b+=a
print ( "deposited amount" , self .b)
def withdraw( self ,k):
try :
if k> 20000 :
raise withdrawError
else :
self .b-=k
print ( "withdrawed" )
except withdrawError:
print ( "cant withdraw ore than 20000" )
def display( self ):
print ( self .b)
c1 = Circle( 5 )
c1 = Circle( 5000 )
c1.deposit( 10000 )
c1.withdraw( 100000 )
c1.withdraw( 100 )
c1.display()
