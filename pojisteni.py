
LOGO = """
_________________________________________

      EVIDENCE POJISTENYCH  
_________________________________________
"""
moznosti = """
1 - Pridat noveho pojistence
2 - Vypsat vsechny pojistence
3 - Vyhledat pojistence
4 - Konec                                          
Vyberte akci: 
"""
class Pojistenec:
    def __init__(self,jmeno,prijmeni,vek,telefonni_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefonni_cislo = telefonni_cislo
    def __str__(self):
        return "Pojistenec jmenem: {0} ,prijemnim: {1} ,vekem: {2} ,telefonnim cislem: {3}".format(
            self.jmeno,self.prijmeni,self.vek,self.telefonni_cislo
        )
def main():
    print(LOGO)
    evi = Evidence()
    while (user_input := input(moznosti)):
        if user_input == "1":
            print("Pridat noveho pojistence")
            evi.pridani_pojistence() 
        elif user_input == "2":
            print("Vypsat vsechny pojistence")
            evi.vypsat_pojistence()
        elif user_input == "3":
            print("Vyhledat pojistence")
            evi.vyhledat_pojistence()
        elif user_input == "4":
            print("Konec")
            break
class Evidence:
    pojistenci = []

    def pridani_pojistence(self):
        jmeno = input("Zadej jmeno pojistence: ")
        prijmeni = input("Zadejte prijmeni: ")
        vek = int(input("Zadejte vek: "))   
        telefonni_cislo = int(input("Zadejte telefonni cislo: "))
        p = Pojistenec(jmeno,prijmeni,vek,telefonni_cislo)
        self.pojistenci.append(p)                                 

    def vypsat_pojistence(self):
        for pojistenec in self.pojistenci:                     
            print(pojistenec)

    def vyhledat_pojistence(self):
        j = input("Zadejte jmeno pojisteneho: ")
        p = input("Zadejte prijmeni pojisteneho: ")
        for pojistenec in self.pojistenci:
            if pojistenec.jmeno == j and p == pojistenec.prijmeni:
                print(pojistenec)
           

if __name__ == "__main__":
    main()

    
              
