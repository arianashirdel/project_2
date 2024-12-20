class User:
    current_user=None
    def register(self):
     name=input('enter name:')
        
     while True:
            try:
               password=input('enter your password (only numbers allowed):')
               if password.isdigit():
                 break
               else:
                   print('Please enter a valid number for password')
            except:
                print('Please enter number')

        
     with open('new_info.txt','a') as f:
      f.write(name +'-'+ password+'-\n')
      f.close()

      print(f"User {name} registered successfully.")
      User.current_user = {'name': name, 'password': password}
      main_menu().show2()
      
      
     #just for test   
    def show_info(self):
        s=open('new_info.txt','r')
    
        print(s.readlines())
        s.close()
      
    

    def log_in(self):
        name=input('enter your name:')
        while True:
            try:
               password=input('enter your password (only numbers allowed):')
               if password.isdigit():
                 break
               else:
                   print('Please enter a valid number for password')
            except:
                print('Please enter number')
        
        flag=0
        with open('new_info.txt','r') as f:
         for line in f :
           line=line.strip().split('-')       
           if line[0]==(name) and line[1]==(password):
            flag=1
            if line[0]==('admin') and line[1]==('1384'):
               admin_pannel().add_item()
   
      
        if flag==1:
           print(f'>> Welcome {line[0]}<<')
           User.current_user = {'name': name, 'password': password}
           main_menu().show2()

        else:
           print('No user data found. Please register a user first.')
           main_menu().show1()



class product:
   def menu(self):
      while True:
       print('1-search product\n2-Display product by quantity\n3-Display product by price\n4-back to menu')
       op=int(input('enter your option: '))
       if op==1:
         self.search_product()
       elif op==2:
         self.show_number()
       elif op==3:
         self.show_price()
       elif op==4:
          main_menu().show2()
       else:
          break
        
         
   def search_product(self):
      item=input('Enter name item:')
      flag=0
      with open('items.txt','r') as f:
         for line in f:
            line=line.strip().split('-')
            if line[0]==item:
               print(f'name:{line[0]},number:{line[1]},price:{line[2]}')
               flag=1
            
            
         if flag==0:
            print('this item not found!!')
      self.menu
   def show_number(self):
      with open('items.txt','r') as f:  
       lines=f.readlines()
       list1=[]
       for i in lines:
        cs=i.rstrip().split('-')
        name, number, price = cs[0], int(cs[1]), int(cs[2])
        list1.append((name,number,price))
       list1.sort(key=lambda number: number[1])

      print(list1)
      self.menu

   def show_price(self):
      with open('items.txt','r') as f:
         lines=f.readlines()
         list1=[]
         for i in lines:
          cs=i.rstrip().split('-')
          name, number, price=cs[0],int(cs[1]),int(cs[2])   
          list1.append((name,number,price))
          list1.sort(key=lambda price: price[2])  
      print(list1)
      self.menu()

class shopping_cart:
   def buy(self):
      items=[]
      while True:
       print('Stop the process by writing the word > End <')
       name=input('Enter name item:')
       if name=='End':
         break
       while True:
         try:
            num=int(input(f'Enter number of {name}:'))
            break
         except:
            print('please enter  number!! ')
      
       f=open('items.txt','r')
       temp=open('temp.txt','w')
       flag=0
       for l in f:
         line=l.strip().split('-')
         if line[0]==name:
            flag=1
            if int(line[1])>num:
               thisitem=[name,num,line[2]]
               items.append(thisitem)
               temp.write(f'{name}-{str(int(line[1])-num)}-{line[2]}\n')
               break
            else:
               temp.write(l)
               print(' ... sorry not enough items exist :( ')
         else:
            temp.write(l)

       if flag==0:
         print('this item not exist')
      
       f.close()
       temp.close()
 
       f=open('items.txt','w')
       temp=open('temp.txt','r')
       for line in temp:
         f.write(line)

       f.close()
       temp.close()
      

      totalprice=0  
      for item in items:
       totalprice= int(item[1])*int(item[2]) + totalprice
   
      print(f'totalprice:{totalprice}')
      with open('user_info','a') as f:
        f.write(f'User: {User.current_user["name"]}, Purchases: {items}, Total Price: {totalprice}\n')
      print('Thank you for your purchase')
      main_menu().show2()

class admin_pannel:
   def add_item(self):
       name=input('Enter item name:')
       number=input('Enter number of item:')
       price=input('Enter price of number:')
       with open('items.txt','a')as f:
        f.write(name + '-' + number + '-' + price+'\n')

        print(' item added :) ')
        main_menu().show1()




class main_menu:
   def show1(self):
      while True:
       print('1-register\n2-log in \n')
       op=int(input('enter your option:'))
       p1=User()
       if op==1:
        p1.register()
       elif op==2:
         p1.log_in()
       elif op==3:
         p1.show_info()
        
       else:
        break
   def show2(self):
      while True:
         print('1-products\n2-shpping cart')
         op=int(input('enter your option:'))
         if op==1:
            product().menu()
         elif op==2:
            shopping_cart().buy()
         else:
            break
            
            
            
main_menu().show1()