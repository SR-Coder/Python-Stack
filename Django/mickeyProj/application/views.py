from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
# DISPLAY METHODS
def dispIndex(request):
    return render(request, 'index.html')

def dispCongrats(request, name):
    print(request)
    context = {
        'a_name': name,
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