
class Zwierzak:
    __slots__ = ("rasa", "imie", "__kolor", "glod", "higiena", "energia", "humor", "wiek")


    def __init__(self, rasa, imie):
        self.rasa = rasa
        self.imie = imie
        self.wiek = 0
        self.glod = 30
        self.higiena = 40
        self.energia = 70
        self.humor = 10

        self.__kolor = ""


    # def __str__(self):
    #     return (f"imie: {self.imie}\nglod: {self.glod}, higiena: {self.higiena}, energia: {self.energia}, humor: {self.humor}")

    def __kalibrujZakres(self, dane):
        if dane < 0:
            return 0
        if dane > 100:
            return 100
        return dane

    def uplywCzasu(self):
        self.glod += 20
        self.humor -= 10
        self.higiena -= 40
        self.energia -= 30

        self.glod = self.__kalibrujZakres(self.glod)
        self.humor = self.__kalibrujZakres(self.humor)
        self.higiena = self.__kalibrujZakres(self.higiena)
        self.energia = self.__kalibrujZakres(self.energia)

    def jedzenie(self, ile):
        self.glod -= ile*10
        self.humor += ile*5

        self.glod = self.__kalibrujZakres(self.glod)
        self.humor = self.__kalibrujZakres(self.humor)


    def spanie(self, godziny):
        self.humor +=  godziny
        self.energia += godziny
        self.glod +=  godziny

        self.humor = self.__kalibrujZakres(self.humor)
        self.energia = self.__kalibrujZakres(self.energia)
        self.glod = self.__kalibrujZakres(self.glod)


    def bawienie(self, tury):
       self.humor += tury*10
       self.energia -= tury*3
       self.glod += tury*2
       self.higiena -= tury*4

       self.humor = self.__kalibrujZakres(self.tury)
       self.energia = self.__kalibrujZakres(self.tury)
       self.glod = self.__kalibrujZakres(self.tury)
       self.higiena = self.__kalibrujZakres(self.tury)


    def mycie(self):
        self.higiena = 100
        self.humor -= 0.5*self.humor

        self.higiena = self.__kalibrujZakres(100)
        self.humor = self.__kalibrujZakres(0.5*self.humor)


z1 = Zwierzak("Pies","Burek")
z2 = Zwierzak("Kot", "Mruczek")
z3 = Zwierzak("Żółw", "Skorupa")
z4 = Zwierzak("Królik", "Buggs")
z5 = Zwierzak("Rybka", "Karp")
z6 = Zwierzak("Chomik", "Gryzoń")

zwierzaki = []

zwierzaki.append(z1)
zwierzaki.append(z2)
zwierzaki.append(z3)
zwierzaki.append(z4)
zwierzaki.append(z5)
zwierzaki.append(z6)

for el in zwierzaki:
    el.wiek = 2

print(zwierzaki[3].wiek)



while True:
    print("---menu---")
    print("1. Stwórz zwierzaka")
    print("2. Pokaż wszystkie zwierzaki")
    print("3. Opieka nad zwierzakiem")
    print("4. Upływ czasu - kolejna tura")
    print("5. Wyjście z programu")

    wybor = input("Twój wybór: ")
    if wybor == "1":
        print("Wybrałeś 1")
        # rasa = input("Podaj rasę: ")
        imie = input("Podaj imię: ")
        zwierzaki.append(Zwierzak(imie))
    elif wybor == "2":
        print("Wybrałeś 2")
        for i, v in enumerate(zwierzaki):
            print("Pod indeksem: " , i , " jest zwierzak o imieniu: ", v.imie)
    elif wybor == "3":
        print("Wybrałeś 3")
        nr = input("Podaj nr zwierzaka:")
        wybrany = zwierzaki[int(nr)]
        print(f"Wybrałeś zwierzaka o imieniu {wybrany.imie}. Co robimy?")
        print("a - karm, b - myj, c- baw, d - usypianie")
        decyzja = input("Twoja decyzja: ")
        if decyzja == "a":
            print("Zdecydowałeś o a")
            wybrany.jedzenie(3)
        elif decyzja == "b":
            print("Zdecydowałeś o b")
        elif decyzja == "c":
            print("Zdecydowałeś o c")
        else:
            print("Nie ma takiej opcji")
    elif wybor == "4":
        print("Wybrałeś 4 - Leci tura")
        for i, v in enumerate(zwierzaki):
            v.uplywCzasu()
            print(f"Pod indeksem: {i}, imie: {v.imie} ,glod: {v.glod}, higiena: {v.higiena}, energia: {v.energia}, humor: {v.humor}")
    elif wybor == "5":
        print("Wybrałeś 5")
        break
    else:
        print("Nie ma takiej opcji")

















