# import sys
# print(sys.path)
# -------------------------
# import json
# x={"a": "john","b": 5}
# y=json.dumps(x,indent=4,separators=(". ","= "))
# print(y)
# print(type(y))
# -------------------------------------------
# a=[1,2,3,4]
# print(a*2)
# ------------------------------------
a = [1,2,3]
b = a* 3
print(b)
b[0][0] = 99

print(b)

