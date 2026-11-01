# class BankAccount:
#     def __init__(self,account_number,owner_name,balance):
#         self.account_number=account_number
#         self.owner_name=owner_name
#         self.balance=balance

#     def deposit(self,amount):
#         self.balance+=amount
#         return self.balance
    
#     def withdrawal(self,amount):
#        if(amount<=self.balance):
#         self.balance-=amount
#         return self.balance
#        else:
#           return "Insufficient Balance"

#     def check_balance(self):
#         return self.balance


# B1=BankAccount(100,"Mahipal",100000)
# print(B1.deposit(50000))   
# print(B1.withdrawal(20000))
# print(B1.check_balance()) 


#Q2

# class Book:

#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#         self.reviews = []

#     def add_review(self,review):
#         self.reviews.append(review)  

#     def count_reviews(self):
#            return len(self.reviews)

#     def display_reviews(self):
#          for review in self.reviews:
#               print(review)


# B1 = Book("The Alchemist", "Paulo Coelho")

# B1.add_review("Very interesting book")
# B1.add_review("Excellent story")
# B1.add_review("Must read book")

# print("Book:", B1.title)
# print("Author:", B1.author)

# print("Total Reviews:", B1.count_reviews())

# print("All Reviews:")
# B1.display_reviews()

#Q3
# class Student:
#     def __init__(self, name, roll_no, marks):
#         self._name = name
#         self._roll_no = roll_no
#         self._marks = marks

#     # Name setter
#     def set_name(self, name):
#         if name.strip() != "":
#             self._name = name
#         else:
#             print("Name cannot be empty")

#     # Roll number setter
#     def set_roll_no(self, roll_no):
#         if 1 <= roll_no <= 100:
#             self._roll_no = roll_no
#         else:
#             print("Roll number must be between 1 and 100")

#     # Marks setter
#     def set_marks(self, marks):
#         if marks >= 0:
#             self._marks = marks
#         else:
#             print("Marks cannot be negative")

#     # Getter methods
#     def get_name(self):
#         return self._name

#     def get_roll_no(self):
#         return self._roll_no

#     def get_marks(self):
#         return self._marks


# # Object creation
# s1 = Student("Mahipal", 10, 85)

# print("Name:", s1.get_name())
# print("Roll No:", s1.get_roll_no())
# print("Marks:", s1.get_marks())

# # Updating values
# s1.set_name("Rahul")
# s1.set_roll_no(50)
# s1.set_marks(90)

# print("\nUpdated Details:")
# print("Name:", s1.get_name())
# print("Roll No:", s1.get_roll_no())
# print("Marks:", s1.get_marks())
  

#Q4
class Shape:
    def area(self):
        pass


# Circle subclass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# Rectangle subclass
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth


# Triangle subclass
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


# Creating objects
c = Circle(5)
r = Rectangle(10, 5)
t = Triangle(8, 6)

print("Circle Area:", c.area())
print("Rectangle Area:", r.area())
print("Triangle Area:", t.area())