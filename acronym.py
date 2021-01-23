'''
Queston:Given a string representing a phrase, return its acronym. Acronyms should be capitalized and should not include the word "and".

Ex:
s = "National Aeronautics and Space Administration"
Output: NASA


'''


def solve(s):
    acr = ''
    lst = s.split() #obtain individual words

    for i in lst:
        if i!='and':
            acr+=i[0].capitalize() #take 1st letter and capitalize it
    return acr
print(solve('For your information'))