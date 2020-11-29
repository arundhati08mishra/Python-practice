'''
Given a string delete consecutive duplicates i.e. if a list contains repeated characters, replace with a single copy of the character. 
The order should not change.
Ex:
Input:	s = "aaaaaabbbccccaaaaddf"

Output:	"abcadf
'''
s='aaaaaabbbccccaaaaddf'
new_str ='' # to store compressed string
current = s[0] # store the 1st char in current

for i in s:
	if i!=current: #when a diff. char is encountered 
		new_str+=current #add current i.e. previous char in new_str
		current=i #change current to i
new_str+=current #for the last char
print(new_str)
