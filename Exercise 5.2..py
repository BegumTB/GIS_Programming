>>> def check_fermat (a,b,c,d,n):
	if n > 2 and (a**n + b**n == c**n):
		print ("Holy smokes, Fermat was wrong!")
	else:
		print ("No, that doesn’t work.")

		
>>> a= int (input("Pick a value for a "))
Pick a value for a 5
>>> b= int (input("Pick a value for b "))
Pick a value for b 10
>>> c= int (input("Pick a value for c "))
Pick a value for c 7
>>> d= int (input("Pick a value for d "))
Pick a value for d 8
>>> n=2
>>> 
>>> print (check_fermat (a,b,c,d,n))
No, that doesn’t work.
None
>>> 
