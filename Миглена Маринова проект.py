
prices={1: 2.10, 2: 3.50, 3: 4.60, 4: 3.00}

class Shop:

    def info_user_order(self):

            details={}
        
            name=input("Hello, welcome to Meghan's coffee shop. What is your name sir/madam?  ")
            print()
            print("*" * 10 + "MAIN MENU" + "*" * 10 + "\n"
                "\n"     
                "\t(1) Macciato    2.10$ \n"                              
                "\t(2) Americano   3.50$\n"
                "\t(3) Iced latte  4.60$\n"
                "\t(4) Espresso    3.00$\n" +
                "_" * 72)

            
            order=int(input("Your choice:  "))

           
            quant=int(input("\nHow quantity do you want:  "))

            
            if order == 1: # macciato 2.10
                total=prices[1]*quant
                details['name']=name
                details['type']="Macciato"
                details['total']=total
            

            elif order==2: #americano 3.50
                total=prices[2]*quant
                details['name']=name
                details['type']="Americano"
                details['total']=total
            

            elif order==3: # iced latte 4.60
                total=prices[3]*quant
                details['name']=name
                details['type']="Iced latte"
                details['total']=total
            

            elif order==4: # espresso 3.00
                 total=prices[4]*quant
                 details['name']=name
                 details['type']="Espresso"
                 details['total']=total
                    
            return details
            
    
    def receipt(self,info_user_order):
                print()
                print("*" * 10 + "Receipt for client" + "*" * 10 + "\n")

                name=info_user_order['name']
                type=info_user_order['type']
                total=info_user_order['total']

                print("Client's name: "+name+"\nType of coffe: "+type+"\nTotal price: $"+"%.2f" % total+"\n")
     

coffee=Shop()
coffee.receipt(coffee.info_user_order())


choice=input("\nDo you want to calculate for another client? / Yes or No:  ")

while choice.lower()=="yes":
    print()
    coffee.receipt(coffee.info_user_order())
    choice=input("\nDo you want to calculate for another client? / Yes or No:  ")

print(" ")




    
    

        
         

      




     






#print("Hello, welcome to Meghan's coffee shop. What is your name sir/madam?")
# print("*" * 10 + "MAIN MENU" + "*" * 10 + "\n")
#              #               "\n"     
# #               "\t(S1) Macciato: 2.10$ \n"                              
# #               "\t(S2) Long Macciato: 2.30$ \n"
# #               "\t(33) Iced latte: 3.40$ \n"
# #               "\t(S4) Caffe latte: 3.00$ \n"
# #               "\t(S5) Black coffee: 2.00$\n"
# #               "\t(S6) Cappuccino: 4.10$\n"
# #               "\t(S7) Americano: 2.50$\n"
# #               "\t(S8) Vienna: 2.60$\n"
# #               "\t(S9) Espresso: 2.80$\n"
# #               "\t(S10) Double Espresso: 3.00$\n"+

#              "_" * 72)

# coffee_file=open("coffee.txt","r")

# order=input("Your choice (S1-S10):")     


# total=0

# while (order !="E"):
#     for item in coffee_file:
#         data=item.split(";")
#         item_order=data[0]
#         item_type=data[1]
#         item_price=float (data[2])
#         if item_order==order:
#          print(item_order+"-"+item_type+"-"+str(item_price)+"$")
#          total=total+item_price
#     order=input("Enter another order or press E for exit:")

# print("Total cost of your order:"+str(total)+"$")
# print("Have a nice day!")
# coffee_file.close()










              




