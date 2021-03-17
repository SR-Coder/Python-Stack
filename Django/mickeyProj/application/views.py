from django.shortcuts import render, redirect, HttpResponse
from . models import User

# Create your views here.
# DISPLAY METHODS
def dispIndex(request):
    return render(request, 'index.html')

def dispCongrats(request):
    if 'user_id' not in request.session:
        return redirect('/')
    print(request.session.get('user_id'))
    context = {
        'thisUser': User.objects.get(id=request.session['user_id']),
        'people': ['Brice', 'Marc', 'Ryder']

    }
    return render(request, 'congrats.html', context)

def dispMyForm(request):
    # print(request.POST['email'])
    return render(request, 'myForm.html')

# ACTION METHODS
def getEmail(request):
    print(request.POST['email'])
    return redirect('/form')


def login(request):
    user_matching_email = User.objects.filter(email=request.POST['email']).first()
    print(user_matching_email)

    if user_matching_email is not None:
        if user_matching_email.password == request.POST['password']:
            request.session['user_id'] = user_matching_email.id
            return redirect('/congrats')
        else:
            print('password incorrect')
            return redirect('/')
    else:
        print('no user found')
        return redirect('/')

def logout(request):
    request.session.clear()
    # del request.session['sEmail']
    return redirect('/')