"""
Ir uzrakstīta programma Python, izmantojot funkciju.
Summējot divus norādītos veselos skaitļus. 
Tomēr, ja summa ir no 15 līdz 20, tā atgriezīs 20.

"""
def getSum(n1, n2):
    getSum=n1+n2
    if getSum >=15 and getSum < 20:
        return 20
sum=getSum(15,3)
print(sum)