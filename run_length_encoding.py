str1 = 'aaaabbbcccca'
enc_str='' #string to store encoding
current= str1[0] #1st character
count= 0
for i in str1:
  if i == current:
    count += 1 #increase count 
  else:
    enc_str += current + str(count) #if different character encountered then store previous char and its count
    current=i #change current to present character
    count =1 #inialize count as 1
enc_str += current + str(count) #for the last character
print(enc_str) 