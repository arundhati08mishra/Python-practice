# divide a list into k equal parts.

l1=[1,2,3,4,5,6] #i/p list
n = 2 #number of parts
k=len(l1)//n # if no. of parts is n then length of each part = len(list)/n. Here k =3

for i in range(0, len(l1), k): # step=3. i.e. 1st iteration: i=0  then 2nd iteration: i=0+3=3
        print(l1[i:i + k]) #print from 0 till 0+3=3 so print 0th,1st,2nd index(exclude 3rd index here) Then i=3.Print till 3+3=6 So print 3rd,4th,5th index.