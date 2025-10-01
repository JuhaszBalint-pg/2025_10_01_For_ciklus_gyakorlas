"""
5. Szorzótábla
Írasd ki egy adott szám szorzótábláját 1-től 10-ig. Például, ha a felhasználó 5-öt ad meg, akkor az eredmény legyen:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50
"""

a = int(input("Adj meg egy számot! "))

for i in range(1 , 11):
    print (f"{a} x {i} = {i * a}")