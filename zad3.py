import random
import getpass

liczbarund = input("Podaj liczbe rund: ")
trybgry = input("Podaj tryb gry komputer/2 graczy (hot seats): ")

gracz1 = input("nazwe gracza: ")

if trybgry == "komputer":
    gracz2 = "komputer"
elif trybgry == "hot seats" or trybgry == "2 graczy":
    gracz2 = input("nazwe gracza 2: ")
else:
    gracz2 = "komputer"
    print("tryb domyślny (komputer)")

listarund = []
listaznakow = ['p','k','n']

for i in range(int(liczbarund)):

    if gracz2 == "komputer":
        g1znak = input("Podaj znak dla gracza: ")
        g2znak = random.choice(listaznakow)
    else:
        g1znak = getpass.getpass('Podaj znak dla gracza: ')
        g2znak = getpass.getpass('Podaj znak dla gracza 2: ')

    if g1znak.startswith("p") and g2znak.startswith("p"):
        listarund.append("draw")
    if g1znak.startswith("p") and g2znak.startswith("k"):
        listarund.append(gracz1)
    if g1znak.startswith("p") and g2znak.startswith("n"):
        listarund.append(gracz2)
    if g1znak.startswith("k") and g2znak.startswith("p"):
        listarund.append(gracz2)
    if g1znak.startswith("k") and g2znak.startswith("k"):
        listarund.append("draw")
    if g1znak.startswith("k") and g2znak.startswith("n"):
        listarund.append(gracz1)
    if g1znak.startswith("n") and g2znak.startswith("p"):
        listarund.append(gracz1)
    if g1znak.startswith("n") and g2znak.startswith("k"):
        listarund.append(gracz2)
    if g1znak.startswith("n") and g2znak.startswith("n"):
        listarund.append("draw")

g1score = 0
g2score = 0
draws = 0

for s in listarund:
    if s == gracz1:
        g1score += 1
    if s == gracz2:
        g2score += 1
    if s == "draw":
        draws += 1

i = 0
for s in listarund:
    i += 1
    print(f"runda {i}: {s}")

print(f"scores: {gracz1} {g1score} | {gracz2} {g2score} | draws {draws}")

if(g1score > g2score):
    print(f"winner {gracz1}")
elif(g2score > g1score):
    print(f"winner {gracz2}")
else:
    print("draw")