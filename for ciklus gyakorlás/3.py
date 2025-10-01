"""
3. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""

a = True

while a:
    jelszo = input("Adja meg a jelszót! ")
    if jelszo == "kakaoscsiga":
        print ("Helyes jelszó!")
        a = False
    
    else:
        print ("Próbálkozzon újra!")