
    # works with lists, tuples, sets, strings
        
    # output row : numbers, english, greek

def new_sort(x:list|set|tuple|str,capitalized=False,original=False):
    if not isinstance(x, (list,set,tuple,str)):
        raise TypeError('This module only accepts list, set, tuple, string.')
    
    if original==False:
        temp=[]
        corrected_list=[]

        if capitalized==False:
            for i in x:
                if not isinstance(i, str):
                    raise TypeError('Wrong type. Has to be str.')
                
                temp.append(i.lower())

            corrected_list=sorted(temp)

            return corrected_list
        else:
            for i in x:
                if not isinstance(i, str):
                    raise TypeError('Wrong type. Has to be str.')
                
                temp.append(i.capitalize())

            corrected_list=sorted(temp)

            return(corrected_list)
    
    if original==True: # capitalized can be True or False. Will be the same result.
        list_with_lowers=[]
        list_with_others=[]
        temp=[]

        for i in x:
            if not isinstance(i,str):
                raise TypeError('Wrong type. Has to be str')
            if i.islower():
                list_with_lowers.append(i)
            else:
                list_with_others.append(i)

        temp=list_with_lowers.copy()

        for s in list_with_others:
            temp.append(s.lower())
        temp.sort()

        #Here we will find the same word in lowers, and replace it from the original list.
        for s in list_with_others:
            for i,t in enumerate(temp):
                if s.lower() == t:
                    temp[i]=s
                    break

        return temp
