#fibonacci
"""def fib(n):
    a=0
    b=1
    for i in range(n):
        print(a)
        a,b=b,a+b
fib(100)

def fib(n):
    a=0
    b=1
    c=2
    for i in range(n):
        print(a)
        a,b,c=b,c,a+b+c
fib(10)
#slicing
list=[1,2,3,45,8]
print(list[4])
print(list[:4])"""

"""#concatenation operator(+)
a=[1,2,5,8]
b=[5,7,9,3]
print(a+b)
#realtime usage
# 2)repetation operator(*)
num=[1,2]
print(num*3)
#membership operater(in,not-in)
fruits=["apple","grape","banana"]
print("apple" in fruits)
print("citrus" in fruits)
#comparisioin operator
list1=[2,5,8]
list2=[2,5,9]
print(list1==list2)
print(list1<list2)

a=[1,78,56,25,76,36,88]
b=[51,78,98,13]
print(a+b)

num=[11,12,56,78,95,36,21]
print(num*3)

num=[21,22,53,84,18,76,7,78,59]
print("22,55" in num)
print("88,999" in num)

list1=[55,5,8]
list2=[55,5,8]
print(list1==list2)
print(list1<list2)

#list method
num=[1,2,3,4]
num.append(5)
print(num)
num.insert(2,5)
print(num)
num.remove(3)
print(num)
num.pop(1)
print(num)
print(num.index(2))
#extend()
a=[1,5,6,8]
b=[5,7,8,9]
a.extend(b)
print(a)
a=[1,2,3,4,5,6]
print(a.count(2))
#sort
a.sort()
print(a)
a.sort(reverse=True)
print(a)
#reverse
a.reverse()
print(a)
#copy
b=a.copy()
print(b)

#map(),filter() and list ()--> functional programming -->iterates
#should use it on list
num=[1,2,3,4]
result=list(map(lambda x:x*2,num))
print(result )

def func(x):
    return x*3
result=list(map(func,num))
print(result)

num1=[1,2,3,4,5,6,7,8,9]
result1=list(filter(lambda x:x%2==0,num1))
print(result1)

#reduce--> convert into a single value -->functional module
#syntax
#reduce(functional) 
from functools import reduce
num=[1,2,3,4,5,6]
result=reduce(lambda a,b:a+b,num)
print(result)

num1=[1,2,3,4,5,6,7,8,9,10]
result1=list(filter(lambda x:x%2==0,num1))  
print(result1,sum(result1))

num1=[1,2,3,4,5,6,7,8,9]
result1=list(filter(lambda x:x%2==1,num1))
print(result1,sum(result1))

#palindrome--->A value that needs the same backward and forward

#1st method-->slicing
word=input("enter a word")
if word==word[::1]:
    print("palindrome")
else:
    print("not a palindrome")

num = input("Enter a number: ")

rev = ""

for ch in num:
    rev = ch + rev

if num == rev:
    print("Palindrome")
else:
    print("Not a Palindrome")"""
#without slicing-->only for number
num=int(input("enter the number"))
orginal=num
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num //10
print(rev)
if orginal==rev:
    print("palindrome")
else:
    print("not a palindrome")