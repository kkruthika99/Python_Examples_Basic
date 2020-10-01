def main():
try :
number1, number2 = eval ( input ( "Enter two numbers, separated by a comma: " ))
result = number1 / number2
print ( "Result is " + str (result))
ages = { 'a' : 30 , 'b' : 28 , 'd' : 33 }
k = input ( "enter a key in dictionary" )
print (ages[k])
l = [ 1 , 2 , 3 , 4 , 5 ]
z = int ( input ( "enter the index of list" ))
print (l[z])
k = int ( input ( "enter a number" ))
print (k)
except ValueError :
print ( "value error handled" )
except ZeroDivisionError :
print ( "Division by zero!" )
except SyntaxError :
print ( "A comma may be missing in the input" )
except KeyError :
print ( "key error handled" )
except IndexError :
print ( "index wrong " )
else :
print ( "No exceptions" )
finally :
print ( "The finally clause is executed" )
main()
