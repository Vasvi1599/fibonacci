# fibonacci series till n-th term

n= int(input(" No of terms: "))

# 1st two terms

n1=0
n2=1
count=0

if n<= 0:
    print("Please enter a positive number")
elif n==1:
    print("Fibonacci series upto" , n , "is:")
    print(n1)
else:
    print("Fibonacci series upto" , n , "is:")
    while count<n:
        print(n1)
        nth= n1 + n2

        n1 = n2
        n2 = nth
        count += 1
        
