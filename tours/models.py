from django.db import models

class Tour(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.desc
