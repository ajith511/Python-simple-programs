import pandas as pd
 
 
 
gh= pd.read_csv('weather.csv',parse_dates=['EST'])

 
 
 
l=gh.loc[gh['Temperature'].idxmax()]
print('Maximum Temperature in the month of January is',l.Temperature)

print('\nList of days it Rained : ') 
a=gh.Events
for i in range(len(a)):
    if a[i]=='Rain':
        t= gh.EST[i]
        print(t)
        
b= gh.WindSpeedMPH.sum()
print('\nAverage speed of wind in the month of January is :',b/len(gh.WindSpeedMPH))


    

 


 