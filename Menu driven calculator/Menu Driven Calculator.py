num = int(input("Enter a Number: "))
print("--------Select Options----------")
print("        1.Factorial\n        2.Palindrome\n        3.Fibonacci\n        4.Table of the given number")
n=int(input())
result=1
count=1

if(n<=0 or n>4):
    print("Invalid Input")
elif(n==1):
    while (count<=num):
        result=result*count
        count+=1
    print(result)
    
elif(n==2):
    rev=0
    temp=num
    while (temp>0):
        lastDigit=temp%10
        rev=(rev*10)+lastDigit
        temp=temp//10
    if rev == num:
        print('Palindrome')
    else:
        print("Not Palindrome")
    
        
elif(n==3):
    count=0
    current=1
    prev=0
    sum=0
    while (count<=num):
        sum=prev+current
        prev=current
        print(sum)
        current=sum
        count+=1
          
        
elif(n==4):
    while (count <= 10):
        print(count*num)
        count+=1