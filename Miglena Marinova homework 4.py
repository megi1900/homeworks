      
print("zad.1, zad.2")
empty_set=set()
new_list=[4,5,66]
new_list2={33,0,88}
for i in range(0,50):   
   empty_set.add(i)
   empty_set.update(new_list,new_list2)  
print(empty_set)


print("\nzad.3")

ll=[j for j in empty_set]   
print(ll)



print("\nzad.4")

dict_ll={k:k*2 for k in empty_set}   
print(dict_ll)



print("\nzad.5")

for idx, value in enumerate(dict_ll):  
   if idx%2==1:
      print(idx,value)


print("\nzad.6")

def func(arr,num):
 sum=0

 for i in range(len(arr)):
      for j in range(i+1, len(arr)):
            sum=arr[i] + arr[j]
            if sum==num:
              print(arr[i], arr[j])
        
arr=[1,2,3,4,5,6,7,8,9]
num=8
func(arr,num) 

