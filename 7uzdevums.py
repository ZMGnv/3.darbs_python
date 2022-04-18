"""
Uzrakstiet programmu Python, lai aprēķinātu 
trīs ievadīto skaitļu summu.
Ja ievadītās vērtības ir vienādas, atgrieziet summu, trīskāršojot to.
"""
num1=int(input("Ievadi skaitli nr1: "))
num2=int(input("Ievadi skaitli nr2: "))
num3=int(input("Ievadi skaitli nr3: "))

def getSum(num1, num2, num3):
    Sum = num1+num2+num3
    if num1==num2 and num2==num3:
        Sum=(num1+num2+num3)*3
    return Sum
Sum=getSum(num1, num2, num3)
print(Sum)