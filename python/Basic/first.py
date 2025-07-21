# a=1
# b=2
# c=3
# d=4
# e=(a<b and c<d)
# e=(a<b or a>d)

# print(e)


# a= 'hello'+' world'
# b='hi '
# print(a)
# print(b*4)
# print(a[0])
# print(a[0:2])
# print(len(a))



# age=43

# if age<18:
#     print("under age")
# else:
#     print("upper age")
    


# marks=85
# if marks>=90:
#     print("A Gread")  #mendentation
# elif marks>=80:
#     print("B Gread")  #mendentation
# else:
#     print("C Gread") 


# a="hello"
# b="   hello world "
# c=str(input("Enter the input:"))

# print(a.upper())
# print(a.replace('h','H'))
# print(b.split())
# print(b.strip())
# print(c)


# a=int(input("Enter the first Number:"))
# b=int(input("Enter the second number:"))

# if a>b:
#     print("a is greater number")
# elif b>b:
#     print("b is greater number")
# else:
#     print("a and b are equal number")    





# marks=[7,54,6,54,7,54]
# marks.append(98)
# # print(marks)
# marks.remove(7)


# insert

# marks.insert(3,0)
# print(marks)



# sort
# x=[4,67,7,0]
# x.sort()
# print(x)
# x.sort(reverse=True)
# print(x)



# reverse 

# m=[2,5,7]
# m.reverse()
# print(m)


# Tuple is immutable

# t=(21,4,65,75,8,89)
# print(t.index(2))
# t.index(4)
# print(t)


# list=str[input("Enter the movie names:")]
# print(list)

# l=[]
# l.append(input("Enter the movie Name:"))
# l.append(input("Enter the movie Name:"))
# l.append(input("Enter the movie Name:"))
# print(l)



# palendrom

# pal=['121','tenet']
# copy=pal.copy()
# copy.reverse()
# if(copy == list):
#     print("its Palindrom")
# else:
#     print("its not palindrom")    


#Gread Count #
# g=['a','b','a','c','a','b','A','B']
# c=g.count('a')  
# print(c)

# num=[1,2,3,4,5,6]
# e_count=0
# even=[]
# odd=[]
# e_count=0
# o_count=0
# if(num %2 ==0):
#     {
#         even.append
#     }
# else:
#     {
#         odd.append
#     }
# print(odd)
# print(even)  



# stu={
#     "Name":"Karan",
#     "age":21,
#     "marks":[65,76,86]

# }


# print(stu["Name"])
# print(stu["marks"])
# stu["college"]="PVP college"
# print(stu)
# print(stu.keys())
# print(stu.items())
# print(stu.get("Name"))




# s=set()          #empty set define
# b={"c","c++",}
# s.add("c++")
# s.add("Java")
# s.add("js")
# # print(s)
# print(s.union(b))

# s={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(s))





# dir

# stu={}
# sub=int(input("Enter the 1st suject mark:"))
# stu.update({"math":sub})
# sub=int(input("Enter the 2nd suject mark:"))
# stu.update({"c++":sub})
# sub=int(input("Enter the 3rd suject mark:"))
# stu.update({"java":sub})
# print(stu)



# a=("float",9.0 )
# print(a)
# b=()










# Nested if else

# num=15
# if num>0:
#     if num % 2==0:
#         print("Positive Even Number :")
#     else:
#         print("Positive Negaive Number")
# else:
#     print("Number is not Positive ")






# Logical Operator
    
    # and Or not




# Ternary Operator   
      #Shorcut For If-else 

# a=15
# b=20
# gre= a if a>b else b
# print(gre)'








# Pass Statement

# x=10
# if x>5:
#     pass
# print("Continue With The Program")






# Leap Year Problem


# year=int(input("Enter The Year:"))

# if (year %4==0 and year % 100 !=0)or (year % 400 ==0):
#     print(year,"is a Leap year")
# else:
#     print(year,"Not leap Year")    




# In This we check the specified string


# import csv
# n="Name"
# with open("data.txt","w",newline="") as f:
#     f.write("Name")

# with open("data.txt","r") as a:
#     data=a.read()
# if n in data:
#     print("yes")
# else:
#     print("no")
 


# Number Swaping 


# a = 10
# b = 5

# a = a + b
# b = a - b
# a = a - b
# print("After swap: a =", a, "b =", b)


#  Area Of circle 


# radius = float(input("Enter the radius of the circle: "))
# pi = 3.14
# area = pi * radius*radius
# print("Area of circule is:",area)



# Number Positive or Negative

# a=int(input("Enter the Number :"))

# if a<0:
#     print("Number is Negative")
# elif a>0:
#     print("Number Is Positive")    
# else:
#     print("Number Is Zero")    





# Identify the Character Type


# char = input("Enter a single character: ")
# if len(char) != 1:
#     print("Please enter exactly one character.")
# else:
#     if char.isalpha():
#         if char.lower() in 'aeiou':
#             print("It is a Vowel.")
#         else:
#             print("It is a Consonant.")
#     elif char.isdigit():
#         print("It is a Digit.")
#     else:
#         print("It is a Special Character.")



# Find the Smallest of Three Numbers

# a=int(input("Enter the first Number :"))
# b=int(input("Enter the second  Number :"))
# c=int(input("Enter the Therd Number :"))

# if ((a<b) and(a<c)):
#     print("a Is smallest",a)
# elif ((b<a) and(b<c)):
#     print("B is Smallest",b)   
# else:
#     print("C is small",c)




# Calculate the Sum of Digits

