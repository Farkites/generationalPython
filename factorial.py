#python factorial.py argv[1] returns argv[1] factorial

import sys

def factorial(number):
 if number == 1:
  return 1
 else:
  return number * factorial(number-1)

print("This is "+sys.argv[0]+"\nthe factorial of "+sys.argv[1]+ " is " +str(factorial(int(sys.argv[1]))))


