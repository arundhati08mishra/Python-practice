'''
Question : ROTATE LIST  by k
Given a list of numbers and an integer k, rotate the list to the left by k elements such that numbers wrap around.

For example, [1, 2, 3, 4, 5, 6] rotated by 3 becomes [4, 5, 6, 1, 2,3].

Note: The list is guaranteed to have at least one element, and k is guaranteed to be less than or equal to the length of the list.
'''
nums = [1,2,3,4,5,6]
k=3
print(nums[k:] + nums[:k]) #if k =3, print elements after 2nd index i.e. from 3rd index till last. And then concat with the numbers till k.