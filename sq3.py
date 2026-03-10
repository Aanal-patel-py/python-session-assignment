
import sys

z=[x*x for x in range(1,101) if((x%3==0 )^ (x%5==0 )) if x*x<1000]
print(z)
print(sys.getsizeof(z))

x=(x*x for x in range(1,101) if((x%3==0 )^ (x%5==0 )) if x*x<1000)

print(sys.getsizeof(x))

# def divisible(n):
#     return n%3==0 ^ n%5==0 


# z= filter(divisible,x)
# new=list(z)
# print(list(z))

