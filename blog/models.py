from django.db import models

class Blog (models.Model) :
    title = models.TextField(max_length = 200 )
    description = models.TextField(max_length = 200 )
    date = models.DateField()
