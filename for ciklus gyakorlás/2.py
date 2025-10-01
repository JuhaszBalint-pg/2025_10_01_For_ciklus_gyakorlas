"""
2. Két szám közötti számok
Kérj be két számot a felhasználótól (a és b). Írasd ki az összes számot a és b között.
2.1. Ha b nagyobb, mint a, akkor csökkenő sorrendben írasd ki őket.
"""

a = int(input ("Add meg az A számot "))
b = int(input ("Add meg az B számot "))

for i in range (a, b -1):
    i += 1
    i == a
    print (f" A két szám közötti számok: {i}")