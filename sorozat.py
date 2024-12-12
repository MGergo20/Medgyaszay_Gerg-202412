import random

def fejek_szama():
    lista = []
    i:int = 0
    fejek:int = 0

    for i in range(7):
        lista.append(random.randint(0,1))


    for i in range(len(lista)):
        if lista[i] == 1:
            print("FEJ", end=" ")
        else:
            print("ÍRÁS", end=" ")
        if i < len(lista) - 1:
            print("-", end=" ")


    for dobas in lista:
        if dobas == 1:
            fejek +=1
    return fejek

def konzol_kiir(fejek):
    print("\nII/D, E: ")
    print(f"A fejek száma: {fejek}")

def file_kiir(fejek):
    fajlom = open("fejek.txt", "w", encoding="UTF-8")
    
    fajlom.write("II/F\n")
    fajlom.write(f"A fejek száma: {fejek}.")
    fajlom.close()
    
