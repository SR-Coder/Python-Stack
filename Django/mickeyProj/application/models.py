from django.db import models

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