from django.urls import path

from pages.views import HomePageView, DetailsPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('details/', DetailsPageView.as_view(), name='details')
]
