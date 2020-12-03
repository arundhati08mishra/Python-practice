'''
Question: Given 2 strings older and newer, both representing versions, return whether the newer is actually newer than older.


''' 
'''
I initially solved using this method:

def solve(older, newer):
	lst1 = list(map(int,older.split('.'))) #split the string when '.' is encountered and store in a list 
	lst2 = list(map(int,newer.split('.')))
	if lst2[0] > lst1[0]:
		return True
	elif lst2[0]==lst1[0] and lst2[1] > lst1[1]:
		return True
	elif lst2[0]==lst1[0] and lst2[1]== lst1[1] and lst2[2]>lst1[2]:
		return True
	return False

  '''


# But simply lists could be compared directly:
def solve(older, newer):
	lst1 = list(map(int,older.split('.'))) #split the string when '.' is encountered and store in a list 
	lst2 = list(map(int,newer.split('.')))
	return lst1 < lst2

print(solve("11.1.2", "11.1.3"))
print(solve("0.1.2", "0.2.3"))
print(solve("0.0.100", "0.0.3"))