'''
Vernam cipher uses a key of the same length of message for encryption. Explanation of Vernam cipher:
EX: Message ="HELLO" Key = "MXCKL". The numerical values of corresponding message and key letters (A->0 B->1) are added together and then modulo 26. 
7(H) 4(E) 11(L) 11(L) 14(O) message 
+ 12(M) 23(X) 2(C) 10(K) 11(L) key
= 19 27 13 21 25 message + key
= 19() 1(B) 13(N) 21(V) 25(Z) (message + key) mod 26 
T B N V Z → ciphertext 

'''
#Encryption
msg = input('Enter message:   ')
msg= msg.upper()
key = input('Enter key:   ')
key = key.upper()
if len(key)!=len(msg):
  print('Length of key and msg should be equal')

msg_lst = [ord(i)-65 for i in msg] #The ord() function returns the number representing the unicode code of the character passed. We then substract by 65. For ex ord('B')=66.  66-65=1. 
key_lst = [ord(i)-65 for i in key]

cipher_lst = []
for i in range(len(msg_lst)):
  cipher_lst.append(chr ( ( (msg_lst[i]+ key_lst[i])%26) + 65 )) #Message + key % 26 gives us the numbers. Add the number by 65 to get unicode represntation. Then using chr() function convert unicode to char.

cipher_txt = (''.join(cipher_lst)) #convert the list to string

print("Encrypted message is:   ", cipher_txt) #Encrypted message

#Decryption:
dec_lst=[]

for i in range(len(cipher_lst)):
  int1 = (ord(cipher_lst[i])- 65) - key_lst[i]
  if int1<0:
    int1+=26
  dec_lst.append( chr( (int1%26)+65))

dec_txt = ''.join(dec_lst)
print("Decrypted message is:    ", dec_txt)