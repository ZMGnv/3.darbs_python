"""
Uzrakstiet programmu Python, lai dotajā sarakstā saskaitītu 
cik skaitļi 4 ir  dotajā sarakstā.
"""
lst = []
 
n = int(input("Ievadi elementu skaitu: "))

for i in range(0, n):
    ele = int(input("Ievadi skaitli: "))
 
    lst.append(ele) # adding the element
    elm_count = lst.count(4)
     
print("Dotais saraksts: ", lst)
print('Elementa 4 skaits sarakstā: ', elm_count)
"""
lst=[1,2,3,4,5,4,6,4,7,4,8,4,9,4]
elm_count = lst.count(4)
print('Elementa 4 skaits sarakstā: ', elm_count)
"""