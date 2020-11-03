#Given a 32-bit signed integer, reverse digits of an integer i.e. Range: [−2^31,  2^31 − 1].
def reverse_number(x):
        """
        type(x): int
        """
        rev = int(str(abs(x))[::-1]) #rev will store reverse of absolute value of the x i.e. if x = -123, abs(x)= 123 and rev=321
        
        if rev < -2**31 or rev > 2**31-1: #return 0 when reversed integer out of specified range. 
            return 0
        
        else:
            if x <  0: return -rev #add -ve sign if x was negative.
            if x >= 0: return rev
print(reverse_number(-1112))
