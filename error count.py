with open('new.txt','r') as read_file:

    h= read_file.read()
    a=h.count('err')
    b=h.count('error')
    c=h.count('Error')
    
    print('###Finding number of errors\n')
    
    print('Number of "err" is ',a-b,'Number of "error" is ',b,'Number of "Error" is ',c,'\n')
    read_file.seek(0)
    h= read_file.readlines()
    
    print('###"Finding By lines" \n')
    
    for i in h :
        print(i)
        q=i.find('error')
        if q==-1:
            print('word "error" Not found')
        else :
            print('word "error" at',q)
        w= i.find('err')
        if i[w+3]==' ':
            if w==-1:
                print('word "err" Not found')
            else :
                print('word "err" at',w)
        else:
            print('word "err" Not found')
        e= i.find('Error')
        if e==-1:
            print('word "error" Not found')
        else :
            print('word "error" at',e)
     
        
        
        
        
    

