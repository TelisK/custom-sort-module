def new_sort(mylist,capitalized=False,original=False):
    if original==False:
        temp=[]
        corrected_list=[]
        if capitalized==False:
            for i in mylist:
                temp.append(i.lower())
            corrected_list=sorted(temp)
            print(temp)
            print(corrected_list)
            return corrected_list
        else:
            for i in mylist:
                temp.append(i.capitalize())
                print(i)
            corrected_list=sorted(temp)
            print(temp)
            print(corrected_list)
            return(corrected_list)
    
    if original==True:
        list_with_lowers=[]
        list_with_others=[]
        temp=[]
        for i in mylist:
            if i.islower():
                list_with_lowers.append(i)
            else:
                list_with_others.append(i)
        print(list_with_lowers)
        print(list_with_others)
        temp=list_with_lowers.copy()
        print(temp)
        for s in list_with_others:
            temp.append(s.lower())
        temp.sort()
        print(temp)
        #Here we will find the same word in lowers, and replace it from the original list.
        for s in list_with_others:
            for i,t in enumerate(temp):
                if s.lower() == t:
                    temp[i]=s
                    break
        print(f'Teliko apotelesma: {temp}')
        #works with lists, tuples, sets
        
        # prepei na valo raise error ean baloyn int floats klp
                
    

#new_sort(['2','5','3','-1','adffe','zfrj','dje','Dje','bahd','Ghrs','Kggfr','Ygfg'],original=True)


strings = {
    "Καλημέρα",        # 1
    "γειάΣΟΥ",         # 2
    "Hello",           # 3
    "WORLD",           # 4
    "Python3",         # 5
    "δοκιμή123",       # 6
    "Test_One",        # 7
    "ΑΒΓΔ",            # 8
    "abcd",            # 9
    "ΜικράΚεφαλαία",   # 10
    "Data2025",        # 11
    "αριθμοί456",      # 12
    "STRING",          # 13
    "string",          # 14
    "Συμβολοσειρά",    # 15
    "example99",       # 16
    "HELLOworld",      # 17
    "κόσμε",           # 18
    "Test123Test",     # 19
    "γειά123",         # 20
    "OpenAI",          # 21
    "chatGPT",         # 22
    "ΤΕΣΤ",            # 23
    "τεστ",            # 24
    "Alpha1",          # 25
    "BETA2",           # 26
    "γάμμα3",          # 27
    "Delta_4",         # 28
    "pythonικός",      # 29
    "Code2024",        # 30
    "Αθήνα",           # 31
    "London",          # 32
    "12345",           # 33
    "000abc",          # 34
    "Mix3dCase",       # 35
    "Κεφαλαία123",     # 36
    "lowercase",       # 37
    "UPPERCASE",       # 38
    "ΤεστTest",        # 39
    "δοκιμήTest9",     # 40
    "Σ123Α",           # 41
    "abcDEF",          # 42
    "Παράδειγμα",      # 43
    "example",         # 44
    "EXAMPLE1",        # 45
    "τελικό",          # 46
    "Final99",         # 47
    "End",             # 48
    "ΤΕΛΟΣ",           # 49
    "last_item7"       # 50
}

new_sort(strings,original=True)
print(type(strings))