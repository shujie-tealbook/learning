import json

"""
A simple task to learn ***json.dump*** and ***json.load***.
"""

# string1 = """{
#    "OrgUnit": "OrgUnit-1111111111111111-5629499534213120",
#    "org": {
#        "yearlyRevenue":"340.7 million (2018)",
#        "yearlyRevenueNum":"340700000",
#        "yearlyRevenueCurrency":"USD",
#        "yearlyRevenueYear":"2018",
#        "employeeNumber": "145 (2018)",
#        "employeeNumberNum": "145",
#        "employeeNumberYear": "2018",
#        "yearFounded": "June 16, 2001, Endicott, NY",
#        "yearFoundedYear": "2001"
#    },
#    "name": "Some Co Ltd",
#    "description": {
#        "en": "Some description text."
#    },
#    "domains": [
#        "somedomain.com"
#    ],
#    "info": {
#        "mlLoadDate": "2022-02-05T16:40:03.461126+00:00"
#    }
# }"""

# a = json.loads(string1) # turn a string to a json format(dictionary)
# print(type(a))
# # a is a dictionary

# with open("data.json", "w", encoding="utf-8") as f:
#     json.dump(a, f, ensure_ascii=False, indent=4) # turn a dictionary to a readable file
#     print(json.dumps(a, ensure_ascii=False, indent=4)) # turn a dictionary to a string, and needs to assign an attribute to it.

dict1 = {"name": "Tealbook", "address": "38 cammem street", "CEO": "steph", "num": 198}
print(dict1.keys())


