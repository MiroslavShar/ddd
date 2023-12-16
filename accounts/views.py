from django.shortcuts import render, redirect

from polka.models import Person


# Create your views here.

def login(request, user):
    request.session['user_id'] = user.id

def authenticate(username, password):
    try:
        user = Person.objects.get(username=username, password=password)
        return user
    except (Person.DoesNotExist, Person.MultipleObjectsReturned) as f:
        return

def loginView(request):
    if request.method == 'GET':
        return render(request, 'loginform.html')
    else:
        url_redirect = request.GET.get('next', '/')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username, password)
        if user is None:
            return redirect('login')
        login(request, user)
        return redirect(url_redirect)

def login_by_cookie(request):
    request.COOKIES['user_id']
    if request.method == 'GET':
        return render(request, 'loginform.html')
    else:
        url_redirect = request.GET.get('next', '/')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username, password)
        if user is None:
            return redirect('login')
        # login(request, user)
        httpresponse = redirect(url_redirect)
        httpresponse.set_cookie('user_id', user.id)
        return httpresponse



def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect('/')