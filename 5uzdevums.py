"""
Uzrakstiet Python programmu, lai iegūtu 
starpību starp ievadīto skaitli un 17.
Ja skaitlis ir lielāks par 17, iegūstiet absolūtās starpības 
dubultu.
"""
a=int(input("Ievadi skaitli: "))
sum=a-17
if sum>17 and sum>0:
    print("Starpības dubulta summa: ",sum*2)
else:
    print("Starpība: ",sum)