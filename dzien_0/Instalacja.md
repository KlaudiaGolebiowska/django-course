# Instalacja
Poniższe kroki powinny być Ci znane z bloku Python Technologie. Przed wykonaniem kroków sprawdź, które są konieczne.
* Zainstaluj python3
* Dodaj do zmiennej środowiskowej PATH katalog
    - Windows: KatalogPython oraz KatalogPython/Scripts
    - Linux, Mac: KatalogPython/bin
* Upewnij się, że z poziomu terminala lub konsoli cmd możesz uruchomić pythona oraz wywołać managera pakietów pip
```console
foo@bar:~$ python3
foo@bar:~$ pip3
```
* Zainstaluj pakiet virtualenv za pomocą managera pakietów pip, oraz zweryfikuj czy możesz je uruchomić z poziomu terminala lub cmd.
```console
foo@bar:~$ pip install virtualenv
foo@bar:~$ virtualenv
```
* Utwórz nowe środowisko wirtualne w znanym Ci położeniu za pomocą narzędzia virtualenv
```console
foo@bar:~$ virtualenv -p python3 nazwa
```
* Uaktywnij środowisko za pomocą skryptu activate a następnie zainstaluj bibliotekę django:

```console
Linux / Mac: foo@bar:~$ source activate
Windows:     foo@bar:~$ activate.bat

(env_name) foo@bar:~$ pip install django
```
* Musisz mieć możliwość i wiedzieć jak:
    - Uruchomić python3 z terminala lub cmd
    - Uruchomić managera pakietów pip z terminala lub cmd
    - Utworzyć nowe środowisko wirtualne za pomocą narzędzia virtualenv w wybranym przez siebie katalogu z terminala lub cmd
    - Aktywować środowisko wirtualne z poziomu terminala lub cmd
    - Zainstalować bibliotekę django przy użyciu pip.

* __Zaznaczam, że instrukcja jest krótka i poglądowa. Nie gwarantuję, że wszystkie kroki zadziałają bezproblemowo na każdym komputerze.__ Jednakże powyższa lista operacji będzie nam konieczna do realizacji kolejnych zajęć.