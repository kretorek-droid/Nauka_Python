import random

from PIL import Image
from pathlib import Path

from pytania import PYTANIA

pytania = list(PYTANIA)


dir = Path("img")


while pytania:
    komenda = input('\nWpisz "next" aby wylosować następne pytanie: ')

    if komenda == "next":
        para = random.choice(pytania)
        pytanie, odpowiedz, plik = para
        print("\nPytanie:")
        print(pytanie)

        while True:
            komenda_odp = input('\nWpisz "odp" aby wyświetlić odpowiedź: ')
            if komenda_odp == "odp":

                src = dir / plik
                if not src.exists():
                    print("brak pliku obrazka: ", src.resolve())
                else:
                    Image.open(src).show()


                print("\nOdpowiedź:")
                print(odpowiedz)
                break
            else:
                print('\nNieznana komenda. Wpisz "odp"')
        pytania.remove(para)
    else:
        print('\nNieznana komenda. Wpisz "next"')

print("\nKoniec - wszystkie pytania zostały zadane")