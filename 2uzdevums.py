"""
    Funkcija koks akceptē trīs argumentus - skaiļus viens, divi un trīs, 
    aprēķina to summas kvadrātu un atgriež to.
    Pārbaudiet funkcijas darbību ar dažādiem argumentiem, 
    parādot skaitli ar diviem simboliem aiz komata.

    Argumenti:
        viens {int vai float} -- pirmais skaitlis
        divi {int vai float} -- otrais skaitlis
        tris {int vai float} -- trešais skaitlis
    Atgriež:
        int vai float -- argumentu summa
"""
def summa(viens, divi, tris):
  rez=(viens+divi+tris)**2
  rez="{:.2f}".format(rez)
  print(rez)
  return 0

aba=summa(2,1,2)
print(aba)