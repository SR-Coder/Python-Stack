from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
# DISPLAY METHODS
def dispIndex(request):
    return render(request, 'index.html')

def dispCongrats(request):
    if 'sEmail' not in request.session:
        return redirect('/')
    print(request.session.get('sEmail'))
    context = {
        'a_name': request.session['sEmail'],
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
    request.session['sEmail'] = request.POST['email']
    return redirect('/congrats')

def logout(request):
    request.session.clear()
    # del request.session['sEmail']
    return redirect('/')