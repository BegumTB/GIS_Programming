>>> def first(word):
	return word[0]

>>> def last (word):
	return word [-1]

>>> def middle (word):
	return word[1:-1]

>>> def is_palindrome(word):
	if len(word) <= 2 and word[0] == word[-1]:
		print ("True")
	elif first(word) == last(word):
		print ("True")
	else :
		print ("False")

		
>>> is_palindrome ("word")
False
>>> is_palindrome ("begum")
False
>>> is_palindrome ("rotar")
True
>>> 
