#1. Küsige kasutajalt 2 arvu. Printige kõik paarisarvud mis jäävad nende kahe arvu vahele.
a = int(input("Mis on esimene arv?: "))
b = int(input("Mis on teine arv?: "))

if(a > b):
    while(a > b):
        if(b % 2 != 0):
            b = b + 1
        elif(b % 2 == 0):
            print(b)
            b = b + 1
elif(b > a):
    while(b > a):
        if(a % 2 != 0):
            a = a + 1
        elif(a % 2 == 0):
            print(a)
            a = a + 1
