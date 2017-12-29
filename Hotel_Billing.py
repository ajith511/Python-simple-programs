## A program for hotel billing service

def hotel(billing_menu):                ##viewing menu
    for key,val in menu.items():
        print(key, 'Rs.',val ,'\n')
def order_table(table):                 ##printing ordered items per table
    for key1,val1 in table.items():
        print(key1,'\t\t',val1)
def bill_table1():                      ##billing of table1
    total_table1=0
    for ite, pri in menu.items():
        total1=0
        for tab_item1,tab_quant1 in table1.items():
             if tab_item1 == ite:
                 total1=int(pri)*int(tab_quant1)
                 break
        total_table1 += total1
    print('\nTotal for table number 1 is ', total_table1,'\n')
def bill_table2():                      ##billing of table2
    total_table2=0
    for ite, pri in menu.items():
        total2=0
        for tab_item2,tab_quant2 in table2.items():
            if tab_item2 == ite:
                total2=int(pri)*int(tab_quant2)
                break
        total_table2 += total2
    print('\nTotal for table number 2 is ', total_table2,'\n')
def bill_table3():                      ##billing of table3
    total_table3=0
    for ite, pri in menu.items():
        total3=0
        for tab_item3,tab_quant3 in table3.items():
            if tab_item3 == ite:
                total3=int(pri)*int(tab_quant3)
                break
        total_table3 += total3
    print('\nTotal for table number 3 is ', total_table3,'\n')
def bill_table4():                      ##billing of table4
    total_table4=0
    for ite, pri in menu.items():
        total4=0
        for tab_item4,tab_quant4 in table4.items():
            if tab_item4 == ite:
                total4=int(pri)*int(tab_quant4)
                break
        total_table4 += total4
    print('\nTotal for table number 4 is ', total_table4,'\n')
def bill_table5():                      ##billing of table5
    total_table5=0
    for ite, pri in menu.items():
        total5=0
        for tab_item5,tab_quant5 in table5.items():
            if tab_item5 == ite:
                total5=int(pri)*int(tab_quant5)
                break
        total_table5 += total5
    print('\nTotal for table number 5 is ', total_table5,'\n')



menu =  {}
order = {}
table1 ={}
table2 ={}
table3 ={}
table4 ={}
table5 ={}
while True:
    choice = int(input('\n1. Add items to the Menu \n2. Show Menu \n3. Order for a Table \n4. Bill for a table \n5. Exit \n'))
    if choice ==1:
        while True:
            item = input ('Enter the name of the item:  ')
            price = input('Enter the price of the item:  ')
            menu[item] = price
            q= input('Do you want to enter more items y/n:  ')
            if q == 'n':
                 break
            elif q == 'y':
                 continue
            else:
                 print('Invalid entry')
    if choice == 2:
        hotel(menu)
    if choice == 3:
        table = int(input('Enter the table number:  '))
        if table ==1:
              while True:
                    item = input('Enter the name of item:  ')
                    quantity = input('Enter the quantity of item:  ')
                    table1[item] = quantity
                    order_table(table1)
                    p = input('Continue? y/n:  ')
                    if p == 'n':
                        break
                    elif p == 'y':
                        continue
                    else:
                        print('Invalid entry')
        if table ==2:
              while True:
                    item = input('Enter the name of item:  ')
                    quantity = input('Enter the quantity of item:  ')
                    table2[item] = quantity
                    order_table(table2)
                    p = input('Continue? y/n:  ')
                    if p == 'n':
                        break
                    elif p == 'y':
                        continue
                    else:
                        print('Invalid entry')
        if table ==3:
              while True:
                    item = input('Enter the name of item:  ')
                    quantity = input('Enter the quantity of item:  ')
                    table3[item] = quantity
                    order_table(table3)
                    p = input('Continue? y/n:  ')
                    if p == 'n':
                        break
                    elif p == 'y':
                        continue
                    else:
                        print('Invalid entry')

        if table ==4:
              while True:
                    item = input('Enter the name of item:  ')
                    quantity = input('Enter the quantity of item:  ')
                    table4[item] = quantity
                    order_table(table4)
                    p = input('Continue? y/n:  ')
                    if p == 'n':
                        break
                    elif p == 'y':
                        continue
                    else:
                        print('Invalid entry')
        if table ==5:
              while True:
                    item = input('Enter the name of item:  ')
                    quantity = input('enter the quantity of item:  ')
                    table5[item] = quantity
                    order_table(table5)
                    p = input('Continue? y/n:  ')
                    if p == 'n':
                        break
                    elif p == 'y':
                        continue
                    else:
                        print('Invalid entry')
    if choice ==4:
        user = int(input('Table number to be billed:(1 to 5):  '))
        if user==1:
            bill_table1()
            table1.clear()
        if user==2:
            bill_table2()
            table2.clear()
        if user==3:
            bill_table3()
            table3.clear()
        if user==4:
            bill_table4()
            table4.clear()
        if user==5:
            bill_table5()
            table5.clear()



    if choice == 5:
        break
    





