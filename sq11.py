import time
import sys,itertools
# iterator class
class Fibonacci:
    def __init__(self,limit,start_index):
        self.limit=limit
        self.index=0
        self.start_index=start_index
        self.a,self.b=0,1

        for _ in range(start_index): #skipping till custom index
            self.a, self.b = self.b, self.a + self.b

    def __iter__(self):
        return self
    def __next__(self):
        if self.limit <=self.index:
            raise StopIteration
        
        current=self.a
        self.a,self.b=self.b, self.a+self.b
        self.index+=1
        return current
    

# generator function
def fibonacci_gen(limit,start_index):
    a,b=0,1
    index=0
    for _ in range(start_index):
        a, b = b, a + b
    while index<limit:
        yield a
        a,b=b,a+b
        index+=1

def fibonacci_gen_inf():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

# x=Fibonacci(4,0)
# for y in x:
#     print(y, end=" ")
# print("\n")

starttime=time.time()
for _ in Fibonacci(1_000_000, 0):
    pass
endtime=time.time()
print(f"time taken by iteraor class: {endtime-starttime}")
print("Memory of list from iterator:", sys.getsizeof(Fibonacci(1_000_000,0)), "bytes")


# q=fibonacci_gen(4)
# print(q)


# for z in fibonacci_gen(,0):
#     print(z, end=" ")
# print("\n")


start = time.time()

for _ in fibonacci_gen(1_000_000,0):
    pass

end = time.time()

print("Generator time:", end - start)
print("Generator object memory:", sys.getsizeof(fibonacci_gen(1_000_000,0)), "bytes")


starttime1 = time.time()
for num in itertools.islice(fibonacci_gen_inf(), 1_000_000):
    pass
endtime1 = time.time()
print(f"time taken by generator function: {endtime-starttime}")
