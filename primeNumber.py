# THIS code will help people tell whether a number is prime or non prime.

fim = input("Enter a number to check whether it's a prime or not:")
p=None
y= None
import sys
try:
    f= int(fim)
except:
    print("Not a number")
    sys.exit()

h =f/2
i=2.00
while i<h:
    if f%i==0:
        p=1
    else:
        p=0
    i=i+1

if p ==0:
    print("Yes,",f,"is a prime number")
elif p==1:
      print("No,",f," is not a prime number")
