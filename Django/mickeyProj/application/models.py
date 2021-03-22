from django.db import models
import re

class MickeyManager(models.Manager):
    def registration_validator(self, postData):
        errors ={}
        if len(postData['fName']) < 2:
            errors['fName'] = 'First names must be greater than 2 characters!'
        if len(postData['lName']) < 2:
            errors['lName'] = 'Last names must be greater than 2 characters!'
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = 'Invalid email address!!'
        if len(postData['password']) < 7:
            errors['password'] = 'Passwords must be 8 characters or greater!!'
        if postData['password'] != postData['chkPassword']:
            errors['chkPassword'] = 'Passwords dont match!!'
        # things you may want to do...
        #  you NEED TO CHECK TO SEE IF A EMAIL IS UNIQUE!!!!
        return errors
    def login_validator(self, postData):
        pass
        

# Create your models here.
class User(models.Model):
    # id = IntField() (Automatically Created)
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True) # (Automatically Created)
    updated_at = models.DateTimeField(auto_now=True) # (Automatically Created)
    # reviews.all() (phantom property)
    # trips.all()
    # trips_joined.all()
    objects = MickeyManager()

    def __str__(self):
        s = '\n'
        s += f'id: {self.id}\n'
        s += f"first_name: {self.first_name}\n"
        s += f"last_name: {self.last_name}\n"
        s += f"email: {self.email}\n"
        return s


class Review(models.Model):
    rating = models.IntegerField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # (Automatically Created)
    updated_at = models.DateTimeField(auto_now=True) # (Automatically Created)

    reviewer = models.ForeignKey(User, related_name='reviews', on_delete=models.CASCADE)


class Trip(models.Model):
    location = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    organizer = models.ForeignKey(User, related_name='trips', on_delete=models.CASCADE)
    users_joined = models.ManyToManyField(User, related_name = 'trips_joined') # using the .all()


# user1 = User.objects.create(first_name='Shayan', last_name='Valaie', email='s@v.com', password='asdfasdf')
# user1.first_name # returns 'Shayan'

# review1 = Review.objects.create(rating=7.5, content='Looks Good', reviewer=user1)
# review2 = Review.objects.create(rating=1.5, content='Looks bad', reviewer=user1)

# review1.content # returns 'Looks Good'
# review1.reviewer # returns the whole user object that is related

# user1.reviews.all() # returns a list of reviews [review1, review2]