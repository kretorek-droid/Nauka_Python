# x = 3
# print ("x: " , x)
# i = 3.423
# print ("i+x: ", i+x)
# print (7/2)

# k = "Hello World!"
# j = '\n'

# print (x,i,k,j)

# if x>2:
#   print ("warunek" + j + "spelniony")
# else:
#   print ("warunek niespelniony")


# print("max:", max(tablica))

# tablica.append(123)

# for el in tablica:
#   if el > 24:
#     print(el)

# for  el in  tablica:
#  print(el*10)


# print('*'*10)


# for i in range(10):
#   print(i)


# print("------------------------------------")

# def suma1(a,b):
#   print (a + b)

# def suma2(a,b):
#    print (a + b)
#    return a+b


# suma1(2,3)

# print(   suma2(4,3)   )


# def tabMax(tab):
#   max = tab[0]
#   for el in tab:
#     if el > max:
#       max = el
#   return max


# print(tabMax(tablica))


# def tabSuma(tab):
#   suma = 0
#   for el in tab:
#     suma += el
#   return suma

# print(tabSuma(tablica))


# def iloscParzystych(tab):
#   ilosc_parzystych = 0
#   for el in tab:
#     if el%2 == 0:
#       ilosc_parzystych += 1
#   return ilosc_parzystych


# print(iloscParzystych(tablica))

tablica = [3, 7, 34, 23, 43, 444, 12, 77]


def tylkoParzyste(tab):
    tab_parzyste = []
    for el in tab:
        if el % 2 == 0:
            tab_parzyste.append(el)
    return tab_parzyste


print(tylkoParzyste(tablica))

imiona = ["Adam", "Ewa", "Kajfasz", "Annasz", "Abraham", "Mojżesz"]


def tylkoNalitereA(tab):
    tab_tylko_na_litere_a = []
    for el in tab:
        if el[0] == 'A':
            tab_tylko_na_litere_a.append(el)
    return tab_tylko_na_litere_a


print(tylkoNalitereA(imiona))


def tabKwadraty(tab):
    tab_kwadraty = []
    for el in tab:
        tab_kwadraty.append(el * el)
    return tab_kwadraty


print(tabKwadraty(tablica))


# [3,7,34,23, 43, 444, 12,77]
def czyElementWystepuje(tab, szukana):
    for el in tab:
        if el == szukana:
            return True
    return False


w_szukana = 312312312

if czyElementWystepuje(tablica, w_szukana):
    print("Element wystepuje w tablicy")
else:
    print("Element nie wystepuje w tablicy")
