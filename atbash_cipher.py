'''
You are given a lowercase alphabet string text. Return a new string where every character in text is mapped to its reverse in the alphabet, so that a becomes z, b becomes y, c becomes x, and so on.

'''
srt1 = ord('a')+ord('z') 
        return ''.join([chr(srt1 - ord(i)) for i in text]) 