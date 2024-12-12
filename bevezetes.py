def adatbekeres():
    jatekos_neve:str = str(input("Játékos neve: "))
    szerepkore:str = str(input("\nSzerepköre:"))
    
    if (szerepkore == "varázsló"):
        print(f"Üdvözlünk {jatekos_neve}, 2 életed van!")
    elif (szerepkore == "harcos"):
        print(f"Üdvözlünk {jatekos_neve}, 10 életed van!")
    else:
        print(f"Üdvözlünk {jatekos_neve}, 8 életed van!")