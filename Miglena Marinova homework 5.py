class Bill:

    def __init__(self,amount):
        self.amount=amount

        if not (isinstance(amount,int)):
         raise TypeError
        if amount<0:
         raise ValueError


    def __str__(self):
        return "A "+ str(self.amount)+"$ Bill"

    def __repr__(self):
        return "A "+ str(self.amount)+"$ Bill"    

    def __int__(self):
        return self.amount  

    def __eq__(self, other):
        return self.amount==other.amount

    def __hash__(self):
        return hash(self.amount)

     


a=Bill(10)
b=Bill(5)
c=Bill(10)
#d=Bill(-1)

print(a)
print(int(a))        
print(a==c)        
print(hash(a))
#print(d)

money_holder = {}
money_holder[a] = 1 
if c in money_holder:
    money_holder[c] += 1
print(money_holder)



class BatchBill:

    def __init__(self,list_of_bills):

        self.list_of_bills=list_of_bills

    def __len__(self):
        return len(self.list_of_bills)
    
    def total(self):
        total=0
        for i in self.list_of_bills:
            total+=int(i)
        print(total)
        return total
    
    def __getitem__(self,index):
        return self.list_of_bills[index]


mylist=BatchBill([Bill(10),Bill(20),Bill(50),Bill(100)])
print(len(mylist))
mylist.total()
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[3])



class CashDeck:
    pass


