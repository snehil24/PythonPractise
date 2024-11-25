


def sum(a: int , b:int):
    print(a+b)


def greet():
# Using +
 greeting = "Hello, " + "world!"
 print(greeting)  # Output: Hello, world!

# Using f-strings (preferred for readability)
 name = "Alice"
 message2 = f"What's up {name}!"
 print(message2)  # Output: Hello, Alice!


def greet2():
   message = "greeting from third function"
   print(message)

def sampleNumber(num):
   str = ""
   for i in range(1,num+1):
      str += f"{i}"
   print(str.strip())

def fibonacciNumbers(index):
   if index == 0:
      return 0
   elif index == 1:
      return 1
   else:
      return fibonacciNumbers(index - 2) + fibonacciNumbers(index-1)
   
def reverseNumber(num):
   rev = 0
   while(num>0):
      rev = (rev * 10 ) + (num % 10)
      num = num //10
   print(rev)

def reverseString(str): 
   rev=""
   for i in range(len(str)):
      rev = str[i] + rev
   print(rev.strip())

def arraysStuff():
   my_list = [0] * 5
   # Initialize the list
   my_list = [10, 20, 30, 40, 50]

# # Loop through the list using its length
# for i in range(len(my_list)):
#     print(f"Element at index {i}: {my_list[i]}")

def numberIs(param:float):
   if param==0:
       return "Zero"
   elif(param>0):
       return "Greater Than 0"
   else:
       return "Less Than 0"
   
def sumOfNaturalNumbers(num):
    totalSum = 0
    for i in range(1,int(num)+1):
      totalSum += i
    
    return f"Sum of N Natural numbers until {int(num)} : {totalSum}"

def leapYearOrNot(year):
   if (year % 4 == 0) & (year %100 != 0) | (year % 400 == 0):
      print(f"{year} is a leap year")
   else:
      print(f"{year} is not a leap year")

def factorial(num1):
    num = 1
    for i in range(1,num1+1):
       num = num*i
    print(num)

def factorialrecurvisely(num):
   if (num == 0 ) | (num ==1):
      return 1
   else:
      return num * factorialrecurvisely(num-1)
   

def frequencyOfChar(str):
   dict = {}
   for i in range(0, len(str)):
      char = str[i]
      if char not in dict:
         dict[char] = 1
      else:
         dict[char] += 1
    
   for key, value in dict.items():
    print(f"{key}: {value}")
      
   

if __name__ == '__main__':
    # print("This script is running directly!")
    # sum(5,5)
    # greet()
    # greet2()
    # num1 = int(input("Enter a number Please "))
    # print(factorialrecurvisely(num1))

    str = input("Enter a string my bro:  ")
    frequencyOfChar(str)

       
    # reverseNumber(num1)
    # reverseString(num1)
    # sampleNumber(num1)

    # for i in range (0, num1+1):
    #    print(fibonacciNumbers(i))

    # num = float(input("Please enter a number:  "))
    # # String concatenation
    # message= "Number is " + f"{(numberIs(num))}" 
    # print(message)

    # if num > 0 :
    #    print(sumOfNaturalNumbers(num))
    
    # year = input("please enter a year to check for leap year: ")
    # leapYearOrNot(int(year))


    

