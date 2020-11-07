#Find the longest common prefix string amongst an array of strings.

def longestCommonPrefix(strs):
    """
    type(strs): List[str]
    """
    strs.sort()						#first we sort the list. So for ["flower","flow","flight"], sorted list will be ["flight","flow","flower"]
    prefix =''						#initialize as empty string
    i=0
    if len(strs)==0:
        return(prefix)
    str1= strs[0]					#take the 1st element of list i.e. "flight"
    str2 =strs[-1]					#take the last element of list i.e. "flower"
    len1=len(str1)
    len2=len(str2)
        
    while (i<len1 and i<len2):
        if str1[i]!=str2[i]:		#start from comparing character of 0th index of both elements till characters don't match. Break then. For "flight" and flower", cosider 'f','l' and then next chars don't match so break out of loop. 
            break
        prefix+= str1[i]			#store matching characters in prefix 
            
        i+=1
    return (prefix)
print(longestCommonPrefix(["flower","flow","flight"])) #test