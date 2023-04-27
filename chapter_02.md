[[_TOC_]]
# Wstęp do programowania
## Algorytm - "przepis" na wykonanie jakiegoś zadania
## Paradygmaty programowania - wzorzec programowania komputerów przekładany w danym okresie rozwoju informatyki ponad inne lub ceniony w pewnych okolicznościach lub zastosowaniach. Definiuje sposób patrzenia programisty na przepływ sterowania i wykonywanie programu komputerowego
* programowanie imperatywne - skupia się na poszczególnych krokach, które prowadzą do rozwiążania problemu. (ciąg instrukcji) 
* programowanie delkaratywne - mówimy komputerowi co ma zrobić, ważny jest wynik, a nie sposób jego osiągnięcia. (skupienie na celu)
* programowanie funkcyjne - opiera się na pewnych specyficznych mechanizmach. kładzie się nacisk na obliczanie wartości funkcji, ich kompozycje oraz funkcje wyższego rzędu
* programowanie proceduralne - Pisany kod jako zbiór kolejnych instrukcji, które komputrer ma wykonać
* programowanie obiektowe - bazuje na klasach oraz obiektach. Za ich pomocą definiujemy komponenty, z których można korzystać wielokrotnie
## Języki programowania
* C - imperatywny język ogólnego przeznaczenia, stworzony przez Dennisa Ritchiego
* C++ - język ogólnego przeznaczenia,zaprojektowany przez Bjarne Stroustrupa jako rozszerzenie języka C o obiektowe mechanizmy abstrakcji danych i silną statyczną kontrolę typów. 
* Java - współbieżny, oparty na klasach, obiektowy język programowania ogólnego zastosowania. Stworzony przez Jamesa Goslinbga. Jest językiem tworzenia programów źródłowych kompilowanych do kodu bajtowego, czyli postaci wykonywanej przez maszynę wirtualną
* javascript - skryptowy oraz wieloparadygmatowy język, stworzony przez Brendana Eicha, najczęściej stosowany na stronach WW
* Python - język wysokiego poziomu ogólnego przeznaczenia, o rozbudowanym pakiecie bibliotek standardowych, którego ideą przewodnią jest czytelność i klarowność kodu źródłowego. Składnia cechuje się przejrzystością izwięzłością
* PHP - interpretowany, skryptowy język zaprojektowany do generowania stron WWW i budowania aplikacji webowych w czasie rzeczywistym
* Rust - kompilowany język programowania ogólnego przeznaczenia. Stworzony z myślą o "bezpieczeństwie, współbieżnośći i praktyczności"
* Go - wieloparadygmatowy język, który łączy w sobie łatwość pisania aplikacji charakterystyczną dla języków dynamicznych, jak również wydajność języków kompilowanych
* MATLAB - program komputerowy będący interaktywnym środowiskiem do wykorzystania obliczeń naukowych i inżynierskich, oraz do tworzenia symulacji komputerowych
* Scala - język łączący cechy języków funkcyjnych i obiektowych
* Haskell - język funkcyjny
* HTML - język znaczników stosowany do tworzenia dokumentów hipertekstowych
* CSS - język służący do opisu formy prezentacji stron WWW
* LaTeX - oprogramowanie do zautomatyzowanego składu tekstu, a także związany z nim język znaczników, służący do formatowania dokumentów tekstowych i tekstowo-graficznych
* markdown - język znaczników ze składnią formatowania zwykłego tekstu
* SQL - strukturalny oraz deklarytywny język zapytań. Język dziedzinowy do tworzenia, modyfikacji relacyjnych baz dabych oraz do umieszczania i pobierania danych z tych baz
### kompilowane - język, który by uzyskać działający program musi zostac uprzednio skompilowany do postaci kodu maszynowego
### interpretowane - język, który zazwyczaj jest implementowany w formie interpretera, a nie kompilatora. Program w tym języku nie jest kompilowany, lecz przechowywany w postaci kodu źródłowego i dopiero podczas uruchomienia wczytywany
# Python
## RELP -proste, interaktywne środowisko programowania
## shell - program komputerowy pełniący rolę pośrednika, pomiędzy systemem operacyjnym lub aplikacjami, a użytkownikiem, przyjmując jego polecenia i "wprowadzając" wyniki działania programów
## Typy danych
#### operatory matematyczne :
* + - dodawanie
* - - odejmowanie
* / - dzielenie 
* * - mnożenie
* % - reszta z dzielenia
### int - reprezentuje liczbę całkowitą
### float - reprezentuje liczby zmiennoprzecinkowe
### bool - watośc logiczna: true or false
### string - reprezentuje tekstowy typ danych, przechowuje ciągi znaków
## Struktury danych
### list - tworzy listę
### tuple - krotka, odzwierciedlenie matematycznej n-ki. Uporządkowany ciąg wartości, przechowują stale wartości o różnych typach danych, lecz nie można zmodyfikować żadnego elementu
### set - Zbiór, sklada się z elementów. Elementy mogą być liczbami lub dowolnymi obiektami, które da się reprezentować za pomocą bitów w komputerze
### dict - słownik, struktura danych reprezentująca dynamiczny zbiór elementów. 
### dostęp przez referrencje vs wartość
### generatory
#### yield - pozwala na powrót do metody wywołującej, metoda wywołująca wykonuje swoje zadanie, a następnie powrót do kolekcji w miejscu, w którym ta kolekcja została opuszczona
## Instrukcje sterujące przepływem (słowa kluczowe)
### if
#### not
#### and
#### or
### if-else
### if-elif
### if-elif-else
### for
#### in
#### break
#### continue
### while
### try-except
### with
#### otwieranie i czytanie plików, csv
### with-as
## list/dict comprahensions
## Funkcje
### def
### dekoratory
# Projekt
Napisz program do wyznaczania tras turystycznych. Niech program zna nazwy lokalizacji i odległości między nimi. Niech program pyta użytkownika skąd chce wyruszyć i jak długą pętle (pętla to wycieczka kończąca się w punkcie startu) chce zrobić i niech wypisuje wszystkie możliwe pętle o długości mniejszej lub równej długości podanej przez użytkownika.
