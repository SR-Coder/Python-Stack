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

    def __str__(self):
        s = '\n'
        s += f'id: {self.id}\n'
        s += f"first_name: {self.first_name}\n"
        s += f"last_name: {self.last_name}\n"
        s += f"email: {self.email}\n"
        return s