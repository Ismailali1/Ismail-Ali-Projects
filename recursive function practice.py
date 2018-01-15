#Ismail Ali Recursive Function Practice





#Part 3   

def digit_sum(num):
  '''(int)->int
  Returns the sum of numbers inputed'''
  if num == 0:
    return 0
  
  return (num%10) + digit_sum(num//10)


def digit_root(num):
  '''(int)->int
  Returns the sum of the root of numbers until length of num is 1'''
  if num < 10:
    return num
    
  else:
    num = digit_sum(num)
    return   digit_root(num)
           


















