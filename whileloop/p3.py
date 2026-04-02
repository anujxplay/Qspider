'''
#1. WAP to print 1 to 100 natural numbers
i=1
while i<=50:
    print(i)
    i+=1





#2. WAP to print n natural numbers
n=int(input("Enter a number --"))  
i=1
while i<=n:
    print(i)
    i+=1    
'''









'''
#3. WAP to print user name 10 times
user = eval(input("Enter your number--"))
i=1
while i<=10:
    print(user)
    i+=1    
'''







'''
#4. WAP to print natural numbers in a given range
#(start and end point will be provided by the user)

start= int(input("Enter the start point--"))
end = int(input("Enter the end point--"))
while start<=end:
    print(start)
    start+=1
'''









'''
#5.   WAP to print the multiplication table

n = int(input("Enter the number: "))
i=1
while i<=10:
    print(n,'X',i,'=',n*i)
    i+=1
'''








'''
#6.   WAP to print n natural even numbers

n = int(input("Enter the number: "))
i=2
while i<=n:
    print(i)
    i+=2
'''







'''
#7.  Odd numbers
i=1
while i<=50:
    print(i)
    i+=2   
'''







'''
#8.   Factorial of a number (product of n natural no.)
n=3
fact = 1
while n>=1:
    fact = fact*n
    n = n-1
print(fact)    
'''






#9.  Find the product of odd digits and sum of even digits of a given number
n=int(input("Enter a number: "))
sum= 0
pro= 1
while n>0:
    ld=n%10
    if ld%2==0:
        sum+=ld
    else:
        pro*=ld
    n//=10 
print("sum:",sum)
print("product:",pro)       






'''
#10.  WAP to find the product of digits less than 5
n=int(input("Enter a number: "))
sum= 0
pro= 1
while n>0:
    ld=n%10
    if ld<5:
        pro*=ld
    n//=10 
print("sum:",sum)
print("product:",pro)       
'''





'''
# WAP to count no. digits of a number
n = int(input("Enter a number: "))
count = 0
while n > 0:
    last_digit = n % 10
    if last_digit % 2 == 0:
        count += 1
    n = n//10
print(count)   
'''






'''
# WAP to extract all the strings from a list.
list1 = eval( input(" Enter the list: "))
i =0
while i < len(list1):
    if type(list1[i]) == str:
        print(list1[i])
    i += 1
'''
