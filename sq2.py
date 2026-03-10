company = {
    "Engineering": {
        "Backend": ["Alice", "Bob", "Charlie"],
        "Frontend": ["David", "Eve"],
        "DevOps": ["Frank"]
    },
    "Sales": {
        "North": ["Grace", "Henry"],
        "South": ["Ivy"]
    }
}

# x=[]
# for z in company:  
#     for y in company[z]:         
#        for p in company[z][y]:
#         x.append(p)
# print(x)

def count_of_employees():
    d={}
    for x in company.values():
        y=0
        for team,emp in x.items():
            y+=len((emp))
   
# count_of_employees()

def get_key_from_value(val):
    for dept,team in company.items():
        for team, emp in team.items():
            if val in emp:
                print(team)

get_key_from_value("Ivy")


def reverse_mapping():
    new_dict={}
    x= {employee:[dept,team] for dept,team in company.items() for team,emp in team.items() for employee in emp}
    print(x)

reverse_mapping()