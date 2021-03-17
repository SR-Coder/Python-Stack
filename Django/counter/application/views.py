from django.shortcuts import render, redirect

# Create your views here.
# Display Method
def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
        # context = {
        #     'currentVal': request.session['counter']
        # }
        return render(request, 'index.html')
    else:
        request.session['counter']+=1
        # context = {
        #     'currentVal': request.session['counter']
        # }
        return render(request, 'index.html')


# Action Method
def reset(request):
    print('in destroy session method')
    del request.session['counter']
    return redirect('/')