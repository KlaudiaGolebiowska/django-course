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

## Kroki konieczne do wykonania z PyCharm
* Otworzenie projektu w Pycharm:
    - W przypadku otworzenia katalogu <MOJE_PROJEKTY_DJANGO>/helloworld nie jest wymagana żadna czynność
    - W przypadku otworzenia katalogu <MOJE_PROJEKTY_DJANGO> należy ustawić katalog <MOJE_PROJEKTY_DJANGO>/helloworld jako 'Sources Root'. Prawy przycisk myszy -> Mark Directory as -> Sources Root.
* Ustawienie wirtualnego środowiska na utworzone wcześniej w PyCharm
* Uruchomienie nowej sesji terminala lub cmd w PyCharm w celu odświeżenia środowiska

## Uruchamianie projektu Django

```console
foo@bar:~$ python manage.py runserver
```
Pod adresem 127.0.0.1:8000 powinieneś zobaczyć stronę początkową Django

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

## Podpięcie URLs aplikacji do URLs projektu.

Prawie skończyliśmy. Ostatnim krokiem jest skonfigurowanie również naszego pliku urls.py na poziomie projektu. Pamiętaj, że powszechne jest posiadanie wielu aplikacji w ramach jednego projektu Django, więc każda z nich potrzebuje własnej trasy.

```py
# helloworld/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
]
```

Pod adresem 127.0.0.1:8000 powinieneś zobaczyć napis Hello World!


## Dodanie dwóch widoków w oparciu o klasy
W utworzonej aplikacji należy zmodyfikować pliki views.py oraz urls.py

```py
#helloworld/pages/views.py
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class DetailsPageView(TemplateView):
    template_name = 'details.html'
```

```py
# pages/urls.py
from django.urls import path
from helloworld.views import HomePageView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home')
]
```

## Dodanie szablonów
Dodanie katalogu templates do projektu w głównym katalogu projektu helloworld a następnie ścieżkę do tego katalogu w pliku settings.py

TEMPLATES = [
    {
        ...
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        ...
    },
]

### base.html
```html
# templates/base.py

<header>
    <a href="{% url 'home' %}">Home</a> === <a href="{% url 'details' %}">Details</a>
</header>

{% block content %}
{% endblock %}
```

### home.html
```html
# templates/home.html

{% extends 'base.html' %}


{% block content %}
<h1>Home Application Page</h1>

<p>New Paragraph</p>
{% endblock %}
```

### details.html
```html
# templates/details.html
{% extends 'base.html' %}

{% block content %}

<h2>Details</h2>
<p>Paragraph Details</p>

{% endblock %}
```