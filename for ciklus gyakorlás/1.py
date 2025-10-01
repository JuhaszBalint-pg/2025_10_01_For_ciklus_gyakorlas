"""
1. Összegszámítás
Kérj be egy egész számot (pl. 10; 13;  20…), és számítsd ki az 1-től a megadott számig terjedő egész számok összegét.
"""

print ("Adj meg egy egész számot!")
x = int (input ("") )
y = 0

for i in range(x):
    y += i
    
print (f"A 0 és megadott szám közötti számok összege: {y-1}")