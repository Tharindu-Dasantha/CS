try:
 while True:
    credit_pass = int(input("Please enter your credits at pass:"))
    if credit_pass>=0 and credit_pass <=120:
        print(credit_pass)
    else:
        print("out of range!")
        continue
    
    while True:   
     credit_differ = int(input("Please enter your credit at defer:"))
     if credit_differ>=0 and credit_differ <=120:
        print(credit_differ)
     else:
        print("out of range!")
        continue
        
     while True:
          credit_fail = int(input("Please enter your credit at fail:"))
          if credit_fail>=0 and credit_fail <=120:
           print(credit_fail)
           break
          else:
           print("out of range!")
           continue
    
     total_credit = (credit_pass + credit_differ  +credit_fail)
     if credit_pass==120 and  credit_differ ==0 and credit_fail == 0:
      print('Progress')
     elif credit_pass==100 and  credit_differ ==20 and credit_fail == 0:
      print('Progress (module trailer)')
     elif credit_pass==100 and  credit_differ ==0 and credit_fail == 20:
      print('Progress (module trailer)')
     elif credit_pass==80 and  credit_differ ==40 and credit_fail == 0:
      print('Do not Progress – module retriever')
     elif credit_pass==80 and  credit_differ ==20 and credit_fail == 20:
      print('Do not Progress – module retriever')
     elif credit_pass==80  and  credit_differ ==0 and credit_fail == 40:
      print('Do not Progress – module retriever')
     elif credit_pass==60 and  credit_differ ==60 and credit_fail == 0:
      print('Do not Progress – module retriever')
     elif credit_pass==60 and  credit_differ ==40 and credit_fail == 20:
      print('Do not Progress – module retriever')
     elif credit_pass==60 and  credit_differ ==20 and credit_fail == 40:
      print('Do not Progress – module retriever')
     elif credit_pass==60 and  credit_differ ==0 and credit_fail == 60:
      print('Do not Progress – module retriever')
     elif credit_pass==40 and  credit_differ ==80 and credit_fail == 0:
         print('Do not Progress – module retriever')
     elif credit_pass==40 and  credit_differ ==60 and credit_fail == 20:
         print('Do not Progress – module retriever')
     elif credit_pass==40 and  credit_differ ==40 and credit_fail == 40:
        print('Do not Progress – module retriever')
     elif credit_pass==40 and  credit_differ ==20 and credit_fail == 60:
      print('Do not Progress – module retriever')
     elif credit_pass==40 and  credit_differ ==0 and credit_fail == 80:
         print('Exclude')
         
     elif credit_pass==20 and  credit_differ ==100 and credit_fail == 0:
         print('Do not progress – module retriever')
     elif credit_pass==20 and  credit_differ ==80 and credit_fail == 20:
         print('Do not progress – module retriever')
    
     elif credit_pass==20 and  credit_differ ==60 and credit_fail == 40:
         print('Do not progress – module retriever')
     elif credit_pass==20 and  credit_differ ==40 and credit_fail == 60:
         print('Do not progress – module retriever')
     elif credit_pass==20 and  credit_differ ==20 and credit_fail == 80:
         print('Exclude')
     elif credit_pass==20 and  credit_differ ==0 and credit_fail == 100:
         print('Exclude')
     elif credit_pass==0 and  credit_differ ==120 and credit_fail == 0:
         print('Do not progress – module retriever')
     elif credit_pass==0 and  credit_differ ==100 and credit_fail == 20:
         print('Do not progress – module retriever')
     elif credit_pass==0 and  credit_differ ==80 and credit_fail == 40:
         print('Do not progress – module retriever')
     elif credit_pass==0 and  credit_differ ==60 and credit_fail == 60:
         print('Do not progress – module retriever')
     elif credit_pass==0 and  credit_differ ==40 and credit_fail == 80:
         print('Exclude')
     elif credit_pass==0 and  credit_differ ==20 and credit_fail == 100:
         print('Exclude')
     elif credit_pass==0 and  credit_differ ==0 and credit_fail == 120:
         print('Exclude')
    
     
      
    
     enter_newdata= input("Would you like to enter another set of data?\n Enter 'y for yes or 'q' to quit and view results:")
    
    
    
              
   
     if enter_newdata== "q":
        break
     elif enter_newdata == "y":
      continue
except:
    print("Integer required")