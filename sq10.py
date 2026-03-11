from functools import reduce
import itertools
transactions = [
    {"id": 1, "amount": 100, "type": "debit", "category": "food"},
    {"id": 2, "amount": 200, "type": "credit", "category": "salary"},
    {"id": 3, "amount": 50,  "type": "debit", "category": "entertainment"},
    {"id": 4, "amount": 150, "type": "debit", "category": "food"},
    {"id": 5, "amount": 300, "type": "credit", "category": "freelance"},
    {"id": 6, "amount": 70,  "type": "debit", "category": "transport"},
    {"id": 7, "amount": 120, "type": "debit", "category": "entertainment"},
]

x= filter(lambda a:a["type"]=="debit",transactions)
print(list(x))

y=map(lambda a:a["amount"],transactions)
print(list(y))

z=reduce(lambda acc,a:acc+1 if a["type"]=="debit" else acc,transactions,0)
print(z)

sorted_dict=sorted(transactions, key=lambda x: x["category"])
print(sorted_dict)

for cat, items in itertools.groupby(sorted_dict,key=lambda x:x["category"]):
    # print(cat)
    # print(items)
    total=sum(item["amount"] for item in items)
    print(f"{cat} = total amount: {total}")


