def Ters(lst): 
    lst.reverse() 
    return lst 
      
lst =  [[1, 2], [3, 4], [5, 6, 7]]

(Ters(lst))
liste=[]

for i in range(0,3):

    liste.append(lst[i][::-1])
    
print(liste)    



def flatten(x):
    
    for i in x:
        if isinstance(i,list): 
            flatten(i)
        else:
            empty_list.append(i)
    
    

x= [[1,'a',['cat'],2],[[[3]],'dog'],4,5] #
empty_list = [] 
flatten(x)
print(empty_list)

