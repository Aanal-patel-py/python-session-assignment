import pdb
def merge_calls(*funcs,**defaults):
    def wrapper(*args,**kwargs):
        updated_kwargs={**defaults,**kwargs}
        result=None
        pdb.set_trace()
        for i,f in enumerate(funcs):
            if i==0:
                result=f(*args,**kwargs)
            else:
                result=f(result,**updated_kwargs)
        return result
    return wrapper



def add(x, y): return x + y
def multiply(x, factor=2): return x * factor
combined = merge_calls(add, multiply, factor=3)
result = combined(5, 10) 
print(result)
