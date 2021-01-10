'''
Given a list of strings shows, a list of integers durations, and an integer k, where shows[i] and durations[i] 
represent the name and duration watched by the ith person, return the total duration watched of the k most watched shows.

Input: shows = ["Top Gun", "Aviator", "Top Gun", "Roma", "Logan"]
durations = [5, 3, 5, 13, 4]
k = 2

Output: 23

Because the top 2 most watched movies are "Roma" and "Top Gun" for total durations of 13 and 10 = 5+ 5.

Approach: Create a dictionary where a show is mapped to its total duration. Store the durations in a list. Sort list in descending order to obtain
most watched shows first. Return sum of k most watched shows.
'''
def solve(shows, durations, k):
	dict1 = {}
	for i in range(len(shows)):
		if shows[i] in dict1:
			dict1[shows[i]]+= durations[i]
		else:
			dict1[shows[i]] = durations[i]
	lst = [val for val in dict1.values()]
	lst.sort(reverse=True)
	return sum(lst[:k])

print(solve(["Top Gun", "Aviator", "Top Gun", "Roma", "Logan"],[5, 3, 5, 13, 4],2))