from django.shortcuts import render, redirect, HttpResponse
from . models import User, Review, Trip

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
        'allReviews': Review.objects.all(),
        'allTrips': Trip.objects.all(),

    }
    return render(request, 'congrats.html', context)

def dispMyForm(request):
    # print(request.POST['email'])
    return render(request, 'myForm.html')

def dispNewTrip(request):
    return render(request, 'newTrip.html')

# ACTION METHODS
def getEmail(request):
    print(request.POST['email'])
    return redirect('/form')

def register(request):
    new_user = User.objects.create(
        first_name=request.POST['fName'], 
        last_name=request.POST['lName'],
        email=request.POST['email'],
        password=request.POST['password'] 
        )
    request.session['user_id'] = new_user.id
    return redirect('/congrats')


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

def createTrip(request):
    currentUser = User.objects.get(id=request.session['user_id'])
    new_trip = Trip.objects.create(
        location = request.POST['location'],
        description = request.POST['desc'],
        date = request.POST['date'],
        organizer = currentUser
    )
    new_trip.users_joined.add(currentUser)
    new_trip.save()
    return redirect('/congrats')

def joinTrip(request, tripID):
    tripToJoin = Trip.objects.get(id=tripID)
    currentUser = User.objects.get(id=request.session['user_id'])
    tripToJoin.users_joined.add(currentUser)
    tripToJoin.save()
    return redirect('/congrats')

def cancelTrip(request, tripID):
    tripToQuit = Trip.objects.get(id=tripID)
    currentUser = User.objects.get(id=request.session['user_id'])
    tripToQuit.users_joined.remove(currentUser)
    tripToQuit.save()
    return redirect('/congrats')