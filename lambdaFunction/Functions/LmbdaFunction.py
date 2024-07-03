# lambda functio
def apply(criteria,n) :
  count = 0
  for i in range ( n+1):
      if criteria(i) :
         count +=1
      return count

def is_even(x) :
   return x%2 == 0


print(apply(is_even,10))