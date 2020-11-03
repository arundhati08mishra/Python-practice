#ROMAN TO INTEGER

def romanToInt(s):
	'''
	type(s) : string
	'''
	numeral= {  'I': 1,		#create a dictionary for different symbols first. There are 7.
                'V': 5,
                'X': 10,
                'L': 50,
                'C': 100,
                'D' : 500,
                'M' : 1000
        }
	result = 0			#initialize variable that is going to store the int value	
	i = len(s)-1		#start from right to left. take i as the last element of s.
	while i>=0:			#traverse till the 1st index	
		current = s[i]
		if i>0:				
			prev = s[i-1]	#take previous element 
		if i>0 and numeral[current] > numeral[prev]: #for ex: IV. We take V then take I i.e. curent=V and prev=I. Compare their values from the dictionary.  
			i-=1
			result+=numeral[current] - numeral[prev] # result = numeral[V] - numeral[I] = 5-1= 4
		else:										 # i.e. if current is not greater than previous. For ex: take XI
			result+=numeral[current]			     #	result = result+current value: for XI, On i=1 : result = 0+1=1. On i=0: #result=1+10=11.
		i-=1
	return(result)
print(romanToInt("VIII")) #test
