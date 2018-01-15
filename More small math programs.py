##Ismail Ali

#Part a 

def largest_34(a):
    '''(list)->int
    Returns the sum of the 3rd and 4th largest values in list a
    #O(n * log n) number of operations
    '''
    a.sort(key=lambda x: x, reverse=True)
    length=a[2]+a[3]
    return length


#part B

def largest_third(a):
    ''' (list) -> number
    Returns the sum of a third of the list, the summed third being the part with
    the largest numbers.
    Runtime: O(n log_2 n + n/3)
    '''
    a.sort()
    return sum(a[len(a)-len(a)//3:len(a)])




#Part C



def third_at_least(a):
    '''(list)->int
    Returns a value list a, that occurs at least len(a)//3 + 1 times
    Runtime: O(n * log n)
    '''
    
    a.sort()
    k= len(a)//3 +1
    
    n=len(a)
    
    f=False
    for i in range(n-k+1):
        if a[i]==a[i+k-1]:
            f=True
            return a[i]
            
    if f==False:       
        return None
    

#part D


def sum_tri(a,x):
    '''(list,int)->bool
    Returns True if there exist indices a[s]+a[y]+a[z] equal to x
        Runtime: O(n^3)
    '''
    for s in a:
        for y in a:
            for z in a:
                if(s+y+z==x):
                    return True
    return False















