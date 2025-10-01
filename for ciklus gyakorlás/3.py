"""
3. Egyszerű jelszókérés
Készíts egy programot, amely egy előre meghatározott jelszót vár el a felhasználótól. A program addig kérdez, amíg a helyes jelszót meg nem adják.
Ha eltalálja a jelszót, jelenjen meg egy üzenet, hogy „Sikeres belépés”.
"""

jelszo = input(print ("Adja meg a jelszót! "))
helyes = "kakaoscsiga"

while jelszo == helyes:
    if jelszo == helyes:
        print ("Helyes jelszó, belépés engedélyezése")
        break

    elif jelszo != helyes:
        print ("Próbálkozzon újra!")