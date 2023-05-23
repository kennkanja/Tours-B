from django.db import models

class Tour(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    
    

class Pack(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    
class Gallery(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
   

class Site(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.desc
class Serv(models.Model):
    title = models.CharField(max_length=50)
    desc  = models.CharField(max_length=300)
    links = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
    
       
    
    
class Serve(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
class Book(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

class Term(models.Model):
    title = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
 
 

class Reservation(models.Model):
    dest = models.CharField(max_length=50)
    fname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    pno = models.CharField(max_length=50)
    sdate = models.DateField(max_length=50)
    fdate = models.DateField(max_length=50)
    gender = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    no_child = models.IntegerField()
    no_adults = models.IntegerField()


    def __str__(self):
        return self.fname

    
