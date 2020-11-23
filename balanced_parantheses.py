'''
Program to check valid parantheses.
Given a string s:
1)Open brackets must be closed by the same type of brackets.
2)Open brackets must be closed in the correct order.
'''
def isValid(s):
    """
    :type s: str
    """
    dict1 = { "}" : "{", ")" : "(", "]" : "["} #create a dictionary to map closing brackets with same type of opening brackets
    stack=[] 
    for i in range(len(s)): 
        if s[i] not in dict1: #i.e. if they are opening brackets

            stack.append(s[i]) #append opening brackets to stack list

        else: #else if they are closing brackets
            try: #try and except incase there are more closing brackets and nothing in stackto pop
                item = stack.pop() #item=last opening bracket
                if item!=dict1[s[i]]: #if the value of s[i] i.e. the opening bracket value of s[i] != last opening bracket then the order is not correct
                    return False 
            except: 
                return False

    if len(stack)==0: 
        return True
    else:
        return False

print(isValid('{{]')) #test
print(isValid('[{}]')) #test
        