def recurring_numbers(lst,n):
    final_list=[]
    for i in lst:
        g= lst.count(i)
        if g>n:
            if i not in final_list :
                final_list.append(i)
    print(final_list) 


recurring_numbers([2,5,4,1,3,6,2,1,2,4,5,4],2)
