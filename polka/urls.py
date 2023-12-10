"""
URL configuration for biblioteka project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from polka import views

urlpatterns = [
    path('hello/', views.hello_django, name='hello'),
    path('ilosc/<int:ilosc>/', views.napis, name='napis'),
    path('tabliczla/<int:a>/<int:b>/', views.tabliczka, name='tabliczka'),
    path("dodaj_osobe/", views.dodaj_osobe, name='dodaj_osobę'),
    path('osoby/', views.wyswietlanie_osob, name='show_person'),
    path('osoby/<int:id>/', views.osoba, name='detail_person'),
    path('add_book/', views.add_book, name='add_book'),
    path('books/', views.look_book, name='show_books'),
    path('bookid/<int:id>/', views.bookid, name='show_books'),
    path('add_publisher/', views.add_publisher, name='add_publisher'),
    path('publishers/', views.publisher, name='show_publisher'),
    path('add_book_to_cart/<int:book_id>/', views.add_book_to_cart, name='add_to_cart'),
    path('show_cart/', views.show_cart, name='show_cart'),
    path('update_publisher/<int:pk>/', views.UpdatePublisherView.as_view(), name='update_publisher')

]
