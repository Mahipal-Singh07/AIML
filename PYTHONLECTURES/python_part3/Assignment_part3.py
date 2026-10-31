# pal_str=input("enter a str :")

# is_palindrome=True
# for i in range(len(pal_str)):
#     if(pal_str[i] != pal_str[len(pal_str)-1-i]):
#         is_palindrome=False
#         break
# if is_palindrome:
#     print("Palindrome")
# else:
#     print("Not a palindrome")

#Q2
# nums=[1,2,3,4,5,6]

# sum=0
# for val in nums:
#     sum+=val
# avg=sum/len(nums)
# print(f"avg of nums of list is {avg}")

#Q3
# nums1 = []

# n1 = int(input("Enter number of elements for list1: "))

# for i in range(n1):
#     val = int(input("Enter element: "))
#     nums1.append(val)

# nums2=[]
# n2=int(input("Enter number of elements for list2: "))

# for i in range(n2):
#     val=int(input("enter element:"))
#     nums2.append(val)

# nums3=[]
# nums3=nums1+nums2

# nums3.sort()
# print(nums3)

#Q4

tup = (1, 2, 3, 4, 5, 6, 7, 8)

even=()
odd=()

for val in tup:
    if(val%2==0):
        even+=(val,)
    else:
        odd+=(val,) 

print(even)
print(odd)
          
