## Projekt board do wyświetlania i dodawania postów

Dodanie klasy Post do modelu

Utworzenie konta administratora
```console
foo@bar:~$ python manage.py createsuperuser
```

Migracje
Po zmianie modelu bazy danych należy wygenerować migrację a następnie ją wyegzekwować.
Bez tego zabiegu nie będziemy mieli możliwości działania na zdefiniowanych typach.
```console
foo@bar:~$ python manage.py makemigrations
foo@bar:~$ python manage.py migrate
```
Panel administratora
Automatycznie generowany znajduje się pod adresem
127.0.0.1:8000/admin

Żeby mieć dostęp do zdefiniowanego przez nas typu danych zdefiniowanego w modelu
musimy go zarejestrować w pliku admin.py konkretnej aplikacji. Przykładowo:

```py
from django.contrib import admin

from posts.models import Post

admin.site.register(Post)

``` 

Uruchamianie testów wykonywać z poziomu katalogu głównego projektu.
```console
foo@bar:~$ python manage.py test
```
