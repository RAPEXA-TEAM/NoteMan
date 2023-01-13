from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Notes(models.Model):

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    date = models.DateTimeField("Update")
    def __str__(self):
        return "{}  {}  [{}]".format(self.user, self.title, self.date)