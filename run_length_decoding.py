'''
Given an encoded string where each character is followed by its frequency (run length encoding), decode to orignal string.
'''
'''
Method 1: When the frequency is 1 digit only
str1 = 'a2b3c4a1'
dec_str=''
for i in range(0,len(str1),2): #loop over even index as they contain char
  res+= str1[i]*int(str1[i+1]) # char * their frequency
print(dec_str)
'''

# Method 2: Above method only worked if freq. was single digit. What if 'a10' was there?
str1 ='a10b3c4a1'
freq = 0 
current = str1[0] # initially take current as the 1st value 
dec_str=''
for i in range(len(str1)): 
  if str1[i].isdigit(): #if element is digit
    freq = freq * 10 + int(str1[i]) # at index 1: freq = 0*10+1=1. At index 2: freq=1*10+0=10. 
  else: #else if element is char
    dec_str += current * freq # char*freq
    freq = 0 # reset freq to 0
    current = str1[i] 

dec_str += current * freq #for the last char

print(dec_str)


