from django.db import models
from django.conf.global_settings import AUTH_USER_MODEL

# Create your models here.

#THis for category
class category (models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
#__________________________________________________________________
#this for the status of the projects
class projectstatus(models.IntegerChoices):
    PENDING = 1,'pending'
    COMPLETED = 2,'completed'
    POSTPONED = 3,'postponed'
    CANCELED =4, 'canceled'
#___________________________________________________________________


class projects (models.Model):
    title = models.CharField(max_length=255)
    status = models.IntegerField(
        choices= projectstatus.choices,
        default= projectstatus.PENDING,
    )
    desciption = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    #this for relationship/ one to many the many is the projects
    category = models.ForeignKey(category,on_delete=models.PROTECT)
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    #this for the date to be string
    def __str__(self):
        return self.title
#_______________________________________________________________________
class task(models.Model):
    desciption = models.TextField()
    is_complted =models.BooleanField(default=False)
    project = models.ForeignKey(projects,on_delete=models.CASCADE)
    def __str__(self):
        return self.desciption

    