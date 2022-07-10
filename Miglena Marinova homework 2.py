print("zad.1")
def sum_of_min_and_max (arr):
    
    minimum = maximum = arr[0]
    for i in arr[1:]:
        if i < minimum: 
            minimum = i 
        else: 
            if i > maximum: 
                maximum = i
    return (minimum+maximum)

print(sum_of_min_and_max([1,2,3,4,5,6,8,9]))
print(sum_of_min_and_max([-10,5,10,100]))
print(sum_of_min_and_max([1]))


print("\n zad.2")
def sum_of_divisors(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=i
    return sum        
print(sum_of_divisors(8)) 
print(sum_of_divisors(7)) 
print(sum_of_divisors(1)) 
print(sum_of_divisors(1000)) 



print("\n zad.3")

def is_prime(n):
    if n==1:
        return False
    if n>1:   
      for i in range(2,n):
        if n%i==0:
            return False
      return True
    return False 

print(is_prime(-10))    
print(is_prime(8))  
print(is_prime(2))
print(is_prime(11))



print("\n zad.4")

def is_palindrome(n):
     num=n
     rev=0

     while n>0:
         r=n%10
         rev=rev*10+r
         n=n//10
     if (num==rev):
        return True
     else:
        return False   
print (is_palindrome(10001)) 
print (is_palindrome(1)) 
print (is_palindrome(123))
print (is_palindrome(888))  


