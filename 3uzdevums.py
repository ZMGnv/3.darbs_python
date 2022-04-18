"""
Uzrakstiet programmu Python, lai parādītu 
pirmās un pēdējās krāsas no šī saraksta.

krasa_saraksts = ["sarkans", "zaļš", "balts", "melns"]
"""
list1=["sarkans", "zaļš", "balts", "melns"]
print("pirmā krāsa: ", list1[0])
print("pēdējā krāsa: ", list1[-1])

"""
#V2
lst = ["sarkans", "zaļš", "balts", "melns"]
ans = lst[::len(lst)-1]
print ("Pirmais un pēdējais elemts no saraksta: " + str(ans))
"""