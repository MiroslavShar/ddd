from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from polka.models import Person, Book, Publisher, Cart


def index(request):
    user_id = request.session.get('user_id')
    if user_id is not None:
        user = Person.objects.get(pk = user_id)
    else:
        user = "dupa"
    return render(request, 'base.html', {'osoba' : user})

def hello_django(request):
    return HttpResponse("Witaj Django")

def napis(request, ilosc):
    s = ""
    for x in range(ilosc):
        s+= "dupa<br>"
    return HttpResponse(s)


def tabliczka(request, a, b):
    a = int(a)
    tab = "<table border=1>"
    for x in range(1, a+1):
        tab += "<tr>"
        for y in range(1, b+1):
            tab += f"<td>{x*y}</td>"
        tab+= "</tr>"
    tab += "</table>"
    return HttpResponse(tab)


def dodaj_osobe(request):
    if request.method == "GET":
        response = render(request, 'dodaj_osobe.html')
        return response
    else:
        imie = request.POST['first_name']
        nazwisko = request.POST['last_name']
        p = Person (first_name=imie, last_name=nazwisko)
        p.save()
        return render(request, 'osobanew.html', context={'osoba':p})


def wyswietlanie_osob(request):
    osoby = Person.objects.all()
    first_name = request.GET.get('first_name', '')
    last_name = request.GET.get('last_name', '')
    if first_name != '':
        osoby = osoby.filter(first_name__icontains=first_name)
    if last_name != '':
        osoby = osoby.filter(last_name__icontains=last_name)
    return render(request, 'Cosby.html', context={'persons':osoby})

def osoba(request, id):
    o = Person.objects.get(id=id)
    return render(request, 'o.html', {'osoba':o})


def add_book(request):
    if request.method == "GET":
        authors = Person.objects.all()
        response = render(request, 'add_book.html', context={'authors':authors})
        return response
    else:
        title = request.POST['title']
        author_id = request.POST.get('author')
        autor = Person.objects.get(id=author_id)
        p = Book(title=title, author=autor)
        p.save()
        return render(request, 'booknew.html', context={'book':p})
        # return HttpResponse(f'probujesz dodac książkę o nazwie {title} i autorze{author} do bazy')

def look_book(request):
    books = Book.objects.all()
    author = Person.objects.all()
    author_id = request.GET.get('author', '')
    title = request.GET.get('title', '')
    if author_id != '':
        books = books.filter(author_id = author_id)
    books = books.filter(title__icontains = title)
    return render(request, 'books.html', context={'books':books, 'author':author})

def bookid(request, id):
    b = Book.objects.get(id=id)
    return render(request, 'bookid.html', {'book':b})

def add_publisher(request):
    if request.method == "GET":
        publishers = Publisher.objects.all()
        response = render(request, 'add_publisher.html', context={'publisher': publishers})
        return response
    else:
        name = request.POST['name']
        city = request.POST.get('city')
        p = Publisher(name=name, city=city)
        p.save()
        return render(request, 'publishernew.html', context={'publisher': p})

def publisher(request):
    publishers = Publisher.objects.all()
    name = request.GET.get('name', '')
    city = request.GET.get('city', '')
    if city != '':
        publishers = publishers.filter(city__icontains=city)
    if name != '':
        publishers = publishers.filter(name__icontains=name)
    return render(request, 'publishers.html', context={'publishers': publishers})

def add_book_to_cart(request, book_id):
    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect(f'/login/?next=/add_book_to_cart/{book_id}')
    book = Book.objects.get(pk=book_id)
    user = Person.objects.get(pk=user_id)
    cart, created = Cart.objects.get_or_create(owner=user)
    cart.books.add(book)
    messages.add_message(request, messages.INFO, f"Udało się dodać książke do koszyka{book.title}")
    return redirect('/books/')


def show_cart(request):
    user_id = request.session.get('user_id')
    if user_id is None:
        return redirect(f'/login/?next=/cart')
    cart = Cart.objects.get(owner_id=user_id)
    return render(request, 'cart_list.html', {'cart': cart})




