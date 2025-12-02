import random
a=random.randint(1, 99)
b=random.randint(1, 99)
c = a + b
print("Löse folgende Aufgabe", a,"+", b)

eingabe = int(input("Hier kannst du die Lösung eingeben: "))
if c == eingabe:
    print("das ist richtig")
else:
    print("Das ist falsch")
    print(" das Ergebnis lautet:", c)
    
    if eingabe>0:
    print("deine eingabe ist positiv")
elif eingabe <0:
    print("deine Eingabe ist negativ")
else:
    print("deine Eingabe ist gleich 0")  
    
    
    
d=random.randint(1, 99)
e=random.randint(1, 99)
f = d * e
print("Löse folgende Aufgabe", d,"*", e)

eingabe = int(input("Hier kannst du die Lösung eingeben: "))
if f == eingabe:
    print("das ist richtig")
else:
    print("Das ist falsch")
    print(" das Ergebnis lautet:", f)
    
    import random
eingabe = int(input("gib eine Zahl ein"))
x = eingabe


if x>0:
    print("x ist positiv")
elif x<0:
    print("x ist negativ")
else:
    print("x ist gleich 0")    