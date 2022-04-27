'''
#LEC2
#multiple assignment
x=y=z=50
print(x)

#Asssigning multiple value to multiple variables
a,b,c=2,4,5
print(b)

#Keywords
is and or

#Membership Operators
a=7
lst=[45,22,66,2334]
print(a in lst)
print(a not in lst)


#Identity Operators

a=56
b=56
print(a is not b)
print(a is b)


x=100
if x>55:
    print("You won")
print("Congrats")

x=int(input("Enter your number :- "))
if x>=44:
    print("Yess!")
print("OH NO!")

x=int(input("Enter your number :- "))
if x>=44:
    print("+ve")
else:
    print("-ve")

x=int(input("Enter your number :- "))
rem = x%2
if rem == 0:
    print("even")
else:
    print("odd")


#user sub marks 33 pass fail
x=int(input("Enter your marks :- "))

if x>33 :
    print("pass")
else:
    print("fail")
    

#age eligible for vote
x=int(input("Enter your age :- "))

if x>18 :
    print("eligible")
else:
    print("not eligible")

#age senior citizen
x=int(input("Enter your age :- "))

if x>60 :
    print("senior citizen")
else:
    print(" not senior citizen")
   
#find out the greatest no. among two number
x=int(input("Enter your 1st no. :- "))
y=int(input("Enter your 2nd no. :- "))

if x>y :
    print("x greater than y")
else:
    print("y greater than x")

alp=input("Enter letter :- ")

if alp=="a" or alp=="e" or alp=="i" or alp=="o" or alp=="u":
    print("vowel")
else:
    print("consonant")
    '''
#+ve.-ve,=0
x=int(input("Enter your number :- "))
if x>0:
    print("positive")
elif x<0:
    print("negative")
else:
    print("0")

