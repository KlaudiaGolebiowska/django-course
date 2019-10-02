## Tworzenie nowego projektu helloworld
Upewnij się, że pracujesz na aktywowanym środowisku wirtualnym wraz z zainstalowana biblioteką Django.

Stwórz nowy projekt Django o nazwie helloworld w wybranej przez siebie lokalizacji za pomocą polecenia:
```console
foo@bar:~$ cd <MOJE_PROJEKTY_DJANGO>
foo@bar:~$ django-admin startproject helloworld
foo@bar:~$ tree

helloworld
├── helloworld
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py 
└── manage.py
```

## Uruchamianie projektu Django

```console
foo@bar:~$ python manage.py runserver
```

## Dodawanie nowej aplikacji do projektu Django

```console
foo@bar:~$ python manage.py startapp pages
foo@bar:~$ tree

helloworld
├── helloworld
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py 
└── manage.py
├── pages
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
```

- admin.py jest plikiem konfiguracyjnym dla wbudowanej aplikacji Django Admin.
- apps.py jest plikiem konfiguracyjnym dla samej aplikacji.
- migrations/ śledzenie wszelkich zmian w pliku models.py, dzięki czemu nasza baza danych i models.py pozostają zsynchronizowane.
models.py to miejsce, w którym definiujemy nasze modele baz danych, które Django automatycznie przetwarza na tabele bazodanowe. 
tests.py jest dla naszych testów specyficznych dla aplikacji.
- views.py to miejsce, w którym obsługujemy logikę żądania/odpowiedzi dla naszej aplikacji internetowej.

Nawet jeśli nasza nowa aplikacja istnieje w ramach projektu Django, Django nie "wie" o tym, dopóki nie dodamy jej wprost. Otwórz plik settings.py i przewiń w dół do INSTALLED_APPS, gdzie zobaczysz już sześć wbudowanych aplikacji Django. Dodaj nasze nowe strony aplikacji na dole:

```py
# helloworld/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'pages'
]
```

## Widoki i URLs

```py
# pages/views.py
from django.http import HttpResponse

def homePageView(request):
    return HttpResponse('Hello, World!')
```

W utworzonej aplikacji należy dodać plik urls.py

```py
# pages/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePageView, name='home')
]
```

W Django widoki określają, jaka zawartość jest wyświetlana na danej stronie, podczas gdy URLConfs określają, dokąd ta zawartość zmierza.
Kiedy użytkownik żąda konkretnej strony, takiej jak strona główna, URLConf używa wyrażenia regularnego, aby zmapować to żądanie do odpowiedniej funkcji widoku, która następnie zwraca pożądane dane.
Innymi słowy, nasz widok wyświetli tekst "Hello, World", podczas gdy nasz adres url zapewni, że gdy użytkownik odwiedzi stronę główną, zostanie przekierowany do właściwego widoku.












