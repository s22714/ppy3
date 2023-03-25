import random

miastadoodwiedzenia = ['Warszawa'
    ,'Kraków'
    ,'Wrocław'
    ,'Łódź'
    ,'Poznań'
    ,'Gdańsk'
    ,'Szczecin'
    ,'Bydgoszcz'
    ,'Lublin'
    ,'Białystok']

listakoncowa = []

while len(listakoncowa) < 10:
    x = random.randint(0,9)
    if miastadoodwiedzenia[x] not in listakoncowa:
        listakoncowa.append(miastadoodwiedzenia[x])

for s in listakoncowa:
    print(s)