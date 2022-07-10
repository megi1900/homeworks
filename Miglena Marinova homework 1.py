print("zad.1")

def sum_of_digits(num):
    res=0
    if num<0:
        num=num*-1


    while num>0:
       
        res=res+num%10
        num=num//10

    return res

print(sum_of_digits(13251324))
print(sum_of_digits(123))
print(sum_of_digits(6))
print(sum_of_digits(-10))


print("\nzad.2")

def to_digits(num):
    res=[]
    while num>0:
        digit=num%10
        num=num//10
        res.insert(0,digit)
    return res
print(to_digits(123))
print(to_digits(234678))
print(to_digits(1056379857))




print("\nzad.4")

def fib_number(n):
   
    if n == 1:
        return 0
    elif n == 2:
        return [1, 1]
    else:
        fib = [1, 1]
        for i in range(2, n):
            fib.append(fib[i-2] + fib[i-1])
        return fib
print(fib_number(10))
print(fib_number(3))


