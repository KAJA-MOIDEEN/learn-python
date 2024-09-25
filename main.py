# print('kaja') # 
# print("hello worl") # 
# print('''this is my first class 
#       and this class is the python class''') # use to achive multiline  string

# # naming Conversions
# # 1. camelCase  firstName = "kaja"
# # 2. PascalCase   FirstName = "kaja"
# # 3. snake_case     first_name = "kaja"  # this is used in python

# # datatype 
# # 1. int
# # 2. float
# # 3. complex
# # 4. str
# # 5. list
# # 6. tuple
# # 7. range
# # 8. dict

# number1 = 20
# number2 = 30


# print(number1 + number2) # addition
# name = "kaja"
# print(name) # string
# num1 =  int(input("Enter the number 1 ")) #  input function to get user  input
# num2 =  int(input("Enter the number 2 ")) #  mention ini,float,str to convert one datatype to another data type casting 

# # Arithmatic Operation
# print("Aritnmatic Operator")
# print("Adition ",num1+num2)
# print("Division",num1/num2)
# print("Multiplication",num1*num2)
# print("Modulus",num1%num2)
# print("power ", num2**num1)

# a= 20
# b= 30

# #comparition  operator
# print("Comparition Operator a= 20 , b = 30")
# print("a>b",a>b)
# print("a<b",a<b)
# print("a>=b",a>=b)
# print("b<=a",b<=a)

# a = 5
# b = 5

# #logical operator 
# print("a = 5,b = 5 Logical operator AND OR NOT")
# print("",a!=b) #
# print("",a==b and a>b)
# print("",a>b or a>=b)
# print("",not a>b)
# print("Not()",not(a==b and a>b))


# #arugment operator

# # condition  operator
# # if else elif
# # indentdation 
# # if condition:
# #     print("condition is true")
# # elif condition:
# #     print("condition is true")
# # else:

# # test1 case get input from user 
# # test2 check even or odd number

# a = int(input("Enter the number to check odd or even "))
# if a%2==0:
#     print(a," even number")
# else:
#     print(a," odd number")
# age = 24 

# if age<18:
#     print(age," small boy or  girl")
# elif age>18 and age<21:
#     print(age," 18+")
# elif age>21 and age<50:
#     print(age," 21 to 50")
# else:
#     print(age," 50+")

# name = input("Enter your name ")
# age = input("Enter your age as a number ")
# gender = input("Enter your gender ")

# if int(age)>18:
#     if gender=="male":
#         print("--Magor--")
#         print("name: ",name," age: ",age," gender: ",gender)
#     else:
#         print("--Magor--")
#         print("name: ",name," age: ",age," gender: ",gender)
# else:
#     if  gender=="male":
#         print("--Miner--")
#         print("name: ",name," age: ",age," gender: ",gender)
#     else:
#         print("--Miner--")
#         print("name: ",name," age: ",age," gender: ",gender)

# test3 atm

    
    
    #loops in python
    # for loop
    # for i in range(1,11):
    #     print(i)
    
    # while loop
    # i = 1
    # while i<11:
    #     print(i)
    #     i+=1
name = "kaja moideen moideen kaja  moideen"

# print("name "+ name)
# print("name",name)
# x = name.encode()
# print(len(x))
# print(name.find("m"))
# b = "kaja"
# a = [1,2,3,4,5,6,7,8,9]
# print(b.count(""))

# print("1"+"")
name = "{:UserName:f}".format(input("Enter your name"))
email = "{:Email:f}".format(input("Enter your email"))
phone = "{:Phone:f}".format(input("Enter your phone number"))

print(name)
print(email)
print(phone)