def safe_convert(val,target_type):
    try:
        val=target_type(val)
        return (True,val," ")
    except:
        # print("error")
        return (False,val,"error")

x=safe_convert("abc",int)[0]
print(x)