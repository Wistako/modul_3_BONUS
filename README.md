<!-- ZAD 1 -->
#### Znajdź średnią zmodyfikowanej listy
Twoim zadaniem jest zmodyfikowanie listy przypisanej do zmiennej numbers w taki sposób, aby każdy jej element zaokrąglić do pełnej dziesiątki. Postaraj się nie tworzyć nowej listy będącej zmodyfikowaną listą numbers, lecz zmodyfikować listę numbers.

Po zaokrągleniu każdego elementu listy numbers, pozbądź się jej największego oraz najmniejszego elementu, a następnie do zmiennej mean_number przypisz średnią z ostatecznie zmodyfikowanej listy.

Podsumowując:

zaokrąglij każdy element numbers do pełnej 10 (np. 5 -> 10, 32 -> 30)
znajdź, a następnie pozbądź się największego oraz najmniejszego elementu zmodyfikowanej listy
policz średnią z ostatecznie zmodyfikowanej listy numbers i przypisz ją do zmiennej mean_number

<!-- ZAD 2 -->
#### Stwórz funkcję, która sprawdza, czy możemy zbudować most
Naszym zadaniem jest zbudowanie mostu pomiędzy punktem A i punktem B.

Do dyspozycji mamy płytę oraz łącznik, które mają określone długości.

Płyt nie możemy dzielić na mniejsze części, ustawiamy je jedna obok drugiej. Płyty muszą być połączone ze sobą za pomocą łącznika. Łącznik stanowi połowę długości płyty.

Stwórz funkcję build_bridge, która będzie zwracać wartość True, jeśli mając płytę o długości danej zmienną chunk jesteśmy w stanie zbudować most o długości danej zmienną goal.

Niech funkcja build_bridge zwraca wartość False, jeśli zbudowanie mostu przy założeniu zmiennych chunk oraz goal nie jest możliwe.

Na przykład:

Jeśli goal to 20, a chunk to 2 - wtedy możemy użyć 7 płyt i 6 łączników. Możemy zbudować most, a funkcja powinna zwracać wartość True.

Z drugiej strony, jeśli goal to 18, a chunk to 2 - wtedy NIE możemy zbudować mostu, a funkcja powinna zwracać wartość False.

<!-- ZAD 3 -->

Twojemu szefowi udało się znaleźć informacje o najlepiej sprzedających się modelach samochodów w 2018 roku. Dane, które zdobył nie nadają się niestety do analizy, dlatego poprosił Cię o przetworzenie, aby można było z nich w prosty sposób wyciągać informacje.

Do zmiennej models przypisano listę zawierającą najlepiej sprzedające się samochody 2018 roku uszeregowane od najlepiej sprzedającego się w formacie 'producent - model'.

Do zmiennych sales2018, sales2017 oraz sales2016 przypisano liczbę sprzedanych egzemplarzy tych modeli kolejno w roku 2018, 2017 oraz 2016.

Czyli - najlepiej sprzedającym się modelem samochodu w 2018 roku był: Volkswagen Golf (pierwsza pozycja na liście models). Golf w 2018 roku sprzedał się w ilości 445 754 egzemplarzy (pierwsza pozycja na liście sales2018). Wiemy też, że w 2017 roku sprzedano 483 105 modeli Golfa (pierwsza pozycja na liście sales2017), oraz że w 2016 roku sprzedano 492 952 egzemplarzy Golfa (pierwsza pozycja na liście sales2016).

Niektóre samochody nie były sprzedawane przed 2018 rokiem. W takim przypadku dane o ich sprzedaży zastąpione są wartością 'NA'. Zastąp wszystkie 'NA' cyfrą 0.

Na podstawie otrzymanych danych zbuduj słownik o następującej strukturze i przypisz go do zmiennej cars:

cars = {"brand": {"model1":{"sales":{"2016": 123,
                                     "2017": 456,
                                     "2018": 789}},
                  "model2":{"sales":{"2016": 987,
                                     "2017": 654,
                                     "2018": 321}}
                 },
        "brand2": ... }
Czyli na przykładzie rzeczywistych danych powinien wyglądać on następująco:

cars = {"Opel": {"Corsa":{"sales":{"2016": 264844,
                                   "2017": 232738,
                                   "2018": 217036}},
                 "Astra":{"sales":{"2016": 253483,
                                   "2017": 217813,
                                   "2018": 160275}}
                 },
        "Dacia": ... }
Następnie postaraj się odpowiedzieć na pytania zaprezentowane poniżej:

Który model samochodu z listy najlepiej sprzedawał się w 2017 roku? Odpowiedź przypisz do zmiennej answer1.
Który producent z listy sprzedał najwięcej egzemplarzy samochodów w 2018 roku? Odpowiedź przypisz do zmiennej answer2.
Ile modeli samochodów z listy nie sprzedawało się w 2016 roku, a do sprzedaży weszło w roku 2017? Odpowiedź przypisz do zmiennej answer3.
Który z model samochodu z listy ma najmniej sprzedanych egzemplarzy, jeśli weźmiemy pod uwagę lata 2016, 2017 oraz 2018. Odpowiedź przypisz do zmiennej answer4.
O ile procent wzrosła sprzedaż modeli Forda w 2018 roku w stosunku do roku 2017? Odpowiedź przypisz do zmiennej answer5. Odpowiedź podaj w formacie procentowym jako string. Np. '21%'.
UWAGA! Na potrzeby zadania potraktuj 'VW' i 'Volkswagen' jako osobnych producentów


<!-- ZAD 4 -->
#### Rzuty kostką
Gramy w grę polegającą na rzucaniu typową sześcienną kostką.

W każdej kolejce gracz dwukrotnie rzuca kością. Po dwukrotnym rzuceniu kością wynikiem gracza jest suma wyrzuconych oczek z rzutu numer 1 oraz rzutu numer 2.

Napisz program, który do słownika dict przypisuje pary key i value, gdzie:

key - to możliwy do uzyskania wynik w jednej kolejce (suma oczek w dwóch rzutach)
value - to wszystkie kombinacje rzutów, które składają się na dany key
Wszystkie możliwe kombinacje do uzyskania danego wyniku przechowuj jako zbiór, w którym każdy kolejny element to krotka, której pierwsza wartość to rezultat pierwszego rzutu, a druga wartość to rezultat drugiego rzutu.

Na przykład wywołując:

dice[7]
Wynik powinien zawierać następujące elementy:

{(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)}