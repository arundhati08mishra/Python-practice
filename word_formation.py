'''
Question: Given a list of strings words and a string letters, return the length of longest string in words that can be made from letters in letters.

Example:
Input:
words = ["the", "word", "love", "scott", "finder", "dictionary"]
letters = "fanierdow"

Output:	6
we can make the word finder out of letters, which has the longest length of 6.

Approach:
If all the letters of a word are present in the given letters string then the word can be made from it. 
To check this, we take frequency of all letters in the given letter string and of the word. This is done using Counter()
Then we find the intersection of these to find whether all the letters of the word are present in the string.

'''
from collections import Counter
def solve(words, letters):
	l = Counter(letters) 
	max_len = 0
	for word in words:
		w = Counter(word)
		if w == (w & l) and max_len < len(word):
			max_len = len(word)
	return max_len
print(solve(["the", "word", "love", "scott", "finder", "dictionary"], "fanierdow"))