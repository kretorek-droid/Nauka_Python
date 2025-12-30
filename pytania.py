PYTANIA = [
    (
        "Kiedy system liniowy stacjonarny jest niestabilny?",
        "System liniowy stacjonarny jest niestabilny, jeżeli jego odpowiedź impulsowa zdąża do nieskończoności przy czasie zdążającym do nieskończoności",
        ""
    ),
    (
        "Kiedy system liniowy stacjonarny jest asymptotycznie stabilny?",
        "System liniowy stacjonarny jest asymptotycznie stabilny, jeżeli jego odpowiedź impulsowa zdąża do 0 przy czasie zdążającym do nieskończoności",
        ""
    ),
    (
        "Kiedy system liniowy stacjonarny jest stabilny (stabilny krytycznie)?",
        "System liniowy stacjonarny jest stabilny (stabilny krytycznie), jeżeli jego odpowiedź impulsowa ani nie zanika, ani nie wzrasta nieskończenie, lecz pozostaje stała lub oscyluje z niemajlejącą do zera amplitudą przy czasie zdążającym do nieskończoności",
        ""
    ),
    (
        "Podaj warunek konieczny kryterium Hurwitza/Routha",
        "Jeżeli system liniowy stacjonarny jest stabilny asymptotycznie, to wszystkie współczynniki jego równania charakterystycznego są niezerowe i dodatnie  (w ogólności - jednego znaku)",
        ""
    ),
    (
        "Podaj warunek wystarczający kryterium Hurwitza",
        "Jeżeli wyznacznik macierzy Hurwitza (wyznacznik Hurwitza) i wszystkie podwyznaczniki wyznacznika Hurwitza są większe od zera to system liniowy stacjonarny jest stabilny asymptotycznie.Jeżeli wyznacznik Hurwitza i/lub jeden lub więcej podwyznaczników Hurwitza jest równy zeru to system jest stabilny (stabilny krytycznie).",
        ""
    ),
    (
        "Co to są zmienne przepływu?",
        "Zmienne przepływu są wielkościami, które wyrażają intensywność przepływu określonej wielkości przez element obiektu/systemu, bądź szybkość zmian w czasie określonej wielkości",
        ""
    ),
    (
        "Co to są zmienne naporu?",
        "Zmienne naporu są wielkościami, które są miarą różnicy wartości określonej wielkości na dwóch końcach elementu obiektu/systemu, wyrażają napór jakiemu poddany jest element",
        ""
    ),
    (
        "Czym zajmuje się automatyka?",
        "Automatyka jest dziedziną wiedzy, która zajmuje się możliwościami ograniczania udziału lub eliminowania udziału człowieka w sterowaniu różnorodnymi obiektami/systemami",
        ""
    ),
    (
        "Co to jest sterowanie?",
        "Sterowanie to celowe oddziaływanie czegoś/kogoś (element, który oddziałuje) na coś/kogoś (element, na który skierowane jest oddziaływanie",
        ""
    ),
    (
        "Co to jest wspomaganie decyzji?",
        "Wspomaganie decyzji jest dziedziną wiedzy, która zajmuje się możliwościami pomagania człowiekowi w procesach podejmowania różnorodnych decyzji związanych z oddziaływaniem na obiekty bądź środowisko",
        ""
    ),
    (
        "Co to jest automatyczne sterowanie?",
        "Automatyczne sterowanie jest dziedziną wiedzy, która zajmuje się możliwościami eliminowania udziału człowieka z procesów sterowania różnorodnymi obiektami bądź środowiskiem",
        ""
    ),
    (
        "Co to jest obiekt/system sterowany?",
        "Coś na co wywierane jest celowe oddziaływanie",
        ""
    ),
    (
        "Co to jest układ/system sterujący?",
        "Coś co celowe oddziałuje",
        ""
    ),
    (
        "Podaj przykłady obiektu sterowanego",
        "Np. zbiornik z cieczą, piec gazowy, brama garażowa, statek pasażerski, rurociąg z cieczą, samolot, młyn kulowy, samochód, robot przemysłowy",
        ""
    ),
    (
        "Podaj przykłady procesu sterowanego",
        "Np. proces destylacji/rektyfikacji - kolumna rektyfikacyjna, procesy odzysku siarki - instalacja Clausa, procesy biologiczne w oczyszczalni ścieków - reaktor biologiczny, procesy wytapiania w hutach - wielki piec, żeliwiak, procesy produkcji energii cieplnej, elektrycznej, itd. - elektrownia  wodna, elektrownia jądrowa",
        ""
    ),
    (
        "Podaj przykład układu sterującego (urządzenia sterującego)",
        "Np. operator procesu (sterowanie ręczne), regulator aparaturowy - wielofunkcyjny, sterownik programowalny (PLC), programowalny sterownik automatyki (PAC), komputer przemysłowy",
        ""
    ),
    (
        "Co to jest system?",
        "To wyodrębniony przez nas fragment rzeczywistości, którego właściwości chcielibyśmy badać i który składa się z więcej niż jednego niepodzielnego elementu, a elementy te tworzą funkcjonalną całość",
        ""
    ),
    (
        "Co to jest otoczenie?",
        "To pozostająca poza systemem część rzeczywistość, z którą system może być powiązany dwoma rodzajami zmiennych - wielkościami wejściowymi i wyjściowymi",
        ""
    ),
    (
        "Co to wielkości wejściowe (wymuszenia systemu)?",
        "To wielkości, którymi otoczenie oddziałuje na system",
        ""
    ),
    (
        "Co to wielkości wyjściowe (reakcje systemu)?",
        "To wielkości, którymi system oddziałuje na otoczenie",
        ""
    ),
    (
        "Podaj przykłady urządzenia pomiarowego",
        "Np. urządzenia pomiaru temperatury, urządzenia pomiaru ciśnienia, urządzenia pomiaru przepływu, urządzenia pomiaru poziomu",
        ""
    ),
    (
        "Podaj przykłady urządzenia wykonwaczego",
        "Np. zawory, przepustnice, zasuwy, pompy, dmuchawy, grzałki, wentylatory, dozowniki, podajniki, przenośniki, chwytaki",
        ""
    ),
    (
        "Wymień podstawowe struktury systemu sterowania (automatycznego)",
        "Otwarty układ sterowania, otwarty układ sterowania ze sprzężeniem w przód od wielkości zakłócającej obiektu sterowanego (z pomiarem wielkości zakłócającej), zamknięty układ sterowania ze sprzężeniem zwrotnym od wielkości sterowanej (zamknięty układ sterowania)",
        ""
    ),
    (
        "Narysuj otwarty  układ sterowania ze sprzężeniem zwrotnym w przód od wielkości zakłócającej obiektu sterowanego (z pomiarem wielkości zakłócającej obiektu)",
        "",
        "Odpowiedź w pliku do wykładu 1"
    ),
    (
        "Co to informacyjne sprzężenie w przód?",
        "Informacyjne sprzężenie w przód to przekazanie informacji o wartości wielkości zakłóceniowych (ogólniej o wartościach wielkości przyczynowych) oddziałujących na obiekt sterowany do układu sterującego",
        ""
    ),
    (
        "Narysuj otwarty układ sterowania",
        "",
        "Odpowiedź w pliku do wykładu 1"
    ),
    (
        "Narysuj zamknięty układ sterowania ze sprzężeniem zwrotnym od wielkości sterowanej (zamknięty układ sterowania)",
        "",
        "Odpowiedź w pliku do wykładu 1"
    ),
    (
        "Co to informacyjne sprzężenie zwrotne?",
        "Informacyjne sprzężenie zwrotne to przekazanie informacji o aktualnej wartości wielkości sterowanej (ogólnie o wartościach wielkości skutkowych) do układu sterującego",
        ""
    ),
    (
        "Co to ujemne sprzężenie zwrotne?",
        "Ujemne sprzężenie zwrotne to takie skonfigurowanie sprzężenia zwrotnego, aby informacja o efektach/wynikach sterowania przeciwdziałała niepożądanym zmianom wielkości sterowanej (wielkości sterowanych)",
        ""
    ),
    (
        "Co to regulator?",
        "Regulator to urządzenie generujące sygnał sterujący",
        ""
    ),
    (
        "Co to układ regulacji?",
        "Układ regulacji to system sterowania z ujemnym sprzężeniem zwrotnym",
        ""
    ),
    (
        "Co to urządzenie wykonawcze?",
        "Urządzenie wykonawcze (UW)  to urządzenie realizujące zadania urządzenia sterującego (regulatora R) i bezpośrednio wpływające na obiekt sterowania OS, podstawowe elementy: element nastawczy, element napędowy",
        ""
    ),
    (
        "Co to urządzenie pomiarowe?",
        "Urządzenie pomiarowe (UP)  to urządzenie służące do przetworzenia wielkości sterowanej y na sygnał odpowiedni do wprowadzenia do urządzenia sterującego (regulatora R), podstawowe elementy: czujnik, przetwornik",
        ""
    ),
    (
        "Wymień 3 elementarne struktury połączeń elementów w systemie.",
        "Połączenie szeregowe, połączenie równoległe, połączenie ze sprzężeniem zwrotnym",
        ""
    ),
    (
        "Na czym polega pierwsza grupa przekształceń schematów blokowych? Wymień nazwy przekształceń  należących do tej grupy.",
        "Pierwsza grupa polega na redukcji trzech elementarnych struktur połączeń do pojedynczego elementu. Przekształcenia należące do tej grupy to: 1. Redukcja połączenia szeregowego; 2. Redukcja połączenia równoległego; 3. Redukcja połączenia ze sprzężeniem zwrotnym",
        ""
    ),
    (
        "Za pomocą rysunku przedstaw redukcję połączenia szeregowego",
        "",
        "Obraz1.png"
    ),
    (
        "Za pomocą rysunku przedstaw redukcję połączenia równoległego",
        "",
        "Obraz2.png"
    ),
    (
        "Za pomocą rysunku przedstaw redukcję połączenia ze sprzężeniem zwrotnym",
        "",
        "Obraz4.png"
    ),
    (
        "Na czym polega druga grupa przekształceń schematów blokowych? Wymień nazwy przekształceń  należących do tej grupy.",
        "Druga grupa polega na przekształceniu schematu w celu uzyskania w nim jednej z trzech elementarnych struktur. Przekształcenia należące do tej grupy to :  1. Przeniesienie węzła sumacyjnego z wejścia elementu na jego wyjście; 2. Przeniesienie węzłą sumacyjnego z wyjścia elementu na jego wejście; 3. Przeniesienie węzła zaczepowego z wejścia elementu na jego wyjście; 4. Przeniesienie węzła zaczepowego z wyjścia elementu na jego wejście; 5. Zamiana miejscami węzłów sumacyjnych sąsiadujących ze sobą; 6. Zamiana miejscami węzłów zaczepowych sąsiadujących ze sobą; 7. Zamiana miejscami węzła sumacyjnego i zaczepowego sąsiadujących ze sobą; 8. Zamiana miejscami węzła zaczepowego i sumacyjnego sąsiadujących ze sobą",
        ""
    ),
    (
        "Za pomocą rysunku przedstaw przeniesienie węzła sumacyjnego z wejścia elementu na jego wyjście",
        "",
        "Obraz4.png"
    ),
    (
        "Za pomocą rysunku przedstaw przeniesienie węzła sumacyjnego z wyjścia elementu na jego wejście",
        "",
        "Obraz4.png"
    ),
    (
        "Za pomocą rysunku przedstaw przeniesienie węzła zaczepowego z wyjścia elementu na jego wejście",
        "",
        "Obraz4.png"
    ),
    (
        "Za pomocą rysunku przedstaw zamianę miejscami węzła zaczepowego i sumacyjnego sąsiadujących ze sobą",
        "",
        "Obraz4.png"
    ),
    (
        "Za pomocą rysunku przedstaw zamianę miejscami węzła sumacyjnego i zaczepowego sąsiadujących ze sobą",
        "",
        "Obraz4.png"
    ),
    (
        "Za pomocą rysunku przedstaw zamianę miejscami węzłów sumacyjnych sąsiadujących ze sobą",
        "",
        "Obraz4.png"
    ),
    (
        "Za pomocą rysunku przedstaw zamianę miejscami węzłów zaczepowych sąsiadujących ze sobą",
        "",
        "Obraz4.png"
    ),
    (
        "Za pomocą rysunku przedstaw przeniesienie węzła zaczepowego z wyjścia elementu na jego wejście",
        "",
        "Obraz4.png"
    )
]