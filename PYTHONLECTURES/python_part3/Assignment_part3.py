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

# tup = (1, 2, 3, 4, 5, 6, 7, 8)

# even=()
# odd=()

# for val in tup:
#     if(val%2==0):
#         even+=(val,)
#     else:
#         odd+=(val,) 

# print(even)
# print(odd)
          
#Q5
students = {}

while True:
    print("\n----- Student Management System -----")
    print("A. Add a student")
    print("B. Update marks")
    print("C. Search for a student")
    print("D. Display all students and marks")
    print("E. Exit")

    choice = input("Enter your choice: ").upper()

    if choice == 'A':
        name = input("Enter student name: ")
        marks = int(input("Enter marks: "))

        students[name] = marks
        print("Student added successfully!")

    elif choice == 'B':
        name = input("Enter student name: ")

        if name in students:
            marks = int(input("Enter updated marks: "))
            students[name] = marks
            print("Marks updated successfully!")
        else:
            print("Student not found!")

    elif choice == 'C':
        name = input("Enter student name: ")

        if name in students:
            print(f"{name} obtained {students[name]} marks")
        else:
            print("Student not found!")

    elif choice == 'D':
        if students:
            for name, marks in students.items():
                print(f"Student: {name}, Marks: {marks}")
        else:
            print("No student records found!")

    elif choice == 'E':
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")