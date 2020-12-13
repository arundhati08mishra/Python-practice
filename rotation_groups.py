'''
A rotation group for a string contains all of its unique rotations. For example, "abc" can be rotated to "bca" and "cab" and they are all in the same rotation group.

Question: Given a list of strings words return the total number of groups.

Note: "abc" and "bac" contain same letters and when sorted become "abc" but they don't belong to the same rotation group. 
Because we can't rotate "abc" to become "bac" in any way.
Hence, simply sorting them cannot give us the result.

Approach:
Add all possible rotations of a word in a set. 
Check if the next word exists in the set, if not increase the count and add all possible rotations of this word to the set also.
'''

def solve(words):
	s=set()
	groups=0
	for i in words:
		if i not in s: 
			groups+=1 #increase count of groups when word is not in the set
			for j in range(len(i)): 
				s.add(i[j:]+i[:j]) #add all possible rotations of that word to the set. For ex:if word="the": when j=0, add "the", when j=1, add he+t=het, when j=2 add e+th=eth. That is all possible rotation sof the word "the." 
	return groups
print(solve(["abc", "xy", "yx", "z", "bca"]))
print(solve(["abc","bac", "bca"]))


