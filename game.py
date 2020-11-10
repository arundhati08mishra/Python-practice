#GAME: select a random question from question list. Ask user for answer. If answer is correct, don't ask that question again, if wrong, ask that question again. All question should be asked before the game ends.
#Question and answer is in same list.
from random import randrange


question_list =['2+1:3','3+1:4','5+0:5','9+1:10'] #question is 2+1 and answer is 3


while len(question_list)>0:
#selecting a random elemenet from question list:
  random_index = randrange(len(question_list)) #select random index between 0 and len(question_list). Here b/w 0 and 4. randrange excludes end point so b/w 0 to 3.
  print(question_list[random_index].split(':')[0]) #print the question of that index. Split when ':' is encountered so we obtain a list with 2 elements. 1st element has question,2nd has answer. Print the 0th index element i.e question. 

  ans = input("enter your answer: ")
  if ans==question_list[random_index].split(':')[1]: #compare i/p answer with answer stored in list 
    print("Right answer")
    del(question_list[random_index]) #if answer if right, don't ask that question again. Therefore delete that question from list.
  else:
   print("Wrong answer")