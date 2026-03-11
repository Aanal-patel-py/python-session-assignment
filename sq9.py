
import time
import random

def timer(func):
    def wrapper(*args,**kwargs):
        starttime=time.perf_counter()
        result=func(*args,**kwargs)
        endtime=time.perf_counter()
        executiontime=endtime-starttime
        print(f"execution time: {executiontime}")
        return result
    return wrapper

def retry(attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args,**kwargs):
            count=0
            for i in range(attempts):
                try: 
                    result=func(*args,**kwargs)
                    return result
                except:
                    count+=1
                    print("Attempt failed retrying...")
                    time.sleep(delay)
            if count==attempts:
                raise Exception("failed all the time")
        return wrapper
    return decorator

def cache(max_size=5):
    def decorator(func):
        cache_dict = {}  
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))

            if key in cache_dict:
                return cache_dict[key]  

            result = func(*args, **kwargs)
            cache_dict[key] = result

            if len(cache_dict) > max_size:
                first_key = next(iter(cache_dict))  
                del cache_dict[first_key]
            return result
        return wrapper
    return decorator

def validate_type(func):
    def wrapper(*args,**kwargs):
        if 'user_id' in kwargs:
            user_id = kwargs['user_id']
        else:
            user_id = args[0]  

        if not isinstance(user_id, int):
            raise TypeError(f"user_id must be int, got {type(user_id).__name__}")
        
        return func(*args,**kwargs)
    return wrapper


@validate_type
@cache()
@retry(attempts=3, delay=1)
@timer
def fetch(user_id):
    print("fetching data from API...")
    time.sleep(2)
    x=random.random()
    if x>0.5:
        raise Exception("API failed")
    else:
        print({"user_id":user_id,"data":"api response"})
        return {"user_id":user_id,"data":"api response"}


fetch(7)
