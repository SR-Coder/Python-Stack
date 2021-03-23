from django.db import models

# Create your manager here!!
class ShowManager(models.Manager):
    def show_validator(self, postData):
        errors = {}
        if len(postData['title'])<2:
            errors['title'] = 'Title should be at least two characters long!!'
        if len(postData['network'])<3:
            errors['network'] = 'Network should be at least three characters long!!'
        if len(postData['desc'])<10:
            errors['desc'] = 'Descriptions should be at least ten characters long!!'
        return errors


# Create your models here.
class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=25)
    release_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()
